#!/usr/bin/env python
"""
Script to generate Lib/objc/test/testbnd2.m and Lib/objc/test/test_methods2.py.

These files test method passing from Objective-C to Python subclasses of 
Objective-C classes, and method passing from Python to Objective-C. 

Note that we need two variations for calls from Objective-C to Python: direct
calls and calls using an NSInvocation. The latter use a different calling
mechanism.

NOTES:
* These tests are generated because doing this by hand is *very* labour 
  intensive and boring. The chance of bugs in the testsuite is IMHO larger when
  you manually build these.
* Two argument test-cases are needed to check argument aligment. Three argument
  test-cases would also be nice, but would take way to many space. An inital
  version with 3 argument test-cases generated a C file with over 150K lines
  of code.
* Note that the testcases are very explicit (no loops with self.assert* calls)
  to make it easier to debug problems.

TODO:
- Add structured types (struct, array), we currently only test NSPoint/NSRect
- Check that we include all tests from the manually generated version.
  (We don't, see below)
- Fix bugs found by these tests ('in' arguments don't work correctly)
- The 'values' items in the TYPES array need more work: We don't really test
  boundary conditions.
- We don't test invalid arguments, bad number of arguments
- We don't test calling class-methods defined in Python. I wouldn't be 
  surprised if that doesn't work at all.
"""
import sys
import objc

OBJC_HEADER="""\
/*
 *          THIS IS A GENERATED FILE DO NOT EDIT
 *
 * This file implements a number classes that are used to test calling methods,
 * both from Python to Objective-C and from Objective-C to Python. See 
 * test_methods.py for the actual tests.
 *
 */

#import <Foundation/Foundation.h>

#include <Python.h>
#include <pyobjc-api.h>
"""

OBJC_FOOTER="""\

/* 
 * Some glue to make this a valid Python extension module
 */

static PyMethodDef no_methods[] = {
        { 0, 0, 0, 0 }
};

void inittestbndl2(void); // Remove GCC warning
void inittestbndl2(void)
{
        PyObject* m;

        m = Py_InitModule4("testbndl2", no_methods,
                    NULL, NULL, PYTHON_API_VERSION);
        if (!m) return;

        if (PyObjC_ImportAPI(m) < 0) return;

        PyModule_AddObject(m, "PyObjC_TestClass1",
            PyObjCClass_New([PyObjC_TestClass1 class]));
        PyModule_AddObject(m, "PyObjC_TestClass2",
            PyObjCClass_New([PyObjC_TestClass2 class]));

"""

PY_HEADER="""\
'''
          THIS IS A GENERATED FILE DO NOT EDIT

This file tests method calling to and from Objective-C. See testbndl.m for
the Objective-C helper classes used in theses tests.

'''
import unittest
import objc
from objc import YES, NO, nil
from Foundation import NSFTPPropertyFileOffsetKey 
import sys

NSArray = objc.runtime.NSArray

# First make sure that the pass-by-reference methods have the correct signature
set_signature = objc.set_signature_for_selector
"""

PY_MIDTEXT="""
from objc.test.testbndl2 import *

if hasattr(unittest.TestCase, 'assertAlmostEquals'):
    TestCase = unittest.TestCase
else:
    # We use assertAlmostEquals for comparing floats, python 2.2 doesn't
    # have this method in unittest.TestCase.

    class TestCase (unittest.TestCase):
        def assertAlmostEquals(self, val1, val2, message=None):
            self.assert_ (abs (val1 - val2) < 0.00001, message)

"""

PY_FOOTER="""\

if __name__ == "__main__":
    unittest.main()
"""

TYPES=[
    # ( typename, objc_signature, testvalues )
    ('BOOL', objc._C_BOOL, [ 'YES', 'NO' ]),
    ('char', objc._C_CHR, ('-128', '0', '127') ),
    ('signed short', objc._C_SHT, ('-(1<<14)', '-42', '0', '42', '1 << 14') ),
    ('signed int', objc._C_INT, ('-(1<<30)', '-42', '0', '42', '1 << 30') ),
    ('signed long', objc._C_LNG, ('-(1<<30)', '-42', '0', '42', '1 << 30') ),
    ('signed long long', objc._C_LNGLNG, ('-(1LL << 60)', '-42', '0', '42', '1LL << 60') ),
    ('unsigned char', objc._C_UCHR, ( '0', '128', '255') ),
    ('unsigned short', objc._C_USHT, ('0', '42', '1<<14') ),
    ('unsigned int', objc._C_UINT, ('0', '42', '1 << 30') ),
    ('unsigned long', objc._C_ULNG, ('0', '42', '1L << 30') ),
    ('unsigned long long', objc._C_ULNGLNG, ( '0', '42', '1LL << 62') ),
    ('float', objc._C_FLT, ( '0.128', '1.0', '42.0', '1e10')),
    ('double', objc._C_DBL, ( '0.128', '1.0', '42.0', '1e10')),
    ('id', objc._C_ID, ( 'NSFTPPropertyFileOffsetKey', )), # Fix me
    ('char*', objc._C_CHARPTR, ('"hello"', '"world"', '"foobar"')),
    ('NSPoint', "{_NSPoint=ff}", ((1, 2), (3,4),)),
    ('NSRect', "{_NSRect={_NSPoint=ff}{_NSSize=ff}}", (((1,2), (3,4)), ((7,8),(9,10)),)),
]

def tp2ident(tp):
    return tp.replace(' ', '').replace('*', 'Ptr')

def emit_objc_interfaces(fp):
    fp.write('@interface PyObjC_TestClass1 : NSObject\n{\n}\n\n')

    fp.write('/* Reset the test counter */\n')
    fp.write('+(void)clsReset;\n')
    fp.write('-(void)reset;\n')
    fp.write('\n')

    fp.write('/* Test return values */\n')
    for tp, sign, values in TYPES:
        if not values: continue;
        fp.write('+(%s)%sClsMethod;\n'%(tp, tp2ident(tp)))
        fp.write('-(%s)%sMethod;\n'%(tp, tp2ident(tp)))

    fp.write('/* Single argument passing */\n')
    for tp, sign, values in TYPES:
        fp.write('-(id)%sArg:(%s)arg;\n'%(tp2ident(tp), tp))

    fp.write('/* Multiple arguments */\n')
    for tp1, sign1, values2 in TYPES:
        for tp2, sign2, values2 in TYPES:
            fp.write('-(id)%sArg:(%s)arg1 and%sArg:(%s)arg2;\n'%(tp2ident(tp1), tp1, tp2ident(tp2), tp2))

    fp.write('/* in, out and in-out arguments */\n')
    for tp, sign, values in TYPES:
        fp.write('-(id)%sInArg:(%s*)arg;\n'%(tp2ident(tp), tp))
        fp.write('-(void)%sOutArg:(%s*)arg;\n'%(tp2ident(tp), tp))
        fp.write('-(id)%sInOutArg:(%s*)arg;\n'%(tp2ident(tp), tp))

    fp.write('\n@end // interface PyObjC_TestClass1\n')

    fp.write('\n\n\n\n')
    fp.write('@interface PyObjC_TestClass2 : NSObject\n{\n}\n\n')

    for tp, sign, values in TYPES:
        fp.write('+(%s)call%sMethodOf:(PyObjC_TestClass1*)obj;\n'%(tp, tp2ident(tp)))
        fp.write('+(%s)invoke%sMethodOf:(PyObjC_TestClass1*)obj;\n'%(tp, tp2ident(tp)))

    fp.write('/* Single argument passing */\n')
    for tp, sign, values in TYPES:
        fp.write('+(id)call%sArg:(%s)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))
        fp.write('+(id)invoke%sArg:(%s)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))

    fp.write('/* Multiple arguments */\n')
    for tp1, sign1, values2 in TYPES:
        for tp2, sign2, values2 in TYPES:
            fp.write('+(id)call%sArg:(%s)arg1 and%sArg:(%s)arg2 of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp1), tp1, tp2ident(tp2), tp2))
            fp.write('+(id)invoke%sArg:(%s)arg1 and%sArg:(%s)arg2 of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp1), tp1, tp2ident(tp2), tp2))

    fp.write('/* in, out and in-out arguments */\n')
    for tp, sign, values in TYPES:
        fp.write('+(id)invoke%sInArg:(%s*)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))
        fp.write('+(id)call%sInArg:(%s*)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))
        fp.write('+(void)invoke%sOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))
        fp.write('+(void)call%sOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))
        fp.write('+(id)invoke%sInOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))
        fp.write('+(id)call%sInOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj;\n'%(tp2ident(tp), tp))

    fp.write('\n@end // interface PyObjC_TestClass2\n\n')


def write_objc_item(fp, item):
    if isinstance(item, (tuple, list)):
        fp.write('{')
        for i in item[:-1]:
            write_objc_item(fp, i)
            fp.write(', ')
        write_objc_item(fp, item[-1])
        fp.write('}')
    else:
        fp.write(str(item))

def write_py_item(fp, item):
    if isinstance(item, (tuple, list)):
        if len(item) > 1:
            fp.write('(')
            for i in item[:-1]:
                write_py_item(fp, i)
                fp.write(', ')
            write_py_item(fp, item[-1])
            fp.write(')')
        else:
            fp.write('(')
            write_py_item(fp, item[0])
            fp.write(',)')
    else:
        fp.write(str(item).replace('LL', 'L'))

def emit_objc_implementations(fp):

    fp.write('/* Some global variables */\n')
    fp.write('static int g_idx = 0;\n')

    for tp, sign, values in TYPES:
        if not values: continue

        if tp == 'id':
            fp.write('static %s g_%s_values[%d];\n'%(tp, tp2ident(tp), len(values)))
            continue

        fp.write('static %s g_%s_values[] = {\n'%(tp, tp2ident(tp)))
        for item in values[:-1]:
            fp.write('\t')
            write_objc_item(fp, item)
            fp.write(",\n")
        fp.write('\t')
        write_objc_item(fp, values[-1])
        fp.write('\n};\n\n')


    fp.write('static id arg2id(const char* argtype, void* argptr)\n')
    fp.write('{\n')
    fp.write('\tid res;\n')
    fp.write('\tPyObject* tmp;\n')
    fp.write('\ttmp = PyObjC_ObjCToPython(argtype, argptr);\n')
    fp.write('\tif (tmp == NULL) { PyObjCErr_ToObjC(); return nil; }\n')
    fp.write('\tres = PyObjC_PythonToId(tmp);\n')
    fp.write('\tPy_DECREF(tmp);\n')
    fp.write('\tif (PyErr_Occurred()) { PyObjCErr_ToObjC(); return nil; }\n')
    fp.write('\treturn res;')
    fp.write('}\n\n\n')

    fp.write('@implementation PyObjC_TestClass1 : NSObject\n\n')

    fp.write('+(void)clsReset\n')
    fp.write('{\n')
    fp.write('\tg_idx = 0;\n')
    fp.write('}\n')
    fp.write('-(void)reset;\n')
    fp.write('{\n')
    fp.write('\tg_idx = 0;\n')
    fp.write('}\n')
    fp.write('\n')

    for tp, sign, values in TYPES:
        fp.write('+(%s)%sClsMethod\n'%(tp, tp2ident(tp)))
        fp.write('{\n')
        fp.write('\tif (g_idx > %d) g_idx = 0;\n'%(len(values),))
        fp.write('\treturn g_%s_values[g_idx++];\n'%(tp2ident(tp),))
        fp.write('}\n\n')

        fp.write('-(%s)%sMethod;\n'%(tp, tp2ident(tp)))
        fp.write('{\n')
        fp.write('\tif (g_idx > %d) g_idx = 0;\n'%(len(values),))
        fp.write('\treturn g_%s_values[g_idx++];\n'%(tp2ident(tp),))
        fp.write('}\n\n')

    fp.write('/* Single argument passing */\n')
    for tp, sign, values in TYPES:
        fp.write('-(id)%sArg:(%s)arg\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\treturn arg2id(@encode(%s), &arg);\n'%(tp))
        fp.write('}\n\n')

    for tp1, sign1, values1 in TYPES:
        for tp2, sign2, values2 in TYPES:
            fp.write('-(id)%sArg:(%s)arg1 and%sArg:(%s)arg2\n'%(tp2ident(tp1), tp1, tp2ident(tp2), tp2))
            fp.write('{\n')
            fp.write('\tNSMutableArray* res;\n')
            fp.write('\tres = [NSMutableArray array];\n')
            fp.write('\t[res addObject:arg2id(@encode(%s), &arg1)];\n'%(tp1,))
            fp.write('\t[res addObject:arg2id(@encode(%s), &arg2)];\n'%(tp2,))
            fp.write('\treturn res;\n')
            fp.write('}\n\n')

    fp.write('/* in, out and in-out arguments */\n')
    for tp, sign, values in TYPES:
        fp.write('-(id)%sInArg:(%s*)arg\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\treturn arg2id(@encode(%s), arg);\n'%(tp,))
        fp.write('}\n\n')

        fp.write('-(void)%sOutArg:(%s*)arg;\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\tif (g_idx > %d) g_idx = 0;\n'%(len(values),))
        fp.write('\t*arg = g_%s_values[g_idx++];\n'%(tp2ident(tp),))
        fp.write('}\n\n')

        fp.write('-(id)%sInOutArg:(%s*)arg;\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\tid res = arg2id(@encode(%s), arg);\n'%(tp,))
        fp.write('\tif (g_idx > %d) g_idx = 0;\n'%(len(values),))
        fp.write('\t*arg = g_%s_values[g_idx++];\n'%(tp2ident(tp),))
        fp.write('\treturn res;\n')
        fp.write('}\n\n')

    fp.write('\n@end // implementation PyObjC_TestClass1\n')

    fp.write('\n\n\n\n')

    fp.write('@implementation PyObjC_TestClass2 : NSObject\n\n')

    fp.write('#define SETUP_INVOCATION(inv, target, selector)\\\n')
    fp.write('\t{\\\n')
    fp.write('\t\tid sign = [target methodSignatureForSelector:selector];\\\n')
    fp.write('\t\tif (sign == NULL) {\\\n')
    fp.write('\t\t\tPyErr_SetString(PyExc_AttributeError, SELNAME(selector));\\\n')
    fp.write('\t\t\tPyObjCErr_ToObjC();\\\n')
    fp.write('\t\t}\\\n')
    fp.write('\t\tinv = [NSInvocation invocationWithMethodSignature:\\\n')
    fp.write('\t\t\t[target methodSignatureForSelector:selector]];\\\n')
    fp.write('\t\t[inv setTarget:target];\\\n')
    fp.write('\t\t[inv setSelector:selector];\\\n')
    fp.write('\t}\n')
    fp.write('\n\n')

    for tp, sign, values in TYPES:
        fp.write('+(%s)call%sMethodOf:(PyObjC_TestClass1*)obj\n'%(tp, tp2ident(tp)))
        fp.write('{\n')
        fp.write('\treturn [obj %sMethod];\n'%(tp2ident(tp)))
        fp.write('}\n\n')
        fp.write('+(%s)invoke%sMethodOf:(PyObjC_TestClass1*)obj\n'%(tp, tp2ident(tp)))
        fp.write('{\n')
        fp.write('\t%s res;\n'%(tp,))
        fp.write('\tNSInvocation* inv;\n\n')
        fp.write('\tSETUP_INVOCATION(inv, obj, @selector(%sMethod))\n'%(tp2ident(tp),))
        fp.write('\t[obj forwardInvocation:inv];\n')
        fp.write('\t[inv getReturnValue:&res];\n')
        fp.write('\treturn res;\n')
        fp.write('}\n\n')


    for tp, sign, values in TYPES:
        fp.write('+(id)call%sArg:(%s)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\treturn [obj %sArg:arg];\n'%(tp2ident(tp),))
        fp.write('}\n\n')
            
        fp.write('+(id)invoke%sArg:(%s)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\tid res;\n')
        fp.write('\tNSInvocation* inv;\n\n')
        fp.write('\tSETUP_INVOCATION(inv, obj, @selector(%sArg:))\n'%(tp2ident(tp),))
        fp.write('\t[inv setArgument:&arg atIndex:2];\n')
        fp.write('\t[obj forwardInvocation:inv];\n')
        fp.write('\t[inv getReturnValue:&res];\n')
        fp.write('\treturn res;\n')
        fp.write('}\n\n')

    for tp1, sign1, values1 in TYPES:
        for tp2, sign2, values2 in TYPES:
            fp.write('+(id)call%sArg:(%s)arg1 and%sArg:(%s)arg2 of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp1), tp1, tp2ident(tp2), tp2))
            fp.write('{\n')
            fp.write('\treturn [obj %sArg:arg1 and%sArg:arg2];\n'%(tp2ident(tp1), tp2ident(tp2)))
            fp.write('}\n\n')

            fp.write('+(id)invoke%sArg:(%s)arg1 and%sArg:(%s)arg2 of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp1), tp1, tp2ident(tp2), tp2))
            fp.write('{\n')
            fp.write('\tid res;\n')
            fp.write('\tNSInvocation* inv;\n\n')
            fp.write('\tSETUP_INVOCATION(inv, obj, @selector(%sArg:and%sArg:))\n'%(tp2ident(tp1), tp2ident(tp2)))
            fp.write('\t[inv setArgument:&arg1 atIndex:2];\n')
            fp.write('\t[inv setArgument:&arg2 atIndex:3];\n')
            fp.write('\t[obj forwardInvocation:inv];\n')
            fp.write('\t[inv getReturnValue:&res];\n')
            fp.write('\treturn res;\n')
            fp.write('}\n\n')

    for tp, sign, values in TYPES:
        fp.write('+(id)call%sInArg:(%s*)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\treturn [obj %sInArg:arg];\n'%(tp2ident(tp),))
        fp.write('}\n\n')
        fp.write('+(void)call%sOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\t[obj %sOutArg:arg];\n'%(tp2ident(tp),))
        fp.write('}\n\n')
        fp.write('+(id)call%sInOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\treturn [obj %sInOutArg:arg];\n'%(tp2ident(tp),))
        fp.write('}\n\n')
        fp.write('+(id)invoke%sInArg:(%s*)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\tid res;\n')
        fp.write('\tNSInvocation* inv;\n\n')
        fp.write('\tSETUP_INVOCATION(inv, obj, @selector(%sInArg:))\n'%(tp2ident(tp),))
        fp.write('\t[inv setArgument:&arg atIndex:2];\n')
        fp.write('\t[obj forwardInvocation:inv];\n')
        fp.write('\t[inv getReturnValue:&res];\n')
        fp.write('\treturn res;\n')
        fp.write('}\n\n')
        fp.write('+(void)invoke%sOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\tNSInvocation* inv;\n\n')
        fp.write('\tSETUP_INVOCATION(inv, obj, @selector(%sOutArg:))\n'%(tp2ident(tp),))
        fp.write('\t[inv setArgument:&arg atIndex:2];\n')
        fp.write('\t[obj forwardInvocation:inv];\n')
        fp.write('}\n\n')
        fp.write('+(id)invoke%sInOutArg:(%s*)arg of:(PyObjC_TestClass1*)obj\n'%(tp2ident(tp), tp))
        fp.write('{\n')
        fp.write('\tid res;\n')
        fp.write('\tNSInvocation* inv;\n\n')
        fp.write('\tSETUP_INVOCATION(inv, obj, @selector(%sInOutArg:))\n'%(tp2ident(tp),))
        fp.write('\t[inv setArgument:&arg atIndex:2];\n')
        fp.write('\t[obj forwardInvocation:inv];\n')
        fp.write('\t[inv getReturnValue:&res];\n')
        fp.write('\treturn res;\n')
        fp.write('}\n\n')

    fp.write('\n@end // implementation PyObjC_TestClass2\n\n')

def emit_py_method_signatures(fp):
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('set_signature("PyObjC_TestClass1", "%sInOutArg:", "@@:N^%s")\n'%(nm, sign))
        fp.write('set_signature("PyObjC_TestClass1", "%sOutArg:", "v@:o^%s")\n'%(nm, sign))
        fp.write('set_signature("PyObjC_TestClass1", "%sInArg:", "@@:n^%s")\n'%(nm, sign))

        fp.write('set_signature("PyObjC_TestClass2", "call%sInOutArg:of:", "@@:N^%s@")\n'%(nm, sign))
        fp.write('set_signature("PyObjC_TestClass2", "call%sOutArg:of:", "v@:o^%s@")\n'%(nm, sign))
        fp.write('set_signature("PyObjC_TestClass2", "call%sInArg:of:", "@@:n^%s@")\n'%(nm, sign))
        fp.write('set_signature("PyObjC_TestClass2", "invoke%sInOutArg:of:", "@@:N^%s@")\n'%(nm, sign))
        fp.write('set_signature("PyObjC_TestClass2", "invoke%sOutArg:of:", "v@:o^%s@")\n'%(nm, sign))
        fp.write('set_signature("PyObjC_TestClass2", "invoke%sInArg:of:", "@@:n^%s@")\n'%(nm, sign))

def emit_py_to_objc(fp):
    fp.write('class PyToObjC (TestCase):\n')
    fp.write('\t# Test calling Objective-C from Python\n')

    # Simple returns (Class methods)
    fp.write('\t# Simple returns from class methods\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef testCls%sResult(self):\n'%(nm,))
        fp.write('\t\tPyObjC_TestClass1.clsReset()\n')
        for v in values:
            if tp not in ('float', 'double'):
                fp.write('\t\tself.assertEquals')
            else:
                fp.write('\t\tself.assertAlmostEquals')

            fp.write('(PyObjC_TestClass1.%sClsMethod(), '%(nm,))
            write_py_item(fp, v)
            fp.write(')\n')
        fp.write('\n\n')

    # Simple returns (Instance methods)
    fp.write('\t# Simple returns from instance methods\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef test%sResult(self):\n'%(nm,))
        fp.write('\t\to = PyObjC_TestClass1.alloc().init()\n')
        fp.write('\t\tself.assert_(o is not None)\n')
        fp.write('\t\to.reset()\n')
        for v in values:
            if tp not in ('float', 'double'):
                fp.write('\t\tself.assertEquals')
            else:
                fp.write('\t\tself.assertAlmostEquals')

            fp.write('(o.%sMethod(), '%(nm, ))
            write_py_item(fp, v)
            fp.write(')\n')
        fp.write('\n\n')

    # One argument
    fp.write('\t# One argument\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef test%sArg(self):\n'%(nm,))
        fp.write('\t\to = PyObjC_TestClass1.alloc().init()\n')
        fp.write('\t\tself.assert_(o is not None)\n')
        for v in values:
            fp.write('\t\tr = o.%sArg_('%(nm,))
            write_py_item(fp, v)
            fp.write(')\n')

            if tp not in ('float', 'double'):
                fp.write('\t\tself.assertEquals(r, ')
            else:
                fp.write('\t\tself.assertAlmostEquals(r, ')
            write_py_item(fp, v)
            fp.write(')\n')
        fp.write('\n\n')

    # Two arguments
    fp.write('\t# Two arguments\n\n')
    for tp1, sign1, values1 in TYPES:
        nm1 = tp2ident(tp1)
        for tp2, sign2, values2 in TYPES:
            nm2 = tp2ident(tp2)
            fp.write('\tdef test%sAnd%sArg(self):\n'%(nm1,nm2))
            fp.write('\t\to = PyObjC_TestClass1.alloc().init()\n')
            fp.write('\t\tself.assert_(o is not None)\n')
            for v1 in values1:
                for v2 in values2:
                    fp.write('\t\tr = o.%sArg_and%sArg_('%(nm1,nm2))
                    write_py_item(fp, v1)
                    fp.write(', ')
                    write_py_item(fp, v2)
                    fp.write(')\n')

                    if tp1 not in ('float', 'double'):
                        fp.write('\t\tself.assertEquals(r[0], ')
                    else:
                        fp.write('\t\tself.assertAlmostEquals(r[0], ')
                    write_py_item(fp, v1)
                    fp.write(')\n')

                    if tp2 not in ('float', 'double'):
                        fp.write('\t\tself.assertEquals(r[1], ')
                    else:
                        fp.write('\t\tself.assertAlmostEquals(r[1], ')
                    write_py_item(fp, v2)
                    fp.write(')\n')
            fp.write('\n\n')

    # Pass by reference arguments (in)
    fp.write('\t# Pass by reference arguments (in)\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef test%sIn(self):\n'%(nm,))
        fp.write('\t\to = PyObjC_TestClass1.alloc().init()\n')
        fp.write('\t\tself.assert_(o is not None)\n')
        for v in values:
            fp.write('\t\tr = o.%sInArg_('%(nm,))
            write_py_item(fp, v)
            fp.write(')\n')

            if tp not in ('float', 'double'):
                fp.write('\t\tself.assertEquals(r, ')
            else:
                fp.write('\t\tself.assertAlmostEquals(r, ')
            write_py_item(fp, v)
            fp.write(')\n')
        fp.write('\n\n')

    # Pass by reference arguments (out)
    fp.write('\t# Pass by reference arguments (out)\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef test%sOut(self):\n'%(nm,))
        fp.write('\t\to = PyObjC_TestClass1.alloc().init()\n')
        fp.write('\t\tself.assert_(o is not None)\n')
        fp.write('\t\to.reset()\n')
        for v in values:
            fp.write('\t\tr = o.%sOutArg_()\n'%(nm,))

            fp.write('\t\tself.assertEquals(r[0], None)\n')
            if tp not in ('float', 'double'):
                fp.write('\t\tself.assertEquals(r[1], ')
            else:
                fp.write('\t\tself.assertAlmostEquals(r[1], ')
            write_py_item(fp, v)
            fp.write(')\n')
        fp.write('\n\n')
        
    # Pass by reference arguments (inout)
    fp.write('\t# Pass by reference arguments (out)\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef test%sInOut(self):\n'%(nm,))
        fp.write('\t\to = PyObjC_TestClass1.alloc().init()\n')
        fp.write('\t\tself.assert_(o is not None)\n')
        fp.write('\t\to.reset()\n')
        valuesrev = list(values[:])
        valuesrev.reverse()
        valuesrev = tuple(valuesrev)
        for vin, vout in zip(valuesrev, values):
            fp.write('\t\tr = o.%sInOutArg_('%(nm,))
            write_py_item(fp, vin) 
            fp.write(')\n')

            if tp not in ('float', 'double'):
                fp.write('\t\tself.assertEquals(r[0], ')
            else:
                fp.write('\t\tself.assertAlmostEquals(r[0], ')
            write_py_item(fp, vin)
            fp.write(')\n')

            if tp not in ('float', 'double'):
                fp.write('\t\tself.assertEquals(r[1], ')
            else:
                fp.write('\t\tself.assertAlmostEquals(r[1], ')
            write_py_item(fp, vout)
            fp.write(')\n')
        fp.write('\n\n')

def emit_python_subclass(fp):
    fp.write('# Helper arrays\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('g_%s_values = '%(nm,))
        write_py_item(fp, values)
        fp.write('\n')

    fp.write('\n\n')

    fp.write('class Python_TestClass (objc.runtime.NSObject):\n')
    fp.write('\tdef init(self):\n')
    fp.write('\t\tself = super(Python_TestClass, self).init()\n')
    fp.write('\t\tself.reset()\n')
    fp.write('\t\treturn self\n')
    fp.write('\n\n')
    fp.write('\tdef reset(self):\n')
    fp.write('\t\tself.counter = 0\n')
    fp.write('\n\n')

    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef %sMethod(self):\n'%(nm,))
        fp.write('\t\tif self.counter > %d: self.reset()\n'%(len(values),))
        fp.write('\t\tidx = self.counter\n')
        fp.write('\t\tself.counter += 1\n')
        fp.write('\t\treturn g_%s_values[idx]\n'%(nm,))
        fp.write('\t%sMethod = objc.selector(%sMethod, signature="%s@:")\n'%(
            nm, nm, sign))
        fp.write('\n\n')

    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef %sArg_(self, arg):\n'%(nm,))
        fp.write('\t\treturn arg # return the same\n')
        fp.write('\t%sArg_ = objc.selector(%sArg_, signature="@@:%s")\n'%(
            nm, nm, sign))
        fp.write('\n\n')

    for tp1, sign1, values1 in TYPES:
        for tp2, sign2, values2 in TYPES:
            nm1 = tp2ident(tp1)
            nm2 = tp2ident(tp2)
            fp.write('\tdef %sArg_and%sArg_(self, arg1, arg2):\n'%(nm1, nm2))
            fp.write('\t\treturn [ arg1, arg2 ]\n')
            fp.write('\t%sArg_and%sArg_ = objc.selector(%sArg_and%sArg_, signature="@@:%s%s")\n'%(
                nm1, nm2, nm1, nm2, sign1, sign2))
            fp.write('\n\n')

    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        fp.write('\tdef %sInArg_(self, arg):\n'%(nm,))
        fp.write('\t\treturn arg\n')
        fp.write('\t%sInArg_ = objc.selector(%sInArg_, signature="@@:%s^%s")\n'%(
            nm, nm, objc._C_IN, sign))
        fp.write('\n\n')

        fp.write('\tdef %sOutArg_(self):\n'%(tp2ident(tp),))
        fp.write('\t\tif (self.counter > %d): self.reset()\n'%(len(values),))
        fp.write('\t\tres = g_%s_values[self.counter]\n'%(nm,))
        fp.write('\t\tself.counter += 1\n')
        fp.write('\t\treturn (None, res)\n')
        fp.write('\t%sOutArg_ = objc.selector(%sOutArg_, signature="v@:%s^%s")\n'%(
            nm, nm, objc._C_OUT, sign))
        fp.write('\n\n')

        fp.write('\tdef %sInOutArg_(self, arg):\n'%(tp2ident(tp),))
        fp.write('\t\tif (self.counter > %d): self.reset()\n'%(len(values),))
        fp.write('\t\tres = g_%s_values[self.counter];\n'%(nm,))
        fp.write('\t\tself.counter += 1\n')
        fp.write('\t\treturn (arg, res)\n')
        fp.write('\t%sInOutArg_ = objc.selector(%sInOutArg_, signature="@@:%s^%s")\n'%(
            nm, nm, objc._C_INOUT, sign))
        fp.write('\n\n')

def emit_py_from_objc(fp):
    fp.write('class ObjCToPy (TestCase):\n')
    fp.write('\t# Test calling Python from Objective-C\n')

    # Simple returns (Instance methods)
    fp.write('\t# Simple returns from instance methods\n\n')
    for tp, sign, values in TYPES:
        for kind in   ('call', 'invoke'):
            nm = tp2ident(tp)
            fp.write('\tdef test%s%sResult(self):\n'%(kind, nm,))
            fp.write('\t\to = Python_TestClass.alloc().init()\n')
            fp.write('\t\tself.assert_(o is not None)\n')
            fp.write('\t\to.reset()\n')
            for v in values:
                if tp not in ('float', 'double'):
                    fp.write('\t\tself.assertEquals')
                else:
                    fp.write('\t\tself.assertAlmostEquals')

                fp.write('(PyObjC_TestClass2.%s%sMethodOf_(o), '%(kind, nm, ))
                write_py_item(fp, v)
                fp.write(')\n')
            fp.write('\n\n')

    # One argument
    fp.write('\t# One argument\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        for kind in  ('call', 'invoke'):
            fp.write('\tdef test%s%sArg(self):\n'%(kind, nm,))
            fp.write('\t\to = Python_TestClass.alloc().init()\n')
            fp.write('\t\tself.assert_(o is not None)\n')
            for v in values:
                fp.write('\t\tr = PyObjC_TestClass2.%s%sArg_of_('%(kind, nm,))
                write_py_item(fp, v)
                fp.write(', o)\n')

                if tp not in ('float', 'double'):
                    fp.write('\t\tself.assertEquals(r, ')
                else:
                    fp.write('\t\tself.assertAlmostEquals(r, ')
                write_py_item(fp, v)
                fp.write(')\n')
            fp.write('\n\n')

    # Two arguments
    fp.write('\t# Two arguments\n\n')
    for tp1, sign1, values1 in TYPES:
        nm1 = tp2ident(tp1)
        for tp2, sign2, values2 in TYPES:
            nm2 = tp2ident(tp2)
            for kind in ('call', 'invoke'):
                fp.write('\tdef test%s%sAnd%sArg(self):\n'%(kind, nm1,nm2))
                fp.write('\t\to = Python_TestClass.alloc().init()\n')
                fp.write('\t\tself.assert_(o is not None)\n')
                for v1 in values1:
                    for v2 in values2:
                        fp.write('\t\tr = PyObjC_TestClass2.%s%sArg_and%sArg_of_('%(kind, nm1,nm2))
                        write_py_item(fp, v1)
                        fp.write(', ')
                        write_py_item(fp, v2)
                        fp.write(', o)\n')

                        if tp1 not in ('float', 'double'):
                            fp.write('\t\tself.assertEquals(r[0], ')
                        else:
                            fp.write('\t\tself.assertAlmostEquals(r[0], ')
                        write_py_item(fp, v1)
                        fp.write(')\n')

                        if tp2 not in ('float', 'double'):
                            fp.write('\t\tself.assertEquals(r[1], ')
                        else:
                            fp.write('\t\tself.assertAlmostEquals(r[1], ')
                        write_py_item(fp, v2)
                        fp.write(')\n')
                fp.write('\n\n')

    # Pass by reference arguments (in)
    fp.write('\t# Pass by reference arguments (in)\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        for kind in ('call', 'invoke'):
            fp.write('\tdef test%s%sIn(self):\n'%(kind, nm,))
            fp.write('\t\to = Python_TestClass.alloc().init()\n')
            fp.write('\t\tself.assert_(o is not None)\n')
            for v in values:
                fp.write('\t\tr = PyObjC_TestClass2.%s%sInArg_of_('%(kind, nm,))
                write_py_item(fp, v)
                fp.write(', o)\n')

                if tp not in ('float', 'double'):
                    fp.write('\t\tself.assertEquals(r, ')
                else:
                    fp.write('\t\tself.assertAlmostEquals(r, ')
                write_py_item(fp, v)
                fp.write(')\n')
            fp.write('\n\n')

    # Pass by reference arguments (out)
    fp.write('\t# Pass by reference arguments (out)\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        for kind in ('call', 'invoke'):
            fp.write('\tdef test%s%sOut(self):\n'%(kind, nm,))
            fp.write('\t\to = Python_TestClass.alloc().init()\n')
            fp.write('\t\tself.assert_(o is not None)\n')
            fp.write('\t\to.reset()\n')
            for v in values:
                fp.write('\t\tr = PyObjC_TestClass2.%s%sOutArg_of_(o)\n'%(
                    kind, nm,))

                fp.write('\t\tself.assertEquals(r[0], None)\n')
                if tp not in ('float', 'double'):
                    fp.write('\t\tself.assertEquals(r[1], ')
                else:
                    fp.write('\t\tself.assertAlmostEquals(r[1], ')
                write_py_item(fp, v)
                fp.write(')\n')
            fp.write('\n\n')
            
    # Pass by reference arguments (inout)
    fp.write('\t# Pass by reference arguments (out)\n\n')
    for tp, sign, values in TYPES:
        nm = tp2ident(tp)
        for kind in ('call', 'invoke'):
            fp.write('\tdef test%s%sInOut(self):\n'%(kind, nm,))
            fp.write('\t\to = Python_TestClass.alloc().init()\n')
            fp.write('\t\tself.assert_(o is not None)\n')
            fp.write('\t\to.reset()\n')
            valuesrev = list(values[:])
            valuesrev.reverse()
            valuesrev = tuple(valuesrev)
            for vin, vout in zip(valuesrev, values):
                fp.write('\t\tr = PyObjC_TestClass2.%s%sInOutArg_of_('%(
                    kind, nm,))
                write_py_item(fp, vin) 
                fp.write(', o)\n')

                if tp not in ('float', 'double'):
                    fp.write('\t\tself.assertEquals(r[0], ')
                else:
                    fp.write('\t\tself.assertAlmostEquals(r[0], ')
                write_py_item(fp, vin)
                fp.write(')\n')

                if tp not in ('float', 'double'):
                    fp.write('\t\tself.assertEquals(r[1], ')
                else:
                    fp.write('\t\tself.assertAlmostEquals(r[1], ')
                write_py_item(fp, vout)
                fp.write(')\n')
            fp.write('\n\n')


print "------------- testbndl.m -----------"
fp = open('Lib/objc/test/testbndl2.m', 'w')
fp.write(OBJC_HEADER)
emit_objc_interfaces(fp)
emit_objc_implementations(fp)
fp.write(OBJC_FOOTER)
for tp, sign, values in TYPES:
    if tp != 'id': continue
    
    fp.write('\t/* Initialize g_id_values */\n')
    for idx, v in enumerate(values):
        fp.write('\tg_id_values[%d] = %s;\n'%(idx, v))

fp.write('}\n')
fp.close()

print "------------- test_methods.py -----------"
fp = open('Lib/objc/test/test_methods2.py', 'w')
fp.write(PY_HEADER)
emit_py_method_signatures(fp)
fp.write(PY_MIDTEXT)
emit_py_to_objc(fp)
emit_python_subclass(fp)
emit_py_from_objc(fp)

fp.write(PY_FOOTER)

fp.close()

