import unittest
import objc
from objc.test.testclassandinst import PyObjC_TestClassAndInstance

class PyObjC_TestClassAndInstanceSubclass(PyObjC_TestClassAndInstance):
    """Simple subclass, just make sure it still works"""
    pass

class PyObjC_TestClassAndInstanceClassOverride(PyObjC_TestClassAndInstance):
    """return YES for both"""
    def isInstance(klass):
        return objc.YES
    isInstance = classmethod(isInstance)

class PyObjC_TestClassAndInstanceInstanceOverride(PyObjC_TestClassAndInstance):
    """return NO for both"""
    def isInstance(self):
        return objc.NO

# class PyObjC_TestClassAndInstanceBothOverride(PyObjC_TestClassAndInstance):
#     """flipped"""
#     def isInstance__class__(self):
#         return objc.YES
#
#     def isInstance__inst__(self):
#         return objc.NO

class TestClassAndInstance(unittest.TestCase):
    def testClassAndInstanceInstanceOverrideWorkaround(self):
        self.assertEquals(PyObjC_TestClassAndInstanceInstanceOverride.pyobjc_classMethods.isInstance(), objc.NO)
        self.assertEquals(PyObjC_TestClassAndInstanceInstanceOverride.alloc().init().pyobjc_instanceMethods.isInstance(), objc.NO)

    def testClassAndInstanceClassOverrideWorkaround(self):
        self.assertEquals(PyObjC_TestClassAndInstanceClassOverride.pyobjc_classMethods.isInstance(), objc.YES)
        self.assertEquals(PyObjC_TestClassAndInstanceClassOverride.alloc().init().pyobjc_instanceMethods.isInstance(), objc.YES)

    def testClassAndInstanceSubclassWorkaround(self):
        self.assertEquals(PyObjC_TestClassAndInstanceSubclass.pyobjc_classMethods.isInstance(), objc.NO)
        self.assertEquals(PyObjC_TestClassAndInstanceSubclass.alloc().init().pyobjc_instanceMethods.isInstance(), objc.YES)
    
    def testClassAndInstanceWorkaround(self):
        self.assertEquals(PyObjC_TestClassAndInstance.pyobjc_classMethods.isInstance(), objc.NO)
        self.assertEquals(PyObjC_TestClassAndInstance.alloc().init().pyobjc_instanceMethods.isInstance(), objc.YES)
    
    def testClassAndInstanceClassOverride(self):
        self.assertEquals(PyObjC_TestClassAndInstanceClassOverride.isInstance(), objc.YES)
        self.assertEquals(PyObjC_TestClassAndInstanceClassOverride.alloc().init().isInstance(), objc.YES)

    def testClassAndInstanceInstanceOverride(self):
        self.assertEquals(PyObjC_TestClassAndInstanceInstanceOverride.isInstance(), objc.NO)
        self.assertEquals(PyObjC_TestClassAndInstanceInstanceOverride.alloc().init().isInstance(), objc.NO)

    def testClassAndInstanceSubclass(self):
        self.assertEquals(PyObjC_TestClassAndInstanceSubclass.isInstance(), objc.NO)
        self.assertEquals(PyObjC_TestClassAndInstanceSubclass.alloc().init().isInstance(), objc.YES)

    def testClassAndInstance(self):
        self.assertEquals(PyObjC_TestClassAndInstance.isInstance(), objc.NO)
        self.assertEquals(PyObjC_TestClassAndInstance.alloc().init().isInstance(), objc.YES)

if __name__ == '__main__':
    unittest.main()
