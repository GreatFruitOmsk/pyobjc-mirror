#ifndef OBJC_UTIL
#define OBJC_UTIL

extern PyObject* PyObjCExc_Error;
extern PyObject* PyObjCExc_NoSuchClassError;
extern PyObject* PyObjCExc_InternalError;
extern PyObject* PyObjCExc_UnInitDeallocWarning;
extern PyObject* PyObjCExc_ObjCRevivalWarning;
extern PyObject* PyObjCExc_LockError;
extern PyObject* PyObjCExc_BadPrototypeError;
extern PyObject* PyObjCExc_UnknownPointerError;

extern int PyObjCUtil_Init(PyObject* module);

extern void PyObjCErr_FromObjC(NSException* localException);
extern void PyObjCErr_ToObjC(void) __attribute__((__noreturn__));

extern void PyObjCErr_ToObjCWithGILState(PyGILState_STATE* state) __attribute__((__noreturn__));

extern NSException* PyObjCErr_AsExc(void);

extern PyObject* PyObjC_CallPython(id self, SEL selector, PyObject* arglist, BOOL* isAlloc, BOOL* isCFAlloc);

extern char* PyObjCUtil_Strdup(const char* value);

extern NSMapTableKeyCallBacks PyObjCUtil_PointerKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_PointerValueCallBacks;

extern NSMapTableKeyCallBacks PyObjCUtil_ObjCIdentityKeyCallBacks;
extern NSMapTableValueCallBacks PyObjCUtil_ObjCValueCallBacks;

extern void PyObjC_FreeCArray(int, void*);
extern int PyObjC_PythonToCArray(BOOL, BOOL, const char*, PyObject*, void**, Py_ssize_t*, PyObject**);
extern PyObject* PyObjC_CArrayToPython(const char*, void*, Py_ssize_t);
extern PyObject* PyObjC_CArrayToPython2(const char*, void*, Py_ssize_t, bool already_retained, bool already_cfretained);
extern int PyObjC_IsPythonKeyword(const char* word);

extern int PyObjCRT_SimplifySignature(const char* signature, char* buf, size_t buflen);

extern int PyObjCObject_Convert(PyObject* object, void* pvar);
extern int PyObjCClass_Convert(PyObject* object, void* pvar);

extern int PyObjC_is_ascii_string(PyObject* unicode_string, const char* ascii_string);
extern int PyObjC_is_ascii_prefix(PyObject* unicode_string, const char* ascii_string, size_t n);

extern PyObject* PyObjC_ImportName(const char* name);

extern PyObject* PyObjC_AdjustSelf(PyObject* object);

extern PyObject* PyObjC_FindSELInDict(PyObject*, SEL);
extern int PyObjCRT_SignaturesEqual(const char*, const char*);

static inline Py_ssize_t align(Py_ssize_t offset, Py_ssize_t alignment)
{
    Py_ssize_t rest = offset % alignment;
    if (rest == 0) return offset;
    return offset + (alignment - rest);
}



#endif /* OBJC_UTIL */
