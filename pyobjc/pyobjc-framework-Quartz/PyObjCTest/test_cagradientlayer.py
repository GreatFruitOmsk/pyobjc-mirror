from Quartz import *
from PyObjCTools.TestSupport import *

class TestCAGradientLayer (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultHasType(CAGradientLayer.startPoint, CGPoint.__typestr__)
        self.failUnlessResultHasType(CAGradientLayer.endPoint, CGPoint.__typestr__)

        self.failUnlessArgHasType(CAGradientLayer.setStartPoint_, 0, CGPoint.__typestr__)
        self.failUnlessArgHasType(CAGradientLayer.setEndPoint_, 0, CGPoint.__typestr__)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCAGradientLayerAxial, unicode)

if __name__ == "__main__":
    main()
