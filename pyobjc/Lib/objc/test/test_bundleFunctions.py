import objc
import Foundation
import unittest

def S(*args):
    return ''.join(args)

FUNCTIONS=[
    ( 'NSIsFreedObject', S(objc._C_NSBOOL, objc._C_ID) ),
    ( 'NSCountFrames', S(objc._C_UINT) ),
]

class TestBundleFunctions (unittest.TestCase):
    def setUp(self):
        self.bundle = Foundation.NSBundle.bundleForClass_(Foundation.NSBundle)

    def testSimple(self):
        d = {}
        objc.loadBundleFunctions(self.bundle, d, FUNCTIONS)

        self.assert_('NSIsFreedObject' in d)
        self.assert_('NSCountFrames' in d)

        fn = d['NSIsFreedObject']
        obj = objc.runtime.NSObject.alloc().init()
        value = fn(obj)
        self.assert_(not value)

        # Need to look for a different example, NSCountFrames crashes
        # (that is the actual function, not the dynamic wrapper)
        #fn = d['NSCountFrames']
        #import Foundation
        #fn = Foundation.NSCountFrames
        #value = fn()
        #self.assert_(isistance(value, int))





if __name__ == "__main__":
    unittest.main()


