from PyObjCTools.TestSupport import *

import objc._lazyimport as lazyimport
import objc
import sys
import os
import struct

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a


class TestLazyImport (TestCase):
    def test_exports(self):
        self.assertIs(objc.ObjCLazyModule, lazyimport.ObjCLazyModule)
        self.assertTrue(issubclass(objc.ObjCLazyModule, type(objc)))


    def test_getattr_map(self):
        o = lazyimport.GetAttrMap(sys)
        self.assertEqual(o['path'], sys.path)
        self.assertEqual(o['version'], sys.version)
        self.assertRaises(KeyError, o.__getitem__, 'nosuchkey')

    def test_load_bundle(self):
        NSBundle = objc.lookUpClass('NSBundle')

        # _objc is linked with Foundation, hence should be able to load without
        # providing a valid path
        o = lazyimport._loadBundle('Foundation', 'com.apple.Foundation', '/dev/null')
        self.assertIsInstance(o, NSBundle)
        self.assertEqual(o.bundleIdentifier(), 'com.apple.Foundation')
        self.assertTrue(o.isLoaded())

        # Load using path
        o = lazyimport._loadBundle('AppKit', None, '/System/Library/Frameworks/AppKit.framework')
        o.load()
        self.assertEqual(o.bundleIdentifier(), 'com.apple.AppKit')
        self.assertTrue(o.isLoaded())

        # Should not be loaded yet, hence fallback from identifier to path
        o = lazyimport._loadBundle('PreferencePanes', 'com.apple.frameworks.preferencepanes', '/System/Library/Frameworks/PreferencePanes.framework')
        o.load()
        self.assertEqual(o.bundleIdentifier(), 'com.apple.frameworks.preferencepanes')
        self.assertTrue(o.isLoaded())


    def test_all_types_without_all(self):
        self.do_test_all_types(all=False)

    def test_all_types_with_all(self):
        self.do_test_all_types(all=True)

    def do_test_all_types(self, all):
        # NOTE: Test isn't ready yet
        # Note: this test uses the real functions, other tests can (and will) mock
        #       functions in objc._objc to test failure condictions, but the full
        #       API stack should be used in at least one testcase.
        metadict = {
            'constants': '$NSWorkspaceMoveOperation$NSWorkspaceCopyOperation@@$',
            'constants_dict': {
                'NSWorkspaceLinkOperation': '@',
            },
            'enums': '$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$',

            'functions': {
                'NSRectClipList': (
                    sel32or64(b'v^{_NSRect={_NSPoint=ff}{_NSSize=ff}}i', b'v^{CGRect={CGPoint=dd}{CGSize=dd}}q'),
                    '',
                    {
                        'arguments': {
                            0: {
                                'c_array_length_in_arg': 1,
                                'type_modifier': b'n'
                            }
                        }
                    }
                ),
                'FunctionThatDoesNotExist': (
                    sel32or64(b'v^{_NSRect={_NSPoint=ff}{_NSSize=ff}}i', b'v^{CGRect={CGPoint=dd}{CGSize=dd}}q'),
                    '', {}
                ),
                'NSAccessibilityActionDescription': (
                    b'@@', '', {}
                ),
            },
            'aliases': {
                'doc_string': '__doc__',
                'invalid_alias': 'does_not_exist',
            },
            'expressions': {
                'mysum': 'NSAWTEventType + NSAboveBottom + 3',
                'invalid_expression1': 'no_such_name + 1',
                'invalid_expression2': 'NSAboveBottom + "b"',
            }
        }

        initial_dict = {
                '__doc__': 'AppKit test module',
        }

        mod = objc.ObjCLazyModule ('AppKit', None, '/System/Library/Frameworks/AppKit.framework', metadict, None,
                initial_dict, ())
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        if all:
            # Force precalculation of all attributes by accessing the __all__
            # attribute
            self.assertEqual(set(dir(mod)), set(mod.__all__))

        self.assertEqual(mod.__doc__, initial_dict['__doc__'])
        self.assertEqual(mod.doc_string, initial_dict['__doc__'])
        self.assertRaises(AttributeError, getattr, mod, 'invalid_alias')
        self.assertIsInstance(mod.NSWorkspaceMoveOperation, objc.pyobjc_unicode)
        self.assertIsInstance(mod.NSWorkspaceCopyOperation, objc.pyobjc_unicode)
        self.assertIsInstance(mod.NSWorkspaceLinkOperation, objc.pyobjc_unicode)
        self.assertEqual(mod.NSAWTEventType, 16)
        self.assertEqual(mod.NSAboveBottom, 4)
        self.assertEqual(mod.NSAboveTop, 1)
        self.assertIsInstance(mod.NSRectClipList, objc.function)
        self.assertEqual(mod.NSRectClipList.__name__, 'NSRectClipList')
        self.assertArgSizeInArg(mod.NSRectClipList, 0, 1)
        self.assertRaises(AttributeError, getattr, mod, 'FunctionThatDoesNotExist')
        self.assertEqual(mod.mysum, mod.NSAWTEventType + mod.NSAboveBottom + 3)
        self.assertRaises(AttributeError, getattr, mod, 'invalid_expression1')
        self.assertRaises(AttributeError, getattr, mod, 'invalid_expression2')
        self.assertIs(mod.NSURL, objc.lookUpClass('NSURL'))
        self.assertRaises(AttributeError, getattr, mod, 'NSNonExistingClass')



        self.assertEqual(set(dir(mod)), set(mod.__all__))
        self.assertIn('NSRectClipList', mod.__dict__)
        self.assertIn('NSRectClipList', mod.__all__)
        self.assertIn('NSAccessibilityActionDescription', mod.__all__)
        self.assertIn('mysum', mod.__all__)
        self.assertIn('NSWorkspaceMoveOperation', mod.__all__)
        self.assertNotIn('__doc__', mod.__all__)

    def test_without_framework(self):
        initial_dict = {
                '__doc__': 'rootless test module',
        }
        metadict = {
            'constants': '$ABAddressBookErrorDomain$',
            'constants_dict': {
                'ABMultiValueIdentifiersErrorKey': '@',
            },
            'enums': '$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$',

            'functions': {
                'NSRectClipList': (
                    sel32or64(b'v^{_NSRect={_NSPoint=ff}{_NSSize=ff}}i', b'v^{CGRect={CGPoint=dd}{CGSize=dd}}q'),
                    '',
                    {
                        'arguments': {
                            0: {
                                'c_array_length_in_arg': 1,
                                'type_modifier': b'n'
                            }
                        }
                    }
                ),
                'NSAccessibilityActionDescription': (
                    b'@@', '', {}
                ),
            },
            'aliases': {
                'doc_string': '__doc__',
            },
            'expressions': {
                'mysum': 'NSAWTEventType + NSAboveBottom + 3',
            }
        }

        mod = objc.ObjCLazyModule ('RootLess', None, None, metadict, None,
                initial_dict, ())

        self.assertEqual(mod.__doc__, 'rootless test module')
        self.assertEqual(mod.__doc__, mod.doc_string)
        self.assertEqual(mod.NSAboveBottom, 4)
        self.assertEqual(mod.mysum, mod.NSAWTEventType + mod.NSAboveBottom + 3)
        self.assertRaises(AttributeError, getattr, mod, 'NSRectClipList')
        self.assertRaises(AttributeError, getattr, mod, 'ABAddressBookErrorDomain')
        self.assertRaises(AttributeError, getattr, mod, 'ABMultiValueIdentifiersErrorKey')


    def test_with_parents(self):
        mod = objc.ObjCLazyModule ('RootLess', None, None, None, None,
                None, (sys, os))

        self.assertEqual(mod.path, sys.path)
        self.assertIn('path', mod.__dict__)
        self.assertEqual(mod.unlink, os.unlink)
        self.assertIn('unlink', mod.__dict__)

        mod.__dict__['version_info'] = 42
        self.assertEqual(mod.version_info, 42)

        self.assertIn('walk', mod.__all__)
        self.assertIn('version', mod.__all__)
        self.assertNotIn('__doc__', mod.__all__)

    def test_all_clearing(self):
        metadict = {
            'enums': '$NSAWTEventType@16$NSAboveBottom@4$NSAboveTop@1$',
        }

        initial_dict = {
                '__doc__': 'AppKit test module',
        }

        mod = objc.ObjCLazyModule ('AppKit', None, '/System/Library/Frameworks/AppKit.framework', metadict, None,
                initial_dict, (sys,))
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        mod.__all__ = 42
        self.assertIs(mod.path, sys.path)
        self.assertNotIn('__all__', mod.__dict__)

        mod.__all__ = 42
        self.assertEqual(mod.NSAWTEventType, 16)
        self.assertNotIn('__all__', mod.__dict__)

        mod.__all__ = 42
        self.assertIs(mod.NSObject, objc.lookUpClass('NSObject'))
        self.assertNotIn('__all__', mod.__dict__)

        self.assertTrue('NSAWTEventType' in mod.__all__)
        self.assertTrue('NSAboveBottom' in mod.__all__)

    def test_enum_formats(self):
        metadict = {
            'enums': '$intval@16$floatval@4.5$charval@\'1234\'$floatval2@1e3$',
        }

        initial_dict = {
                '__doc__': 'AppKit test module',
        }

        mod = objc.ObjCLazyModule ('AppKit', None, '/System/Library/Frameworks/AppKit.framework', metadict, None,
                initial_dict, ())
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        self.assertEqual(mod.intval, 16)
        self.assertEqual(mod.floatval, 4.5)
        self.assertEqual(mod.charval, struct.unpack('>l', b'1234')[0])
        self.assertEqual(mod.floatval2, 1.0e3)

    def test_magic_aliases(self):
        metadict = {
            'aliases': {
                'umax': 'ULONG_MAX',
                'max': 'LONG_MAX',
                'min': 'LONG_MIN',
            }
        }

        initial_dict = {
                '__doc__': 'AppKit test module',
        }

        mod = objc.ObjCLazyModule ('AppKit', None, '/System/Library/Frameworks/AppKit.framework', metadict, None,
                initial_dict, ())
        self.assertIsInstance(mod, objc.ObjCLazyModule)

        if sys.maxsize > 2**32:
            self.assertEqual(mod.umax, 2**64-1)
        else:
            self.assertEqual(mod.umax, 2**32-1)
        self.assertEqual(mod.max, sys.maxsize)
        self.assertEqual(mod.min, -sys.maxsize-1)


    # XXX: add tests for the rest of the module
    # - metadict with/without various elements (that is, with/without 'misc', 'constants', ...)
    # - metadict with invalid data
    # - verify that look-ups are done in the expected order (and document?)
    # - dotted name ('Quartz.CoreGraphics')
    # - test with frameworkIdentifier == frameworkPath == None (both with and without a parents.
    # - test with protocols in metadict

if __name__ == "__main__":
    main()
