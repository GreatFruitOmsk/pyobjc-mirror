
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABGlobals (TestCase):
    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(kABOrganizationPhoneticProperty, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(kABSocialProfileServiceTencentWeibo, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(kABSocialProfileServiceYelp, unicode)
        self.assertIsInstance(kABAlternateBirthdayComponentsProperty, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(kABSocialProfileServiceSinaWeibo, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kABMobileMeLabel, unicode)
        self.assertIsInstance(kABBirthdayComponentsProperty, unicode)
        self.assertIsInstance(kABOtherDateComponentsProperty, unicode)
        self.assertIsInstance(kABInstantMessageProperty, unicode)
        self.assertIsInstance(kABInstantMessageUsernameKey, unicode)
        self.assertIsInstance(kABInstantMessageServiceKey, unicode)
        self.assertIsInstance(kABInstantMessageServiceAIM, unicode)
        self.assertIsInstance(kABInstantMessageServiceFacebook, unicode)
        self.assertIsInstance(kABInstantMessageServiceGaduGadu, unicode)
        self.assertIsInstance(kABInstantMessageServiceGoogleTalk, unicode)
        self.assertIsInstance(kABInstantMessageServiceICQ, unicode)
        self.assertIsInstance(kABInstantMessageServiceJabber, unicode)
        self.assertIsInstance(kABInstantMessageServiceMSN, unicode)
        self.assertIsInstance(kABInstantMessageServiceQQ, unicode)
        self.assertIsInstance(kABInstantMessageServiceSkype, unicode)
        self.assertIsInstance(kABInstantMessageServiceYahoo, unicode)
        self.assertIsInstance(kABSocialProfileProperty, unicode)
        self.assertIsInstance(kABSocialProfileURLKey, unicode)
        self.assertIsInstance(kABSocialProfileUsernameKey, unicode)
        self.assertIsInstance(kABSocialProfileUserIdentifierKey, unicode)
        self.assertIsInstance(kABSocialProfileServiceKey, unicode)
        self.assertIsInstance(kABSocialProfileServiceTwitter, unicode)
        self.assertIsInstance(kABSocialProfileServiceFacebook, unicode)
        self.assertIsInstance(kABSocialProfileServiceLinkedIn, unicode)
        self.assertIsInstance(kABSocialProfileServiceFlickr, unicode)
        self.assertIsInstance(kABSocialProfileServiceMySpace, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kABPhoneiPhoneLabel, unicode)
        self.assertEqual(kABShowAsResource, 2)
        self.assertEqual(kABShowAsRoom, 3)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kABCalendarURIsProperty, unicode)

    @expectedFailureIf(os_level_key(os_release()) < os_level_key('10.14'))
    def testConstants_10_7_broken(self):
        self.assertIsInstance(kABEmailMobileMeLabel, unicode)
        self.assertIsInstance(kABAIMMobileMeLabel, unicode)

    def testConstants(self):
        self.assertEqual(kABShowAsMask, 0o7)
        self.assertEqual(kABShowAsPerson, 0o0)
        self.assertEqual(kABShowAsCompany, 0o1)
        self.assertEqual(kABNameOrderingMask, 0o70)
        self.assertEqual(kABDefaultNameOrdering, 0o0)
        self.assertEqual(kABFirstNameFirst, 0o40)
        self.assertEqual(kABLastNameFirst, 0o20)


        self.assertIsInstance(kABUIDProperty, unicode)
        self.assertIsInstance(kABCreationDateProperty, unicode)
        self.assertIsInstance(kABModificationDateProperty, unicode)
        self.assertIsInstance(kABFirstNameProperty, unicode)
        self.assertIsInstance(kABLastNameProperty, unicode)
        self.assertIsInstance(kABFirstNamePhoneticProperty, unicode)
        self.assertIsInstance(kABLastNamePhoneticProperty, unicode)
        self.assertIsInstance(kABNicknameProperty, unicode)
        self.assertIsInstance(kABMaidenNameProperty, unicode)
        self.assertIsInstance(kABBirthdayProperty, unicode)

        self.assertIsInstance(kABOrganizationProperty, unicode)
        self.assertIsInstance(kABJobTitleProperty, unicode)
        self.assertIsInstance(kABHomePageProperty, unicode)
        self.assertIsInstance(kABURLsProperty, unicode)
        self.assertIsInstance(kABHomePageLabel, unicode)
        self.assertIsInstance(kABEmailProperty, unicode)
        self.assertIsInstance(kABEmailWorkLabel, unicode)
        self.assertIsInstance(kABEmailHomeLabel, unicode)
        self.assertIsInstance(kABAddressProperty, unicode)
        self.assertIsInstance(kABAddressStreetKey, unicode)
        self.assertIsInstance(kABAddressCityKey, unicode)
        self.assertIsInstance(kABAddressStateKey, unicode)
        self.assertIsInstance(kABAddressZIPKey, unicode)
        self.assertIsInstance(kABAddressCountryKey, unicode)
        self.assertIsInstance(kABAddressCountryCodeKey, unicode)
        self.assertIsInstance(kABAddressHomeLabel, unicode)
        self.assertIsInstance(kABAddressWorkLabel, unicode)
        self.assertIsInstance(kABOtherDatesProperty, unicode)
        self.assertIsInstance(kABAnniversaryLabel, unicode)
        self.assertIsInstance(kABRelatedNamesProperty, unicode)
        self.assertIsInstance(kABFatherLabel, unicode)
        self.assertIsInstance(kABMotherLabel, unicode)
        self.assertIsInstance(kABParentLabel, unicode)
        self.assertIsInstance(kABBrotherLabel, unicode)
        self.assertIsInstance(kABSisterLabel, unicode)
        self.assertIsInstance(kABChildLabel, unicode)
        self.assertIsInstance(kABFriendLabel, unicode)
        self.assertIsInstance(kABSpouseLabel, unicode)
        self.assertIsInstance(kABPartnerLabel, unicode)
        self.assertIsInstance(kABAssistantLabel, unicode)
        self.assertIsInstance(kABManagerLabel, unicode)
        self.assertIsInstance(kABDepartmentProperty, unicode)
        self.assertIsInstance(kABPersonFlags, unicode)
        self.assertIsInstance(kABPhoneProperty, unicode)
        self.assertIsInstance(kABPhoneWorkLabel, unicode)
        self.assertIsInstance(kABPhoneHomeLabel, unicode)
        self.assertIsInstance(kABPhoneMobileLabel, unicode)
        self.assertIsInstance(kABPhoneMainLabel, unicode)
        self.assertIsInstance(kABPhoneHomeFAXLabel, unicode)
        self.assertIsInstance(kABPhoneWorkFAXLabel, unicode)
        self.assertIsInstance(kABPhonePagerLabel, unicode)
        self.assertIsInstance(kABAIMInstantProperty, unicode)
        self.assertIsInstance(kABAIMWorkLabel, unicode)
        self.assertIsInstance(kABAIMHomeLabel, unicode)
        self.assertIsInstance(kABJabberInstantProperty, unicode)
        self.assertIsInstance(kABJabberWorkLabel, unicode)
        self.assertIsInstance(kABJabberHomeLabel, unicode)
        self.assertIsInstance(kABMSNInstantProperty, unicode)
        self.assertIsInstance(kABMSNWorkLabel, unicode)
        self.assertIsInstance(kABMSNHomeLabel, unicode)
        self.assertIsInstance(kABYahooInstantProperty, unicode)
        self.assertIsInstance(kABYahooWorkLabel, unicode)
        self.assertIsInstance(kABYahooHomeLabel, unicode)
        self.assertIsInstance(kABICQInstantProperty, unicode)
        self.assertIsInstance(kABICQWorkLabel, unicode)
        self.assertIsInstance(kABICQHomeLabel, unicode)
        self.assertIsInstance(kABNoteProperty, unicode)
        self.assertIsInstance(kABMiddleNameProperty, unicode)
        self.assertIsInstance(kABMiddleNamePhoneticProperty, unicode)
        self.assertIsInstance(kABTitleProperty, unicode)
        self.assertIsInstance(kABSuffixProperty, unicode)
        self.assertIsInstance(kABGroupNameProperty, unicode)
        self.assertIsInstance(kABWorkLabel, unicode)
        self.assertIsInstance(kABHomeLabel, unicode)
        self.assertIsInstance(kABOtherLabel, unicode)
        self.assertIsInstance(kABDatabaseChangedNotification, unicode)
        self.assertIsInstance(kABDatabaseChangedExternallyNotification, unicode)
        self.assertIsInstance(kABInsertedRecords, unicode)
        self.assertIsInstance(kABUpdatedRecords, unicode)
        self.assertIsInstance(kABDeletedRecords, unicode)

    def testFunctions(self):
        v = ABLocalizedPropertyOrLabel(kABAssistantLabel)
        self.assertIsInstance(v, unicode)

if __name__ == "__main__":
    main()
