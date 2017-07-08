import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import Intents

    class TestINMessage (TestCase):
        @min_os_level('10.12')
        def testConstants(self):
            self.assertEqual(Intents.INMessageTypeUnspecified, 0)
            self.assertEqual(Intents.INMessageTypeText, 1)
            self.assertEqual(Intents.INMessageTypeAudio, 2)
            self.assertEqual(Intents.INMessageTypeDigitalTouch, 3)
            self.assertEqual(Intents.INMessageTypeHandwriting, 4)
            self.assertEqual(Intents.INMessageTypeSticker, 5)
            self.assertEqual(Intents.INMessageTypeTapbackLiked, 6)
            self.assertEqual(Intents.INMessageTypeTapbackDisliked, 7)
            self.assertEqual(Intents.INMessageTypeTapbackEmphasized, 8)
            self.assertEqual(Intents.INMessageTypeTapbackLoved, 9)
            self.assertEqual(Intents.INMessageTypeTapbackQuestioned, 10)
            self.assertEqual(Intents.INMessageTypeTapbackLaughed, 11)
            self.assertEqual(Intents.INMessageTypeMediaCalendar, 12)
            self.assertEqual(Intents.INMessageTypeMediaLocation, 13)
            self.assertEqual(Intents.INMessageTypeMediaAddressCard, 14)
            self.assertEqual(Intents.INMessageTypeMediaImage, 15)
            self.assertEqual(Intents.INMessageTypeMediaVideo, 16)
            self.assertEqual(Intents.INMessageTypeMediaPass, 17)
            self.assertEqual(Intents.INMessageTypeMediaAudio, 18)

if __name__ == "__main__":
    main()
