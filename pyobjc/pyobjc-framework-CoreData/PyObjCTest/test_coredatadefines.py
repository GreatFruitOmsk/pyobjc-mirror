
from PyObjCTools.TestSupport import *
from CoreData import *

class TestCoreDataDefines (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSCoreDataVersionNumber, float)

        self.failUnlessEqual(NSCoreDataVersionNumber10_4, 46.0)
        self.failUnlessEqual(NSCoreDataVersionNumber10_4_3, 77.0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSCoreDataVersionNumber10_5, 185.0)
        self.failUnlessEqual(NSCoreDataVersionNumber10_5_3, 186.0)


if __name__ == "__main__":
    main()
