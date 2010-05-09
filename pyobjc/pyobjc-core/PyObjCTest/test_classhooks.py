from PyObjCTools.TestSupport import *

import objc


class specialproperty(object):
    def __init__(self):
        self.name = None

    def __pyobjc_class_setup__(self, name, class_dict, instance_method_list, class_method_list):
        self.name = name

        def dospecial(self):
            pass
        m = objc.selector(dospecial, selector=("special"+name).encode('latin1'))
        #instance_method_list.append(m)
        class_dict['myspecialprop'] = m

class TestClassSetupHook (TestCase):
    def testSpecialProperty(self):

        class TestSpecialProperty (objc.lookUpClass('NSObject')):
            myprop = specialproperty()

            self.assertEquals(myprop.name, None)

        self.assertEquals(TestSpecialProperty.myprop.name, 'myprop')

        o = TestSpecialProperty.alloc().init()
        self.assertHasAttr(o, 'specialmyprop')

    def testInvalidTypes(self):
        self.fail("todo")

        # Add values of invalid types (not selector with right flags) to
        # the class and instance method lists and check that PyObjC behaves
        # correctly.

    def testIncomplete(self):
        self.fail("Test (and implementation) incomplete")


class TestKVOProperty_Array (TestCase):
    def testIncomplete(self):
        self.fail("Implement objc.array_property")

class TestKVOProperty_Set (TestCase):
    def testIncomplete(self):
        self.fail("Implement objc.set_property")


if __name__ == "__main__":
    main()
