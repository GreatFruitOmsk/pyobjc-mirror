#ifndef OBJC_UTIL
#define OBJC_UTIL

#include <Python.h>
#include <Foundation/NSException.h>

extern PyObject* ObjCExc_error;
extern PyObject* ObjCExc_noclass_error;
extern PyObject* ObjCExc_internal_error;

int ObjCUtil_Init(PyObject* module);

extern PyObject* ObjC_class_extender;
int ObjC_AddConvenienceMethods(Class cls, PyObject* type_dict);
int  ObjC_UpdateConvenienceMethods(PyObject* cls);

void ObjCErr_Set(PyObject* exc, char* fmt, ...);
void ObjCErr_FromObjC(NSException* localException);
void ObjCErr_ToObjC(void);

PyObject* ObjC_call_to_python(id self, SEL selector, PyObject* arglist);

char* ObjC_strdup(const char* value);

#if 0 /* Multithread support */

void ObjC_AcquireGIL(void);
void ObjC_ReleaseGIL(void);

#define ObjC_BEGIN_OBJC_CALL { ObjC_ReleaseGIL();
#define ObjC_END_OBJC_CALL ObjC_AcquireGIL(); }
#define ObjC_BEGIN_PYTHON_CALL { ObjC_AcquireGIL();
#define ObjC_END_PYTHON_CALL ObjC_ReleaseGIL(); }

#else 

#define ObjC_BEGIN_OBJC_CALL {
#define ObjC_END_OBJC_CALL }

#define ObjC_BEGIN_PYTHON_CALL {
#define ObjC_END_PYTHON_CALL }

#endif /* No multithread support */

#endif /* OBJC_UTIL */
