#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static const void* 
mod_CFTreeRetainCallback(const void* info) 
{
	return [(NSObject*)info retain];
}

static void
mod_CFTreeReleaseCallback(const void* info)
{
	[(NSObject*)info release];
}

static CFStringRef
mod_CFTreeCopyDescriptionCallback(const void* info)
{
	NSString* result = [(NSObject*)info description];
	[result retain];
	return (CFStringRef)result;
}

static CFTreeContext mod_CFTreeContext = {
	0,		
	NULL,
	mod_CFTreeRetainCallback,
	mod_CFTreeReleaseCallback,
	mod_CFTreeCopyDescriptionCallback
};

static PyObject*
mod_CFTreeGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_tree;
	PyObject* py_context = NULL;
	CFTreeRef tree;
	CFTreeContext context;

	if (!PyArg_ParseTuple(args, "O|O", &py_tree, &py_context)) {
		return NULL;
	}

	if (py_context != NULL &&  py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFTreeRef), py_tree, &tree) < 0) {
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFTreeGetContext(tree, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (context.version != 0) {
		PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
		return NULL;
	}

	if (context.retain != mod_CFTreeRetainCallback) {
		PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
		return NULL;
	}

	return PyObjC_ObjCToPython(@encode(id), &context.info);
}

static PyObject*
mod_CFTreeSetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_tree;
	PyObject* py_context = NULL;
	CFTreeRef tree;
	CFTreeContext context;
	NSObject* info;

	if (!PyArg_ParseTuple(args, "O|O", &py_tree, &py_context)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFTreeRef), py_tree, &tree) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(id), py_context, &info) < 0) {
		return NULL;
	}

	context = mod_CFTreeContext;
	context.info = info;

	PyObjC_DURING
		CFTreeSetContext(tree, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}


static PyObject*
mod_CFTreeCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_context = NULL;
	CFTreeRef tree;
	CFTreeContext context;
	CFAllocatorRef allocator;
	NSObject* info;

	if (!PyArg_ParseTuple(args, "O|O", &py_allocator, &py_context)) {
		return NULL;
	}
	
	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(id), py_context, &info) < 0) {
		return NULL;
	}

	context = mod_CFTreeContext;
	context.info = info;


	tree = NULL;

	PyObjC_DURING
		tree = CFTreeCreate(allocator, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (tree == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyObject* py_tree = PyObjC_ObjCToPython(@encode(CFTreeRef), &tree);
	CFRelease(tree); /* we're donated a reference */

	return py_tree;
}

static PyObject*
mod_CFTreeGetChildren(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_tree;
	PyObject* py_buffer;
	CFTreeRef tree;
	CFIndex count;
	CFTreeRef* children = NULL;
	PyObject* result;

	if (!PyArg_ParseTuple(args, "OO", &py_tree, &py_buffer)) {
		return NULL;
	}

	if (py_buffer != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFTreeRef), py_tree, &tree) < 0) {
		return NULL;
	}

	PyObjC_DURING
		count = CFTreeGetChildCount(tree);
		children = malloc(count * sizeof(CFTreeRef));
		if (children != NULL) {
			CFTreeGetChildren(tree, children);
		}

	PyObjC_HANDLER
		count = -1; children = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (children == NULL) {
		PyErr_NoMemory();
		return NULL;
	}
		

	if (PyErr_Occurred()) {
		if (children) {
			free(children);
		}
		return NULL;
	}

	result = PyObjC_CArrayToPython(@encode(CFTreeRef), children, count);
	free(children);
	return result;
}


static PyMethodDef mod_methods[] = {
        {
		"CFTreeCreate",
		(PyCFunction)mod_CFTreeCreate,
		METH_VARARGS,
		NULL
	},
        {
		"CFTreeGetContext",
		(PyCFunction)mod_CFTreeGetContext,
		METH_VARARGS,
		NULL
	},
        {
		"CFTreeSetContext",
		(PyCFunction)mod_CFTreeSetContext,
		METH_VARARGS,
		NULL
	},
	{
		"CFTreeGetChildren",
		(PyCFunction)mod_CFTreeGetChildren,
		METH_VARARGS,
		NULL,
	},
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_CFTree",
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

PyObject* PyInit__CFTree(void);

PyObject*
PyInit__CFTree(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_CFTree(void);

void
init_CFTree(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_CFTree", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) {
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	INITDONE();
}
