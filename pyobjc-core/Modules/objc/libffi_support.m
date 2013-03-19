/*
 * Support for libffi (http://sources.redhat.com/libffi)
 *
 * libffi is a library that makes it possible to dynamicly create calls
 * to C functions (without knowing the signature at compile-time). It also
 * provides a way to create closures, that is dynamicly create functions with
 * a runtime specified interface.
 *
 * This file contains functions to dynamicly call objc_msgSendSuper and to
 * dynamicly create IMPs for use in Objective-C method dispatch tables. The
 * file 'register.m' contains compile-time generated equivalents of these.
 *
 * FIXME: There's way to much duplicated code in here, please refactor me.
 */
#include "pyobjc.h"

#import <Foundation/NSHost.h>
#import <CoreFoundation/CoreFoundation.h>

#ifdef __ppc64__
extern bool ffi64_stret_needs_ptr(const ffi_type* inType, unsigned short*, unsigned short*);
#endif

/*
 * Define SMALL_STRUCT_LIMIT as the largest struct that will be returned
 * in registers instead of with a hidden pointer argument.
 */

static const char gCharEncoding[] = { _C_CHR, 0 };
static const char gCFRangeEncoding[1024] = { 0 };

#if defined(__ppc__)

#   define SMALL_STRUCT_LIMIT    4

#elif defined(__ppc64__)

#   define SMALL_STRUCT_LIMIT    8

#elif defined(__i386__)

#   define SMALL_STRUCT_LIMIT     8

#elif defined(__x86_64__)

#   define SMALL_STRUCT_LIMIT    16

#else

#   error "Unsupported MACOSX platform"

#endif


#ifndef FFI_CLOSURES
#    error "Need FFI_CLOSURES!"
#endif

#ifdef PyObjC_DEBUG
/*
 * describe_ffitype and describe_cif are useful during debugging,
 * and are therefore made available when PyObjC_DEBUG is turned on
 * even though they aren't actually called anywhere.
 */

static void describe_ffitype(ffi_type* type)
{
    switch (type->type) {
    case FFI_TYPE_VOID: printf("%s", "void"); break;
    case FFI_TYPE_INT: printf("%s", "int"); break;
    case FFI_TYPE_FLOAT: printf("%s", "float"); break;
    case FFI_TYPE_DOUBLE: printf("%s", "double"); break;
    case FFI_TYPE_UINT8: printf("%s", "uint8"); break;
    case FFI_TYPE_SINT8: printf("%s", "sint8"); break;
    case FFI_TYPE_UINT16: printf("%s", "uint16"); break;
    case FFI_TYPE_SINT16: printf("%s", "sint16"); break;
    case FFI_TYPE_UINT32: printf("%s", "uint32"); break;
    case FFI_TYPE_SINT32: printf("%s", "sint32"); break;
    case FFI_TYPE_UINT64: printf("%s", "uint64"); break;
    case FFI_TYPE_SINT64: printf("%s", "sint64"); break;
    case FFI_TYPE_POINTER: printf("%s", "*"); break;
    case FFI_TYPE_STRUCT: {
            ffi_type** elems = type->elements;

            printf("%s", "struct { ");
            if (elems) {
                while (*elems) {
                    describe_ffitype(*(elems++));
                    printf("%s", "; ");
                }
            }
            printf("%s", "}");
        }
           break;

    default:
           // Don't abort, this is called from the debugger
           printf("?(%d)", type->type);
    }
}

static void describe_cif(ffi_cif* cif) __attribute__((__unused__));
static void describe_cif(ffi_cif* cif)
{
    size_t i;

    printf("<ffi_cif abi=%d nargs=%d  bytes=%d flags=%#x args=[",
        cif->abi, cif->nargs, cif->bytes, cif->flags);
    for  (i = 0; i < cif->nargs; i++) {
        describe_ffitype(cif->arg_types[i]);
        printf("%s", ", ");
    }
    printf("%s", "] rettype=");
    describe_ffitype(cif->rtype);
    printf("%s", ">\n");
}

#endif /* PyObjC_DEBUG */



static Py_ssize_t
num_struct_fields(const char* argtype)
{
    Py_ssize_t res = 0;

    if (*argtype != _C_STRUCT_B) return -1;
    while (*argtype != _C_STRUCT_E && *argtype != '=') argtype++;
    if (*argtype == _C_STRUCT_E) return 0;

    argtype++;
    while (*argtype != _C_STRUCT_E) {
        if (*argtype == '"') {
            /* Skip field name */
            argtype++;
            while (*argtype++ != '"') {}
        }

        argtype = PyObjCRT_SkipTypeSpec(argtype);
        if (argtype == NULL) return -1;
        res ++;
    }
    return res;
}


static void
free_type(void *obj)
{
    PyMem_Free(((ffi_type*)obj)->elements);
    PyMem_Free(obj);
}

static ffi_type* signature_to_ffi_type(const char* argtype);

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 6

static void cleanup_ffitype_capsule(void* ptr)
{
    free_type(ptr);
}

#else /* Python >= 2.7 */

static void cleanup_ffitype_capsule(PyObject* ptr)
{
    free_type(PyCapsule_GetPointer(ptr, "objc.__ffi_type__"));
}

#endif /* Python >= 2.7 */


static ffi_type*
array_to_ffi_type(const char* argtype)
{
static PyObject* array_types = NULL;

    PyObject* v;
    ffi_type* type;
    Py_ssize_t field_count;
    Py_ssize_t i;
    const char* key = argtype;

    if (array_types == NULL) {
        array_types = PyDict_New();
        if (array_types == NULL) return NULL;
    }

    v = PyDict_GetItemString(array_types, (char*)argtype);
    if (v != NULL) {
        return (ffi_type*)PyCapsule_GetPointer(v, "objc.__ffi_type__");
    }

    /* We don't have a type description yet, dynamicly
     * create it.
     */
    field_count = atoi(argtype+1);

    type = PyMem_Malloc(sizeof(*type));
    if (type == NULL) {
        PyErr_NoMemory();
        return NULL;
    }
    type->size = PyObjCRT_SizeOfType(argtype);
    type->alignment = PyObjCRT_AlignOfType(argtype);

    /* Libffi doesn't really know about arrays as part of larger
     * data-structures (e.g. struct foo { int field[3]; };). We fake it
     * by treating the nested array as a struct. These seems to work
     * fine on MacOS X.
     */
    type->type = FFI_TYPE_STRUCT;
    type->elements = PyMem_Malloc((1+field_count) * sizeof(ffi_type*));
    if (type->elements == NULL) {
        PyMem_Free(type);
        PyErr_NoMemory();
        return NULL;
    }

    while (isdigit(*++argtype));
    type->elements[0] = signature_to_ffi_type(argtype);
    for (i = 1; i < field_count; i++) {
        type->elements[i] = type->elements[0];
    }
    type->elements[field_count] = 0;

    v = PyCapsule_New(type, "objc.__ffi_type__", cleanup_ffitype_capsule);
    if (v == NULL) {
        free_type(type);
        return NULL;
    }

    PyDict_SetItemString(array_types, (char*)key, v);
    if (PyErr_Occurred()) {
        Py_DECREF(v);
        return NULL;
    }
    Py_DECREF(v);
    return type;
}

static ffi_type*
struct_to_ffi_type(const char* argtype)
{
static  PyObject* struct_types = NULL;

    PyObject* v;
    ffi_type* type;
    Py_ssize_t field_count;
    const char* curtype;

    if (struct_types == NULL) {
        struct_types = PyDict_New();
        if (struct_types == NULL) return NULL;
    }

    v = PyDict_GetItemString(struct_types, (char*)argtype);
    if (v != NULL) {
        return (ffi_type*)PyCapsule_GetPointer(v, "objc.__ffi_type__");
    }

    /* We don't have a type description yet, dynamicly
     * create it.
     */
    field_count = num_struct_fields(argtype);
    if (field_count == -1) {
        PyErr_Format(PyObjCExc_InternalError,
            "Cannot determine layout of %s", argtype);
        return NULL;
    }

    type = PyMem_Malloc(sizeof(*type));
    if (type == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    type->size = PyObjCRT_SizeOfType(argtype);
    type->alignment = PyObjCRT_AlignOfType(argtype);
    type->type = FFI_TYPE_STRUCT;
    type->elements = PyMem_Malloc((1+field_count) * sizeof(ffi_type*));

    if (type->elements == NULL) {
        PyMem_Free(type);
        PyErr_NoMemory();
        return NULL;
    }

    field_count = 0;
    curtype = argtype+1;
    while (*curtype != _C_STRUCT_E && *curtype != '=') curtype++;

    if (*curtype == '=') {
        curtype ++;

        while (*curtype != _C_STRUCT_E) {
            if (*curtype == '"') {
                /* Skip field name */
                curtype++;
                while (*curtype++ != '"') {}
            }

            type->elements[field_count] =
                signature_to_ffi_type(curtype);

            if (type->elements[field_count] == NULL) {
                PyMem_Free(type->elements);
                return NULL;
            }

            field_count++;
            curtype = PyObjCRT_SkipTypeSpec(curtype);

            if (curtype == NULL) {
                PyMem_Free(type->elements);
                return NULL;
            }
        }
    }

    type->elements[field_count] = NULL;

    v = PyCapsule_New(type, "objc.__ffi_type__", cleanup_ffitype_capsule);
    if (v == NULL) {
        free_type(type);
        return NULL;
    }

    PyDict_SetItemString(struct_types, (char*)argtype, v);
    if (PyErr_Occurred()) {
        Py_DECREF(v);
        return NULL;
    }
    Py_DECREF(v);
    return type;
}

ffi_type*
PyObjCFFI_Typestr2FFI(const char* argtype)
{
#ifdef __ppc__
static const char long_type[] = { _C_LNG, 0 };
static const char ulong_type[] = { _C_ULNG, 0 };

    switch (*argtype) {
    case _C_CHR: case _C_SHT: case _C_UNICHAR:
        return signature_to_ffi_type(long_type);

    case _C_UCHR: case _C_USHT:
        return signature_to_ffi_type(ulong_type);

#ifdef _C_BOOL
    case _C_BOOL: return signature_to_ffi_type(long_type);
#endif

    case _C_NSBOOL:
              return signature_to_ffi_type(long_type);
    default:
        return signature_to_ffi_type(argtype);
    }

#else /* !__ppc__ */
    return signature_to_ffi_type(argtype);

#endif /* ! __ppc__ */
}


static ffi_type*
signature_to_ffi_type(const char* argtype)
{
    argtype = PyObjCRT_SkipTypeQualifiers(argtype);
    switch (*argtype) {
    case _C_VOID: return &ffi_type_void;
    case _C_ID: return &ffi_type_pointer;
    case _C_CLASS: return &ffi_type_pointer;
    case _C_SEL: return &ffi_type_pointer;
    case _C_CHR: return &ffi_type_schar;
    case _C_CHAR_AS_INT: return &ffi_type_schar;
    case _C_CHAR_AS_TEXT: return &ffi_type_schar;

#ifdef _C_BOOL
    case _C_BOOL:
         /* sizeof(bool) == 4 on PPC32, and 1 on all others */
#if defined(__ppc__) && !defined(__LP64__)
         return &ffi_type_sint;
#else /* !defined(__ppc__) || defined(__LP64__) */
         return &ffi_type_schar;
#endif /* !defined(__ppc__) || defined(__LP64__)  */

#endif /* _C_BOOL */

    case _C_NSBOOL: return &ffi_type_schar;
    case _C_UCHR: return &ffi_type_uchar;
    case _C_SHT: return &ffi_type_sshort;
    case _C_UNICHAR: return &ffi_type_ushort;
    case _C_USHT: return &ffi_type_ushort;
    case _C_INT: return &ffi_type_sint;
    case _C_UINT: return &ffi_type_uint;

     /* The next to definitions are incorrect, but the correct definitions
      * don't work (e.g. give testsuite failures).
      */
#ifdef __LP64__
    case _C_LNG: return &ffi_type_sint64;  /* ffi_type_slong */
    case _C_ULNG: return &ffi_type_uint64;  /* ffi_type_ulong */
#else /* !__LP64__ */
    case _C_LNG: return &ffi_type_sint;  /* ffi_type_slong */
    case _C_ULNG: return &ffi_type_uint;  /* ffi_type_ulong */
#endif /* !__LP64__ */
    case _C_LNG_LNG: return &ffi_type_sint64;
    case _C_ULNG_LNG: return &ffi_type_uint64;
    case _C_FLT: return &ffi_type_float;
    case _C_DBL: return &ffi_type_double;
    case _C_CHARPTR: return &ffi_type_pointer;
    case _C_PTR: return &ffi_type_pointer;

    case _C_ARY_B:
        return array_to_ffi_type(argtype);

    case _C_IN: case _C_OUT: case _C_INOUT: case _C_CONST:
        return signature_to_ffi_type(argtype+1);

    case _C_STRUCT_B:
        return struct_to_ffi_type(argtype);

    case _C_UNDEF:
        return &ffi_type_pointer;

    default:
        PyErr_Format(PyExc_NotImplementedError,
            "Type '0x%x' (%c) not supported", *argtype, *argtype);
        return NULL;
    }
}

static Py_ssize_t
extract_count(const char* type, void* pvalue)
{
    type = PyObjCRT_SkipTypeQualifiers(type);
    switch (*type) {
    case _C_ID:
        {
            NSArray* value = *(id*)pvalue;
            if (!value) {
                return 0;
            } else if ([value respondsToSelector:@selector(count)]) {
                return [value count];
            } else {
                /* Fall through to error case */
            }
        }
        break;

    case _C_CHR: return (Py_ssize_t)*(char*)pvalue;
    case _C_CHAR_AS_INT: return (Py_ssize_t)*(char*)pvalue;
    case _C_UCHR: return (Py_ssize_t)*(unsigned char*)pvalue;
    case _C_SHT: return (Py_ssize_t)*(short*)pvalue;
    case _C_USHT: return (Py_ssize_t)*(unsigned short*)pvalue;
    case _C_INT: return (Py_ssize_t)*(int*)pvalue;
    case _C_UINT: return (Py_ssize_t)*(unsigned int*)pvalue;
    case _C_LNG: return (Py_ssize_t)*(long*)pvalue;
    case _C_ULNG: return (Py_ssize_t)*(unsigned long*)pvalue;
    case _C_LNG_LNG: return (Py_ssize_t)*(long long*)pvalue;
    case _C_ULNG_LNG: return (Py_ssize_t)*(unsigned long long*)pvalue;
    case _C_PTR:
        switch(type[1]) {
        case _C_CHR: return (Py_ssize_t)**(char**)pvalue;
        case _C_CHAR_AS_INT: return (Py_ssize_t)**(char**)pvalue;
        case _C_UCHR: return (Py_ssize_t)**(unsigned char**)pvalue;
        case _C_SHT: return (Py_ssize_t)**(short**)pvalue;
        case _C_USHT: return (Py_ssize_t)**(unsigned short**)pvalue;
        case _C_INT: return (Py_ssize_t)**(int**)pvalue;
        case _C_UINT: return (Py_ssize_t)**(unsigned int**)pvalue;
        case _C_LNG: return (Py_ssize_t)**(long**)pvalue;
        case _C_ULNG: return (Py_ssize_t)**(unsigned long**)pvalue;
        case _C_LNG_LNG: return (Py_ssize_t)**(long long**)pvalue;
        case _C_ULNG_LNG: return (Py_ssize_t)**(unsigned long long**)pvalue;
        }

        if (strncmp(type+1, @encode(NSRange), sizeof(@encode(NSRange)) - 1) == 0) {
            return (Py_ssize_t)((*(NSRange**)pvalue)->length);
        }

        /* Fall through: */
    }

    if (strncmp(type, @encode(NSRange), sizeof(@encode(NSRange)) - 1) == 0) {
        return (Py_ssize_t)(((NSRange*)pvalue)->length);
    }

    if (strncmp(type, @encode(CFRange), sizeof(@encode(CFRange)) - 1) == 0) {
        return (Py_ssize_t)(((CFRange*)pvalue)->length);
    }

#ifdef __LP64__
    if (strncmp(type, "{_CFRange=qq}", sizeof("{_CFRange=qq}") - 1) == 0) {
        return (Py_ssize_t)(((CFRange*)pvalue)->length);
    }

#else /* !__LP64__ */
    if (strncmp(type, "{_CFRange=ii}", sizeof("{_CFRange=ii}") - 1) == 0) {
        return (Py_ssize_t)(((CFRange*)pvalue)->length);
    }
#endif /* !__LP64__ */

    if (strncmp(type, "{_CFRange=ll}", sizeof("{_CFRange=ll}") - 1) == 0) {
        return (Py_ssize_t)(((CFRange*)pvalue)->length);
    }

    if (strncmp(type, @encode(CFArrayRef), sizeof(@encode(CFArrayRef))-1) == 0 ||
        strncmp(type, @encode(CFMutableArrayRef), sizeof(@encode(CFMutableArrayRef))-1) == 0) {

        return (Py_ssize_t)CFArrayGetCount(*(CFArrayRef*)pvalue);
    }

    PyErr_Format(PyExc_TypeError,
            "Don't know how to convert to extract count: %s", type);
    return -1;
}

/* Support for printf format strings */
static Py_ssize_t
parse_printf_args(
    PyObject* py_format,
    PyObject* argtuple, Py_ssize_t argoffset,
    void** byref, struct byref_attr* byref_attr,
    ffi_type** arglist, void** values,
    Py_ssize_t curarg)
{
    /* Walk the format string as a UTF-8 encoded ASCII value. This isn't
     * perfect but keeps the code simple.
     */
    Py_ssize_t maxarg = PyTuple_Size(argtuple);

    PyObject* encoded;
    const char* format;
    PyObject* v;

    if (PyBytes_Check(py_format)) {
        encoded = py_format;
        Py_INCREF(encoded);
        format = PyBytes_AsString(encoded);

    } else if (PyUnicode_Check(py_format)) {
#ifdef PyObjC_FAST_UNICODE_ASCII
        format = PyObjC_Unicode_Fast_Bytes(py_format);
        if (format != NULL) {
            encoded = py_format;
            Py_INCREF(encoded);

        } else {
            PyErr_Clear();
            encoded = PyUnicode_AsEncodedString(py_format, "utf-8", NULL);
            if (encoded == NULL) {
                return -1;
            }
            format = PyBytes_AsString(encoded);
        }

#else /* !PyObjC_FAST_UNICODE_ASCII */

        encoded = PyUnicode_AsEncodedString(py_format, "utf-8", NULL);
        if (encoded == NULL) {
            return -1;
        }
        format = PyBytes_AsString(encoded);

#endif /* !PyObjC_FAST_UNICODE_ASCII */

    } else {
        PyErr_SetString(PyExc_TypeError, "Unsupported format string type");
        return -1;
    }

    if (format == NULL) {
        if (!PyErr_Occurred()) {
            PyErr_SetString(PyExc_ValueError, "Empty format string");
        }
        Py_DECREF(encoded);
        return -1;
    }

    format = strchr(format, '%');
    while (format && *format != '\0') {
        char typecode;

        /* Skip '%' */
        format ++;

        /* Check for '%%' escape */
        if (*format == '%') {
            format++;
            format = strchr(format, '%');
            continue;
        }

        /* Skip flags */
        while (1) {
           if (!*format)  break;
           if (
               (*format == '#')
            || (*format == '0')
            || (*format == '-')
            || (*format == ' ')
            || (*format == '+')
            || (*format == '\'')) {

            format++;
           } else {
            break;
           }
        }

        /* Field width */
        if (*format == '*') {
            if (argoffset >= maxarg) {
                PyErr_Format(PyExc_ValueError, "Too few arguments for format string [cur:%"PY_FORMAT_SIZE_T"d/len:%"PY_FORMAT_SIZE_T"d]", argoffset, maxarg);
                Py_DECREF(encoded);
                return -1;
            }
            format++;
            byref[curarg] = PyMem_Malloc(sizeof(int));
            if (byref[curarg] == NULL) {
                Py_DECREF(encoded);
                return -1;
            }

            if (depythonify_c_value(@encode(int), PyTuple_GET_ITEM(argtuple, argoffset), byref[curarg]) < 0) {
                Py_DECREF(encoded);
                return -1;
            }
            values[curarg] = byref[curarg];
            arglist[curarg] = signature_to_ffi_type(@encode(int));

            argoffset++;
            curarg++;

        } else {
            while (isdigit(*format)) format++;
        }

        /* Precision */
        if (*format == '.') {
            format++;
            if (*format == '*') {
                format++;
                if (argoffset >= maxarg) {
                    PyErr_Format(PyExc_ValueError, "Too few arguments for format string [cur:%"PY_FORMAT_SIZE_T"d/len:%"PY_FORMAT_SIZE_T"d]", argoffset, maxarg);
                    Py_DECREF(encoded);
                    return -1;
                }
                byref[curarg] = PyMem_Malloc(sizeof(long long));
                if (byref[curarg] == NULL) {
                    Py_DECREF(encoded);
                    return -1;
                }


                if (depythonify_c_value(@encode(int), PyTuple_GET_ITEM(argtuple, argoffset), byref[curarg]) < 0) {
                    Py_DECREF(encoded);
                    return -1;
                }
                values[curarg] = byref[curarg];
                arglist[curarg] = signature_to_ffi_type(@encode(int));
                argoffset++;
                curarg++;
            } else {
                while (isdigit(*format)) format++;
            }
        }

        /* length modifier */
        typecode = 0;

        if (*format == 'h') {
            format++;

            if (*format == 'h') {
                format++;
            }

        } else if (*format == 'l') {
            format++;
            typecode = _C_LNG;
            if (*format == 'l') {
                typecode = _C_LNG_LNG;
                format++;
            }

        } else if (*format == 'q') {
            format++;
            typecode = _C_LNG_LNG;

        } else if (*format == 'j') {
            typecode = _C_LNG_LNG;
            format++;

        } else if (*format == 'z') {
            typecode = *@encode(size_t);
            format++;

        } else if (*format == 't') {
            typecode = *@encode(ptrdiff_t);
            format++;

        } else if (*format == 'L') {
            /* typecode = _C_LNGDBL, that's odd: no type encoding for long double! */
            format++;

        }

        if (argoffset >= maxarg) {
            PyErr_Format(PyExc_ValueError, "Too few arguments for format string [cur:%"PY_FORMAT_SIZE_T"d/len:%"PY_FORMAT_SIZE_T"d]", argoffset, maxarg);
            Py_DECREF(encoded);
            return -1;
        }

        /* And finally the info we're after: the actual format character */
        switch (*format) {
        case 'c': case 'C':
#if SIZEOF_WCHAR_T != 4
#    error "Unexpected wchar_t size"
#endif

            byref[curarg] = PyMem_Malloc(sizeof(int));
            arglist[curarg] = signature_to_ffi_type(@encode(int));
            v = PyTuple_GET_ITEM(argtuple, argoffset);
#if PY_MAJOR_VERSION == 2
            if (PyString_Check(v)) {
                if (PyString_Size(v) != 1) {
                    PyErr_SetString(PyExc_ValueError, "Expecting string of length 1");
                    Py_DECREF(encoded);
                    return -1;
                }
                *(int*)byref[curarg] = (wchar_t)*PyString_AsString(v);
            } else
#endif
            if (PyUnicode_Check(v)) {

                if (PyUnicode_GetSize(v) != 1) {
                    PyErr_SetString(PyExc_ValueError, "Expecting string of length 1");
                    Py_DECREF(encoded);
                    return -1;
                }
                *(int*)byref[curarg] = (wchar_t)*PyUnicode_AsUnicode(v);
            } else if (depythonify_c_value(@encode(int), v, byref[curarg]) < 0) {
                Py_DECREF(encoded);
                return -1;
            }

            values[curarg] = byref[curarg];

            argoffset++;
            curarg++;
            break;

        case 'd': case 'i': case 'D':
            /* INT */
            if (*format == 'D') {
                typecode = _C_LNG;
            }

            if (typecode == _C_LNG_LNG) {
                byref[curarg] = PyMem_Malloc(sizeof(long long));

            } else if (typecode == _C_LNG) {
                byref[curarg] = PyMem_Malloc(sizeof(long));

            } else {
                typecode = _C_INT;
                byref[curarg] = PyMem_Malloc(sizeof(int));
            }
            if (byref[curarg] == NULL) {
                PyErr_NoMemory();
                return -1;
            }
            if (depythonify_c_value(&typecode, PyTuple_GET_ITEM(argtuple, argoffset), byref[curarg]) < 0) {
                Py_DECREF(encoded);
                return -1;
            }
            values[curarg] = byref[curarg];
            arglist[curarg] = signature_to_ffi_type(&typecode);

            argoffset++;
            curarg++;
            break;

        case 'o': case 'u': case 'x':
        case 'X': case 'U': case 'O':
            /* UNSIGNED */
            if (*format == 'U' || *format == 'X') {
                typecode = _C_LNG;
            }

            if (typecode == _C_LNG_LNG) {
                byref[curarg] = PyMem_Malloc(sizeof(long long));
                typecode = _C_ULNG_LNG;

            } else if (typecode == _C_LNG) {
                byref[curarg] = PyMem_Malloc(sizeof(long));
                typecode = _C_ULNG;

            } else {
                byref[curarg] = PyMem_Malloc(sizeof(int));
                typecode = _C_UINT;
            }
            if (byref[curarg] == NULL) {
                PyErr_NoMemory();
                Py_DECREF(encoded);
                return -1;
            }
            if (depythonify_c_value(&typecode, PyTuple_GET_ITEM(argtuple, argoffset), byref[curarg]) < 0) {
                Py_DECREF(encoded);
                return -1;
            }
            values[curarg] = byref[curarg];
            arglist[curarg] = signature_to_ffi_type(&typecode);

            argoffset++;
            curarg++;
            break;

        case 'f': case 'F': case 'e': case 'E':
        case 'g': case 'G': case 'a': case 'A':
            /* double */
            typecode = _C_DBL;
            byref[curarg] = PyMem_Malloc(sizeof(double));
            if (byref[curarg] == NULL) {
                PyErr_NoMemory();
                Py_DECREF(encoded);
                return -1;
            }

            if (depythonify_c_value(&typecode, PyTuple_GET_ITEM(argtuple, argoffset), byref[curarg]) < 0) {
                Py_DECREF(encoded);
                return -1;
            }
            values[curarg] = byref[curarg];
#if defined(__ppc__)
            /* Passing floats to variadic functions on darwin/ppc
             * is slightly convoluted. Lying to libffi about the
             * type of the argument seems to trick it into doing
             * what the callee expects.
             */
            arglist[curarg] = &ffi_type_uint64;

#else /* !defined(__ppc) */
            arglist[curarg] = signature_to_ffi_type(&typecode);
#endif /* !defined(__ppc) */

            argoffset++;
            curarg++;
            break;


        case 's': case 'S':
            /* string */
            if (*format == 'S' || typecode == _C_LNG) {
                /* whar_t */
                v = byref_attr[curarg].buffer = PyUnicode_FromObject( PyTuple_GET_ITEM(argtuple, argoffset));
                if (byref_attr[curarg].buffer == NULL) {
                    Py_DECREF(encoded);
                    return -1;
                }

                Py_ssize_t sz = PyUnicode_GetSize(v);
                byref[curarg] = PyMem_Malloc(sizeof(wchar_t)*(sz+1));
                if (byref[curarg] == NULL) {
                    Py_DECREF(encoded);
                    return -1;
                }

                if (PyUnicode_AsWideChar(UNICODE_CAST(v), (wchar_t*)byref[curarg], sz)<0) {
                    Py_DECREF(encoded);
                    return -1;
                }
                ((wchar_t*)byref[curarg])[sz] = 0;
                arglist[curarg] = signature_to_ffi_type(@encode(wchar_t*));
                values[curarg] = byref + curarg;

            } else {
                /* char */
                typecode = _C_CHARPTR;
                byref[curarg] = PyMem_Malloc(sizeof(char*));
                if (byref[curarg] == NULL) {
                    PyErr_NoMemory();
                    Py_DECREF(encoded);
                    return -1;
                }
                if (depythonify_c_value(&typecode, PyTuple_GET_ITEM(argtuple, argoffset), byref[curarg]) < 0) {
                    Py_DECREF(encoded);
                    return -1;
                }
                arglist[curarg] = signature_to_ffi_type(&typecode);
                values[curarg] = byref[curarg];
            }

            argoffset++;
            curarg++;
            break;

        case '@': case 'K':
            /* object (%K is only used by NSPredicate */
            typecode = _C_ID;
            byref[curarg] = PyMem_Malloc(sizeof(char*));
            if (byref[curarg] == NULL) {
                PyErr_NoMemory();
                Py_DECREF(encoded);
                return -1;
            }
            if (depythonify_c_value(&typecode, PyTuple_GET_ITEM(argtuple, argoffset), byref[curarg]) < 0) {
                Py_DECREF(encoded);
                return -1;
            }
            values[curarg] = byref[curarg];
            arglist[curarg] = signature_to_ffi_type(&typecode);

            argoffset++;
            curarg++;
            break;

        case 'p':
            /* pointer */
            byref[curarg] = PyMem_Malloc(sizeof(char*));
            if (byref[curarg] == NULL) {
                PyErr_NoMemory();
                Py_DECREF(encoded);
                return -1;
            }
            *((char**)byref[curarg]) = (char*)PyTuple_GET_ITEM(argtuple, argoffset);
            values[curarg] = byref[curarg];
            arglist[curarg] = signature_to_ffi_type(@encode(void*));

            argoffset++;
            curarg++;
            break;

        case 'n':
            /* pointer-to-int */
            byref[curarg] = PyMem_Malloc(sizeof(long long));
            if (byref[curarg] == NULL) {
                PyErr_NoMemory();
                Py_DECREF(encoded);
                return -1;
            }
            values[curarg] = byref[curarg];
            arglist[curarg] = signature_to_ffi_type(&typecode);

            argoffset++;
            break;

        default:
            PyErr_SetString(PyExc_ValueError, "Invalid format string");
            Py_DECREF(encoded);
            return -1;
        }


        format = strchr(format+1, '%');
    }

    Py_DECREF(encoded);

    if (argoffset != maxarg) {
        PyErr_Format(PyExc_ValueError, "Too many values for format [%"PY_FORMAT_SIZE_T"d/%"PY_FORMAT_SIZE_T"d]", argoffset, maxarg);
        return -1;
    }
    return curarg;
}

static Py_ssize_t parse_varargs_array(
    PyObjCMethodSignature* methinfo,
    PyObject* argtuple, Py_ssize_t argoffset,
    void** byref,
    ffi_type** arglist, void** values, Py_ssize_t count)
{
    Py_ssize_t curarg = Py_SIZE(methinfo)-1;
    Py_ssize_t maxarg = PyTuple_Size(argtuple);
    Py_ssize_t argSize;

    if (count != -1) {
        if (maxarg - curarg != count) {
            PyErr_Format(PyExc_ValueError, "Wrong number of variadic arguments, need %" PY_FORMAT_SIZE_T "d, got %" PY_FORMAT_SIZE_T "d",
                    count, (maxarg - curarg));
            return -1;
        }
    }

    struct _PyObjC_ArgDescr* argType = (
            methinfo->argtype + Py_SIZE(methinfo) - 1);

    argSize = PyObjCRT_SizeOfType(argType->type);

    if (count == -1) {
        if (argType->type[0] != _C_ID) {
            PyErr_Format(PyExc_TypeError,
                "variadic null-terminated arrays only supported for type '%c', not '%s' || %s", _C_ID, argType->type, PyObject_REPR((PyObject*)methinfo));
            return -1;
        }
    }

    for (;argoffset < maxarg; curarg++, argoffset++) {
        byref[curarg]  = PyMem_Malloc(argSize);
        if (byref[curarg] == NULL) {
            return -1;
        }
        if (depythonify_c_value(argType->type,
            PyTuple_GET_ITEM(argtuple, argoffset),
            byref[curarg]) < 0) {

            return -1;
        }

        values[curarg] = byref[curarg];
        arglist[curarg] = &ffi_type_pointer;
    }
    byref[curarg]  = NULL;
    values[curarg] = &byref[curarg];
    arglist[curarg] = &ffi_type_pointer;
    return curarg+1;
}

/* This function decodes its arguments into Python values, then
 * calls the python method and finally encodes the return value
 */

enum closureType {
    PyObjC_Function,
    PyObjC_Method,
    PyObjC_Block,
};

typedef struct {
    PyObject* callable;
    Py_ssize_t argCount;
    PyObjCMethodSignature* methinfo;
    enum closureType closureType;
} _method_stub_userdata;

static void
method_stub(ffi_cif* cif __attribute__((__unused__)), void* resp, void** args, void* _userdata)
{
    int err;
    PyObject* seq;
    _method_stub_userdata* userdata = (_method_stub_userdata*)_userdata;
    PyObject* callable = userdata->callable;
    PyObjCMethodSignature* methinfo = userdata->methinfo;
    Py_ssize_t i, startArg;
    PyObject* arglist;
    PyObject* res;
    PyObject* v = NULL;
    int have_output = 0;
    const char* rettype;
    PyObject* pyself;
    int cookie;
    Py_ssize_t count;
    BOOL haveCountArg;

    PyGILState_STATE   state = PyGILState_Ensure();

    rettype = methinfo->rettype.type;

    arglist = PyList_New(0);

    /* First translate 'self' from Objective-C to python */
    if (userdata->closureType == PyObjC_Method) {
        pyself = PyObjCObject_NewTransient(*(id*)args[0], &cookie);
        if (pyself == NULL) {
            goto error;
        }

        pyself = PyObjC_AdjustSelf(pyself);
        if (pyself == NULL) {
            goto error;
        }

        if (PyList_Append(arglist, pyself) == -1) {
            goto error;
        }

        startArg = 2;

    } else if (userdata->closureType == PyObjC_Block) {
        startArg = 1;
        pyself = NULL;

    } else {
        startArg = 0;
        pyself = NULL;
    }

    for (i = startArg; i < Py_SIZE(methinfo); i++) {

        const char* argtype = methinfo->argtype[i].type;

        switch (*argtype) {

        case _C_INOUT:
            if (argtype[1] == _C_PTR) {
                have_output ++;
            }
            /* FALL THROUGH */

        case _C_IN: case _C_CONST:
            if (argtype[1] == _C_PTR && argtype[2] == _C_VOID && methinfo->argtype[i].ptrType == PyObjC_kPointerPlain) {
                /* A plain 'void*' that was marked up.
                 * This is wrong, but happens in the official metadata included
                 * with 10.5.x
                 */
                v = pythonify_c_value(argtype, args[i]);

            } else if (argtype[1] == _C_PTR || argtype[1] == _C_CHARPTR) {
                const char* resttype;

                if (argtype[1] == _C_PTR) {
                    resttype = argtype + 2;
                } else {
                    resttype = gCharEncoding;
                }

                if (*(void**)args[i] == NULL) {
                    v = PyObjC_NULL;
                    Py_INCREF(v);

                } else {
                    switch (methinfo->argtype[i].ptrType) {
                    case PyObjC_kPointerPlain:
                        v = pythonify_c_value(resttype,
                            *(void**)args[i]);
                        break;

                    case PyObjC_kNullTerminatedArray:
                        v = pythonify_c_array_nullterminated(resttype, *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                        break;

                    case PyObjC_kArrayCountInArg:
                        count = extract_count(
                            methinfo->argtype[methinfo->argtype[i].arrayArg].type,
                            args[methinfo->argtype[i].arrayArg]);
                        if (count == -1 && PyErr_Occurred()) {
                            v = NULL;
                        } else {
                            v = PyObjC_CArrayToPython2(resttype, *(void**)args[i], count, methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                        }
                        break;

                    case PyObjC_kFixedLengthArray:
                        count = methinfo->argtype[i].arrayArg;
                        v = PyObjC_CArrayToPython2(resttype, *(void**)args[i], count, methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                        break;

                    case PyObjC_kVariableLengthArray:
                        v = PyObjC_VarList_New(resttype, *(void**)args[i]);
                        break;
                    }
                }

            } else {
                if (argtype[1] == _C_ARY_B) {
                    v = pythonify_c_value(argtype+1, *(void**)(args[i]));

                } else {
                    v = pythonify_c_value(argtype+1, args[i]);
                }

            }
            break;

        case _C_OUT:
            if (argtype[1] == _C_PTR) {
                have_output ++;
            }

            if (userdata->argCount == Py_SIZE(methinfo)-1) {
                /* Python method has parameters for the output
                 * arguments as well, pass a placeholder value.
                 *
                 * XXX: For some types of arguments we could
                 * well pass in a buffer/array.array-style object!
                 */
                if (*(void**)args[i] == NULL) {
                    v = PyObjC_NULL;
                } else {
                    v = Py_None;
                }
                Py_INCREF(v);
            } else {
                /* Skip output parameter */
                continue;
            }
            break;

        case _C_CHARPTR:
             /* XXX: Not quite happy about this, why special case 'char*' but not 'int*' (both without in/out/inout markup) */
            if (*(void**)args[i] == NULL) {
                v = PyObjC_NULL;
                Py_INCREF(v);
            } else {
                switch (methinfo->argtype[i].ptrType) {
                case PyObjC_kPointerPlain:
                    v = pythonify_c_value(argtype, args[i]);
                    break;

                case PyObjC_kNullTerminatedArray:
                    v = pythonify_c_array_nullterminated(argtype, args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    break;

                case PyObjC_kArrayCountInArg:
                    count = extract_count(
                        methinfo->argtype[methinfo->argtype[i].arrayArg].type,
                        args[methinfo->argtype[i].arrayArg]);

                    if (count == -1 && PyErr_Occurred()) {
                        v = NULL;

                    } else {
                        v = PyBytes_FromStringAndSize(args[i], count);

                    }
                    break;

                case PyObjC_kFixedLengthArray:
                    count = methinfo->argtype[i].arrayArg;
                    v = PyBytes_FromStringAndSize(args[i], count);
                    break;

                case PyObjC_kVariableLengthArray:
                    v = PyObjC_VarList_New(gCharEncoding, args[i]);
                    break;
                }
            }
            break;

        case _C_ARY_B:
            /* An array is actually a pointer to the first
             * element of the array. Libffi passes a pointer to
             * that pointer, we need to strip one level of
             * indirection to ensure that pythonify_c_value works
             * correctly.
             */
            v = pythonify_c_value(argtype, *(void**)args[i]);
            break;

        default:
            v = pythonify_c_value(argtype, args[i]);
        }

        if (v == NULL) {
            Py_DECREF(arglist);
            goto error;
        }

        if (PyList_Append(arglist, v) == -1) {
            Py_DECREF(v);
            Py_DECREF(arglist);
            goto error;
        }
        Py_DECREF(v);
    }

    v = PyList_AsTuple(arglist);
    if (v == NULL) {
        Py_DECREF(arglist);

        if (pyself) {
            PyObjCObject_ReleaseTransient(pyself, cookie);
        }

        goto error;
    }

    Py_DECREF(arglist);
    arglist = v;

    if (!callable) {
        PyErr_SetString(PyObjCExc_InternalError,
                "Missing callable in closure object");
        Py_DECREF(arglist);
        goto error;
    }

    /* Avoid calling a PyObjCPythonSelector directory, it does
     * additional work that we don't need.
     */
    if (PyObjCPythonSelector_Check(callable)) {
        callable = ((PyObjCPythonSelector*)callable)->callable;
    }

    res = PyObject_Call(callable, arglist, NULL);
    Py_DECREF(arglist);

    if (res == NULL) {
        goto error;
    }

    if (!have_output) {
        if (*rettype != _C_VOID) {
            const char* unqualified_type = PyObjCRT_SkipTypeQualifiers(rettype);

            if (unqualified_type[0] == _C_PTR || unqualified_type[0] == _C_CHARPTR) {
                const char* rest = unqualified_type + 1;
                if (*unqualified_type == _C_CHARPTR) {
                    rest = gCharEncoding;
                }

                if (res == PyObjC_NULL) {
                    *(void**)resp = NULL;

                } else {
                    switch (methinfo->rettype.ptrType) {
                    case PyObjC_kPointerPlain:
                        err = depythonify_c_return_value(unqualified_type, res, resp);
                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kFixedLengthArray:
                        count = methinfo->rettype.arrayArg;
                        err = depythonify_c_return_array_count(rest, count, res, resp, methinfo->rettype.alreadyRetained, methinfo->rettype.alreadyCFRetained);
                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kVariableLengthArray:
                        err = depythonify_c_return_array_count(rest, -1, res, resp, methinfo->rettype.alreadyRetained, methinfo->rettype.alreadyCFRetained);
                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kNullTerminatedArray:
                        err = depythonify_c_return_array_nullterminated(rest, res, resp, methinfo->rettype.alreadyRetained, methinfo->rettype.alreadyCFRetained);
                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kArrayCountInArg:
                        /* We don't have output arguments, thus can calculate the response immediately */
                        count = extract_count(
                            methinfo->argtype[methinfo->rettype.arrayArg].type,
                            args[methinfo->rettype.arrayArg]);
                        if (count == -1 && PyErr_Occurred()) {
                            goto error;
                        }
                        err = depythonify_c_return_array_count(rest, count, res, resp, methinfo->rettype.alreadyRetained, methinfo->rettype.alreadyCFRetained);
                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                    }
                }

            } else {
                err = depythonify_c_return_value(rettype,
                    res, resp);

                if (methinfo->rettype.alreadyRetained) {
                   /* Must return a 'new' instead of a borrowed
                    * reference.
                    */
                   [(*(id*)resp) retain];

                } else if (methinfo->rettype.alreadyCFRetained) {
                   /* Must return a 'new' instead of a borrowed
                    * reference.
                    */
                   CFRetain((*(id*)resp));

                } else if (*rettype == _C_ID && Py_REFCNT(res) == 1) {
                    /* make sure return value doesn't die before
                     * the caller can get its hands on it.
                     */
                    [[(*(id*)resp) retain] autorelease];
                }

                if (err == -1) {
                    if (res == Py_None) {
                        if (userdata->closureType == PyObjC_Method) {
                            PyErr_Format(PyExc_ValueError,
                               "%s: returned None, expecting "
                               "a value",
                               sel_getName(*(SEL*)args[1]));
                        } else {
                            PyErr_Format(PyExc_ValueError,
                               "%R: returned None, expecting "
                               "a value",
                               userdata->callable);
                        }

                    }
                    Py_DECREF(res);
                    goto error;
                }
            }

        } else {
            if (res != Py_None) {
                if (userdata->closureType == PyObjC_Method) {
                    PyErr_Format(PyExc_ValueError,
                        "%s: did not return None, expecting "
                        "void return value",
                        sel_getName(*(SEL*)args[1]));
                } else {
                    PyErr_Format(PyExc_ValueError,
                       "%R: returned None, expecting "
                       "a value",
                       userdata->callable);
                }
                goto error;
            }
        }

    } else {
        /* We have some output parameters, locate them and encode
         * their values
         */
        Py_ssize_t idx;
        PyObject* real_res;

        if (*rettype == _C_VOID && have_output == 1) {
            /* Special case: the python method returned only
             * the return value, not a tuple.
             */

            for (i = startArg; i < Py_SIZE(methinfo); i++) {
                const char* argtype = methinfo->argtype[i].type;

                switch (*argtype) {
                case _C_INOUT: case _C_OUT:
                    if (argtype[1] == _C_PTR) {
                        argtype += 2;
                    } else if (argtype[1] == _C_CHARPTR) {
                        argtype = gCharEncoding;
                    } else {
                        continue;
                    }
                    break;
                default: continue;
                }

                if (*(void**)args[i] == NULL) {
                    break;
                }

                switch (methinfo->argtype[i].ptrType) {
                case PyObjC_kPointerPlain:
                    err = depythonify_c_value(argtype, res, *(void**)args[i]);

                    if (err == -1) {
                        goto error;
                    }

                    if (argtype[0] == _C_ID && methinfo->argtype[i].alreadyRetained) {
                        [**(id**)args[i] retain];

                    } else if (argtype[0] == _C_ID && methinfo->argtype[i].alreadyCFRetained) {
                        CFRetain(**(id**)args[i]);

                    } else if (Py_REFCNT(res) == 1 && argtype[0] == _C_ID) {
                        /* make sure return value doesn't die before
                         * the caller can get its hands on it.
                         */
                        [[**(id**)args[i] retain] autorelease];
                    }
                    break;

                case PyObjC_kNullTerminatedArray:
                    count = c_array_nullterminated_size(res, &seq);

                    if (count == -1) {
                        goto error;
                    }

                    err = depythonify_c_array_nullterminated(argtype, count, seq, *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    Py_DECREF(seq);
                    if (err == -1) {
                        goto error;
                    }

                    break;

                case PyObjC_kArrayCountInArg:
                    count = extract_count(
                            methinfo->argtype[methinfo->argtype[i].arrayArg].type,
                            args[methinfo->argtype[i].arrayArg]);

                    if (count == -1 && PyErr_Occurred()) {
                        goto error;
                    }

                    err = depythonify_c_array_count(argtype, count, NO, res, *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    if (err == -1) {
                        goto error;
                    }
                    break;

                case PyObjC_kFixedLengthArray:
                    count = methinfo->argtype[i].arrayArg;
                    err = depythonify_c_array_count(argtype, count, YES, res, *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    if (err == -1) {
                        goto error;
                    }
                    break;

                case PyObjC_kVariableLengthArray:
                    err = depythonify_c_array_count(argtype, -1, YES, res, *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    if (err == -1) {
                        goto error;
                    }
                    break;
                }

                break;
            }

            PyGILState_Release(state);
            return;
        }

        if (*rettype != _C_VOID) {
            if (!PyTuple_Check(res) || PyTuple_Size(res) != have_output+1) {
                PyErr_Format(PyExc_TypeError,
                    "%s: Need tuple of %d arguments as result",
                    sel_getName(*(SEL*)args[1]), have_output+1);
                Py_DECREF(res);
                goto error;
            }

            real_res = PyTuple_GET_ITEM(res, 0);
            idx = 1;

            const char* unqualified_type = PyObjCRT_SkipTypeQualifiers(rettype);
            if (unqualified_type[0] == _C_PTR || unqualified_type[0] == _C_CHARPTR) {
                const char* resttype = rettype + 1;
                if (unqualified_type[0] == _C_CHARPTR) {
                    resttype = gCharEncoding;
                }

                if (real_res == PyObjC_NULL) {
                    *(void**)resp = NULL;

                } else {
                    switch (methinfo->rettype.ptrType) {
                    case PyObjC_kPointerPlain:

                        err = depythonify_c_return_value(unqualified_type,
                            real_res, resp);

                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kFixedLengthArray:
                        count = methinfo->rettype.arrayArg;
                        err = depythonify_c_return_array_count(resttype, count, real_res, resp, methinfo->rettype.alreadyRetained, methinfo->argtype[i].alreadyCFRetained);

                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kVariableLengthArray:
                        err = depythonify_c_return_array_count(resttype, -1, real_res, resp, methinfo->rettype.alreadyRetained, methinfo->argtype[i].alreadyCFRetained);

                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kNullTerminatedArray:
                        err = depythonify_c_return_array_nullterminated(resttype, real_res, resp, methinfo->rettype.alreadyRetained, methinfo->argtype[i].alreadyCFRetained);

                        if (err == -1) {
                            Py_DECREF(res);
                            goto error;
                        }
                        break;

                    case PyObjC_kArrayCountInArg:
                        if (*PyObjCRT_SkipTypeQualifiers(methinfo->argtype[methinfo->rettype.arrayArg].type) != _C_PTR) {
                            count = extract_count(
                                methinfo->argtype[methinfo->rettype.arrayArg].type,
                                args[methinfo->rettype.arrayArg]);

                            if (count == -1 && PyErr_Occurred()) {
                                goto error;
                            }
                            err = depythonify_c_return_array_count(resttype, count, real_res, resp, methinfo->rettype.alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                            if (err == -1) {
                                Py_DECREF(res);
                                goto error;
                            }
                        } else {
                            /* Wait until after the arguments have been depythonified */
                            *(void**)resp = NULL;
                            break;
                        }

                    }
                }

            } else {
                err = depythonify_c_return_value(rettype,
                    real_res, resp);

                if (methinfo->rettype.alreadyRetained) {
                   /* Must return a 'new' instead of a borrowed
                    * reference.
                    */
                   [(*(id*)resp) retain];

                } else if (methinfo->rettype.alreadyCFRetained) {
                    CFRetain(*(id*)resp);

                } else if (*rettype == _C_ID && Py_REFCNT(real_res) == 1) {
                    /* make sure return value doesn't die before
                     * the caller can get its hands on it.
                     */
                    [[(*(id*)resp) retain] autorelease];
                }
                if (err == -1) {
                    if (real_res == Py_None) {
                        PyErr_Format(PyExc_ValueError,
                           "%s: returned None, expecting "
                           "a value",
                           sel_getName(*(SEL*)args[1]));
                    }
                    Py_DECREF(res);
                    goto error;
                }
            }
        } else {
            if (!PyTuple_Check(res) || PyTuple_Size(res) != have_output) {
                PyErr_Format(PyExc_TypeError,
                    "%s: Need tuple of %d arguments as result",
                    sel_getName(*(SEL*)args[1]), have_output);
                Py_DECREF(res);
                goto error;
            }
            real_res = NULL;
            idx = 0;
        }

        haveCountArg = NO;
        for (i = startArg; i < Py_SIZE(methinfo); i++) {
            const char* argtype = methinfo->argtype[i].type;

            switch (*argtype) {
            case _C_INOUT: case _C_OUT:
                if (argtype[1] == _C_PTR) {
                    argtype += 2;
                } else if (argtype[1] == _C_CHARPTR) {
                    argtype ++;
                } else {
                    continue;
                }
                break;
            default: continue;
            }

            if (*(void**)args[i] == NULL) {
                idx++;
                continue;
            }

            switch (methinfo->argtype[i].ptrType) {
            case PyObjC_kPointerPlain:
                err = depythonify_c_value(argtype, PyTuple_GET_ITEM(res, idx++), *(void**)args[i]);
                if (err == -1) {
                    goto error;
                }

                if (argtype[0] == _C_ID && methinfo->argtype[i].alreadyRetained) {
                    [**(id**)args[i] retain];

                } else if (argtype[0] == _C_ID && methinfo->argtype[i].alreadyCFRetained) {
                    CFRetain(**(id**)args[i]);

                } else if (Py_REFCNT(res) == 1 && argtype[0] == _C_ID) {
                    /* make sure return value doesn't die before
                     * the caller can get its hands on it.
                     */
                    [[**(id**)args[i] retain] autorelease];
                }
                break;

            case PyObjC_kNullTerminatedArray:
                count = c_array_nullterminated_size(PyTuple_GET_ITEM(res, idx++), &seq);
                if (count == -1) {
                    goto error;
                }

                err = depythonify_c_array_nullterminated(argtype, count, seq, *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                Py_DECREF(seq);
                if (err == -1) {
                    goto error;
                }
                break;

            case PyObjC_kArrayCountInArg:
                if (methinfo->argtype[i].arraySizeInRetval) {
                    count = extract_count(methinfo->rettype.type, resp);
                    if (count == -1 && PyErr_Occurred()) goto error;

                    err = depythonify_c_array_count(argtype, count, NO, PyTuple_GET_ITEM(res, idx++), *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    if (err == -1) {
                        goto error;
                    }

                } else {
                    haveCountArg = YES;
                }
                break;

            case PyObjC_kFixedLengthArray:
                if (methinfo->argtype[i].arraySizeInRetval) {
                    count = extract_count(methinfo->rettype.type, resp);
                    if (count == -1 && PyErr_Occurred()) goto error;

                } else {
                    count = methinfo->argtype[i].arrayArg;
                }
                err = depythonify_c_array_count(argtype, count, YES, PyTuple_GET_ITEM(res, idx++), *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                if (err == -1) {
                    goto error;
                }
                break;

            case PyObjC_kVariableLengthArray:
                if (methinfo->argtype[i].arraySizeInRetval) {
                    count = extract_count(methinfo->rettype.type, resp);
                    if (count == -1 && PyErr_Occurred()) goto error;

                } else {
                    count = -1;
                }
                err = depythonify_c_array_count(argtype, count, YES, PyTuple_GET_ITEM(res, idx++), *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                if (err == -1) {
                    goto error;
                }
                break;

            }
        }

        if (haveCountArg) {
            if (real_res == NULL) {
                idx = 0;
            } else {
                idx = 1;
            }
            for (i = 2; i < Py_SIZE(methinfo); i++) {
                const char* argtype = methinfo->argtype[i].type;

                switch (*argtype) {
                case _C_INOUT: case _C_OUT:
                    if (argtype[1] == _C_PTR) {
                        argtype += 2;
                    } else if (argtype[1] == _C_CHARPTR) {
                        argtype ++;
                    } else {
                        continue;
                    }
                    break;
                default: continue;
                }

                if (*(void**)args[i] == NULL) {
                    idx++;
                    continue;
                }

                switch (methinfo->argtype[i].ptrType) {
                case PyObjC_kPointerPlain:
                case PyObjC_kNullTerminatedArray:
                case PyObjC_kFixedLengthArray:
                case PyObjC_kVariableLengthArray:
                    idx++;
                    break;

                case PyObjC_kArrayCountInArg:
                    count = extract_count(
                            methinfo->argtype[methinfo->argtype[i].arrayArg].type,
                            args[methinfo->argtype[i].arrayArg]);
                    if (count == -1 && PyErr_Occurred()) {
                        goto error;
                    }
                    err = depythonify_c_array_count(argtype, count, NO, PyTuple_GET_ITEM(res, idx++), *(void**)args[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    if (err == -1) {
                        goto error;
                    }
                    break;
                }
            }
        }

        if (*rettype != _C_VOID) {
            const char* unqualified = PyObjCRT_SkipTypeQualifiers(rettype);
            if (unqualified[0] == _C_PTR || unqualified[0] == _C_CHARPTR) {
                if (methinfo->rettype.ptrType == PyObjC_kArrayCountInArg) {
                    const char* rest = unqualified + 1;
                    if (unqualified[0] == _C_CHARPTR) {
                        rest = gCharEncoding;
                    }

                    count = extract_count(
                        methinfo->argtype[methinfo->rettype.arrayArg].type,
                        args[methinfo->rettype.arrayArg]);

                    if (count == -1 && PyErr_Occurred()) {
                        goto error;
                    }

                    err = depythonify_c_return_array_count(rest, count, real_res, resp, methinfo->rettype.alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                    if (err == -1) {
                        Py_DECREF(res);
                        goto error;
                    }
                }
            }
        }
    }
    Py_DECREF(res);

    /* Do this at the end to ensure we work correctly when
     * 'res' is 'pyself' and 'pyself' those are the only
     * references from Python (that is, 'pyself' is a
     * "transient" reference.
     */
    if (pyself) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }

    PyGILState_Release(state);

    return;

error:
    if (pyself) {
        PyObjCObject_ReleaseTransient(pyself, cookie);
    }
    PyObjCErr_ToObjCWithGILState(&state);
}

/*
 * Return an IMP that is suitable for forwarding a method with the specified
 * signature from Objective-C to Python.
 */

static Py_ssize_t
_argcount(PyObject* callable, BOOL* haveVarArgs, BOOL* haveVarKwds)
{
    PyCodeObject *func_code;

    if (PyFunction_Check(callable)) {
        func_code = (PyCodeObject *)PyFunction_GetCode(callable);
        *haveVarArgs = (func_code->co_flags & CO_VARARGS) != 0;
        *haveVarKwds = (func_code->co_flags & CO_VARKEYWORDS) != 0;
        return func_code->co_argcount;

    } else if (PyMethod_Check(callable)) {
        func_code = (PyCodeObject *)PyFunction_GetCode(
            PyMethod_Function (callable));
        *haveVarArgs = (func_code->co_flags & CO_VARARGS) != 0;
        *haveVarKwds = (func_code->co_flags & CO_VARKEYWORDS) != 0;
        if (PyMethod_Self(callable) == NULL) {
            return func_code->co_argcount;
        } else {
            return func_code->co_argcount - 1;
        }

    } else if (PyObjCPythonSelector_Check(callable)) {
        return _argcount(((PyObjCPythonSelector*)callable)->callable, haveVarArgs, haveVarKwds);

    } else if (PyObjCNativeSelector_Check(callable)) {
        PyObjCMethodSignature* sig = PyObjCSelector_GetMetadata(callable);
         Py_ssize_t result = Py_SIZE(sig) - 1;

         Py_DECREF(sig);
         return result;

    } else {
        PyErr_Format(PyExc_TypeError,
            "Sorry, cannot create IMP for instances of type %s",
            Py_TYPE(callable)->tp_name);
        return -1;
    }
}


PyObjC_callback_function
PyObjCFFI_MakeFunctionClosure(PyObjCMethodSignature* methinfo, PyObject* callable)
{
    _method_stub_userdata* stubUserdata;
    PyObjC_callback_function closure;

    stubUserdata = PyMem_Malloc(sizeof(*stubUserdata));
    if (stubUserdata == NULL) {
        return NULL;
    }

    stubUserdata->methinfo = methinfo;
    Py_INCREF(methinfo);
    stubUserdata->closureType = PyObjC_Function;

    if (callable) {
        BOOL haveVarArgs = NO;
        BOOL haveVarKwds = NO;

        stubUserdata->argCount = _argcount(callable, &haveVarArgs, &haveVarKwds);
        if (stubUserdata->argCount == -1) {
            Py_DECREF(methinfo);
            PyMem_Free(stubUserdata);
            return NULL;
        }


        if (stubUserdata->argCount == Py_SIZE(methinfo) && !haveVarArgs && !haveVarKwds) {
            /* OK */

        } else if ((stubUserdata->argCount <= 1) && (haveVarArgs || haveVarKwds)) {
            /* OK:
             *    def m(self, *args, **kwds), or
             *    def m(*args, **kwds)
             */

        } else {
            /* Wrong number of arguments, raise an error */
            PyErr_Format(PyObjCExc_BadPrototypeError,
                "Objective-C expects %"PY_FORMAT_SIZE_T"d arguments, Python argument has %d arguments for %R",
                Py_SIZE(methinfo), stubUserdata->argCount,
                callable);
            Py_DECREF(methinfo);
            PyMem_Free(stubUserdata);
            return NULL;
        }

        stubUserdata->callable = callable;
        Py_INCREF(stubUserdata->callable);
    } else {
        stubUserdata->callable = NULL;
        stubUserdata->argCount = 0;
    }

    closure = (PyObjC_callback_function)PyObjCFFI_MakeClosure(methinfo, method_stub, stubUserdata);
    if (closure == NULL) {
        Py_DECREF(methinfo);
        if (stubUserdata->callable) {
            Py_DECREF(stubUserdata->callable);
        }
        PyMem_Free(stubUserdata);
        return NULL;
    }

    return closure;
}


static int
_coloncount(SEL sel)
{
    const char* selname = sel_getName(sel);
    int result = 0;
    while (*selname != 0) {
        if (*selname++ == ':') {
            result ++;
        }
    }
    return result;
}

IMP
PyObjCFFI_MakeIMPForSignature(PyObjCMethodSignature* methinfo, SEL sel, PyObject* callable)
{
    _method_stub_userdata* stubUserdata;
    IMP closure;

    stubUserdata = PyMem_Malloc(sizeof(*stubUserdata));
    if (stubUserdata == NULL) {
        return NULL;
    }

    stubUserdata->methinfo = methinfo;
    Py_INCREF(methinfo);
    stubUserdata->closureType = PyObjC_Method;

    if (callable) {
        BOOL haveVarArgs = NO;
        BOOL haveVarKwds = NO;
        stubUserdata->argCount = _argcount(callable, &haveVarArgs, &haveVarKwds);
        if (stubUserdata->argCount == -1) {
            Py_DECREF(methinfo);
            PyMem_Free(stubUserdata);
            return NULL;
        }

        if (stubUserdata->argCount == Py_SIZE(methinfo) - 1 && !haveVarArgs && !haveVarKwds) {
            /* OK */

        } else if ((stubUserdata->argCount <= 1) && haveVarArgs && haveVarKwds) {
            /* OK */

        } else {
            /* Wrong number of arguments, raise an error */
            PyErr_Format(PyObjCExc_BadPrototypeError,
                "Objective-C expects %"PY_FORMAT_SIZE_T"d arguments, Python argument has %d arguments for %R",
                Py_SIZE(methinfo) - 1, stubUserdata->argCount,
                callable);
            Py_DECREF(methinfo);
            PyMem_Free(stubUserdata);
            return NULL;
        }

        if (!haveVarArgs && !haveVarKwds) {
            /* Check if the number of colons is correct */
            int cc= _coloncount(sel);

            if (cc != 0 && stubUserdata->argCount - 1 != cc) {
                PyErr_Format(PyObjCExc_BadPrototypeError,
                    "Python signature doesn't match implied Objective-C signature for %R",
                    callable);
                Py_DECREF(methinfo);
                PyMem_Free(stubUserdata);
                return NULL;
            }
        }

        stubUserdata->callable = callable;
        Py_INCREF(stubUserdata->callable);
    } else {
        stubUserdata->callable = NULL;
        stubUserdata->argCount = 0;
    }

    closure = PyObjCFFI_MakeClosure(methinfo, method_stub, stubUserdata);
    if (closure == NULL) {
        Py_DECREF(methinfo);
        if (stubUserdata->callable) {
            Py_DECREF(stubUserdata->callable);
        }
        PyMem_Free(stubUserdata);
        return NULL;
    }

    return closure;
}

void
PyObjCFFI_FreeIMP(IMP imp)
{
    _method_stub_userdata* userdata = PyObjCFFI_FreeClosure(imp);

    if (userdata) {
        Py_XDECREF(userdata->methinfo);
        Py_DECREF(userdata->callable);
        PyMem_Free(userdata);
    }
}

IMP
PyObjCFFI_MakeIMPForPyObjCSelector(PyObjCSelector *aSelector)
{
    if (PyObjCNativeSelector_Check(aSelector)) {
        PyObjCNativeSelector *nativeSelector =
            (PyObjCNativeSelector *) aSelector;
        Method aMeth;

        if (nativeSelector->sel_flags & PyObjCSelector_kCLASS_METHOD) {
            aMeth = class_getClassMethod(nativeSelector->sel_class, nativeSelector->sel_selector);

        } else {
            aMeth = class_getInstanceMethod(nativeSelector->sel_class, nativeSelector->sel_selector);
        }

        return method_getImplementation(aMeth);

    } else {
        IMP result;

        PyObjCPythonSelector *pythonSelector = (PyObjCPythonSelector *) aSelector;
        PyObjCMethodSignature* methinfo = PyObjCMethodSignature_ForSelector(
                pythonSelector->sel_class,
                (pythonSelector->sel_flags & PyObjCSelector_kCLASS_METHOD) != 0,
                pythonSelector->sel_selector,
                pythonSelector->sel_python_signature,
                PyObjCNativeSelector_Check(pythonSelector));

        result = PyObjCFFI_MakeIMPForSignature(methinfo, pythonSelector->sel_selector, pythonSelector->callable);
        Py_DECREF(methinfo);
        return result;
    }
}


PyObjCBlockFunction
PyObjCFFI_MakeBlockFunction(PyObjCMethodSignature* methinfo, PyObject* callable)
{
    _method_stub_userdata* stubUserdata;
    PyObjCBlockFunction closure;

    stubUserdata = PyMem_Malloc(sizeof(*stubUserdata));
    if (stubUserdata == NULL) {
        return NULL;
    }

    stubUserdata->methinfo = methinfo;
    Py_INCREF(methinfo);

    stubUserdata->closureType = PyObjC_Block;

    if (callable) {
        BOOL haveVarArgs = NO;
        BOOL haveVarKwds = NO;

        stubUserdata->argCount = _argcount(callable, &haveVarArgs, &haveVarKwds);

        if (stubUserdata->argCount == -1) {
            Py_DECREF(methinfo);
            PyMem_Free(stubUserdata);
            return NULL;
        }

        if (stubUserdata->argCount == Py_SIZE(methinfo) -1 && !haveVarArgs && !haveVarKwds) {
            /* OK */

        } else if ((stubUserdata->argCount <= 1) && haveVarArgs && haveVarKwds) {
            /* OK */

        } else {
            /* Wrong number of arguments, raise an error */
            PyErr_Format(PyObjCExc_BadPrototypeError,
                "Objective-C expects %"PY_FORMAT_SIZE_T"d arguments, Python argument has %d arguments for %R",
                Py_SIZE(methinfo) - 1, stubUserdata->argCount,
                callable);
            Py_DECREF(methinfo);
            PyMem_Free(stubUserdata);
            return NULL;
        }

        stubUserdata->callable = callable;
        Py_INCREF(stubUserdata->callable);

    } else {
        stubUserdata->callable = NULL;
        stubUserdata->argCount = 0;
    }

    closure = (PyObjCBlockFunction)PyObjCFFI_MakeClosure(methinfo, method_stub, stubUserdata);

    if (closure == NULL) {
        Py_DECREF(methinfo);

        if (stubUserdata->callable) {
            Py_DECREF(stubUserdata->callable);
        }

        PyMem_Free(stubUserdata);
        return NULL;
    }

    return closure;
}

void
PyObjCFFI_FreeBlockFunction(PyObjCBlockFunction imp)
{
    _method_stub_userdata* userdata = PyObjCFFI_FreeClosure((IMP)imp);

    if (userdata) {
        Py_XDECREF(userdata->methinfo);
        Py_DECREF(userdata->callable);
        PyMem_Free(userdata);
    }
}

/* Count the number of arguments and their total size */
/* argument_size is not cleared and should be initialized to the amount of
 * bufferspace that will be allocated just before the argument array
 */
int
PyObjCFFI_CountArguments(
        PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
        Py_ssize_t* byref_in_count,
        Py_ssize_t* byref_out_count,
        Py_ssize_t* plain_count,
        Py_ssize_t* argbuf_len,
        BOOL* variadicAllArgs)
{
    Py_ssize_t i;
    Py_ssize_t itemAlign;
    Py_ssize_t itemSize;

    *byref_in_count = *byref_out_count = *plain_count = 0;

    for (i = argOffset; i < Py_SIZE(methinfo); i++) {
        const char *argtype = methinfo->argtype[i].type;

        switch (*argtype) {
        case _C_INOUT:
            if (argtype[1] == _C_PTR && PyObjCPointerWrapper_HaveWrapper(argtype+1)) {
                itemAlign = PyObjCRT_AlignOfType(argtype+1);
                itemSize = PyObjCRT_SizeOfType(argtype+1);

            } else if (argtype[1] == _C_PTR) {
                (*byref_out_count) ++;
                (*byref_in_count) ++;
                itemAlign = PyObjCRT_AlignOfType(argtype+2);
                itemSize = PyObjCRT_SizeOfType(argtype+2);
                if (itemSize == -1) {
                    return -1;
                }

            } else if (argtype[1] == _C_CHARPTR) {
                (*byref_out_count) ++;
                (*byref_in_count) ++;
                itemAlign = PyObjCRT_AlignOfType(gCharEncoding);
                itemSize = PyObjCRT_SizeOfType(gCharEncoding);
                if (itemSize == -1) {
                    return -1;
                }

            } else {
                itemSize = PyObjCRT_SizeOfType(argtype+1);
                itemAlign = PyObjCRT_AlignOfType(argtype+1);
                if (itemSize == -1) {
                    return -1;
                }
            }

            *argbuf_len = align(*argbuf_len, itemAlign);
            (*argbuf_len) += itemSize;
            break;

        case _C_IN: case _C_CONST:
            if (argtype[1] == _C_PTR && argtype[2] == _C_VOID && methinfo->argtype[i].ptrType == PyObjC_kPointerPlain) {
                itemSize = PyObjCRT_SizeOfType(argtype);
                itemAlign = PyObjCRT_AlignOfType(argtype);
                if (itemSize == -1) {
                    return -1;
                }
                *argbuf_len = align(*argbuf_len, itemAlign);
                (*argbuf_len) += itemSize;
                (*plain_count)++;

            } else if (argtype[1] == _C_PTR) {
                (*byref_in_count) ++;
                itemSize = PyObjCRT_SizeOfType(argtype+2);
                itemAlign = PyObjCRT_AlignOfType(argtype+2);
                if (itemSize == -1) {
                    return -1;
                }

            } else if (argtype[1] == _C_CHARPTR) {
                (*byref_in_count) ++;
                itemAlign = PyObjCRT_AlignOfType(gCharEncoding);
                itemSize = PyObjCRT_SizeOfType(gCharEncoding);
                if (itemSize == -1) {
                    return -1;
                }

            } else {
                (*plain_count) ++;
                itemSize = PyObjCRT_SizeOfType(argtype+1);
                itemAlign = PyObjCRT_AlignOfType(argtype+1);
                if (itemSize == -1) {
                    return -1;
                }
            }

            *argbuf_len = align(*argbuf_len, itemAlign);
            (*argbuf_len) += itemSize;
            break;

        case _C_OUT:
            if (argtype[1] == _C_PTR) {
                (*byref_out_count) ++;
                itemSize = PyObjCRT_SizeOfType(argtype+2);
                itemAlign = PyObjCRT_AlignOfType(argtype+2);

                if (itemSize == -1) {
                    return -1;
                }

            } else if (argtype[1] == _C_CHARPTR) {
                (*byref_out_count) ++;
                itemAlign = PyObjCRT_AlignOfType(gCharEncoding);
                itemSize = PyObjCRT_SizeOfType(gCharEncoding);

                if (itemSize == -1) {
                    return -1;
                }

            } else {
                (*plain_count)++;
                itemSize = PyObjCRT_SizeOfType(argtype+1);
                itemAlign = PyObjCRT_AlignOfType(argtype+1);

                if (itemSize == -1) {
                    return -1;
                }
            }

            *argbuf_len = align(*argbuf_len, itemAlign);
            (*argbuf_len) += itemSize;
            break;

        case _C_STRUCT_B: case _C_UNION_B: case _C_ARY_B:
            (*plain_count)++;
            itemSize = PyObjCRT_SizeOfType(argtype);
            itemAlign = PyObjCRT_AlignOfType(argtype);

            if (itemSize == -1) {
                return -1;
            }

            *argbuf_len = align(*argbuf_len, itemAlign);
            (*argbuf_len) += itemSize;
            break;

        default:
            if (methinfo->argtype[i].printfFormat) {
                *variadicAllArgs = YES;
                *argbuf_len += sizeof(NSObject*) * 2;
            }

            itemSize = PyObjCRT_SizeOfType(argtype);
            itemAlign = PyObjCRT_AlignOfType(argtype);
            if (itemSize == -1) {
                return -1;
            }
            *argbuf_len = align(*argbuf_len, itemAlign);
            (*argbuf_len) += itemSize;
            (*plain_count)++;
            break;
        }
    }

    return 0;
}


#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 7
static void imp_capsule_cleanup(void* ptr)
{
    PyObjCFFI_FreeIMP(ptr);
}

static void block_capsule_cleanup(void* ptr)
{
    PyObjCBlock_Release(ptr);
}

#else /* Python >= 2.7 */

static void imp_capsule_cleanup(PyObject* ptr)
{
    PyObjCFFI_FreeIMP(PyCapsule_GetPointer(ptr, "objc.__imp__"));
}

static void block_capsule_cleanup(PyObject* ptr)
{
    PyObjCBlock_Release(PyCapsule_GetPointer(ptr, "objc.__imp__"));
}
#endif /* Python >= 2.7 */


Py_ssize_t
PyObjCFFI_ParseArguments(
        PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
        PyObject* args,
        Py_ssize_t argbuf_cur, unsigned char* argbuf,
        Py_ssize_t argbuf_len __attribute__((__unused__)), // only used in debug builds
        void** byref,
        struct byref_attr* byref_attr,
        ffi_type** arglist, void** values)
{
    Py_ssize_t py_arg = 0;
    Py_ssize_t i;
    void* arg;
    Py_ssize_t count;
    PyObject* seq;
    BOOL have_counted_array = NO;
    PyObject* printf_format = NULL;
    Py_ssize_t sz;
    void* buffer = NULL;
    Py_ssize_t bufferlen = 0;

    /* We have to do two passes over the argument array: the first to deal
     * with plain arguments, the second deals with arrays whose size is
     * the value of another argument.
     */

    Py_ssize_t meth_arg_count;

    if (methinfo->variadic && (methinfo->null_terminated_array || (methinfo->arrayArg != -1))) {
        meth_arg_count = Py_SIZE(methinfo) - 1;

    }  else {
        meth_arg_count = Py_SIZE(methinfo);
    }


    for (i = argOffset; i < meth_arg_count; i++) {

        int error = 0;
        PyObject *argument = NULL;
        const char *argtype = methinfo->argtype[i].type;

        if (argtype[0] == _C_OUT && (
                (argtype[1] == _C_PTR && !PyObjCPointerWrapper_HaveWrapper(argtype + 1))
                 || (argtype[1] == _C_CHARPTR)
            )) {

            /* Just allocate room in argbuf and set that*/
            const char* resttype = argtype+2;
            if (argtype[1] == _C_CHARPTR) {
                resttype = gCharEncoding;
            }

            argument = PyTuple_GET_ITEM (args, py_arg);
            py_arg ++;

            if (argument == Py_None) {
                /* Fall through to the default
                 * behaviour
                 */
                error = 1; /* misuse of this flag ... */

            } else if (argument == PyObjC_NULL) {
                if (methinfo->argtype[i].allowNULL) {

                    byref[i] = NULL;
                    arglist[i] = &ffi_type_pointer;
                    values[i] = byref + i;

                    error = 0;

                } else {
                    PyErr_Format(
                        PyExc_ValueError,
                        "argument %" PY_FORMAT_SIZE_T "d isn't allowed to be NULL",
                        i - argOffset);
                    error = -1;
                }

            } else {

                switch (methinfo->argtype[i].ptrType) {
                case PyObjC_kFixedLengthArray:
                case PyObjC_kVariableLengthArray:
                case PyObjC_kArrayCountInArg:
                    if (PyObject_AsWriteBuffer(argument, &buffer, &bufferlen) != -1) {
                        error = 1;
                        break;

                    } else {
                        PyErr_Clear();
                        /* FALL THROUGH */
                    }

                default:
                    PyErr_Format(
                        PyExc_ValueError,
                        "argument %" PY_FORMAT_SIZE_T "d must be None or objc.NULL",
                        i - argOffset);
                    error = -1;
                }
            }

            if (error == -1) {
                return -1;

            }  else if (error == 0) {
                continue;

            }

            switch (methinfo->argtype[i].ptrType) {
            case PyObjC_kPointerPlain:
                argbuf_cur = align(argbuf_cur,
                    PyObjCRT_AlignOfType(resttype));
                sz = PyObjCRT_SizeOfType(resttype);
                byref[i] = PyMem_Malloc(sz);
                arg = NULL;

                arglist[i] = &ffi_type_pointer;
                values[i] = byref+i;

                /* Clear the output buffer, just in case the called
                 * function doesn't write anything into the buffer.
                 */
                memset(byref[i], 0, sz);
                break;

            case PyObjC_kNullTerminatedArray:
                PyErr_SetString(PyExc_TypeError,
                    "NULL-terminated 'out' arguments are not supported");
                return -1;

            case PyObjC_kFixedLengthArray:
                if (PyObject_AsWriteBuffer(argument, &buffer, &bufferlen) != -1) {

                    count = methinfo->argtype[i].arrayArg;
                    byref_attr[i].token = PyObjC_PythonToCArray(
                        YES, YES,
                        resttype,
                        argument,
                        byref + i,
                        &count,
                        &byref_attr[i].buffer);

                    if (byref_attr[i].token == -1) {
                        return -1;
                    }


                } else {
                    PyErr_Clear();

                    sz = PyObjCRT_SizeOfType(resttype) * methinfo->argtype[i].arrayArg;
                    byref[i] = PyMem_Malloc(sz);
                    if (byref[i] == NULL) {
                        PyErr_NoMemory();
                        return -1;
                    }
                    memset(byref[i], 0, sz);
                }

                arglist[i] = &ffi_type_pointer;
                values[i] = byref+i;
                break;

            case PyObjC_kVariableLengthArray:
                if (PyObject_AsWriteBuffer(argument, &buffer, &bufferlen) != -1) {

                    count = methinfo->argtype[i].arrayArg;
                    byref_attr[i].token = PyObjC_PythonToCArray(
                        YES, YES,
                        resttype,
                        argument,
                        byref + i,
                        NULL,
                        &byref_attr[i].buffer);

                    if (byref_attr[i].token == -1) {
                        return -1;
                    }

                } else {
                    PyErr_Format(PyExc_TypeError,
                        "Need explict buffer for variable-length array argument");
                    return -1;
                }

                arglist[i] = &ffi_type_pointer;
                values[i] = byref+i;
                break;

            case PyObjC_kArrayCountInArg:
                have_counted_array = YES;
                break;
            }

        } else {
            /* Encode argument, maybe after allocating space */

            if (argtype[0] == _C_OUT) argtype ++; /* XXX: is this correct ???? */

            argument = PyTuple_GET_ITEM (args, py_arg);
            switch (*argtype) {
            case _C_STRUCT_B: case _C_ARY_B: case _C_UNION_B:
                /* Allocate space and encode */

                sz = PyObjCRT_SizeOfType(argtype);
                byref[i] = PyMem_Malloc(sz);
                if (byref[i] == NULL) {
                    PyErr_NoMemory();
                    return -1;
                }
                error = depythonify_c_value (
                    argtype,
                    argument,
                    byref[i]);

                arglist[i] = signature_to_ffi_type(argtype);
                                if (arglist[i] == NULL) {
                                    PyErr_Format(PyObjCExc_InternalError,
                                            "Cannot calculate FFI type for %s",
                                            argtype);
                                    return -1;
                                }

                if (*argtype == _C_ARY_B) {
                    values[i] = &byref[i];

                } else {
                    values[i] = byref[i];
                }
                break;

            case _C_INOUT:
            case _C_IN:
            case _C_CONST:
                if (argtype[1] == _C_PTR && argtype[2] == _C_VOID && methinfo->argtype[i].ptrType == PyObjC_kPointerPlain) {
                    argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype));
                    arg = argbuf + argbuf_cur;
                    argbuf_cur += PyObjCRT_SizeOfType(argtype);
                    PyObjC_Assert(argbuf_cur <= argbuf_len, -1);

                    if (methinfo->argtype[i].printfFormat) {
                        printf_format = argument;
                        Py_INCREF(argument);
                    }

                    error = depythonify_c_value (
                        argtype,
                        argument,
                        arg);

                    arglist[i] = signature_to_ffi_type(argtype);
                    values[i] = arg;

                } else if (argtype[1] == _C_CHARPTR || (argtype[1] == _C_PTR && !PyObjCPointerWrapper_HaveWrapper(argtype+1))) {
                    /* Allocate space and encode */
                    const char* resttype = argtype + 2;
                    if (argtype[1] == _C_CHARPTR) {
                        resttype = gCharEncoding;
                    } else if (argtype[2] == _C_UNDEF) {
                        /* This better be a function argument, other types of 'undefined' arguments
                         * aren't supported.
                         */
                        if (methinfo->argtype[i].callable == NULL) {
                            PyErr_SetString(PyExc_ValueError, "calling method/function with 'undefined' argument");
                            return -1;
                        }
                        argbuf_cur = align(argbuf_cur, __alignof__(PyObjC_callback_function));
                        arg = argbuf + argbuf_cur;
                        argbuf_cur += sizeof(PyObjC_callback_function);
                        PyObjC_Assert(argbuf_cur <= argbuf_len, -1);
                        arglist[i] = signature_to_ffi_type(argtype);
                        values[i] = arg;

                        if (argument == Py_None) {
                            *(PyObjC_callback_function*)arg = NULL;

                        } else {
                            PyObjC_callback_function closure;
                            PyObject* v = PyObject_GetAttrString(argument, "pyobjc_closure");
                            if (v == NULL) {
                                if (!methinfo->argtype[i].callableRetained) {
                                    /* The callback isn't retained by the called function,
                                     * therefore we can safely synthesize a closure and
                                     * clean it up after the call.
                                     */
                                    PyErr_Clear();

                                    closure = PyObjCFFI_MakeFunctionClosure(
                                            methinfo->argtype[i].callable,
                                            argument
                                        );
                                    if (closure == NULL) {
                                        return -1;
                                    }
                                    byref_attr[i].buffer = PyCapsule_New(
                                        closure,
                                        "objc.__imp__",
                                        imp_capsule_cleanup);
                                } else {
                                    PyErr_SetString(PyExc_TypeError,
                                        "Callable argument is not a PyObjC closure");
                                    return -1;
                                }

                            } else {
                                if (!PyCapsule_CheckExact(v)) {
                                    PyErr_SetString(PyExc_TypeError,
                                        "Invalid pyobjc_closure attribute");
                                }
                                closure = PyCapsule_GetPointer(v, "objc.__imp__");
                                if (closure == NULL) {
                                    PyErr_SetString(PyExc_TypeError,
                                        "Invalid pyobjc_closure attribute");
                                }
                            }
                            *(PyObjC_callback_function*)arg = closure;
                        }
                        break;
                    }

                    if (argument == PyObjC_NULL || argument == Py_None) {
                        if (methinfo->argtype[i].allowNULL) {

                            byref[i] = NULL;
                            error = 0;
                        } else {
                            PyErr_Format(
                                PyExc_ValueError,
                                "argument %" PY_FORMAT_SIZE_T "d isn't allowed to be NULL", i - argOffset);
                            error = -1;
                        }

                    } else {
                        switch (methinfo->argtype[i].ptrType) {
                        case PyObjC_kPointerPlain:
                            byref[i] = PyMem_Malloc(PyObjCRT_SizeOfType(resttype));
                            error = depythonify_c_value (
                                resttype,
                                argument,
                                byref[i]);
                            break;


                        case PyObjC_kFixedLengthArray:
                            count = methinfo->argtype[i].arrayArg;

                            byref_attr[i].token = PyObjC_PythonToCArray(
                                argtype[0] == _C_INOUT, YES,
                                resttype,
                                argument,
                                byref + i,
                                &count,
                                &byref_attr[i].buffer);
                            if (byref_attr[i].token == -1) {
                                error = -1;
                            } else {
                                error = 0;
                            }
                            break;

                        case PyObjC_kVariableLengthArray:
                             /* TODO: add explicit support for UniChar arrays */
                            byref_attr[i].token = PyObjC_PythonToCArray(
                                    argtype[0] == _C_INOUT, YES,
                                    resttype,
                                    argument,
                                    byref + i,
                                    NULL,
                                    &byref_attr[i].buffer);
                            if (byref_attr[i].token == -1) {
                                error = -1;
                            } else {
                                error = 0;
                            }
                            break;

                        case PyObjC_kNullTerminatedArray:
                             /* TODO: add explicit support for UniChar arrays */
                            if (*resttype == _C_CHAR_AS_TEXT && PyBytes_Check(argument)) {
                                byref[i] = PyMem_Malloc(PyBytes_Size(argument) + 1);
                                memcpy(byref[i], PyBytes_AsString(argument), PyBytes_Size(argument));
                                ((char*)(byref[i]))[PyBytes_Size(argument)] = '\0';

                            } else {
                                seq = NULL;
                                count = c_array_nullterminated_size(argument, &seq);
                                if (seq == NULL) {
                                    error = -1;
                                } else {
                                    byref[i] = PyMem_Malloc(count * PyObjCRT_SizeOfType(resttype));
                                    if (byref[i] == NULL) {
                                        PyErr_NoMemory();
                                        error = -1;
                                    } else {
                                        error = depythonify_c_array_nullterminated(resttype,
                                            count,
                                            seq,
                                            byref[i], methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                                    }
                                    Py_DECREF(seq);
                                }
                            }
                            break;

                        case PyObjC_kArrayCountInArg:
                            have_counted_array = YES;
                            error = 0;
                            break;


                        default:
                            Py_FatalError("Corrupt metadata!");
                        }
                    }

                    arglist[i] = &ffi_type_pointer;
                    values[i] = byref + i;

                } else {
                    /* just encode */
                    argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype+1));
                    arg = argbuf + argbuf_cur;
                    argbuf_cur += PyObjCRT_SizeOfType(argtype+1);
                    PyObjC_Assert(argbuf_cur <= argbuf_len, -1);

                    if (methinfo->argtype[i].printfFormat) {
                        printf_format = argument;
                        Py_INCREF(argument);
                    }
                    error = depythonify_c_value (
                        argtype+1,
                        argument,
                        arg);

                    arglist[i] = signature_to_ffi_type(
                        argtype+1);
                    values[i] = arg;

                }
                break;

            case _C_CHARPTR:

                arglist[i] = NULL;
                if (argument == PyObjC_NULL) {
                    if (methinfo->argtype[i].allowNULL) {
                        byref[i] = NULL;
                        error = 0;

                    } else {
                        PyErr_Format(
                            PyExc_ValueError,
                            "argument %" PY_FORMAT_SIZE_T "d isn't allowed to be NULL", i - argOffset);
                        error = -1;
                    }

                } else {
                    switch (methinfo->argtype[i].ptrType) {
                    case PyObjC_kPointerPlain:
                        argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype));
                        arg = argbuf + argbuf_cur;
                        argbuf_cur += PyObjCRT_SizeOfType(argtype);
                        PyObjC_Assert(argbuf_cur <= argbuf_len, -1);

                        if (methinfo->argtype[i].printfFormat) {
                            printf_format = argument;
                            Py_INCREF(argument);
                        }

                        error = depythonify_c_value (
                            argtype,
                            argument,
                            arg);

                        arglist[i] = signature_to_ffi_type(argtype);
                        values[i] = arg;
                        break;


                    case PyObjC_kFixedLengthArray:
                        {
                            char resttype[] = {  _C_CHR, 0 };
                            count = methinfo->argtype[i].arrayArg;
                            byref_attr[i].token = PyObjC_PythonToCArray(
                                NO, YES,
                                resttype,
                                argument,
                                byref + i,
                                &count,
                                &byref_attr[i].buffer);

                            if (byref_attr[i].token == -1) {
                                error = -1;
                            }
                        }
                        break;

                    case PyObjC_kVariableLengthArray:
                        {
                            const char* buf;
                            Py_ssize_t len;

                            error = PyObject_AsCharBuffer(argument, &buf, &len);
                            if (error != -1) {
                                byref[i] = PyMem_Malloc(len);

                                if (byref[i] == NULL) {
                                    PyErr_NoMemory();
                                    error = -1;

                                } else {
                                    memcpy(byref[i], buf, len);
                                    error = 0;
                                }
                            }
                        }

                        break;

                    case PyObjC_kNullTerminatedArray:
                        {
                            const char* buf;
                            Py_ssize_t len;

                            error = PyObject_AsCharBuffer(argument, &buf, &len);
                            if (error != -1) {
                                byref[i] = PyMem_Malloc(len+1);

                                if (byref[i] == NULL) {
                                    PyErr_NoMemory();
                                    error = -1;

                                } else {
                                    memcpy(byref[i], buf, len);
                                    ((char*)byref[i])[len] = '\0';
                                }

                            } else {
                                error = -1;
                            }
                        }
                        break;

                    case PyObjC_kArrayCountInArg:
                        have_counted_array = YES;
                        error = 0;
                        break;

                    default:
                        Py_FatalError("Corrupt metadata!");
                    }
                }

                if (arglist[i] == NULL) {
                    arglist[i] = &ffi_type_pointer;
                    values[i] = byref + i;
                }
                break;

            case _C_PTR:
                if (argtype[1] == _C_UNDEF) {
                    /* This better be a function argument, other types of 'undefined' arguments
                     * aren't supported.
                     */
                    if (methinfo->argtype[i].callable == NULL) {
                        PyErr_SetString(PyExc_ValueError, "calling method/function with 'undefined' argument");
                        return -1;
                    }

                    argbuf_cur = align(argbuf_cur, __alignof__(PyObjC_callback_function));
                    arg = argbuf + argbuf_cur;
                    argbuf_cur += sizeof(PyObjC_callback_function);
                    PyObjC_Assert(argbuf_cur <= argbuf_len, -1);
                    arglist[i] = signature_to_ffi_type(argtype);
                    values[i] = arg;

                    if (argument == Py_None) {
                        *(PyObjC_callback_function*)arg = NULL;

                    } else {
                        PyObjC_callback_function closure;
                        PyObject* v = PyObject_GetAttrString(argument, "pyobjc_closure");
                        if (v == NULL) {
                            if (!methinfo->argtype[i].callableRetained) {
                                /* The callback isn't retained by the called function,
                                 * therefore we can safely synthesize a closure and
                                 * clean it up after the call.
                                 */
                                PyErr_Clear();

                                closure = PyObjCFFI_MakeFunctionClosure(
                                        methinfo->argtype[i].callable,
                                        argument
                                    );
                                if (closure == NULL) {
                                    return -1;
                                }

                                byref_attr[i].buffer = PyCapsule_New(
                                    closure,
                                    "objc.__imp__",
                                    imp_capsule_cleanup);

                            } else {
                                PyErr_SetString(PyExc_TypeError,
                                    "Callable argument is not a PyObjC closure");
                                return -1;
                            }

                        } else {
                            if (!PyCapsule_CheckExact(v)) {
                                PyErr_SetString(PyExc_TypeError,
                                    "Invalid pyobjc_closure attribute");
                            }

                            closure = PyCapsule_GetPointer(v, "objc.__imp__");
                            if (closure == NULL) {
                                PyErr_SetString(PyExc_TypeError,
                                    "Invalid pyobjc_closure attribute");
                            }
                        }
                        *(PyObjC_callback_function*)arg = closure;
                    }
                    break;
                } else {
                    /* FALL THROUGH */
                }

            case _C_ID:
                if (argtype[1] == '?') {
                    /* Argument is a block */
                    if (methinfo->argtype[i].callable == NULL) {
                        PyErr_Format(PyExc_TypeError, "Argument %"PY_FORMAT_SIZE_T"d is a block, but no signature available", i);
                        return -1;
                    }
                    argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype));
                    arg = argbuf + argbuf_cur;
                    argbuf_cur += PyObjCRT_SizeOfType(argtype);
                    PyObjC_Assert(argbuf_cur <= argbuf_len, -1);
                    *(void**)arg = PyObjCBlock_Create(
                        methinfo->argtype[i].callable, argument);
                    if (*(void**)arg == NULL) {
                        return -1;
                    }
                    byref_attr[i].buffer = PyCapsule_New(
                        *(void**)arg,
                        "objc.__block__",
                        block_capsule_cleanup);
                    arglist[i] = signature_to_ffi_type(argtype);
                    values[i] = arg;

                    break;
                }
                /* else: fallthrough */

            default:
                argbuf_cur = align(argbuf_cur, PyObjCRT_AlignOfType(argtype));
                arg = argbuf + argbuf_cur;
                argbuf_cur += PyObjCRT_SizeOfType(argtype);
                PyObjC_Assert(argbuf_cur <= argbuf_len, -1);

                if (methinfo->argtype[i].printfFormat) {
                    printf_format = argument;
                    Py_INCREF(argument);
                }

                error = depythonify_c_value (
                    argtype,
                    argument,
                    arg);

                arglist[i] = signature_to_ffi_type(argtype);
                values[i] = arg;
            }

            if (error == -1) {
                return -1;
            }
            py_arg++;
        }
    }

    if (have_counted_array) {
        py_arg = 0;

        for (i = argOffset; i < meth_arg_count; i++) {
            PyObject *argument = NULL;
            const char *argtype = methinfo->argtype[i].type;

            if (argtype[0] == _C_OUT && (argtype[1] == _C_PTR || argtype[1] == _C_CHARPTR)) {
                argument = PyTuple_GET_ITEM (args, py_arg);
                py_arg ++;

                const char* resttype = argtype+2;
                if (argtype[1] == _C_CHARPTR) {
                    resttype = gCharEncoding;
                }

                if (methinfo->argtype[i].ptrType == PyObjC_kArrayCountInArg) {
                    count = extract_count(
                            methinfo->argtype[methinfo->argtype[i].arrayArg].type,
                            values[methinfo->argtype[i].arrayArg]);

                    if (count == -1 && PyErr_Occurred()) {
                        return -1;
                    }

                    if (argument && (PyObject_AsWriteBuffer(argument, &buffer, &bufferlen) != -1)) {
                        byref_attr[i].token = PyObjC_PythonToCArray(
                            YES, YES,
                            resttype,
                            argument,
                            byref + i,
                            &count,
                            &byref_attr[i].buffer);
                        if (byref_attr[i].token == -1) {
                            return -1;
                        }

                    } else {
                        PyErr_Clear();

                        byref[i] = PyMem_Malloc(count * PyObjCRT_SizeOfType(resttype));
                        if (byref[i] == NULL) {
                            PyErr_NoMemory();
                            return -1;
                        } else {
                            memset(byref[i], 0, count * PyObjCRT_SizeOfType(resttype));
                        }
                    }
                }

                arglist[i] = &ffi_type_pointer;
                values[i] = byref + i;

            } else {
                /* Encode argument, maybe after allocating space */
                if (argtype[0] == _C_OUT) argtype ++;

                argument = PyTuple_GET_ITEM (args, py_arg);
                py_arg ++;

                switch (*argtype) {
                case _C_INOUT:
                case _C_IN:
                case _C_CONST:
                    if (argtype[1] == _C_PTR || argtype[1] == _C_CHARPTR) {
                        /* Allocate space and encode */
                        const char* resttype = argtype+2;
                        if (argtype[1] == _C_CHARPTR) {
                            resttype = gCharEncoding;
                        }

                        if (argument != PyObjC_NULL) {
                            switch (methinfo->argtype[i].ptrType) {
                            case PyObjC_kPointerPlain:
                            case PyObjC_kNullTerminatedArray:
                            case PyObjC_kFixedLengthArray:
                            case PyObjC_kVariableLengthArray:
                                /* To keep the compiler happy */
                                break;

                            case PyObjC_kArrayCountInArg:
                                count = extract_count(
                                        methinfo->argtype[methinfo->argtype[i].arrayArg].type,
                                        values[methinfo->argtype[i].arrayArg]);
                                if (count == -1 && PyErr_Occurred()) {
                                    return -1;
                                }

                                byref_attr[i].token = PyObjC_PythonToCArray(
                                    argtype[0] == _C_INOUT, NO,
                                    resttype,
                                    argument,
                                    byref + i,
                                    &count,
                                    &byref_attr[i].buffer);
                                if (byref_attr[i].token == -1) {
                                    return -1;
                                }

                                arglist[i] = &ffi_type_pointer;
                                values[i] = byref + i;
                                break;
                            }
                        }
                    }
                    break;

                case _C_CHARPTR:
                    if (argument != PyObjC_NULL) {
                        switch (methinfo->argtype[i].ptrType) {
                        case PyObjC_kPointerPlain:
                        case PyObjC_kNullTerminatedArray:
                        case PyObjC_kFixedLengthArray:
                        case PyObjC_kVariableLengthArray:
                            /* To keep the compiler happy */
                            break;

                        case PyObjC_kArrayCountInArg:
                            count = extract_count(
                                    methinfo->argtype[methinfo->argtype[i].arrayArg].type,
                                    values[methinfo->argtype[i].arrayArg]);
                            if (count == -1 && PyErr_Occurred()) {
                                return -1;
                            }
                            byref_attr[i].token = PyObjC_PythonToCArray(
                                    NO, NO,
                                    gCharEncoding,
                                    argument,
                                    byref + i,
                                    &count,
                                    &byref_attr[i].buffer);
                            if (byref_attr[i].token == -1) {
                                return -1;
                            }
                            arglist[i] = &ffi_type_pointer;
                            values[i] = byref + i;
                        }
                    }
                }
            }
        }
    }

    if (printf_format) {
        Py_ssize_t r;

        r = parse_printf_args(
            printf_format,
            args, py_arg,
            byref, byref_attr,
            arglist, values,
            Py_SIZE(methinfo));
        if (r == -1) {
            return -1;
        }

        Py_DECREF(printf_format);
        printf_format = NULL;

        return r;

    } else if (methinfo->variadic && methinfo->null_terminated_array) {
        Py_ssize_t r;

        r = parse_varargs_array(
                methinfo,
                args, py_arg, byref,
                arglist, values, -1);

        if (r == -1) {
            return -1;
        }

        return r;

    } else if (methinfo->variadic && methinfo->arrayArg != -1) {
        Py_ssize_t r;
        Py_ssize_t cnt = extract_count(
            methinfo->argtype[methinfo->arrayArg].type,
            values[methinfo->arrayArg]);

        if (cnt == -1) {
            return -1;
        }

        r = parse_varargs_array(
                methinfo,
                args, py_arg, byref,
                arglist, values, cnt);

        if (r == -1) {
            return -1;
        }
        return r;
    }

    return Py_SIZE(methinfo);
}


PyObject*
PyObjCFFI_BuildResult(
    PyObjCMethodSignature* methinfo, Py_ssize_t argOffset,
    void* pRetval, void** byref, struct byref_attr* byref_attr,
    Py_ssize_t byref_out_count, PyObject* self, int flags,
    void** argvalues)
{
    PyObject* objc_result = NULL;
    PyObject* result = NULL;
    int py_arg;
    void* arg;
    Py_ssize_t i;
    Py_ssize_t count;

    if ( (*methinfo->rettype.type != _C_VOID) /* && (![methinfo isOneway]) */ ) {
        const char* tp = methinfo->rettype.type;
        BOOL isOut = NO;

        if (tp[0] == _C_CONST) {
            tp++;
        }

        if (tp[0] == _C_OUT) {
            isOut = YES;
            tp++;
        }

        /* Pointer values: */
        if (tp[0] == _C_PTR && tp[1] == _C_UNDEF && methinfo->rettype.callable) {
            if (*(void**)pRetval == NULL) {
                objc_result = Py_None;
                Py_INCREF(Py_None);

            } else {
                objc_result = PyObjCFunc_WithMethodSignature(NULL, *(void**)pRetval, methinfo->rettype.callable);
                if (objc_result == NULL) {
                    return NULL;
                }
            }

        } else if (*tp == _C_CHARPTR || (*tp == _C_PTR && !PyObjCPointerWrapper_HaveWrapper(tp))) {
            const char* resttype = tp + 1;

            if (*tp == _C_CHARPTR) {
                resttype = gCharEncoding;
            }

            if (isOut) {
                objc_result = pythonify_c_return_value (resttype, *(void**)pRetval);
                if (objc_result == NULL) {
                    return NULL;
                }

                if (methinfo->rettype.alreadyRetained) {
                    if (PyObjCObject_Check(objc_result)) {
                        /* pythonify_c_return_value has retained the object, but we already
                         * own a reference, therefore give the ref away again
                         */
                        [PyObjCObject_GetObject(objc_result) release];
                    }
                }

                if (methinfo->rettype.alreadyCFRetained) {
                    if (PyObjCObject_Check(objc_result)) {
                        /* pythonify_c_return_value has retained the object, but we already
                         * own a reference, therefore give the ref away again
                         */
                        CFRelease(PyObjCObject_GetObject(objc_result));
                    }
                }

            } else {

                switch (methinfo->rettype.ptrType) {
                case PyObjC_kPointerPlain:
                    /* 'Fall through' to default behaviour */
                    break;

                case PyObjC_kNullTerminatedArray:
                    if (*(void**)pRetval == NULL) {
                        Py_INCREF(PyObjC_NULL);
                        objc_result = PyObjC_NULL;
                    } else {
                        objc_result = pythonify_c_array_nullterminated(resttype, *(void**)pRetval, methinfo->rettype.alreadyRetained, methinfo->rettype.alreadyCFRetained);
                        if (objc_result == NULL) {
                            return NULL;
                        }
                    }
                    break;

                case PyObjC_kFixedLengthArray:
                    if (*(void**)pRetval == NULL) {
                        Py_INCREF(PyObjC_NULL);
                        objc_result = PyObjC_NULL;

                    } else {
                        objc_result = PyObjC_CArrayToPython2(
                            resttype,
                            *(void**)pRetval,
                            methinfo->rettype.arrayArg, methinfo->rettype.alreadyRetained, methinfo->rettype.alreadyCFRetained);
                        if (objc_result == NULL) {
                            return NULL;
                        }
                    }
                    break;

                case PyObjC_kVariableLengthArray:
                    /* FIXME: explict support for UniChar buffers */
                    if (*(void**)pRetval == NULL) {
                        Py_INCREF(PyObjC_NULL);
                        objc_result = PyObjC_NULL;

                    } else {
                        objc_result = PyObjC_VarList_New(resttype, *(void**)pRetval);
                    }
                    break;

                case PyObjC_kArrayCountInArg:

                    if (*(void**)pRetval == NULL) {
                        Py_INCREF(PyObjC_NULL);
                        objc_result = PyObjC_NULL;

                    } else {
                        count = extract_count(methinfo->argtype[methinfo->rettype.arrayArg].type, argvalues[methinfo->rettype.arrayArg]);

                        if (count == -1 && PyErr_Occurred()) {
                                return NULL;
                        }

                        objc_result = PyObjC_CArrayToPython2(
                            resttype,
                            *(void**)pRetval,
                            count, methinfo->rettype.alreadyRetained, methinfo->rettype.alreadyCFRetained);

                        if (objc_result == NULL) {
                            return NULL;
                        }
                    }
                    break;

                default:
                    PyErr_Format(PyExc_SystemError,
                        "Unhandled pointer type: %d",
                        methinfo->rettype.ptrType);
                    return NULL;
                }

                if (methinfo->free_result) {
                    free(*(void**)pRetval);
                }

            }
         }

        /* default behaviour: */
        if (objc_result == NULL) {
            if (tp[0] == _C_ID && tp[1] == '?') {
                /* The value is a block, those values are
                 * treated slightly differently than normal:
                 * - always use -copy on them to ensure we
                 *   can safely store them.
                 * - try to attach the calling signature to the
                 *   block.
                 */
                id v = [*(id*)pRetval copy];
                objc_result = pythonify_c_return_value (tp, &v);
                [v release];
                if (objc_result == NULL) {
                    return NULL;
                }

                if (PyObjCObject_IsBlock(objc_result) && PyObjCObject_GetBlock(objc_result) == NULL) {
                    /* Result is an (Objective-)C block for which we don't have a Python signature
                     *
                     * 1) Try to extract from the metadata system
                     * 2) Try to extract from the ObjC runtime
                     *
                     * Both systems may not have the required information.
                     */

                    if (methinfo->rettype.callable != NULL) {
                        PyObjCObject_SET_BLOCK(objc_result, methinfo->rettype.callable);
                        Py_INCREF(methinfo->rettype.callable);
                    } else {
                        const char* signature = PyObjCBlock_GetSignature(objc_result);
                        if (signature != NULL) {
                            PyObjCMethodSignature* sig = PyObjCMethodSignature_WithMetaData(signature, NULL, YES);
                            if (sig == NULL) {
                                Py_DECREF(objc_result);
                                return NULL;
                            }
                            PyObjCObject_SET_BLOCK(objc_result, sig);
                            sig = NULL;
                        }
                    }
                }
            } else {

                objc_result = pythonify_c_return_value (tp, pRetval);
                if (objc_result == NULL) {
                    return NULL;
                }

            }

            if (methinfo->rettype.alreadyRetained) {
                if (PyObjCObject_Check(objc_result)) {
                    /* pythonify_c_return_value has retained the object, but we already
                     * own a reference, therefore give the ref away again
                     */
                    [PyObjCObject_GetObject(objc_result) release];
                }
            }

            if (methinfo->rettype.alreadyCFRetained) {
                if (PyObjCObject_Check(objc_result)) {
                    /* pythonify_c_return_value has retained the object, but we already
                     * own a reference, therefore give the ref away again
                     */
                    CFRelease(PyObjCObject_GetObject(objc_result));
                }
            }
        }
    } else {
        Py_INCREF(Py_None);
        objc_result =  Py_None;
    }

    /* XXX: This is for selectors only, need to change this !!!! */

    if (self != NULL && objc_result != self
        && PyObjCObject_Check(self) && PyObjCObject_Check(objc_result)
        && !(flags & PyObjCSelector_kRETURNS_UNINITIALIZED)
        && (((PyObjCObject*)self)->flags & PyObjCObject_kUNINITIALIZED)) {
        [PyObjCObject_GetObject(objc_result) release];
        PyObjCObject_ClearObject(self);
    }

    if (byref_out_count == 0) {
        return objc_result;

    } else {

        if (*methinfo->rettype.type == _C_VOID) {
            if (byref_out_count > 1) {
                result = PyTuple_New(byref_out_count);
                if (result == NULL) {
                    return NULL;
                }
            } else {
                result = NULL;
            }
            Py_DECREF(objc_result);
            py_arg = 0;

        } else {
            result = PyTuple_New(byref_out_count+1);
            if (result == NULL) {
                return NULL;
            }
            PyTuple_SET_ITEM(result, 0, objc_result);
            py_arg = 1;
        }

        objc_result = NULL;

        for (i = argOffset; i < Py_SIZE(methinfo); i++) {
            const char *argtype = methinfo->argtype[i].type;
            PyObject*   v = NULL;

            switch (*argtype) {
            case _C_INOUT:
            case _C_OUT:
                if (argtype[1] == _C_CHARPTR || (argtype[1] == _C_PTR && !PyObjCPointerWrapper_HaveWrapper(argtype+1))) {
                    const char* resttype = argtype+2;
                    if (argtype[1] == _C_CHARPTR) {
                        resttype = gCharEncoding;
                    }

                    arg = byref[i];

                    if (arg == NULL) {
                        v = PyObjC_NULL;
                        Py_INCREF(v);

                    } else if (byref_attr[i].buffer != NULL) {
                        v = byref_attr[i].buffer;
                        Py_INCREF(v);

                    } else {
                        switch (methinfo->argtype[i].ptrType) {
                        case PyObjC_kPointerPlain:

                            if (resttype[0] == _C_ID && resttype[1] == '?') {
                                id tmp = [*(id*)arg copy];
                                v = pythonify_c_value(resttype, &tmp);
                                [tmp release];

                                if (methinfo->argtype[i].callable != NULL) {
                                    if (PyObjCObject_IsBlock(v) && PyObjCObject_GetBlock(v) == NULL) {
                                        PyObjCObject_SET_BLOCK(v, methinfo->argtype[i].callable);
                                        Py_INCREF(methinfo->argtype[i].callable);
                                    }
                                }
                            } else {
                                v = pythonify_c_value(resttype, arg);
                            }
                            if (methinfo->argtype[i].alreadyRetained && PyObjCObject_Check(v)) {
                                [PyObjCObject_GetObject(v) release];
                            }
                            if (methinfo->argtype[i].alreadyCFRetained && PyObjCObject_Check(v)) {
                                CFRelease(PyObjCObject_GetObject(v));
                            }
                            if (!v) goto error_cleanup;
                            break;

                        case PyObjC_kFixedLengthArray:
                            if (methinfo->argtype[i].arraySizeInRetval) {
                                count = extract_count(methinfo->rettype.type, pRetval);
                                if (count == -1 && PyErr_Occurred()) goto error_cleanup;

                            } else {
                                count = methinfo->argtype[i].arrayArg;
                            }

                            if (*resttype == _C_UNICHAR) {

                                int byteorder = 0;
                                v = PyUnicode_DecodeUTF16(
                                    arg, count*2, NULL, &byteorder);
                                if (!v) goto error_cleanup;

                            } else {
                                v = PyObjC_CArrayToPython2(resttype,
                                    arg,
                                    count, methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                                if (!v) goto error_cleanup;
                            }
                            break;

                        case PyObjC_kVariableLengthArray:
                             /* TODO: add support for UniChar arrays */
                            if (methinfo->argtype[i].arraySizeInRetval) {
                                count = extract_count(methinfo->rettype.type, pRetval);
                                if (count == -1 && PyErr_Occurred()) goto error_cleanup;

                                v = PyObjC_CArrayToPython2(resttype,
                                    arg,
                                    count, methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                                if (!v) goto error_cleanup;

                            } else {
                                v = PyObjC_VarList_New(methinfo->rettype.type, pRetval);
                                if (!v) goto error_cleanup;
                            }

                            break;

                        case PyObjC_kNullTerminatedArray:
                             /* TODO: add support for UniChar arrays */
                            v = pythonify_c_array_nullterminated(
                                resttype, arg, methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                            if (!v) goto error_cleanup;
                            break;

                        case PyObjC_kArrayCountInArg:
                            if (methinfo->argtype[i].arraySizeInRetval) {
                                count = extract_count(methinfo->rettype.type, pRetval);

                            } else {
                                count = extract_count(
                                    methinfo->argtype[methinfo->argtype[i].arrayArgOut].type,
                                    argvalues[methinfo->argtype[i].arrayArgOut]);
                            }
                            if (count == -1 && PyErr_Occurred()) goto error_cleanup;

                            if (*resttype == _C_UNICHAR) {
                                int byteorder = 0;
                                v = PyUnicode_DecodeUTF16(
                                    arg, count*2, NULL, &byteorder);
                                if (!v) goto error_cleanup;

                            } else {
                                v = PyObjC_CArrayToPython2(
                                    resttype,
                                    arg,
                                    count, methinfo->argtype[i].alreadyRetained, methinfo->argtype[i].alreadyCFRetained);
                            }

                            if (v == NULL) goto error_cleanup;
                            break;
                        }
                    }

                    if (result != NULL) {
                        if (PyTuple_SetItem(result,
                            py_arg++, v) < 0) {

                            Py_DECREF(v);
                            goto error_cleanup;
                        }
                    } else {
                        result = v;
                    }

                }
                break;
            }
        }
    }

    return result;

error_cleanup:
    Py_XDECREF(result);
    return NULL;
}

int PyObjCFFI_AllocByRef(Py_ssize_t argcount, void*** byref, struct byref_attr** byref_attr)
{
    *byref = NULL; *byref_attr = NULL;

    *byref = PyMem_Malloc(sizeof(void*) * argcount);
    if (*byref == NULL) {
        PyErr_NoMemory();
        return -1;
    }
    memset(*byref, 0, sizeof(void*) * argcount);

    *byref_attr = PyMem_Malloc(sizeof(struct byref_attr) * argcount);
    if (*byref_attr == NULL) {
        free(*byref);
        *byref = NULL;

        PyErr_NoMemory();
        return -1;
    }
    memset(*byref_attr, 0, sizeof(struct byref_attr) * argcount);

    return 0;
}

int PyObjCFFI_FreeByRef(Py_ssize_t argcount, void** byref, struct byref_attr* byref_attr)
{
    Py_ssize_t i;
    if (byref) {
        for (i = 0; i < argcount; i++) {
            if (byref[i] == NULL) continue;

            if (byref_attr[i].token != 0) {
                PyObjC_FreeCArray(byref_attr[i].token, byref[i]);
                byref[i] = NULL;

                Py_XDECREF(byref_attr[i].buffer); byref_attr[i].buffer = NULL;

            } else {
                PyMem_Free(byref[i]); byref[i] = NULL;
            }
        }
        PyMem_Free(byref);
    }

    if (byref_attr) {
        PyMem_Free(byref_attr);
    }

    return 0;
}

int
PyObjCRT_ResultUsesStret(const char* typestr)
{
    Py_ssize_t resultSize = PyObjCRT_SizeOfReturnType(typestr);
    if (resultSize == -1) {
        return -1;
    }

    if (*typestr == _C_STRUCT_B &&
#ifdef  __ppc64__
        ffi64_stret_needs_ptr((typestr), NULL, NULL)

#else /* !__ppc64__ */
        (resultSize > SMALL_STRUCT_LIMIT
#ifdef __i386__
         /* darwin/x86 ABI is slightly odd ;-) */
         || (resultSize != 1
            && resultSize != 2
            && resultSize != 4
            && resultSize != 8)
#endif
#ifdef __x86_64__
             /* darwin/x86-64 ABI is slightly odd ;-) */
         || (resultSize != 1
            && resultSize != 2
            && resultSize != 4
            && resultSize != 8
            && resultSize != 16
            )
#endif
        )
#endif /* !__ppc64__ */
        ) {

        return 1;
    } else {
        return 0;
    }
}


PyObject *
PyObjCFFI_Caller(PyObject *aMeth, PyObject* self, PyObject *args)
{
    Py_ssize_t argbuf_len = 0;
    Py_ssize_t argbuf_cur = 0;
    unsigned char* argbuf = NULL;
    Py_ssize_t byref_in_count = 0;
    Py_ssize_t byref_out_count = 0;
    Py_ssize_t plain_count = 0;
    void** byref = NULL; /* offset for arguments in argbuf */
    struct byref_attr* byref_attr = NULL;
    const char*       rettype;
    PyObjCMethodSignature*  methinfo;
    PyObjCNativeSelector* meth = (PyObjCNativeSelector*)aMeth;
    PyObject* objc_result = NULL;
    PyObject* result = NULL;
    id self_obj = nil;
    struct objc_super super;
    struct objc_super* superPtr;
    ffi_cif cif;
    ffi_type* arglist[128]; /* XX: Magic constant */
    void* values[128];
    Py_ssize_t r;
    void* msgResult;
    Py_ssize_t resultSize;
    int useStret;
    int flags;
    SEL theSel;
    int isUninitialized;
    BOOL variadicAllArgs = NO;

    if (PyObjCIMP_Check(aMeth)) {
        methinfo = PyObjCIMP_GetSignature(aMeth);
        flags = PyObjCIMP_GetFlags(aMeth);

    } else {
        methinfo = PyObjCSelector_GetMetadata(aMeth);
        if (methinfo == NULL) {
            return NULL;
        }
        flags = meth->sel_flags;
    }

    rettype = methinfo->rettype.type;
    variadicAllArgs = methinfo->variadic && (methinfo->null_terminated_array || methinfo->arrayArg != -1);

    if (methinfo->suggestion != NULL) {
        PyErr_SetObject(PyExc_TypeError, methinfo->suggestion);
        return NULL;
    }

    if (Py_SIZE(methinfo) >= 127) {
         PyErr_Format(PyObjCExc_Error,
             "wrapping a function with %"PY_FORMAT_SIZE_T"d arguments, at most 64 "
             "are supported", Py_SIZE(methinfo));
         return NULL;
    }

    resultSize = PyObjCRT_SizeOfReturnType(rettype);
    if (resultSize == -1) {
        return NULL;
    }

    /* First count the number of by reference parameters, and the number
     * of bytes of storage needed for them. Note that arguments 0 and 1
     * are self and the selector, no need to count those.
     */
    argbuf_len = align(resultSize, sizeof(void*));
    r = PyObjCFFI_CountArguments(
        methinfo, 2,
        &byref_in_count,
        &byref_out_count,
        &plain_count,
        &argbuf_len,
        &variadicAllArgs);
    if (r == -1) {
        return NULL;
    }

    /*
     * We need input arguments for every normal argument and for every
     * input argument that is passed by reference.
     */
    if (variadicAllArgs) {
        if (byref_in_count != 0 || byref_out_count != 0) {
            PyErr_Format(PyExc_TypeError, "Sorry, printf format with by-ref args not supported");
            goto error_cleanup;
        }

        if (methinfo->null_terminated_array) {
            if (PyTuple_Size(args) < Py_SIZE(methinfo) - 3) {
                PyErr_Format(PyExc_TypeError,
                    "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
                    Py_SIZE(methinfo) - 3,
                    PyTuple_Size(args));
                goto error_cleanup;
            }

        } else if (PyTuple_Size(args) < Py_SIZE(methinfo) - 2) {
            PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
            Py_SIZE(methinfo) - 2, PyTuple_Size(args));
            goto error_cleanup;
        }

        if (PyTuple_Size(args) > 127) {
            PyErr_Format(PyExc_TypeError, "At most %d arguments are supported, got %" PY_FORMAT_SIZE_T "d arguments", 127, PyTuple_Size(args));
            goto error_cleanup;
        }

    } else if (PyTuple_Size(args) != Py_SIZE(methinfo) - 2) {

        PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
            Py_SIZE(methinfo) - 2, PyTuple_Size(args));
        goto error_cleanup;
    }

    argbuf = PyMem_Malloc(argbuf_len);
    if (argbuf == 0) {
        PyErr_NoMemory();
        goto error_cleanup;
    }

    if (variadicAllArgs) {
        if (PyObjCFFI_AllocByRef(Py_SIZE(methinfo)+PyTuple_Size(args),
                    &byref, &byref_attr) < 0) {
            goto error_cleanup;
        }

    } else {
        if (PyObjCFFI_AllocByRef(Py_SIZE(methinfo), &byref, &byref_attr) < 0) {
            goto error_cleanup;
        }
    }

    /* Set 'self' argument, for class methods we use the class */
    if (flags & PyObjCSelector_kCLASS_METHOD) {
        if (PyObjCObject_Check(self)) {
            self_obj = PyObjCObject_GetObject(self);
            if (self_obj != NULL) {
                self_obj = object_getClass(self_obj);
            }

        } else if (PyObjCClass_Check(self)) {
            self_obj = PyObjCClass_GetClass(self);


        } else if (PyType_Check(self) && PyType_IsSubtype((PyTypeObject*)self, &PyType_Type)) {
            PyObject* c = PyObjCClass_ClassForMetaClass(self);
            if (c == NULL) {
                self_obj = nil;

            } else {
                self_obj = PyObjCClass_GetClass(c);
            }

        } else {
            PyErr_Format(PyExc_TypeError,
                "Need objective-C object or class as self, not an instance of '%s'",
                    Py_TYPE(self)->tp_name);
            goto error_cleanup;
        }

    } else {
        int err;
        if (PyObjCObject_Check(self)) {
            self_obj = PyObjCObject_GetObject(self);

        } else {
            err = depythonify_c_value(@encode(id), self, &self_obj);
            if (err == -1) {
                goto error_cleanup;
            }
        }
    }
    /* XXX: Ronald: why the XXX? */


    useStret = 0;

    if (PyObjCIMP_Check(aMeth)) {
        useStret = 0;
        theSel = PyObjCIMP_GetSelector(aMeth);
        arglist[0] = &ffi_type_pointer;
        values[0] = &self_obj;
        arglist[1] = &ffi_type_pointer;
        values[1] = &theSel;
        msgResult = argbuf;
        argbuf_cur = align(resultSize, sizeof(void*));

    } else {
        objc_superSetReceiver(super, self_obj);
        if (meth->sel_flags & PyObjCSelector_kCLASS_METHOD) {
            objc_superSetClass(super,
                    object_getClass(meth->sel_class));
        } else {
            objc_superSetClass(super,  meth->sel_class);
        }

        useStret = PyObjCRT_ResultUsesStret(rettype);
        if (useStret == -1) {
            goto error_cleanup;
        }

        superPtr = &super;
        arglist[ 0] = &ffi_type_pointer;
        values[ 0] = &superPtr;
        arglist[ 1] = &ffi_type_pointer;
        values[ 1] = &meth->sel_selector;
        theSel = meth->sel_selector;
        msgResult = argbuf;
        argbuf_cur = align(resultSize, sizeof(void*));
    }

    r = PyObjCFFI_ParseArguments(methinfo, 2, args,
        argbuf_cur, argbuf, argbuf_len, byref, byref_attr,
        arglist, values);
    if (r == -1) {
        goto error_cleanup;
    }


    PyErr_Clear();
    ffi_type* retsig = PyObjCFFI_Typestr2FFI(rettype);
    if (retsig == NULL) goto error_cleanup;
    r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, (int)r, retsig, arglist);
    if (r != FFI_OK) {
        PyErr_Format(PyExc_RuntimeError,
            "Cannot setup FFI CIF [%d]", r);
        goto error_cleanup;
    }

    if (PyObjCObject_Check(self)) {
        isUninitialized = ((PyObjCObject*)self)->flags  & PyObjCObject_kUNINITIALIZED;
        ((PyObjCObject*)self)->flags  &= ~PyObjCObject_kUNINITIALIZED;
    } else {
        isUninitialized = NO;
    }

    PyObjC_DURING
        if (PyObjCIMP_Check(aMeth)) {
            ffi_call(&cif, FFI_FN(PyObjCIMP_GetIMP(aMeth)),
                msgResult, values);

        } else {

            if (useStret) {
                ffi_call(&cif, FFI_FN(objc_msgSendSuper_stret),
                    msgResult, values);
            } else {
                ffi_call(&cif, FFI_FN(objc_msgSendSuper),
                    msgResult, values);

            }
        }

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (isUninitialized && PyObjCObject_Check(self)) {
        ((PyObjCObject*)self)->flags  |= PyObjCObject_kUNINITIALIZED;
    }

    if (PyErr_Occurred()) goto error_cleanup;

    result = PyObjCFFI_BuildResult(methinfo, 2, msgResult, byref,
            byref_attr, byref_out_count,
            self, flags, values);

    if (variadicAllArgs) {
        if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo)+PyTuple_Size(args), byref, byref_attr) < 0) {
            byref = NULL; byref_attr = NULL;
            goto error_cleanup;
        }

    } else {
        if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo), byref, byref_attr) < 0) {
            byref = NULL; byref_attr = NULL;
            goto error_cleanup;
        }
    }

    PyMem_Free(argbuf); argbuf = NULL;
    methinfo = NULL;

    return result;

error_cleanup:

    if (objc_result) {
        Py_DECREF(objc_result);
        objc_result = NULL;
    }

    if (result) {
        Py_DECREF(result);
        result = NULL;
    }

    if (variadicAllArgs) {
        if (PyObjCFFI_FreeByRef(PyTuple_Size(args), byref, byref_attr) < 0) {
            byref = NULL; byref_attr = NULL;
            goto error_cleanup;
        }

    } else {
        if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo), byref, byref_attr) < 0) {
            byref = NULL; byref_attr = NULL;
            goto error_cleanup;
        }
    }

    if (argbuf) {
        PyMem_Free(argbuf);
        argbuf = NULL;
    }
    return NULL;
}

/*
 * PyObjCFFI_CIFForSignature - Create CIF for a method signature
 *
 * return the CIF, return NULL on error. pArgOffset is set to 1 if the method
 * should be called using objc_sendMsg_sret (using a pointer to the return value
 * as an initial argument), and is set to 0 otherwise.
 */
ffi_cif*
PyObjCFFI_CIFForSignature(PyObjCMethodSignature* methinfo)
{
    ffi_cif* cif;
    ffi_type** cl_arg_types;
    ffi_type* cl_ret_type;
    const char* rettype;
    ffi_status rv;
    int i;

    rettype = methinfo->rettype.type;

    cl_ret_type = PyObjCFFI_Typestr2FFI(rettype);
    if (cl_ret_type == NULL) {
        return NULL;
    }

    /* Build FFI argumentlist description */
    cl_arg_types = PyMem_Malloc(sizeof(ffi_type*) * (2 + Py_SIZE(methinfo)));
    if (cl_arg_types == NULL) {
        PyMem_Free(cl_ret_type);
        PyErr_NoMemory();
        return NULL;
    }

    for (i = 0; i < Py_SIZE(methinfo); i++) {
        cl_arg_types[i] = signature_to_ffi_type(
            methinfo->argtype[i].type);
        if (cl_arg_types[i] == NULL) {
            PyMem_Free(cl_arg_types);
            return NULL;
        }
    }

    /* Create the invocation description */
    cif = PyMem_Malloc(sizeof(*cif));
    if (cif == NULL) {
        PyMem_Free(cl_arg_types);
        PyErr_NoMemory();
        return NULL;
    }

    rv = ffi_prep_cif(cif, FFI_DEFAULT_ABI, (int)Py_SIZE(methinfo),
        cl_ret_type, cl_arg_types);

    if (rv != FFI_OK) {
        PyMem_Free(cif);
        PyMem_Free(cl_arg_types);
        PyErr_Format(PyExc_RuntimeError,
            "Cannot create FFI CIF: err=%d", rv);
        return NULL;
    }

    return cif;
}

/*
 * PyObjCFFI_FreeCIF - Free the CIF created by PyObjCFFI_CIFForSignature
 */
void
PyObjCFFI_FreeCIF(ffi_cif* cif)
{
    if (cif->arg_types) PyMem_Free(cif->arg_types);
    PyMem_Free(cif);
}

/*
 * PyObjCFFI_MakeClosure - Create a closure for an Objective-C method
 *
 * Return the closure, or NULL. The 'func' will be called with a CIF object,
 * a pointer to the return value, the argument array and the 'userdata'.
 */
IMP
PyObjCFFI_MakeClosure(
    PyObjCMethodSignature* methinfo,
    PyObjCFFI_ClosureFunc func,
    void* userdata)
{
    ffi_cif *cif;
    ffi_closure *cl;
    ffi_status rv;

    cif = PyObjCFFI_CIFForSignature(methinfo);
    if (cif == NULL) {
        return NULL;
    }

    /* And finally create the actual closure */
    /*cl = PyMem_Malloc(sizeof(*cl));*/
    cl = PyObjC_malloc_closure();
    if (cl == NULL) {
        PyObjCFFI_FreeCIF(cif);
        /*PyErr_NoMemory();*/
        return NULL;
    }

    /*printf("create closure for cif\n");
    describe_cif(cif);
    printf("\n\n");*/

    rv = ffi_prep_closure(cl, cif, func, userdata);
    if (rv != FFI_OK) {
        PyObjCFFI_FreeCIF(cif);
        PyErr_Format(PyExc_RuntimeError,
            "Cannot create FFI closure: %d", rv);
        return NULL;
    }

    return (IMP)cl;
}

/*
 * PyObjCFFI_FreeClosure - Free the closure created by PyObjCFFI_MakeClosure
 *
 * Returns the userdata.
 */
void*
PyObjCFFI_FreeClosure(IMP closure)
{
    void* retval;
    ffi_closure* cl;

    cl = (ffi_closure*)closure;
    retval = cl->user_data;
    PyObjCFFI_FreeCIF(cl->cif);
    PyObjC_free_closure(cl); /* XXX: error handling */

    return retval;
}
