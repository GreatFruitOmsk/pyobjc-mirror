import unittest

import objc

class TestConstants(unittest.TestCase):
    def testBooleans(self):
        self.assert_(objc.YES, "YES was not true.")
        self.assert_(not objc.NO, "NO was true.")

    def testNil(self):
        from types import NoneType
        self.assert_(not objc.nil, "nil is not nil/None.")
    
class TestClassLookup(unittest.TestCase):
    def testLookupClassNoSuchClassErrorRaised(self):
        self.assertRaises(objc.nosuchclass_error, objc.lookUpClass, "")
        self.assertRaises(objc.nosuchclass_error, objc.lookUpClass, "ThisClassReallyShouldNotExist")
        self.assertRaises(TypeError, objc.lookUpClass, 1)

    def testRuntimeNoSuchClassErrorRaised(self):
        try:
            objc.runtime.ThisClassReallyShouldNotExist
        except objc.nosuchclass_error:
            pass
        else:
            fail("objc.runtime.ThisClassReallyShouldNotExist should have thrown a nosuchclass_error.  It didn't.")

    def testRuntimeConsistency(self):
        self.assert_(objc.lookUpClass("NSObject"), "Failed to find NSObject class.")
        self.assertEqual(objc.lookUpClass( "NSObject" ), objc.runtime.NSObject,
                          "objc.runtime.NSObject and objc.lookUpClass('NSObject') were different.")

    def testClassList(self):
        ###! This test should probably be moved down to the Foundation test suite... 
        self.assert_(objc.runtime.NSObject in objc.getClassList(), "getClassList() does not appear to contain NSObject class")
        self.assert_(objc.runtime.NSException in objc.getClassList(), "getClassList() does not appear to contain NSException class")
        self.assert_(objc.runtime.NSMutableArray in objc.getClassList(), "getClassList() does not appear to contain NSMutableArray class")

class TestMethodInvocation(unittest.TestCase):
    def setUp(self):
        self.NSObjectInstance = objc.runtime.NSObject.alloc().init()

    def testClassInvocation(self):
        self.assert_(objc.runtime.NSObject.pyobjc_classMethods.description(), "Failed to invoke the +description method.")

    def testInstanceInvocation(self):
        self.assert_(self.NSObjectInstance.description(), "Failed to invoke the -description method.")
        self.assertEqual(self.NSObjectInstance.self(), self.NSObjectInstance, "-self did not return same self.")
        self.assertEqual(self.NSObjectInstance.pyobjc_instanceMethods.self(), self.NSObjectInstance.self())
        self.assertEqual(type(self.NSObjectInstance).pyobjc_instanceMethods.self(self.NSObjectInstance), self.NSObjectInstance.self())

    def testVarargsInvocation(self):
        objc.runtime.NSArray.arrayWithObjects_("foo", "bar", None)

if __name__ == '__main__':
    unittest.main()
