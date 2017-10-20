# This file is generated by objective.metadata
#
# Last update: Tue Aug  8 21:41:45 2017

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$CNContactBirthdayKey$CNContactDatesKey$CNContactDepartmentNameKey$CNContactEmailAddressesKey$CNContactFamilyNameKey$CNContactGivenNameKey$CNContactIdentifierKey$CNContactImageDataAvailableKey$CNContactImageDataKey$CNContactInstantMessageAddressesKey$CNContactJobTitleKey$CNContactMiddleNameKey$CNContactNamePrefixKey$CNContactNameSuffixKey$CNContactNicknameKey$CNContactNonGregorianBirthdayKey$CNContactNoteKey$CNContactOrganizationNameKey$CNContactPhoneNumbersKey$CNContactPhoneticFamilyNameKey$CNContactPhoneticGivenNameKey$CNContactPhoneticMiddleNameKey$CNContactPhoneticOrganizationNameKey$CNContactPostalAddressesKey$CNContactPreviousFamilyNameKey$CNContactPropertyAttribute$CNContactPropertyNotFetchedExceptionName$CNContactRelationsKey$CNContactSocialProfilesKey$CNContactStoreDidChangeNotification$CNContactThumbnailImageDataKey$CNContactTypeKey$CNContactUrlAddressesKey$CNContainerIdentifierKey$CNContainerNameKey$CNContainerTypeKey$CNErrorDomain$CNErrorUserInfoAffectedRecordIdentifiersKey$CNErrorUserInfoAffectedRecordsKey$CNErrorUserInfoKeyPathsKey$CNErrorUserInfoValidationErrorsKey$CNGroupIdentifierKey$CNGroupNameKey$CNInstantMessageAddressServiceKey$CNInstantMessageAddressUsernameKey$CNInstantMessageServiceAIM$CNInstantMessageServiceFacebook$CNInstantMessageServiceGaduGadu$CNInstantMessageServiceGoogleTalk$CNInstantMessageServiceICQ$CNInstantMessageServiceJabber$CNInstantMessageServiceMSN$CNInstantMessageServiceQQ$CNInstantMessageServiceSkype$CNInstantMessageServiceYahoo$CNLabelContactRelationAssistant$CNLabelContactRelationBrother$CNLabelContactRelationChild$CNLabelContactRelationDaughter$CNLabelContactRelationFather$CNLabelContactRelationFriend$CNLabelContactRelationManager$CNLabelContactRelationMother$CNLabelContactRelationParent$CNLabelContactRelationPartner$CNLabelContactRelationSister$CNLabelContactRelationSon$CNLabelContactRelationSpouse$CNLabelDateAnniversary$CNLabelEmailiCloud$CNLabelHome$CNLabelOther$CNLabelPhoneNumberHomeFax$CNLabelPhoneNumberMain$CNLabelPhoneNumberMobile$CNLabelPhoneNumberOtherFax$CNLabelPhoneNumberPager$CNLabelPhoneNumberWorkFax$CNLabelPhoneNumberiPhone$CNLabelURLAddressHomePage$CNLabelWork$CNPostalAddressCityKey$CNPostalAddressCountryKey$CNPostalAddressISOCountryCodeKey$CNPostalAddressLocalizedPropertyNameAttribute$CNPostalAddressPostalCodeKey$CNPostalAddressPropertyAttribute$CNPostalAddressStateKey$CNPostalAddressStreetKey$CNPostalAddressSubAdministrativeAreaKey$CNPostalAddressSubLocalityKey$CNSocialProfileServiceFacebook$CNSocialProfileServiceFlickr$CNSocialProfileServiceGameCenter$CNSocialProfileServiceKey$CNSocialProfileServiceLinkedIn$CNSocialProfileServiceMySpace$CNSocialProfileServiceSinaWeibo$CNSocialProfileServiceTencentWeibo$CNSocialProfileServiceTwitter$CNSocialProfileServiceYelp$CNSocialProfileURLStringKey$CNSocialProfileUserIdentifierKey$CNSocialProfileUsernameKey$'''
enums = '''$CNAuthorizationStatusAuthorized@3$CNAuthorizationStatusDenied@2$CNAuthorizationStatusNotDetermined@0$CNAuthorizationStatusRestricted@1$CNContactDisplayNameOrderFamilyNameFirst@2$CNContactDisplayNameOrderGivenNameFirst@1$CNContactDisplayNameOrderUserDefault@0$CNContactFormatterStyleFullName@0$CNContactFormatterStylePhoneticFullName@1$CNContactSortOrderFamilyName@3$CNContactSortOrderGivenName@2$CNContactSortOrderNone@0$CNContactSortOrderUserDefault@1$CNContactTypeOrganization@1$CNContactTypePerson@0$CNContainerTypeCardDAV@3$CNContainerTypeExchange@2$CNContainerTypeLocal@1$CNContainerTypeUnassigned@0$CNEntityTypeContacts@0$CNErrorCodeAuthorizationDenied@100$CNErrorCodeClientIdentifierDoesNotExist@601$CNErrorCodeClientIdentifierInvalid@600$CNErrorCodeCommunicationError@1$CNErrorCodeContainmentCycle@202$CNErrorCodeContainmentScope@203$CNErrorCodeDataAccessError@2$CNErrorCodeInsertedRecordAlreadyExists@201$CNErrorCodeParentRecordDoesNotExist@204$CNErrorCodePolicyViolation@500$CNErrorCodePredicateInvalid@400$CNErrorCodeRecordDoesNotExist@200$CNErrorCodeVCardMalformed@700$CNErrorCodeValidationConfigurationError@302$CNErrorCodeValidationMultipleErrors@300$CNErrorCodeValidationTypeMismatch@301$CNPostalAddressFormatterStyleMailingAddress@0$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'CNContact', b'areKeysAvailable:', {'retval': {'type': 'Z'}})
    r(b'CNContact', b'isKeyAvailable:', {'retval': {'type': 'Z'}})
    r(b'CNContact', b'isUnifiedWithContactWithIdentifier:', {'retval': {'type': 'Z'}})
    r(b'CNContactFetchRequest', b'mutableObjects', {'retval': {'type': 'Z'}})
    r(b'CNContactFetchRequest', b'setMutableObjects:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CNContactFetchRequest', b'setUnifyResults:', {'arguments': {2: {'type': 'Z'}}})
    r(b'CNContactFetchRequest', b'unifyResults', {'retval': {'type': 'Z'}})
    r(b'CNContactStore', b'containersMatchingPredicate:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CNContactStore', b'enumerateContactsWithFetchRequest:error:usingBlock:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}, 4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'o^Z'}}}}}})
    r(b'CNContactStore', b'executeSaveRequest:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CNContactStore', b'groupsMatchingPredicate:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CNContactStore', b'requestAccessForEntityType:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'CNContactStore', b'unifiedContactWithIdentifier:keysToFetch:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CNContactStore', b'unifiedContactsMatchingPredicate:keysToFetch:error:', {'arguments': {4: {'type_modifier': b'o'}}})
    r(b'CNContactStore', b'unifiedMeContactWithKeysToFetch:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CNContactVCardSerialization', b'contactsWithData:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'CNContactVCardSerialization', b'dataWithContacts:error:', {'arguments': {3: {'type_modifier': b'o'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
