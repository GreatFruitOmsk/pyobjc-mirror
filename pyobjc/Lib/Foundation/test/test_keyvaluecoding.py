import unittest
import objc

from Foundation import *
from PyObjCTools import KeyValueCodingSupport

class StraightPython(object, KeyValueCodingSupport.KeyValueCoding):
    foo = 21
    _bar = 42
    baz = { "bob" : "tail" }
    _didBar = 0

    def bar(self):
        self._didBar = 1
        return self._bar
    def setBar(self, aValue):
        self._bar = aValue
    def didBar(self): 
        return self._didBar

class PyObjCMix(NSObject):

    foo = 21
    _bar = 42
    baz = { "bob" : "tail" }
    _didBar = 0

    def bar(self):
        self._didBar = 1
        return self._bar
    def setBar(self, aValue):
        self._bar = aValue

    def didBar(self): 
        return self._didBar

    def valueForKey_(self, aKey):
        try:
            v = KeyValueCodingSupport.getValueForKey_(self, aKey)
            return v
        except KeyError:
            zuper = super(self.__class__, self)
            if zuper.respondsToSelector_("valueForKey:"):
                return zuper.valueForKey_(aKey)

        raise KeyError, aKey

class TestKeyValueCoding(unittest.TestCase):
    def testValueForKey(self):
        KeyValueCodingSupport.addKeyValueBridgeToClass(PyObjCMix)

        a = StraightPython()
        b = PyObjCMix.new()

        self.assertEqual(a.valueForKey_("foo"), 21)
        self.assertEqual(b.valueForKey_("foo"), 21)
        self.assertEqual(a.didBar(), 0)
        self.assertEqual(b.didBar(), 0)
        self.assertEqual(a.valueForKey_("bar"), 42)
        self.assertEqual(b.valueForKey_("bar"), 42)
        self.assertEqual(a.didBar(), 1)
        self.assertEqual(b.didBar(), 1)

if __name__ == '__main__':
    unittest.main( )
