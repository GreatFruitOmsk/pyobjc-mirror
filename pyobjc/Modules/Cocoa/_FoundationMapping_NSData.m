/*
 * NSData mappings for special methods:
 * - initWithBytes_length_
 * - bytes
 * - mutableBytes
 *
 * Should add:
 * -initWithBytesNoCopy:length:
 * -initWithBytesNoCopy:length:freeWhenDone
 * +dataWith... version of above
 * -getBytes...
 * 
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif
#include "pyobjc-api.h"
#include "objc_support.h"

static PyObject* call_NSData_dataWithBytes_length_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	id        objc_result;

	if  (PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len) < 0) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		objc_result = objc_msgSend(ObjCClass_GetClass(self),
				@selector(dataWithBytes:length:),
				bytes, len);
		result = ObjC_IdToPython(objc_result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* supercall_NSData_dataWithBytes_length_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;

	if  (PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len) < 0) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		RECEIVER(super) = ObjCClass_GetClass(self);
		super.class = GETISA(RECEIVER(super));

		objc_result = objc_msgSendSuper(&super,
				@selector(dataWithBytes:length:),
				bytes, len);
		result = ObjC_IdToPython(objc_result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}


static id imp_NSData_dataWithBytes_length_(id self, SEL sel,
		char* data, unsigned len)
{
	PyObject* result;
	PyObject* arglist;
	id        objc_result;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromStringAndSize(data, len));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(len));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return nil;
	}

	result = ObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	objc_result = ObjC_PythonToId(result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		ObjCErr_ToObjC();
		return nil;
	}

	return objc_result;
}

static PyObject* call_NSData_initWithBytes_length_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	id        objc_result;
	id	  self_obj;

	if  (PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len) < 0) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	self_obj =  ObjCObject_GetObject(self);
	NS_DURING
		[self_obj retain];
		objc_result = objc_msgSend(self_obj,
				@selector(initWithBytes:length:),
				bytes, len);
		[self_obj release];
		result = ObjC_IdToPython(objc_result);

		/* XXX Ronald: If you try to use the result of 
		 * ObjCObject_GetObject(self) after the call to objc_msgSend 
		 * it will crash with large enough values of len (>=32). 
		 * Appearently the original self is recycled during the init.
		 */
		if (self != result) {
			ObjCObject_ClearObject(self);
		}

	NS_HANDLER
		[self_obj release];
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* supercall_NSData_initWithBytes_length_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;

	if  (PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len) < 0) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		RECEIVER(super) = ObjCObject_GetObject(self);
		super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));

		objc_result = objc_msgSendSuper(&super,
				@selector(initWithBytes:length:),
				bytes, len);
		result = ObjC_IdToPython(objc_result);

		/* XXX Ronald: If you try to use the result of 
		 * ObjCObject_GetObject(self) after the call to objc_msgSend 
		 * it will crash with large enough values of len (>=32). 
		 * Appearently the original self is recycled during the init.
		 */
		if (self != result) {
			ObjCObject_ClearObject(self);
		}
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}


static id imp_NSData_initWithBytes_length_(id self, SEL sel,
		char* data, unsigned len)
{
	PyObject* result;
	PyObject* arglist;
	id        objc_result;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromStringAndSize(data, len));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(len));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return nil;
	}

	result = ObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	objc_result = ObjC_PythonToId(result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		ObjCErr_ToObjC();
		return nil;
	}

	return objc_result;
}

static PyObject* call_NSData_bytes(PyObject* method, PyObject* self, PyObject* arguments)
{
  NSData *dataObject;
  const void* bytes;
  unsigned    bytes_len;
  PyObject* result;

  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    dataObject = ObjCObject_GetObject(self);

    bytes = [dataObject bytes];
    bytes_len = [dataObject length];

    result = PyBuffer_FromMemory((void *)bytes, bytes_len);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static PyObject* supercall_NSData_bytes(PyObject* method, PyObject* self, PyObject* arguments)
{
  const void* bytes;
  unsigned    bytes_len;
  PyObject* result;
  struct objc_super super;

  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    RECEIVER(super) = ObjCObject_GetObject(self);
    super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));

    /* bbum: Not at all sure what to do here....   send both to super?  
     *       Just -bytes?
     * ronald: I think both is more correct, neiter one is perfect.
     */
    bytes = objc_msgSendSuper(&super, @selector(bytes));
    bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));

    result = PyBuffer_FromMemory((void*)bytes, bytes_len);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static void *imp_NSData_bytes(id self, SEL sel)
{
  PyObject* result;

  result = ObjC_CallPython(self, sel, NULL);
  if (result == NULL) {
    ObjCErr_ToObjC();
    return NULL;
  }

  if (result == Py_None)
    return NULL;

  if (PyBuffer_Check(result)) {
    const void *p;
    int len;
    if (PyObject_AsReadBuffer(result, &p, &len) == -1) {
      ObjCErr_ToObjC();
      return NULL;
    }
    return (void *)p;
  }

  PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
  return NULL;
}

static PyObject* call_NSMutableData_mutableBytes(PyObject* method, PyObject* self, PyObject* arguments)
{
  NSMutableData *dataObject;
  void*     bytes;
  unsigned  bytes_len;
  PyObject* result;
  
  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    dataObject = ObjCObject_GetObject(self);

    bytes = [dataObject mutableBytes];
    bytes_len = [dataObject length];

    result = PyBuffer_FromReadWriteMemory((void *)bytes, bytes_len);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static PyObject* supercall_NSMutableData_mutableBytes(PyObject* method, PyObject* self, PyObject* arguments)
{
  void*     bytes;
  unsigned  bytes_len;
  PyObject* result;
  struct objc_super super;

  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    RECEIVER(super) = ObjCObject_GetObject(self);
    super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));

    /* bbum: Not at all sure what to do here....   
     *       send both to super?  Just -bytes?
     */
    bytes = objc_msgSendSuper(&super, @selector(mutableBytes));
    bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));

    result = PyBuffer_FromReadWriteMemory((void*)bytes, bytes_len);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static void *imp_NSMutableData_mutableBytes(id self, SEL sel)
{
  PyObject* result;

  result = ObjC_CallPython(self, sel, NULL);
  if (result == NULL) {
    ObjCErr_ToObjC();
    return NULL;
  }

  if (result == Py_None)
    return NULL;

  if (PyBuffer_Check(result)) {
    void *p;
    int len;
    if (PyObject_AsWriteBuffer(result, &p, &len) == -1) {
      ObjCErr_ToObjC();
      return NULL;
    }
    return (void *)p;
  }

  PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
  return NULL;
}

int __pyobjc_install_NSData(void)
{
  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(initWithBytes:length:),
				 call_NSData_initWithBytes_length_,
				 supercall_NSData_initWithBytes_length_,
				 (IMP)imp_NSData_initWithBytes_length_) < 0 ) {
    NSLog(@"Error occurred while installing NSData method bridge (initWithBytes:length:).");
    PyErr_Print();
    return -1;
  }

  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(dataWithBytes:length:),
				 call_NSData_dataWithBytes_length_,
				 supercall_NSData_dataWithBytes_length_,
				 (IMP)imp_NSData_dataWithBytes_length_) < 0 ) {
    NSLog(@"Error occurred while installing NSData method bridge (initWithBytes:length:).");
    PyErr_Print();
    return -1;
  }
  
  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(bytes),
				 call_NSData_bytes,
				 supercall_NSData_bytes,
				 (IMP)imp_NSData_bytes) < 0 ) {
    NSLog(@"Error occurred while installing NSData method bridge (bytes).");
    PyErr_Print();
    return -1;
  }

  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSMutableData"), 
				 @selector(mutableBytes),
				 call_NSMutableData_mutableBytes,
				 supercall_NSMutableData_mutableBytes,
				 (IMP)imp_NSMutableData_mutableBytes) < 0 ) {
    NSLog(@"Error occurred while installing NSMutableData method bridge (mutableBytes).");
    PyErr_Print();
    return -1;
  }
  
  return 0;
}

