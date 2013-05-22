#ifndef  PyObjC_OBJC_CLASS_H
#define  PyObjC_OBJC_CLASS_H
/*!
 * @header objc-class.m
 * @abstract Definition of the wrapper for Objective-C classes
 * @discussion
 *    This module implements the wrappers for Objective-C classes, included
 *    subclasses defined in Python.
 *
 *    The class-wrapper maintains a full __dict__ to make it easier to
 *    support introspection, and to make it easier to detect if someone
 *    does a super() call of a method.
 *
 *    Maintaining a full dict is problematic because the Objective-C runtime
 *    is fairly dynamic and does not have hooks to detect these changes. Our
 *    only way to detect changes is to periodicly check the runtime if
 *    something has changed. See the definition for PyObjCClassObject for
 *    an explanation.
 */

/*!
 * @const PyObjCClass_Type
 * @abstract The type objc.objc_class
 */
extern PyTypeObject PyObjCMetaClass_Type;
extern PyTypeObject PyObjCClass_Type;

/*extern int setup_class_meta(void);*/


/*!
 * @function PyObjCClass_Check
 * @abstract Check if an object is an Objective-C class
 * @param obj An object
 * @result Returns True if the object is an Objective-C class, false otherwise
 */
#define PyObjCClass_Check(obj) PyObject_TypeCheck(obj, &PyObjCClass_Type)
#define PyObjCMetaClass_Check(obj) PyObject_TypeCheck(obj, &PyObjCMetaClass_Type)

// The @const is not correct, but what else can we use here?
/*!
 * @const PyObjC_ClassExtender
 * @discussion
 *     PyObjC_ClassExtender is either NULL or a Python function that can
 *     update a class dictionary.
 *
 *     The interface for the extender function is:
 *          extender(super_class, class_name, class_dict)
 *
 *     The return value of the function is ignored, it should update the
 *     class_dict (which represents the __dict__ of an Objective-C class.
 */
extern PyObject* PyObjC_ClassExtender;


/*!
 * @struct PyObjCClassObject
 * @abstract The type struct for Objective-C classes (Python 2.3 and later)
 * @field base      Type actual type object
 * @field sel_to_py Mapping to speed up finding the correct Python method
 *                  for a selector.
 * @field dictoffset  Offset in the Objective-C instance for the instance
 *                    __dict__
 * @field delmethod  The method that implements __del__
 * @field hasPythonImpl True if the class is implemented in Python
 * @field generation   The value of PyObjC_MappingCount at the last time
 *                     the method-list was updated.
 * @field useKVO    should the class implement automatic KVO notifications?
 *
 * @discussion
 *      This struct is the type-object for on Objective-C class. It stores
 *      some additional information that is used to manage the interface
 *      with the Objective-C runtime.
 *
 *    dictoffset is used by objc-object.m to find the __dict__ for instances.
 *    If the offset is 0 there is no __dict__.
 *
 *    We store the __del__ implementation here instead of in the type itself
 *    to ensure that our teardown code is correctly called.
 */
typedef struct _PyObjCClassObject {
    PyHeapTypeObject base;
    Class class;
    PyObject* sel_to_py;
    PyObject* delmethod;
    PyObject* hiddenSelectors;
    PyObject* hiddenClassSelectors;

    Py_ssize_t dictoffset;
    Py_ssize_t generation;
    unsigned int useKVO:1;
    unsigned int hasPythonImpl:1;
    unsigned int isCFWrapper:1;
} PyObjCClassObject;


extern PyObject* PyObjCClass_DefaultModule;
extern PyObject* PyObjCClass_New(Class objc_class);
extern Class PyObjCClass_GetClass(PyObject* object);
extern PyObject* PyObjCClass_FindSelector(PyObject* cls, SEL selector, BOOL class_method);
extern void PyObjCClass_MaybeRescan(PyObject* class);
extern int ObjC_RegisterClassProxy(Class cls, PyObject* classProxy);
extern void PyObjCClass_CheckMethodList(PyObject* cls, int recursive);
extern Py_ssize_t PyObjCClass_DictOffset(PyObject* cls);
extern PyObject* PyObjCClass_GetDelMethod(PyObject* cls);
extern void PyObjCClass_SetDelMethod(PyObject* cls, PyObject* newval);
extern int PyObjCClass_HasPythonImplementation(PyObject* cls);
extern PyObject* PyObjCClass_ClassForMetaClass(PyObject* meta);
extern PyObject* PyObjCClass_HiddenSelector(PyObject* tp, SEL sel, BOOL classMethod); /* returns borrowed */
extern int PyObjCClass_SetHidden(PyObject* tp, SEL sel, BOOL classMethod, PyObject* metadata);
extern int PyObjCClass_AddMethods(PyObject* cls, PyObject** methods, Py_ssize_t count);
extern PyObject* PyObjCClass_ListProperties(PyObject* cls);

/* Returns a borrowed reference or NULL (without necessarily raising an exception) */
extern PyObject* PyObjCClass_TryResolveSelector(PyObject* base, PyObject* name, SEL sel);
extern PyObject* PyObjCMetaClass_TryResolveSelector(PyObject* base, PyObject* name, SEL sel);

static inline int PyObjCClass_IsCFWrapper(PyTypeObject* tp)
{
	return ((PyObjCClassObject*)tp)->isCFWrapper;
}


#endif /* PyObjC_OBJC_CLASS_H */
