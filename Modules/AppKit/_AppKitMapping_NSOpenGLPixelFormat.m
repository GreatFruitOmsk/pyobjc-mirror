/*
 * Special wrappers for NSOpenGLPixelFormat methods with 'difficult' arguments.
 *
 * TODO:
 * -getValues:forAttribute:forVirtualScreen:
 * -initWithAttributes:
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"
#include <OpenGL/gl.h>

static PyObject*
call_NSOpenGLPixelFormat_initWithAttributes_(
    PyObject* method, PyObject* self, PyObject* arguments)
{
    PyObject *result;
    struct objc_super super;
    GLuint *attribs;
    PyObject *seq;
    NSOpenGLPixelFormat *pixelFormat;
    int i, count;

    if (!PyArg_ParseTuple(arguments, "O", &seq)) {
        return NULL;
    }

    seq = PySequence_Fast(seq, "attributes must be a sequence");
    if (seq == NULL) {
        return NULL;
    }
    count = PySequence_Fast_GET_SIZE(seq);

    attribs = PyMem_New(GLuint, count+1);
    if (attribs == NULL) {
        Py_DECREF(seq);
        PyErr_NoMemory();
        return NULL;
    }
    
    for (i=0; i<count; ++i) {
        /* XXX - this is Python 2.3 specific */
        attribs[i] = PyInt_AsUnsignedLongMask(PySequence_Fast_GET_ITEM(seq, i));
    }
    attribs[count] = 0;
    Py_DECREF(seq);

    if (PyErr_Occurred()) {
        PyMem_Del(attribs);
        PyErr_Clear();
        PyErr_SetString(PyExc_ValueError, "attributes must be GLuint");
        return NULL;
    }
    
    NS_DURING
        PyObjC_InitSuper(&super,
            PyObjCSelector_GetClass(method),
            PyObjCObject_GetObject(self));

        pixelFormat = objc_msgSendSuper(&super,
                PyObjCSelector_GetSelector(method),
                attribs);
        result = PyObjC_IdToPython(pixelFormat);
    NS_HANDLER
        PyObjCErr_FromObjC(localException);
        result = NULL;
    NS_ENDHANDLER
    
    PyMem_Del(attribs);
    return result;
    
}

static int 
_pyobjc_install_NSOpenGLPixelFormat(void)
{
	Class classNSOpenGLPixelFormat = objc_lookUpClass("NSOpenGLPixelFormat");

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLPixelFormat,
		@selector(getValues:forAttribute:forVirtualScreen:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSOpenGLPixelFormat,
		@selector(initWithAttributes:),
        call_NSOpenGLPixelFormat_initWithAttributes_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
