/*
 * This module contains custom mapping functions for problematic methods
 */

#include <Python.h>
#include <Foundation/Foundation.h>
#include <AppKit/AppKit.h> // really should be Cocoa
#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif
#include "objc_support.h"
#include "pyobjc-api.h"


/* begin custom mapping for NSBitmapImageRep.initWithBitmap.... */

  /*
    wrapper for:

    - (id)initWithBitmapDataPlanes:(unsigned char **)planes
    pixelsWide:(int)width
    pixelsHigh:(int)height
    bitsPerSample:(int)bps
    samplesPerPixel:(int)spp
    hasAlpha:(BOOL)alpha
    isPlanar:(BOOL)isPlanar
    colorSpaceName:(NSString *)colorSpaceName
    bytesPerRow:(int)rBytes
    bitsPerPixel:(int)pBits 
  */


static PyObject*
call_NSBitmapImageRep_initWithBitmap(PyObject* method, PyObject* self, PyObject* arguments)
{
  PyObject* result;
  PyObject* maybeNone;
  char *dataPlanes[5];
  int garbage;
  int width, height;
  int bps, spp;
  BOOL hasAlpha, isPlanar;
  char *colorSpaceName;
  NSString *colorSpaceNameString;
  int bpr, bpp;
  NSBitmapImageRep *newImageRep;

  // check for five well defined read buffers in data planes argument
  if (PyArg_ParseTuple(arguments, "(z#z#z#z#z#)iiiibbsii",
		       &dataPlanes[0], &garbage,
		       &dataPlanes[1], &garbage,
		       &dataPlanes[2], &garbage,
		       &dataPlanes[3], &garbage,
		       &dataPlanes[4], &garbage,
		       &width,
		       &height,
		       &bps,
		       &spp,
		       &hasAlpha,
		       &isPlanar,
		       &colorSpaceName,
		       &bpr,
		       &bpp) == 0) {

    if ( !PyErr_ExceptionMatches(PyExc_TypeError) )
      return NULL;

    PyErr_Clear();
    bzero(dataPlanes, sizeof(dataPlanes));

    if (PyArg_ParseTuple(arguments, "Oiiiibbsii",
			 &maybeNone,
			 &width,
			 &height,
			 &bps,
			 &spp,
			 &hasAlpha,
			 &isPlanar,
			 &colorSpaceName,
			 &bpr,
			 &bpp) == 0){
      return NULL; //! any other situations that we need to parse specific args go here
    } else {
      // first arg must be none as nothing else makes sense
      if (maybeNone != Py_None) {
	PyErr_SetString(PyExc_TypeError, "First argument must be a 5 element Tuple or None.");
	return NULL;
      }
    }
  }

  colorSpaceNameString = [NSString stringWithCString: colorSpaceName];

  NS_DURING
    newImageRep = objc_msgSend(ObjCObject_GetObject(self), 
			       @selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:), dataPlanes, width, height, bps, spp, hasAlpha, isPlanar, colorSpaceNameString, bpr, bpp);

    result = ObjC_IdToPython(newImageRep);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    PyErr_Print();
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static PyObject*
supercall_NSBitmapImageRep_initWithBitmap(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
  PyObject* result;
  PyObject* maybeNone;
  char *dataPlanes[5];
  int garbage;
  int width, height;
  int bps, spp;
  BOOL hasAlpha, isPlanar;
  char *colorSpaceName;
  NSString *colorSpaceNameString;
  int bpr, bpp;
  NSBitmapImageRep *newImageRep;
  struct objc_super super;

  // check for five well defined read buffers in data planes argument
  if (PyArg_ParseTuple(arguments, "(z#z#z#z#z#)iiiibbsii",
		       &dataPlanes[0], &garbage,
		       &dataPlanes[1], &garbage,
		       &dataPlanes[2], &garbage,
		       &dataPlanes[3], &garbage,
		       &dataPlanes[4], &garbage,
		       &width,
		       &height,
		       &bps,
		       &spp,
		       &hasAlpha,
		       &isPlanar,
		       &colorSpaceName,
		       &bpr,
		       &bpp) == 0) {

    if ( !PyErr_ExceptionMatches(PyExc_TypeError) )
      return NULL;

    PyErr_Clear();
    bzero(dataPlanes, sizeof(dataPlanes));

    if (PyArg_ParseTuple(arguments, "Oiiiibbsii",
			 &maybeNone,
			 &width,
			 &height,
			 &bps,
			 &spp,
			 &hasAlpha,
			 &isPlanar,
			 &colorSpaceName,
			 &bpr,
			 &bpp) == 0){
      return NULL; //! any other situations that we need to parse specific args go here
    } else {
      // first arg must be none as nothing else makes sense
      if (maybeNone != Py_None) {
	PyErr_SetString(PyExc_TypeError, "First argument must be a 5 element Tuple or None.");
	return NULL;
      }
    }
  }

  colorSpaceNameString = [NSString stringWithCString: colorSpaceName];

  NS_DURING
    RECEIVER(super) = ObjCObject_GetObject(self);
    super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));
    
    newImageRep = objc_msgSendSuper(&super,
			       @selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:), dataPlanes, width, height, bps, spp, hasAlpha, isPlanar, colorSpaceNameString, bpr, bpp);

    result = ObjC_IdToPython(newImageRep);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    PyErr_Print();
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static void
imp_NSBitmapImageRep_initWithBitmap(id self, SEL sel)
{
  NSLog(@"Implementing '@s' in a Python subclass of %@ is not yet supported (%s:%d)", NSStringFromSelector(sel), NSStringFromClass([self class]), __FILE__, __LINE__ );
  abort();
}

static PyObject*
call_NSBitmapImageRep_getBitmapDataPlanes_(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
  PyObject* result;
  
  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    unsigned char *dataPlanes[5];
    int i;
    int bytesPerPlane;
  
    (void)objc_msgSend(ObjCObject_GetObject(self), 
		       @selector(getBitmapDataPlanes:),
		       &dataPlanes);

    bytesPerPlane = (int) objc_msgSend(ObjCObject_GetObject(self), @selector(bytesPerPlane));

    result = PyTuple_New(5);
    if (result != NULL) {
      for(i=0; i<5; i++) {
	if (dataPlanes[i]) {
	  // leak??
	  PyObject* buffer = PyBuffer_FromReadWriteMemory(dataPlanes[i], bytesPerPlane);
	  if ( (!buffer) || PyErr_Occurred()) {
	    Py_DECREF(result);
	    result = NULL;
	  }
	  PyTuple_SET_ITEM(result, i, buffer);
	} else {
	  PyTuple_SET_ITEM(result, i, Py_None);
	}
      }
    }
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static PyObject*
supercall_NSBitmapImageRep_getBitmapDataPlanes_(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
  PyObject* result;
  struct objc_super super;
  
  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    unsigned char *dataPlanes[5];
    int i;
    int bytesPerPlane;

    RECEIVER(super) = ObjCObject_GetObject(self);
    super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));
    
    (void)objc_msgSendSuper(&super, 
			    @selector(getBitmapDataPlanes:),
			    &dataPlanes);
    bytesPerPlane = (int) objc_msgSend(RECEIVER(super), @selector(bytesPerPlane));

    result = PyTuple_New(5);
    if (result != NULL) {
      for(i=0; i<5; i++) {
	if (dataPlanes[i]) {
	  // leak??
	  PyObject* buffer = PyBuffer_FromReadWriteMemory(dataPlanes[i], bytesPerPlane);
	  if ( (!buffer) || PyErr_Occurred()) {
	    Py_DECREF(result);
	    result = NULL;
	  }
	  PyTuple_SET_ITEM(result, i, buffer);
	} else {
	  PyTuple_SET_ITEM(result, i, Py_None);
	}
      }
    }
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static void
imp_NSBitmapImageRep_getBitmapDataPlanes_(id self, SEL sel)
{
  NSLog(@"Implementing '@s' in a Python subclass of %@ is not yet supported (%s:%d)", NSStringFromSelector(sel), NSStringFromClass([self class]), __FILE__, __LINE__ );
  abort();
}

static PyObject*
call_NSBitmapImageRep_bitmapData(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
  PyObject* result;
  
  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    unsigned char *bitmapData;
    int bytesPerPlane;
  
    bitmapData = (unsigned char *)objc_msgSend(ObjCObject_GetObject(self), @selector(bitmapData));
    bytesPerPlane = (int) objc_msgSend(ObjCObject_GetObject(self), @selector(bytesPerPlane));

    result = PyBuffer_FromReadWriteMemory(bitmapData, bytesPerPlane);
    if (PyErr_Occurred()) {
      if (result) {
	Py_DECREF(result);
      }
      result = NULL;
    }
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static PyObject*
supercall_NSBitmapImageRep_bitmapData(PyObject* method, 
		PyObject* self, PyObject* arguments)
{
  PyObject* result;
  struct objc_super super;
  
  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    unsigned char *bitmapData;
    int bytesPerPlane;

    RECEIVER(super) = ObjCObject_GetObject(self);
    super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));
    
    bitmapData = (unsigned char *) objc_msgSendSuper(&super, @selector(bitmapData));
    bytesPerPlane = (int) objc_msgSend(RECEIVER(super), @selector(bytesPerPlane));

    result = PyBuffer_FromReadWriteMemory(bitmapData, bytesPerPlane);
    if (PyErr_Occurred()) {
      if (result) {
	Py_DECREF(result);
      }
      result = NULL;
    }
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static void
imp_NSBitmapImageRep_bitmapData(id self, SEL sel)
{
  NSLog(@"Implementing '@s' in a Python subclass of %@ is not yet supported (%s:%d)", NSStringFromSelector(sel), NSStringFromClass([self class]), __FILE__, __LINE__ );
  abort();
}

PyDoc_STRVAR(mapping_doc,
	"This module registers some utility functions with the PyObjC core \n"
	"and is not used by 'normal' python code"
);

static PyMethodDef mapping_methods[] = {
	{ 0, 0, 0, 0 }
};

void init_AppKitMapping(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_AppKitMapping", mapping_methods, mapping_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;
	

	if (ObjC_ImportModule(m) < 0) {
		return;
	}

	if (ObjC_RegisterMethodMapping(
			objc_lookUpClass("NSBitmapImageRep"), 
			@selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:),
			call_NSBitmapImageRep_initWithBitmap,
			supercall_NSBitmapImageRep_initWithBitmap,
			(IMP)imp_NSBitmapImageRep_initWithBitmap) < 0) {

		PyErr_Print();
		return;
	}

	if (ObjC_RegisterMethodMapping(
			objc_lookUpClass("NSBitmapImageRep"), 
			@selector(getBitmapDataPlanes:),
			call_NSBitmapImageRep_getBitmapDataPlanes_,
			supercall_NSBitmapImageRep_getBitmapDataPlanes_,
			(IMP)imp_NSBitmapImageRep_getBitmapDataPlanes_) < 0) {

		PyErr_Print();
		return;
	}

	if (ObjC_RegisterMethodMapping(
			objc_lookUpClass("NSBitmapImageRep"), 
			@selector(bitmapData),
			call_NSBitmapImageRep_bitmapData,
			supercall_NSBitmapImageRep_bitmapData,
			(IMP)imp_NSBitmapImageRep_bitmapData) < 0) {

		PyErr_Print();
		return;
	}
	
	/* register other specials */
}
