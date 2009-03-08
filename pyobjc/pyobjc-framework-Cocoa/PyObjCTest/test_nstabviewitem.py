
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTabViewItem (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSelectedTab, 0)
        self.failUnlessEqual(NSBackgroundTab, 1)
        self.failUnlessEqual(NSPressedTab, 2)

if __name__ == "__main__":
    main()
