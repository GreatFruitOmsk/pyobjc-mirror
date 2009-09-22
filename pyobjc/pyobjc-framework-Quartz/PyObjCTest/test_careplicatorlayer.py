from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAReplicatorLayer (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(CAReplicatorLayer.preservesDepth)
        self.failUnlessArgIsBOOL(CAReplicatorLayer.setPreservesDepth_, 0)

if __name__ == "__main__":
    main()
