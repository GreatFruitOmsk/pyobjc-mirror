#ifndef OBJC_CLASS_BUILDER
#define OBJC_CLASS_BUILDER

#include <Python.h>
#include <objc/objc.h>

/*
 * The protocol for building a hybrid python&objective-C class
 * 1) Collect the necessary information (name, bases, class_dict)
 * 2) Call ObjC_BuildClass
 * 3) Create the python class
 * 4) Call PyObjCClass_SetClass
 *
 * If step 3 fails, call PyObjCClass_UnbuildClass.
 *
 * NOTE:
 *   It is _not_ possible to remove classes from the objective-C runtime,
 *   and it is therefore not possible to call 'PyObjCClass_UnbuildClass' after
 *   you have called 'PyObjCClass_SetClass'
 */
Class PyObjCClass_BuildClass(Class super_class,  PyObject* protocols,
				char* name, PyObject* class_dict);
void PyObjCClass_UnbuildClass(Class new_class);
int PyObjCClass_SetClass(Class objc_class, PyObject* py_class);

#endif /* OBJC_CLASS_BUILDER */
