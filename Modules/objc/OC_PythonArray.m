#include "pyobjc.h"

@implementation OC_PythonArray 

+ newWithPythonObject:(PyObject*)v;
{
	OC_PythonArray* res;

	res = [[OC_PythonArray alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v;
{
	Py_INCREF(v);
	Py_XDECREF(value);
	value = v;
	return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		Py_XDECREF(value);
		value = NULL;

	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(int)count
{
	int result;

	PyObjC_BEGIN_WITH_GIL
		result = PySequence_Length(value);

	PyObjC_END_WITH_GIL

	return result;
}

-objectAtIndex:(int)idx
{
	PyObject* v;
	id  result;
	int err;
	PyGILState_STATE state = xPyGILState_Ensure();

	v = PySequence_GetItem(value, idx);
	if (v == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	err = depythonify_c_value("@", v, &result);
	Py_DECREF(v);
	if (err == -1) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	xPyGILState_Release(state);
	return result;
}


-(void)replaceObjectAtIndex:(int)idx withObject:newValue;
{
	PyObject* v;
	PyGILState_STATE state = xPyGILState_Ensure();

	v = pythonify_c_value("@", &newValue);
	if (v == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (PySequence_SetItem(value, idx, v) < 0) {
		Py_DECREF(v);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(v);
	xPyGILState_Release(state);
}

-(void)getObjects:(id*)buffer inRange:(NSRange)range
{
	unsigned int i;

	for (i = 0; i < range.length; i++) {
		buffer[i] = [self objectAtIndex:i+range.location];
	}
}

@end /* implementation OC_PythonArray */
