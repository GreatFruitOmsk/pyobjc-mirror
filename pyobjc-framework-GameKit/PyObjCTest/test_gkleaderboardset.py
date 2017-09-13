from PyObjCTools.TestSupport import *

import GameKit

class TestGKLeaderboardSetHelper (GameKit.GKLeaderboardSet):
    def loadImageWithCompletionHandler_(self, h): pass

class TestGKLeaderboardSet (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKLeaderboardSet.loadLeaderboardSetsWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(GameKit.GKLeaderboardSet.loadLeaderboardsWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(TestGKLeaderboardSetHelper.loadImageWithCompletionHandler_, 0, b'v@@')


if __name__ == "__main__":
    main()
