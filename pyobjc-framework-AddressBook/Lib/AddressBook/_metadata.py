# This file is generated by objective.metadata
#
# Last update: Thu May 10 16:21:04 2012

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$ABAddressBookErrorDomain$ABMultiValueIdentifiersErrorKey$ABPeoplePickerDisplayedPropertyDidChangeNotification$ABPeoplePickerGroupSelectionDidChangeNotification$ABPeoplePickerNameSelectionDidChangeNotification$ABPeoplePickerValueSelectionDidChangeNotification$kABAIMHomeLabel$kABAIMInstantProperty$kABAIMMobileMeLabel$kABAIMWorkLabel$kABAddressCityKey$kABAddressCountryCodeKey$kABAddressCountryKey$kABAddressHomeLabel$kABAddressProperty$kABAddressStateKey$kABAddressStreetKey$kABAddressWorkLabel$kABAddressZIPKey$kABAnniversaryLabel$kABAssistantLabel$kABBirthdayComponentsProperty$kABBirthdayProperty$kABBrotherLabel$kABCalendarURIsProperty$kABChildLabel$kABCreationDateProperty$kABDatabaseChangedExternallyNotification$kABDatabaseChangedNotification$kABDeletedRecords$kABDepartmentProperty$kABEmailHomeLabel$kABEmailMobileMeLabel$kABEmailProperty$kABEmailWorkLabel$kABFatherLabel$kABFirstNamePhoneticProperty$kABFirstNameProperty$kABFriendLabel$kABGroupNameProperty$kABHomeLabel$kABHomePageLabel$kABHomePageProperty$kABICQHomeLabel$kABICQInstantProperty$kABICQWorkLabel$kABInsertedRecords$kABInstantMessageProperty$kABInstantMessageServiceAIM$kABInstantMessageServiceFacebook$kABInstantMessageServiceGaduGadu$kABInstantMessageServiceGoogleTalk$kABInstantMessageServiceICQ$kABInstantMessageServiceJabber$kABInstantMessageServiceKey$kABInstantMessageServiceMSN$kABInstantMessageServiceQQ$kABInstantMessageServiceSkype$kABInstantMessageServiceYahoo$kABInstantMessageUsernameKey$kABJabberHomeLabel$kABJabberInstantProperty$kABJabberWorkLabel$kABJobTitleProperty$kABLastNamePhoneticProperty$kABLastNameProperty$kABMSNHomeLabel$kABMSNInstantProperty$kABMSNWorkLabel$kABMaidenNameProperty$kABManagerLabel$kABMiddleNamePhoneticProperty$kABMiddleNameProperty$kABMobileMeLabel$kABModificationDateProperty$kABMotherLabel$kABNicknameProperty$kABNoteProperty$kABOrganizationProperty$kABOtherDateComponentsProperty$kABOtherDatesProperty$kABOtherLabel$kABParentLabel$kABPartnerLabel$kABPersonFlags$kABPhoneHomeFAXLabel$kABPhoneHomeLabel$kABPhoneMainLabel$kABPhoneMobileLabel$kABPhonePagerLabel$kABPhoneProperty$kABPhoneWorkFAXLabel$kABPhoneWorkLabel$kABPhoneiPhoneLabel$kABRelatedNamesProperty$kABSisterLabel$kABSocialProfileProperty$kABSocialProfileServiceFacebook$kABSocialProfileServiceFlickr$kABSocialProfileServiceKey$kABSocialProfileServiceLinkedIn$kABSocialProfileServiceMySpace$kABSocialProfileServiceTwitter$kABSocialProfileURLKey$kABSocialProfileUserIdentifierKey$kABSocialProfileUsernameKey$kABSpouseLabel$kABSuffixProperty$kABTitleProperty$kABUIDProperty$kABURLsProperty$kABUpdatedRecords$kABWorkLabel$kABYahooHomeLabel$kABYahooInstantProperty$kABYahooWorkLabel$'''
enums = '''$ABAddRecordsError@1001$ABMultipleValueSelection@2$ABNoValueSelection@0$ABPropertyReadOnlyError@1014$ABPropertyUnsupportedBySourceError@1013$ABPropertyValueValidationError@1012$ABRemoveRecordsError@1002$ABSingleValueSelection@1$kABArrayProperty@5$kABBitsInBitFieldMatch@11$kABContainsSubString@7$kABContainsSubStringCaseInsensitive@8$kABDataProperty@7$kABDateComponentsProperty@8$kABDateProperty@4$kABDefaultNameOrdering@0$kABDictionaryProperty@6$kABDoesNotContainSubString@12$kABDoesNotContainSubStringCaseInsensitive@13$kABEqual@0$kABEqualCaseInsensitive@6$kABErrorInProperty@0$kABFirstNameFirst@32$kABGreaterThan@4$kABGreaterThanOrEqual@5$kABIntegerProperty@2$kABLastNameFirst@16$kABLessThan@2$kABLessThanOrEqual@3$kABMultiArrayProperty@261$kABMultiDataProperty@263$kABMultiDateComponentsProperty@264$kABMultiDateProperty@260$kABMultiDictionaryProperty@262$kABMultiIntegerProperty@258$kABMultiRealProperty@259$kABMultiStringProperty@257$kABMultiValueMask@256$kABNameOrderingMask@56$kABNotEqual@1$kABNotEqualCaseInsensitive@14$kABNotWithinIntervalAroundToday@19$kABNotWithinIntervalAroundTodayYearless@20$kABNotWithinIntervalFromToday@23$kABNotWithinIntervalFromTodayYearless@24$kABPickerAllowGroupSelection@4$kABPickerAllowMultipleSelection@8$kABPickerMultipleValueSelection@2$kABPickerSingleValueSelection@1$kABPrefixMatch@9$kABPrefixMatchCaseInsensitive@10$kABRealProperty@3$kABSearchAnd@0$kABSearchOr@1$kABShowAsCompany@1$kABShowAsMask@7$kABShowAsPerson@0$kABShowAsResource@2$kABShowAsRoom@3$kABStringProperty@1$kABSuffixMatch@15$kABSuffixMatchCaseInsensitive@16$kABWithinIntervalAroundToday@17$kABWithinIntervalAroundTodayYearless@18$kABWithinIntervalFromToday@21$kABWithinIntervalFromTodayYearless@22$kEventABPeoplePickerDisplayedPropertyChanged@4$kEventABPeoplePickerGroupDoubleClicked@5$kEventABPeoplePickerGroupSelectionChanged@1$kEventABPeoplePickerNameDoubleClicked@6$kEventABPeoplePickerNameSelectionChanged@2$kEventABPeoplePickerValueSelectionChanged@3$kEventClassABPeoplePicker@1633841264$kEventParamABPickerRef@1633841264$'''
misc.update({})
functions={'ABMultiValueReplaceValue': (b'B^{__ABMultiValue=}@l',), 'ABPickerSetDelegate': (b'v^{OpaqueABPicker=}^{OpaqueHIObjectRef=}',), 'ABAddRecord': (b'B^{__ABAddressBookRef=}@',), 'ABPickerSelectIdentifier': (b'v^{OpaqueABPicker=}^{__ABPerson=}^{__CFString=}B',), 'ABPickerSelectGroup': (b'v^{OpaqueABPicker=}^{__ABGroup=}B',), 'ABCopyDefaultCountryCode': (b'^{__CFString=}^{__ABAddressBookRef=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerGetAttributes': (sel32or64(b'L^{OpaqueABPicker=}', b'I^{OpaqueABPicker=}'),), 'ABSave': (b'B^{__ABAddressBookRef=}',), 'ABPersonCreateWithVCardRepresentation': (b'^{__ABPerson=}^{__CFData=}', '', {'retval': {'already_cfretained': True}}), 'ABGroupAddMember': (b'B^{__ABGroup=}^{__ABPerson=}',), 'ABPersonCreateSearchElement': (b'^{__ABSearchElementRef=}^{__CFString=}^{__CFString=}^{__CFString=}@l', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueRemove': (b'B^{__ABMultiValue=}l',), 'ABSearchElementMatchesRecord': (b'B^{__ABSearchElementRef=}@',), 'ABRecordCopyRecordType': (b'^{__CFString=}@', '', {'retval': {'already_cfretained': True}}), 'ABPickerClearSearchField': (b'v^{OpaqueABPicker=}',), 'ABMultiValueCopyPrimaryIdentifier': (b'^{__CFString=}^{__ABMultiValue=}', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueIndexForIdentifier': (b'l^{__ABMultiValue=}^{__CFString=}',), 'ABPickerSelectRecord': (b'v^{OpaqueABPicker=}@B',), 'ABMultiValueCreateMutableCopy': (b'^{__ABMultiValue=}^{__ABMultiValue=}', '', {'retval': {'already_cfretained': True}}), 'ABRecordRemoveValue': (b'B@^{__CFString=}',), 'ABPickerCopySelectedGroups': (b'^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueCopyIdentifierAtIndex': (b'^{__CFString=}^{__ABMultiValue=}l', '', {'retval': {'already_cfretained': True}}), 'ABCancelLoadingImageDataForTag': (b'vl',), 'ABCopyArrayOfMatchingRecords': (b'^{__CFArray=}^{__ABAddressBookRef=}^{__ABSearchElementRef=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerRemoveProperty': (b'v^{OpaqueABPicker=}^{__CFString=}',), 'ABMultiValueCount': (b'l^{__ABMultiValue=}',), 'ABPickerCopySelectedIdentifiers': (b'^{__CFArray=}^{OpaqueABPicker=}^{__ABPerson=}', '', {'retval': {'already_cfretained': True}}), 'ABGroupCreate': (b'^{__ABGroup=}', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueCreateCopy': (b'^{__ABMultiValue=}^{__ABMultiValue=}', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueAdd': (b'B^{__ABMultiValue=}@^{__CFString=}^^{__CFString}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'ABHasUnsavedChanges': (b'B^{__ABAddressBookRef=}',), 'ABMultiValueReplaceLabel': (b'B^{__ABMultiValue=}^{__CFString=}l',), 'ABGroupCopyParentGroups': (b'^{__CFArray=}^{__ABGroup=}', '', {'retval': {'already_cfretained': True}}), 'ABGroupSetDistributionIdentifier': (b'B^{__ABGroup=}^{__ABPerson=}^{__CFString=}^{__CFString=}',), 'ABPickerDeselectRecord': (b'v^{OpaqueABPicker=}@',), 'ABGroupCreateSearchElement': (b'^{__ABSearchElementRef=}^{__CFString=}^{__CFString=}^{__CFString=}@l', '', {'retval': {'already_cfretained': True}}), 'ABCopyRecordTypeFromUniqueId': (b'^{__CFString=}^{__ABAddressBookRef=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ABRemoveRecord': (b'B^{__ABAddressBookRef=}@',), 'ABGroupCopyDistributionIdentifier': (b'^{__CFString=}^{__ABGroup=}^{__ABPerson=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ABPersonCopyImageData': (b'^{__CFData=}^{__ABPerson=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerDeselectGroup': (b'v^{OpaqueABPicker=}^{__ABGroup=}',), 'ABTypeOfProperty': (b'l^{__ABAddressBookRef=}^{__CFString=}^{__CFString=}',), 'ABGroupCopyArrayOfAllSubgroups': (b'^{__CFArray=}^{__ABGroup=}', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueCreate': (b'^{__ABMultiValue=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerSelectInAddressBook': (b'v^{OpaqueABPicker=}',), 'ABGroupCopyArrayOfAllMembers': (b'^{__CFArray=}^{__ABGroup=}', '', {'retval': {'already_cfretained': True}}), 'ABSearchElementCreateWithConjunction': (b'^{__ABSearchElementRef=}l^{__CFArray=}', '', {'retval': {'already_cfretained': True}}), 'ABRemoveProperties': (b'l^{__ABAddressBookRef=}^{__CFString=}^{__CFArray=}',), 'ABPersonSetImageData': (b'B^{__ABPerson=}^{__CFData=}',), 'ABCreateFormattedAddressFromDictionary': (b'^{__CFString=}^{__ABAddressBookRef=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'ABRecordSetValue': (b'B@^{__CFString=}@',), 'ABPickerGetDelegate': (b'^{OpaqueHIObjectRef=}^{OpaqueABPicker=}',), 'ABPersonCreate': (b'^{__ABPerson=}', '', {'retval': {'already_cfretained': True}}), 'ABCopyArrayOfAllPeople': (b'^{__CFArray=}^{__ABAddressBookRef=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerCopyProperties': (b'^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueSetPrimaryIdentifier': (b'B^{__ABMultiValue=}^{__CFString=}',), 'ABPickerCopyDisplayedProperty': (b'^{__CFString=}^{OpaqueABPicker=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerCopySelectedRecords': (b'^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'already_cfretained': True}}), 'ABGroupAddGroup': (b'B^{__ABGroup=}^{__ABGroup=}',), 'ABLocalizedPropertyOrLabel': (b'@@',), 'ABMultiValueCreateMutable': (b'^{__ABMultiValue=}', '', {'retval': {'already_cfretained': True}}), 'ABRecordCreateCopy': (b'@@', '', {'retval': {'already_cfretained': True}}), 'ABGetMe': (b'^{__ABPerson=}^{__ABAddressBookRef=}',), 'ABPickerSetFrame': (sel32or64(b'v^{OpaqueABPicker=}^{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'v^{OpaqueABPicker=}^{CGRect={CGPoint=dd}{CGSize=dd}}'), '', {'arguments': {1: {'type_modifier': 'n'}}}), 'ABAddPropertiesAndTypes': (b'l^{__ABAddressBookRef=}^{__CFString=}^{__CFDictionary=}',), 'ABCopyRecordForUniqueId': (b'@^{__ABAddressBookRef=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ABSetMe': (b'v^{__ABAddressBookRef=}^{__ABPerson=}',), 'ABRecordCopyValue': (b'@@^{__CFString=}',), 'ABGroupRemoveGroup': (b'B^{__ABGroup=}^{__ABGroup=}',), 'ABMultiValueInsert': (b'B^{__ABMultiValue=}@^{__CFString=}l^^{__CFString}', '', {'arguments': {4: {'type_modifier': 'o'}}}), 'ABPickerAddProperty': (b'v^{OpaqueABPicker=}^{__CFString=}',), 'ABMultiValueCopyLabelAtIndex': (b'^{__CFString=}^{__ABMultiValue=}l', '', {'retval': {'already_cfretained': True}}), 'ABPickerChangeAttributes': (sel32or64(b'v^{OpaqueABPicker=}LL', b'v^{OpaqueABPicker=}II'),), 'ABPickerDeselectAll': (b'v^{OpaqueABPicker=}',), 'ABBeginLoadingImageDataForClient': (b'l^{__ABPerson=}^?^v', '', {'arguments': {1: {'callable': {'retval': {'type': [u'v', False]}, 'arguments': {0: {'type': sel32or64(b'^{__CFData=}', b'False')}, 1: {'type': sel32or64(b'l', b'False')}, 2: {'type': sel32or64(b'^v', b'False')}}}}}}), 'ABGetSharedAddressBook': (b'^{__ABAddressBookRef=}',), 'ABRecordIsReadOnly': (b'B@',), 'ABPickerIsVisible': (b'B^{OpaqueABPicker=}',), 'ABRecordCopyUniqueId': (b'^{__CFString=}@', '', {'retval': {'already_cfretained': True}}), 'ABCopyArrayOfAllGroups': (b'^{__CFArray=}^{__ABAddressBookRef=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerCreate': (b'^{OpaqueABPicker=}', '', {'retval': {'already_cfretained': True}}), 'ABGroupRemoveMember': (b'B^{__ABGroup=}^{__ABPerson=}',), 'ABPickerDeselectIdentifier': (b'v^{OpaqueABPicker=}^{__ABPerson=}^{__CFString=}',), 'ABPickerSetColumnTitle': (b'v^{OpaqueABPicker=}^{__CFString=}^{__CFString=}',), 'ABPickerCopySelectedValues': (b'^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerGetFrame': (sel32or64(b'v^{OpaqueABPicker=}^{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'v^{OpaqueABPicker=}^{CGRect={CGPoint=dd}{CGSize=dd}}'), '', {'arguments': {1: {'type_modifier': 'o'}}}), 'ABMultiValuePropertyType': (b'l^{__ABMultiValue=}',), 'ABPersonCopyVCardRepresentation': (b'^{__CFData=}^{__ABPerson=}', '', {'retval': {'already_cfretained': True}}), 'ABCopyArrayOfPropertiesForRecordType': (b'^{__CFArray=}^{__ABAddressBookRef=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerCopyColumnTitle': (b'^{__CFString=}^{OpaqueABPicker=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerSetVisibility': (b'v^{OpaqueABPicker=}B',), 'ABPersonCopyParentGroups': (b'^{__CFArray=}^{__ABPerson=}', '', {'retval': {'already_cfretained': True}}), 'ABMultiValueCopyValueAtIndex': (b'@^{__ABMultiValue=}l',), 'ABCopyLocalizedPropertyOrLabel': (b'^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'ABPickerEditInAddressBook': (b'v^{OpaqueABPicker=}',), 'ABPickerSetDisplayedProperty': (b'v^{OpaqueABPicker=}^{__CFString=}',)}
cftypes=[('ABAddressBookRef', b'^{__ABAddressBookRef=}', None, 'ABAddressBook'), ('ABGroupRef', b'^{__ABGroup=}', None, 'ABGroup'), ('ABMultiValueRef', b'^{__ABMultiValue=}', None, 'ABMultiValue'), ('ABMutableMultiValueRef', b'^{__ABMultiValue=}', None, 'ABMutableMultiValue'), ('ABPersonRef', b'^{__ABPerson=}', None, 'ABPerson'), ('ABSearchElementRef', b'^{__ABSearchElementRef=}', None, 'ABSearchElement'), ('ABPickerRef', b'^{OpaqueABPicker}', None, 'ABPeoplePickerView')]
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('ABAddressBook', b'addRecord:', {'retval': {'type': 'Z'}})
    r('ABAddressBook', b'addRecord:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('ABAddressBook', b'hasUnsavedChanges', {'retval': {'type': 'Z'}})
    r('ABAddressBook', b'removeRecord:', {'retval': {'type': 'Z'}})
    r('ABAddressBook', b'removeRecord:error:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('ABAddressBook', b'save', {'retval': {'type': 'Z'}})
    r('ABAddressBook', b'saveAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('ABGroup', b'addMember:', {'retval': {'type': 'Z'}})
    r('ABGroup', b'addSubgroup:', {'retval': {'type': 'Z'}})
    r('ABGroup', b'removeMember:', {'retval': {'type': 'Z'}})
    r('ABGroup', b'removeSubgroup:', {'retval': {'type': 'Z'}})
    r('ABGroup', b'setDistributionIdentifier:forProperty:person:', {'retval': {'type': 'Z'}})
    r('ABMutableMultiValue', b'removeValueAndLabelAtIndex:', {'retval': {'type': 'Z'}})
    r('ABMutableMultiValue', b'replaceLabelAtIndex:withLabel:', {'retval': {'type': 'Z'}})
    r('ABMutableMultiValue', b'replaceValueAtIndex:withValue:', {'retval': {'type': 'Z'}})
    r('ABMutableMultiValue', b'setPrimaryIdentifier:', {'retval': {'type': 'Z'}})
    r('ABPeoplePickerView', b'allowsGroupSelection', {'retval': {'type': 'Z'}})
    r('ABPeoplePickerView', b'allowsMultipleSelection', {'retval': {'type': 'Z'}})
    r('ABPeoplePickerView', b'selectGroup:byExtendingSelection:', {'arguments': {3: {'type': 'Z'}}})
    r('ABPeoplePickerView', b'selectIdentifier:forPerson:byExtendingSelection:', {'arguments': {4: {'type': 'Z'}}})
    r('ABPeoplePickerView', b'selectRecord:byExtendingSelection:', {'arguments': {3: {'type': 'Z'}}})
    r('ABPeoplePickerView', b'setAllowsGroupSelection:', {'arguments': {2: {'type': 'Z'}}})
    r('ABPeoplePickerView', b'setAllowsMultipleSelection:', {'arguments': {2: {'type': 'Z'}}})
    r('ABPeoplePickerView', b'setGroupDoubleAction:', {'arguments': {2: {'sel_of_type': b'v@:@'}}})
    r('ABPeoplePickerView', b'setNameDoubleAction:', {'arguments': {2: {'sel_of_type': b'v@:@'}}})
    r('ABPerson', b'setImageData:', {'retval': {'type': 'Z'}})
    r('ABPersonView', b'editing', {'retval': {'type': 'Z'}})
    r('ABPersonView', b'setEditing:', {'arguments': {2: {'type': 'Z'}}})
    r('ABRecord', b'isReadOnly', {'retval': {'type': 'Z'}})
    r('ABRecord', b'removeValueForProperty:', {'retval': {'type': 'Z'}})
    r('ABRecord', b'setValue:forProperty:', {'retval': {'type': 'Z'}})
    r('ABRecord', b'setValue:forProperty:error:', {'retval': {'type': 'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('ABSearchElement', b'matchesRecord:', {'retval': {'type': 'Z'}})
    r('NSObject', b'shouldEnableActionForPerson:identifier:', {'retval': {'type': 'Z'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'consumeImageData:forTag:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': sel32or64(b'i', b'l')}}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r('NSObject', b'actionProperty', {'retval': {'type': b'@'}})
    r('NSObject', b'performActionForPerson:identifier:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'shouldEnableActionForPerson:identifier:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSObject', b'titleForPerson:identifier:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
protocols={'ABActionDelegate': objc.informal_protocol('ABActionDelegate', [objc.selector(None, 'shouldEnableActionForPerson:identifier:', b'Z@:@@', isRequired=False), objc.selector(None, 'actionProperty', b'@@:', isRequired=False), objc.selector(None, 'performActionForPerson:identifier:', b'v@:@@', isRequired=False), objc.selector(None, 'titleForPerson:identifier:', b'@@:@@', isRequired=False)])}
expressions = {}

# END OF FILE
