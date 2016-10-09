import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINStartAudioCallIntentHelper (Intents.NSObject):
        def handleStartAudioCall_completion_(self, intent, completion): pass
        def confirmStartAudioCall_completion_(self, intent, completion): pass
        def resolveContactsForStartAudioCall_withCompletion_(self, intent, completion): pass

    class TestINStartAudioCallIntent (TestCase):
        @min_os_level('10.12')
        def testMethods(self):
            self.assertArgIsBlock(TestINStartAudioCallIntentHelper.handleStartAudioCall_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINStartAudioCallIntentHelper.confirmStartAudioCall_completion_, 1, b'v@')
            self.assertArgIsBlock(TestINStartAudioCallIntentHelper.resolveContactsForStartAudioCall_withCompletion_, 1, b'v@')

        @min_sdk_level('10.12')
        def testProtocols(self):
            objc.protocolNamed('INStartAudioCallIntentHandling')

if __name__ == "__main__":
    main()
