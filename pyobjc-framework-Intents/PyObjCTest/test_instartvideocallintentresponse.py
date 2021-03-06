import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINStartVideoCallIntentResponse (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeUnspecified, 0)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeReady, 1)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeContinueInApp, 2)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeFailure, 3)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeFailureRequiringAppLaunch, 4)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeFailureAppConfigurationRequired, 5)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeFailureCallingServiceNotAvailable, 6)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeFailureContactNotSupportedByApp, 7)
            self.assertEqual(Intents.INStartVideoCallIntentResponseCodeFailureInvalidNumber, 8)

if __name__ == "__main__":
    main()
