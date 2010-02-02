/*
 * These NSData methods don't "fit" the metadata model.
 * -bytes
 * -mutableBytes
 */
#include <Python.h>
#include "pyobjc-api.h"

#include <Foundation/Foundation.h>


static PyObject* call_NSData_bytes(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	const void* bytes;
	NSUInteger    bytes_len;
	PyObject* result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes = objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method));
		bytes_len = (NSUInteger) objc_msgSendSuper(&super, @selector(length));


	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		bytes = NULL;
		bytes_len = 0;
	PyObjC_ENDHANDLER

	if (bytes == NULL && PyErr_Occurred()) return NULL;

	result = PyBuffer_FromMemory((void*)bytes, bytes_len);

	return result;
}

static void 
imp_NSData_bytes(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	void** pretval = (void**)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	if (result == Py_None) {
		*pretval = NULL;
		Py_DECREF(result);
		PyGILState_Release(state);
		return;
	}

	if (PyBuffer_Check(result)) {
		/* XXX: Is this correct?? */
		const void *p;
		Py_ssize_t len;
		if (PyObject_AsReadBuffer(result, &p, &len) == -1) {
			goto error;
		}
		Py_DECREF(result);
		*pretval =  (void *)p;
		PyGILState_Release(state);
		return;
	} else if (PyString_Check(result)) {
		/* XXX: Is this correct */
		void* p;

		p = PyString_AsString(result);
		*pretval = (void*)p;
		PyGILState_Release(state);
		return;
	}

	PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
	goto error;

error:
	Py_XDECREF(arglist);
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
}


static PyObject* 
call_NSMutableData_mutableBytes(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	void*     bytes;
	NSUInteger  bytes_len;
	PyObject* result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes = objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method));
		bytes_len = (NSUInteger) objc_msgSendSuper(&super, @selector(length));

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		bytes = NULL;
		bytes_len = 0;
	PyObjC_ENDHANDLER

	if (bytes == NULL && PyErr_Occurred()) return NULL;

	result = PyBuffer_FromReadWriteMemory((void*)bytes, bytes_len);

	return result;
}

static void
imp_NSMutableData_mutableBytes(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	void** pretval = (void**)resp;
	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* pyself = NULL;
	int cookie = 0;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	pyself = PyObjCObject_NewTransient(self, &cookie);
	if (pyself == NULL) goto error;
	PyTuple_SetItem(arglist, 0, pyself); 
	Py_INCREF(pyself);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	PyObjCObject_ReleaseTransient(pyself, cookie); pyself = NULL;
	if (result == NULL) goto error;

	if (result == Py_None) {
		Py_DECREF(result);
		goto error;
	}

	if (result == Py_None) {
		*pretval = NULL;
		Py_DECREF(result);
		PyGILState_Release(state);
		return;
	}

	if (PyBuffer_Check(result)) {
		/* XXX: Is this correct? */
		void *p;
		Py_ssize_t len;
		if (PyObject_AsWriteBuffer(result, &p, &len) == -1) goto error;
		Py_DECREF(result);
		*pretval = (void *)p;
		PyGILState_Release(state);
		return;
	}

	PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
	return;

error:
	Py_XDECREF(arglist);
	if (pyself) {
		PyObjCObject_ReleaseTransient(pyself, cookie); 
	}
	*pretval = NULL;
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 } /* sentinel */
};

/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_data",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__data(void);

PyObject*
PyInit__data(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_data(void);

void
init_data(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_data", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	Class classNSData = objc_lookUpClass("NSData");
	Class classNSMutableData = objc_lookUpClass("NSMutableData");

	if (classNSData != NULL) {

		if (PyObjC_RegisterMethodMapping(classNSData, 
				 @selector(bytes),
				 call_NSData_bytes,
				 imp_NSData_bytes) < 0 ) {
			INITERROR();
		}

	}

	if (classNSMutableData != NULL) {

		if (PyObjC_RegisterMethodMapping(classNSMutableData, 
				@selector(mutableBytes),
				call_NSMutableData_mutableBytes,
				imp_NSMutableData_mutableBytes) < 0 ) {
			INITERROR();
		}
	}

  
	INITDONE();
}
