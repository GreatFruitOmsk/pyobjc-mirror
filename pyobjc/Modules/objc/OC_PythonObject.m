/* Copyright (c) 1996,97 by Lele Gaifax.  All Rights Reserved
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: OC_PythonObject.m,v
 * Revision: 1.23
 * Date: 1998/08/18 15:35:52
 *
 * Created Wed Sep  4 19:57:44 1996.
 */

#include "pyobjc.h"
#include "objc_support.h"
#include "compile.h"

#include <stdarg.h>

#import  <Foundation/NSObject.h>  
#import  <Foundation/NSMethodSignature.h>
#import  <Foundation/NSInvocation.h>
#import  <Foundation/NSString.h>
#import  <Foundation/NSDictionary.h>
#import  <Foundation/NSEnumerator.h>

extern NSString* NSUnknownKeyException; /* Radar #3336042 */

@implementation OC_PythonObject

+ newWithObject:(PyObject *) obj
{
	if (PyObjCObject_Check (obj)) {
		id objc_obj = PyObjCObject_GetObject(obj);
		return objc_obj;
	} else {
		id instance = [[self alloc] initWithObject:obj];
		[instance autorelease];
		return instance;
	}
}

- initWithObject:(PyObject *) obj
{
	Py_XINCREF(obj);
	Py_XDECREF(pyObject);
	pyObject = obj;

	return self;
}

- (void)dealloc
{
	Py_XDECREF(pyObject);
	[super dealloc];
}

- (NSString *) description
{
	PyObject *repr;

	if (pyObject == NULL) return @"no python object";
	
	repr = PyObject_Repr (pyObject);
	if (repr) {
		int err;
		NSString* result;

		err = depythonify_c_value ("@", repr, &result);
		Py_DECREF (repr);
		if (err == -1) {
			PyObjCErr_ToObjC();		
			return @"a python object";
		}
		return result;
	} else {
		PyErr_Clear();
		return [super description];
	}
}
  
- (void) doesNotRecognizeSelector:(SEL) aSelector
{
	[NSException raise:NSInvalidArgumentException
		     format:@"%@ does not recognize -%s",
		     	self, SELNAME(aSelector)];
}


/*#F Check the argument count of the method/function @var{pymethod},
  returning the method itself if it matches @var{argcount}, NULL
  otherwise. */
static inline PyObject *
check_argcount (PyObject *pymethod, int argcount)
{
	PyCodeObject *func_code;

	if (!pymethod) {
		return NULL;
	}
	if (PyFunction_Check(pymethod)) {
        	func_code = (PyCodeObject *)PyFunction_GetCode(pymethod);
		if (argcount == func_code->co_argcount) {
			return pymethod;
		}
	} else if (PyMethod_Check(pymethod)) {
		func_code = (PyCodeObject *)PyFunction_GetCode(
			PyMethod_Function (pymethod));
		if (argcount == func_code->co_argcount - 1) {
			return pymethod;
		}
	} 
	return NULL;
}


/*#F If the Python object @var{obj} implements a method whose name matches
  the Objective-C selector @var{aSelector} and accepts the correct number
  of arguments, return that method, otherwise NULL. */
static PyObject*
get_method_for_selector(PyObject *obj, SEL aSelector)
{
	const char*  meth_name;
	int          len;
	char*        pymeth_name;
	unsigned int argcount;
	PyObject*    pymethod;
	const char*  p;

	if (!aSelector) {
		[NSException raise:NSInvalidArgumentException
			     format:@"nil selector"];
	}

	meth_name = SELNAME(aSelector);
	len = strlen(meth_name);
      
	for (argcount=0, p=meth_name; *p; p++) {
		if (*p == ':') {
			argcount++;
		}
	}
  
	pymeth_name = alloca(PYTHONIFIED_LENGTH(meth_name, len, argcount));
	pythonify_objc_message(meth_name, pymeth_name);

	pymethod = PyObject_GetAttrString(obj, pymeth_name);
	return check_argcount(pymethod, argcount);
}


- (BOOL) respondsToSelector:(SEL) aSelector
{
	PyObject *m;

	if ([super respondsToSelector:aSelector]) {
		return YES;
	} 
    
	m = get_method_for_selector(pyObject, aSelector);

	if (m) {
        	return YES;
	} else {
		PyErr_Clear();
		return NO;
	}
}


- (NSMethodSignature *) methodSignatureForSelector:(SEL) sel
{
	/* We can't call our superclass implementation, NSProxy just raises
	 * and exception.
	 */

	char*        	   encoding;
	PyObject*          pymethod;
	PyCodeObject*      func_code;
	int                argcount;

	encoding = (char*)get_selector_encoding (self, sel);
	if (encoding) {
		/* A real Objective-C method */
		return [NSMethodSignature signatureWithObjCTypes:encoding];
	}

	pymethod = get_method_for_selector(pyObject, sel);
	if (!pymethod) {
		PyErr_Clear();
		[NSException raise:NSInvalidArgumentException 
			format:@"%s: no such selector: %s", GETISA(self)->name, SELNAME(sel)];
	}


	if (PyMethod_Check (pymethod)) {
		func_code = (PyCodeObject *) PyFunction_GetCode(
			PyMethod_Function (pymethod));
		argcount = func_code->co_argcount-1;
	} else {
		func_code = (PyCodeObject *) PyFunction_GetCode(
			pymethod);
		argcount = func_code->co_argcount;
	}

	encoding = alloca(argcount+4);
	memset(encoding, '@', argcount+3);
	encoding[argcount+3] = '\0';
	encoding[2] = ':';
	return [NSMethodSignature signatureWithObjCTypes:encoding];
}

- (void) forwardInvocation:(NSInvocation *) invocation
{
	/* XXX: Needs cleanup */
	NSMethodSignature* msign = [invocation methodSignature];
	SEL                aSelector = [invocation selector];
	PyObject*          pymethod;
	PyObject*          result;
	const char*        rettype = [msign methodReturnType];
	int		   err;
	PyObject*          args = NULL;
	unsigned int       i;
	unsigned int       argcount;      
	int		   retsize = objc_sizeof_type (rettype);
	char*              retbuffer;

	if (retsize == -1) {
		PyObjCErr_ToObjC();
	}
	
	retbuffer = alloca(retsize);
  
	pymethod = get_method_for_selector(pyObject, aSelector);

	if (!pymethod) {
		/* The method does not exist. We cannot forward this to our 
		 * super because NSProxy doesn't implement forwardInvocation. 
		 */
		PyErr_Clear();


		if (aSelector == @selector(description)) {
			id res = [self description];
			[invocation setReturnValue:&res];
			return;
		}
		[self doesNotRecognizeSelector:aSelector];
		return;
	}
 
	argcount = [msign numberOfArguments];
	args = PyTuple_New(argcount-2);
	if (args == NULL) {
		PyObjCErr_ToObjC();
	}
	for (i=2; i< argcount; i++) {
		const char *argtype;
		char *argbuffer;
		int  argsize;
		PyObject *pyarg;

		argtype = [msign getArgumentTypeAtIndex:i];

		/* What if argtype is a pointer? */

		argsize = objc_sizeof_type(argtype);
		if (argsize == -1) {
			PyObjCErr_ToObjC();
		}
		argbuffer = alloca (argsize);
		[invocation getArgument:argbuffer atIndex:i];
		pyarg = pythonify_c_value (argtype, argbuffer);
		if (pyarg == NULL) {
			Py_DECREF(args);
			PyObjCErr_ToObjC();
			return;
		}

		PyTuple_SET_ITEM (args, i-2, pyarg);
	}
	result = PyObject_CallObject(pymethod, args);
	Py_DECREF(args);

	if (result == NULL) {
		PyObjCErr_ToObjC();
	}

	err = depythonify_c_value (rettype, result, retbuffer);
	if (err == -1) {
		PyObjCErr_ToObjC();
	} else {
		[invocation setReturnValue:retbuffer];
	}
}


- (PyObject *)  pyObject
{
	return pyObject;
}

- (PyObject *)  __pyobjc_PythonObject__
{
	Py_INCREF(pyObject);
	return pyObject;
}


/*
 * Implementation for Key-Value Coding.
 *
 * Because this is a subclass of NSProxy we must implement all of the protocol,
 * and cannot rely on the implementation in our superclass. 
 *
 */

+ (BOOL)useStoredAccessor
{
 	return YES;
}

+ (BOOL)accessInstanceVariablesDirectly;
{
	return YES;
}



/*
 *  Call PyObjCTools.KeyValueCoding.getKey to get the value for a key
 */
- valueForKey:(NSString*) key;
{
static  PyObject* getKeyFunc = NULL;

	PyObject* keyName;
	PyObject* val;
	id res;

	if (getKeyFunc == NULL) {
		PyObject* name;
		PyObject* mod;
		name = PyString_FromString( "PyObjCTools.KeyValueCoding");
		if (name == NULL) {
			PyObjCErr_ToObjC();
			return nil;
		}
		mod = PyImport_Import(name);
		if (mod == NULL) {
			Py_DECREF(name);
			PyObjCErr_ToObjC();
			return nil;
		}
		getKeyFunc = PyObject_GetAttrString(mod, "getKey");
		if (getKeyFunc == NULL) {
			Py_DECREF(name);
			Py_DECREF(mod);
			PyObjCErr_ToObjC();
			return nil;
		}
		Py_DECREF(name);
		Py_DECREF(mod);
	}

	keyName = pythonify_c_value(@encode(id), &key);
	if (keyName == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	val = PyObject_CallFunction(getKeyFunc, "OO", pyObject, keyName);
	Py_DECREF(keyName);
	if (val == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	if (depythonify_c_value(@encode(id), val, &res) < 0) {
		Py_DECREF(val);
		PyObjCErr_ToObjC();
		return nil;
	}
	Py_DECREF(val);
	return res;
}

- storedValueForKey: (NSString*) key;
{
	return [self valueForKey: key];
}


/* Calls PyObjCTools.KeyValueCoding.setKey to set the key */
- (void)takeValue: value forKey: (NSString*) key;
{
static  PyObject* setKeyFunc = NULL;

	PyObject* keyName;
	PyObject* pyValue;
	PyObject* val;
	id res;

	if (setKeyFunc == NULL) {
		PyObject* name;
		PyObject* mod;
		name = PyString_FromString( "PyObjCTools.KeyValueCoding");
		if (name == NULL) {
			PyObjCErr_ToObjC();
			return;
		}
		mod = PyImport_Import(name);
		if (mod == NULL) {
			Py_DECREF(name);
			PyObjCErr_ToObjC();
			return;
		}
		setKeyFunc = PyObject_GetAttrString(mod, "setKey");
		if (setKeyFunc == NULL) {
			Py_DECREF(name);
			Py_DECREF(mod);
			PyObjCErr_ToObjC();
			return;
		}
		Py_DECREF(name);
		Py_DECREF(mod);
	}

	keyName = pythonify_c_value(@encode(id), &key);
	if (keyName == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	pyValue = pythonify_c_value(@encode(id), &value);
	if (pyValue == NULL) {
		Py_DECREF(keyName);
		PyObjCErr_ToObjC();
		return;
	}

	val = PyObject_CallFunction(setKeyFunc, "OOO", pyObject, keyName, pyValue);
	Py_DECREF(keyName);
	Py_DECREF(pyValue);
	if (val == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	Py_DECREF(val);
}

- (void)takeStoredValue: value forKey: (NSString*) key;
{
	[self takeValue: value forKey: key];
}

- (NSDictionary*) valuesForKeys: (NSArray*)keys;
{
	NSMutableDictionary* result;
	NSEnumerator* enumerator;
	id aKey, aValue;

	enumerator = [keys objectEnumerator];
	result = [NSMutableDictionary dictionary];

	while ((aKey = [enumerator nextObject]) != NULL) {
		aValue = [self valueForKey: aKey];
		[result setObject: aValue forKey: aKey];
	}

	return result;
}

- valueForKeyPath: (NSString*) keyPath;
{
	NSArray* elems = [keyPath componentsSeparatedByString:@"."];
	NSEnumerator* enumerator = [elems objectEnumerator];
	id aKey;
	id target;

	target = self;
	while ((aKey = [enumerator nextObject]) != NULL) {
		target = [target valueForKey: aKey];
	}

	return target;
}

- (void)takeValue: value forKeyPath: (NSString*) keyPath;
{
	NSArray* elems = [keyPath componentsSeparatedByString:@"."];
	id target;
	int len;
	int i;

	len = [elems count];
	target = self;
	for (i = 0; i < len-1; i++) {
		target = [target valueForKey: [elems objectAtIndex: i]];
	}

	[target takeValue: value forKey: [elems objectAtIndex: len-1]];
}

- (void)takeValuesFromDictionary: (NSDictionary*) aDictionary;
{
	NSEnumerator* enumerator = [aDictionary keyEnumerator];
	id aKey;
	id aValue;

	while ((aKey = [enumerator nextObject]) != NULL) {
		aValue = [aDictionary objectForKey: aKey];
		[self takeValue: aValue forKey: aKey];
	}
}

- (void)unableToSetNilForKey: (NSString*) key;
{
	[NSException 
		raise: NSUnknownKeyException 
		format: @"cannot set Nil for key: %@", key];
}

- (void)handleQueryWithUnboundKey: (NSString*) key;
{
	[NSException 
		raise: NSUnknownKeyException
		format: @"query for unknown key: %@", key];
}

- (void)handleTakeValue: value forUnboundKey: (NSString*) key;
{
	[NSException 
		raise: NSUnknownKeyException 
		format: @"setting unknown key: %@ to <%@>", key, value];
}


@end /* OC_PythonObject class implementation */
