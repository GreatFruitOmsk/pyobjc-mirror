import unittest
from CoreFoundation import *

class TestUserNotification (unittest.TestCase):
    def testTypeID(self):
        id = CFUserNotificationGetTypeID()
        self.failUnless( isinstance(id, (int, long)) )

    def testCreation(self):
        rl = CFRunLoopGetCurrent()

        infoDict = {
                kCFUserNotificationAlertHeaderKey: u"Alert Header",
                kCFUserNotificationProgressIndicatorValueKey: True,
                kCFUserNotificationDefaultButtonTitleKey: "Cancel"
        }

        ref, error = CFUserNotificationCreate(None,
                5.0, 0, None, infoDict)
        self.failUnless( error == 0 )
        self.failUnless( isinstance(ref, CFUserNotificationRef) )

        #FIXME: need to ensure that this function is called during
        # the test
        @objc.callbackFor(CFUserNotificationCreateRunLoopSource)
        def callout(notification, flags):
            print notification, flags
        rls = CFUserNotificationCreateRunLoopSource(None, ref, callout, 1)
        self.failUnless(isinstance(rls, CFRunLoopSourceRef))

        CFRunLoopAddSource(rl, rls, kCFRunLoopDefaultMode)
        CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)

        error, flags = CFUserNotificationReceiveResponse(ref, 1.0, None)
        self.failUnless(isinstance(error, (int, long)))
        self.failUnless(isinstance(flags, (int, long)))

        v = CFUserNotificationGetResponseDictionary(ref)
        self.failUnless(v is None or isinstance(v, CFDictionaryRef))

        error = CFUserNotificationUpdate(ref, 2.0, 0, infoDict)
        self.failUnless(error == 0)

        error = CFUserNotificationCancel(ref)
        self.assertEquals(error, 0)
        
        v = CFUserNotificationGetResponseValue(ref, kCFUserNotificationTextFieldValuesKey, 0)
        self.failUnless(v is None or isinstance(v, unicode))



    def testAlert(self):
        err, flags = CFUserNotificationDisplayAlert(0.1, 0, None, None, None, "Header", "Message", "Cancel", None, None, None)
        self.failUnless(err == 0)
        self.failUnless(isinstance(flags, (int, long)))

        err, flags = CFUserNotificationDisplayAlert(0.1, 0, None, None, None, "Header", "Message", "Cancel", "OK", "Rest", None)
        self.failUnless(err == 0)
        self.failUnless(isinstance(flags, (int, long)))

    def testNotice(self):
        err = CFUserNotificationDisplayNotice(0.1, 0, None, None, None, "Header", "Message", "Cancel")
        self.failUnless(err == 0)





    def testInlines(self):
        flag = CFUserNotificationCheckBoxChecked(2)
        self.failUnless( flag == 1 << 10 )

        flag = CFUserNotificationSecureTextField(2)
        self.failUnless( flag == 1 << 18 )

        flag = CFUserNotificationPopUpSelection(2)
        self.failUnless( flag == 2 << 24 )


    def testConstants(self):
        self.failUnless( kCFUserNotificationStopAlertLevel       == 0)
        self.failUnless( kCFUserNotificationNoteAlertLevel       == 1)
        self.failUnless( kCFUserNotificationCautionAlertLevel    == 2)
        self.failUnless( kCFUserNotificationPlainAlertLevel      == 3)

        self.failUnless( kCFUserNotificationDefaultResponse      == 0)
        self.failUnless( kCFUserNotificationAlternateResponse    == 1)
        self.failUnless( kCFUserNotificationOtherResponse        == 2)
        self.failUnless( kCFUserNotificationCancelResponse       == 3)

        self.failUnless( kCFUserNotificationNoDefaultButtonFlag  == (1 << 5))
        self.failUnless( kCFUserNotificationUseRadioButtonsFlag  == (1 << 6))

        self.failUnless(  isinstance(kCFUserNotificationIconURLKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationSoundURLKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationLocalizationURLKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationAlertHeaderKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationAlertMessageKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationDefaultButtonTitleKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationAlternateButtonTitleKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationOtherButtonTitleKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationProgressIndicatorValueKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationPopUpTitlesKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationTextFieldTitlesKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationCheckBoxTitlesKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationTextFieldValuesKey, unicode) )
        self.failUnless(  isinstance(kCFUserNotificationPopUpSelectionKey, unicode) )


if __name__ == "__main__":
    unittest.main()
