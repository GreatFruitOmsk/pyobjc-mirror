/* Copyright (c) 1996,97,98 by Lele Gaifax.  All Rights Reserved
 * Copyright (2) 2003 Ronald Oussoren
 *
 * This software may be used and distributed freely for any purpose
 * provided that this notice is included unchanged on any and all
 * copies. The author does not warrant or guarantee this software in
 * any way.
 *
 * This file is part of the PyObjC package.
 *
 * RCSfile: objc_support.h,v
 * Revision: 1.16
 * Date: 1998/08/18 15:35:57
 *
 * Created Tue Sep 10 14:11:38 1996.
 */

#ifndef _objc_support_H
#define _objc_support_H

#ifdef GNU_RUNTIME

#  include "objc-runtime-gnu.h"

#else /* NeXTSTEP / Mac OS X */

#  include "objc-runtime-apple.h"

#endif 


/*#F Takes a C value pointed by @var{datum} with its type encoded in
  @var{type}, that should be coming from an ObjC @encode directive,
  and returns an equivalent Python object where C structures and
  arrays are represented as tuples. */
extern PyObject *pythonify_c_value (const char *type,
				    void *datum);
extern PyObject *pythonify_c_return_value (const char *type,
				    void *datum);

/*#F Takes a Python object @var{arg} and translate it into a C value
  pointed by @var{datum} accordingly with the type specification
  encoded in @var{type}, that should be coming from an ObjC @encode
  directive.
  Returns NULL on success, or a static error string describing the
  error. */
extern int depythonify_c_value (const char *type,
					PyObject *arg,
					void *datum);
extern int depythonify_c_return_value (const char *type,
					PyObject *arg,
					void *datum);

/* This one is implemented in super-call.m, should be moved and renamed */
extern void PyObjCRT_SimplifySignature(char* signature, char* buf, size_t buflen);

/* From pointer-support.m */

typedef PyObject* (*PyObjCPointerWrapper_ToPythonFunc)(void*);
typedef int (*PyObjCPointerWrapper_FromPythonFunc)(PyObject*, void*);

int PyObjCPointerWrapper_Register(
	const char*, PyObjCPointerWrapper_ToPythonFunc pythonify,
	PyObjCPointerWrapper_FromPythonFunc depythonify);

PyObject* PyObjCPointerWrapper_ToPython(const char*, void*);

int PyObjCPointerWrapper_FromPython(const char*, PyObject*, void*);
int PyObjCPointerWrapper_Init(void);

extern int PyObjCRT_SizeOfReturnType(const char* type);
extern int PyObjCRT_SizeOfType(const char *type);
extern int PyObjCRT_AlignOfType(const char *type);
extern const char *PyObjCRT_SkipTypeSpec (const char *type);


extern int PyObjCRT_SetupClass(
	Class, Class, const char*, Class, Class, int, struct objc_ivar_list*);
extern void PyObjCRT_ClearClass(Class cls);

#endif /* _objc_support_H */
