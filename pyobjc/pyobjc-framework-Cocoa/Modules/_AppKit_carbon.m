/*
 * Support code for dealing with Carbon types (at least those
 * used in AppKit and wrapped in the python core).
 */

#ifndef __LP64__

#include "pymactoolbox.h"

#else
	/* FIXME: the bits of pymactoolbox.h that we need,
	 * because said header doesn't work in 64-bit mode
	 */
extern PyObject *WinObj_New(WindowPtr);
extern int WinObj_Convert(PyObject *, WindowPtr *);
extern PyObject *WinObj_WhichWindow(WindowPtr);

#endif

static int
py2window(PyObject* obj, void* output)
{
	return WinObj_Convert(obj, (WindowPtr*)output);
}

static PyObject*
window2py(void* value)
{
	return WinObj_New((WindowPtr)value);
}

static int setup_carbon(PyObject* m __attribute__((__unused__)))
{
	if (PyObjCPointerWrapper_Register(@encode(WindowRef),
	                &window2py, &py2window) < 0)
		return -1;

	return 0;
}
