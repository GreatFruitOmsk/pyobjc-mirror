import unittest
import objc
import types
import warnings

from Foundation import *

class TestNSString(unittest.TestCase):
    def testClassTree(self):
        self.assert_(issubclass(objc.pyobjc_unicode, unicode))

    def testCompare(self):
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'bar') == 1,
            u"NSString doesn't compare correctly")
        self.assert_(
            NSString.localizedCaseInsensitiveCompare_(u'foo',u'Foo') == 0,
            u"NSString doesn't compare correctly")

    def testFormatting(self):

        self.assertRaises(TypeError, NSString.stringWithFormat_, "foo")

        # The test on instances is slightly more verbose to avoid warnings
        try:
            obj = NSString.alloc()
            self.assertRaises(TypeError, obj.initWithFormat_, "foo")
            obj = obj.initWithString_("foo")
        except AssertionError, msg:
            raise

        try:
            obj = NSString.alloc()
            self.assertRaises(TypeError, obj.initWithFormat_locale_, "foo", {})
            obj = obj.initWithString_("foo")
        except AssertionError, msg:
            raise

        try:
            obj = NSString.alloc()
            self.assertRaises(TypeError, obj.initWithFormat_arguments_, "foo", [])
            obj = obj.initWithString_("foo")
        except AssertionError, msg:
            raise

        try:
            obj = NSString.alloc()
            self.assertRaises(TypeError, obj.initWithFormat_locale_arguments_, "foo", {}, [])
            obj = obj.initWithString_("foo")
        except AssertionError, msg:
            raise


            


class TestNSStringBridging(unittest.TestCase):
    def setUp(self):
        self.nsUniString = NSString.stringWithString_(u"unifoo")
        self.pyUniString = u"unifoo"

    def testBasicComparison(self):
        self.assertEquals(u"unifoo", NSString.stringWithString_(u"unifoo"))

        u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
        self.assertEquals(u, NSString.stringWithString_(u));

    def testTypesAndClasses(self):
        self.assert_(isinstance(self.nsUniString, unicode))
        self.assert_(isinstance(self.pyUniString, unicode))

    def testStrConversion(self):
        curEnabledFlag = objc.setStrBridgeEnabled(True)
        try:
            v = NSString.stringWithString_("hello")
            self.assert_(isinstance(v, objc.pyobjc_unicode))
            self.assertEquals(v, u"hello")


            self.assertRaises(UnicodeError, unicode, "\xff")
            self.assertRaises(UnicodeError, NSString.stringWithString_, '\xff')

            objc.setStrBridgeEnabled(False)

            warnings.filterwarnings('error', category=objc.PyObjCStrBridgeWarning) 
            try:
                #v = NSString.stringWithString_("hello")
                self.assertRaises(objc.PyObjCStrBridgeWarning,
                        NSString.stringWithString_, "hello")

            finally:
                del warnings.filters[0]


        finally:
            objc.setStrBridgeEnabled(curEnabledFlag)

class TestMutable(unittest.TestCase):
    def testSync(self):
        """
        Test that python and ObjC string representation are not
        automaticly synchronized.
        """
        pyStr = NSMutableString.stringWithString_(u"hello")
        ocStr= pyStr.nsstring()
        self.assertEquals(pyStr, u"hello")
        self.assert_(isinstance(ocStr, NSMutableString))
        ocStr.appendString_(u" world")
        self.assertEquals(pyStr, u"hello")

class TestPickle(unittest.TestCase):
    """
    Testcases for pickling of Objective-C strings. Those are pickled as
    unicode strings.
    """

    def setUp(self):
        self.strVal = NSTaskDidTerminateNotification

    def testPickle(self):
        """
        Check that ObjC-strings pickle as unicode strings
        """
        import pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

    def testCPickle(self):
        """
        Check that ObjC-strings pickle as unicode strings
        """
        import cPickle as pickle

        s = pickle.dumps(self.strVal, 0)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 1)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

        s = pickle.dumps(self.strVal, 2)
        v = pickle.loads(s)
        self.assertEquals(type(v), types.UnicodeType)

if __name__ == '__main__':
    unittest.main()
