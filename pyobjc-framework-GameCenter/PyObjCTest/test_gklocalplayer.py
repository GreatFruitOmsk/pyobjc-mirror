from PyObjCTools.TestSupport import *
import objc
import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKLocalPlayer (TestCase):
        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertIsInstance(GameCenter.GKLocalPlayer, objc.objc_class)
            self.assertResultIsBOOL(GameCenter.GKLocalPlayer.isAuthenticated)

            self.assertArgIsBlock(GameCenter.GKLocalPlayer.setDefaultLeaderboardCategoryID_completionHandler_, 1, b'v@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.loadDefaultLeaderboardCategoryIDWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.loadFriendsWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.authenticateWithCompletionHandler_, 0, b'v@')

        @expectedFailure
        @min_os_level('10.8')
        def testMethods10_8_fail(self):
            self.assertResultIsBOOL(GameCenter.GKLocalPlayer.isUnderage)

        @min_os_level('10.9')
        def testMethods10_9(self):
            self.assertResultIsBlock(GameCenter.GKLocalPlayer.authenticateHandler, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.setAuthenticateHandler_, 0, b'v@@')

        @min_os_level('10.10')
        def testMethods10_10(self):
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.loadFriendPlayersWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.setDefaultLeaderboardIdentifier_completionHandler_, 1, b'v@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.loadDefaultLeaderboardIdentifierWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.generateIdentityVerificationSignatureWithCompletionHandler_, 0, b'v@@@Q@')

        @min_os_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('GKLocalPlayerListener')

        @min_os_level('10.8')
        def testConstants(self):
            self.assertIsInstance(GameCenter.GKPlayerAuthenticationDidChangeNotificationName, unicode)


if __name__ == "__main__":
    main()
