/*
 *  This file contains type and function definitions that are helpfull for
 *  adding constants to the python module
 *
 *  NOTE: The functions are defined as 'static inline' to avoid compiler 
 *  warnings.
 *  NOTE2: The functions are not in a seperate file because I am lazy and
 *  to make using this file easier
 *  NOTE3: This file is used by the files generated by the scripts in
 *         ~/Scripts/CodeGenerators.
 *
 */

#import <Foundation/NSString.h>
#import <Foundation/NSArray.h>

struct vartable {
	NSString* name;
	char* type;

#ifdef GNU_RUNTIME
	const void* ptr;
#endif
};

struct inttable {
	char* 	name;
	int     is_unsigned;
	int	value;
};

struct stringtable {
	char*	  name;
	NSString* const* value;
};

static inline int add_double(PyObject*d, char* name, double value)
{
	int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(double), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	Py_DECREF(v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_float(PyObject*d, char* name, float value)
{
	int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(float), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	Py_DECREF(v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_unsigned(PyObject*d, char* name, unsigned value)
{
	int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(unsigned), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	Py_DECREF(v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_BOOL(PyObject*d, char* name, BOOL value)
{
	int res;
	PyObject* v;

	v = PyBool_FromLong(value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	Py_DECREF(v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_int(PyObject*d, char* name, int value)
{
	int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(int), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	Py_DECREF(v);
	if (res < 0) return -1;
	return 0;
}

static inline int register_ints(PyObject* d, struct inttable* table)
{
	while (table->name != NULL) {
		if (table->is_unsigned) {
			int res = add_unsigned(d, table->name, 
					(unsigned)table->value);
			if (res == -1) return -1;
		} else {
			int res = add_int(d, table->name, table->value);
			if (res == -1) return -1;
		}

		table++;
	}
	return 0;
}

static inline int add_string(PyObject* d, char* name, NSString* value)
{
	int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(id), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_id(PyObject* d, char* name, id value)
{
	int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(id), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}


static inline int register_strings(PyObject* d, struct stringtable* table)
{
	while (table->name != NULL) {
		add_string(d, table->name, *table->value);
		table++;
	}
	return 0;
}

#ifdef GNU_RUNTIME

#import <Foundation/NSBundle.h>
#define CFBundleRef NSBundle*

static inline int
register_variableList(PyObject* d, CFBundleRef bundle, struct vartable* table, size_t count)
{
	PyObject* val;
	int i;

	for (i = 0; i < count; i++) {
		val  = PyObjC_ObjCToPython(table[i].type, (void*)table[i].ptr);
		if (val == NULL) {
			return -1;
		}
		PyDict_SetItemString(d, (char*)[table[i].name cString], val);
		Py_DECREF(val);
	}
	return 0;
}

#else /* !GNU_RUNTIME */

#import <CoreFoundation/CoreFoundation.h>

static inline int
register_variableList(PyObject* d, CFBundleRef bundle __attribute__((__unused__)), struct vartable* table, size_t count)
{
	void** ptrs = NULL;
	NSMutableArray* names = nil;
	size_t i;
	int retVal = 0;

	ptrs = PyMem_Malloc(sizeof(void*) * count);
	if (ptrs == NULL) {
		PyErr_NoMemory();
		return -1;
	}

	names = [[NSMutableArray alloc] init];
	if (names == NULL) {
		PyErr_NoMemory();
		retVal = -1;
		goto cleanup;
	}

	for (i = 0; i < count; i++) {
		[names addObject:table[i].name];
	}

	CFBundleGetDataPointersForNames(bundle,
		(CFArrayRef)names, ptrs);

	for (i = 0; i < count; i++) {
		PyObject* val;
		if (ptrs[i] == NULL) continue; /* Skip undefined names */

		val  = PyObjC_ObjCToPython(table[i].type, ptrs[i]);
		if (val == NULL) {
			retVal = -1;
			goto cleanup;
		}
		PyDict_SetItemString(d, (char*)[table[i].name cString], val);
		Py_DECREF(val);
	}

cleanup:
	if (ptrs) {
		PyMem_Free(ptrs);
	}

	[names release];

	return retVal;
}
#endif /* !GNU_RUNTIME */
