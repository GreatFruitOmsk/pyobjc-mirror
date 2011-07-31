# Generated file, don't edit
# Source: BridgeSupport/AddressBook.bridgesupport
# Last update: Sun Jul 31 16:56:27 2011

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
constants = '''$kABEmailMobileMeLabel$kABBirthdayComponentsProperty$kABOtherDateComponentsProperty$ABPeoplePickerDisplayedPropertyDidChangeNotification$ABPeoplePickerGroupSelectionDidChangeNotification$ABPeoplePickerNameSelectionDidChangeNotification$ABPeoplePickerValueSelectionDidChangeNotification$kABAIMHomeLabel$kABAIMInstantProperty$kABAIMWorkLabel$kABAddressCityKey$kABAddressCountryCodeKey$kABAddressCountryKey$kABAddressHomeLabel$kABAddressProperty$kABAddressStateKey$kABAddressStreetKey$kABAddressWorkLabel$kABAddressZIPKey$kABAnniversaryLabel$kABAIMMobileMeLabel$kABAssistantLabel$kABBirthdayProperty$kABBrotherLabel$kABCalendarURIsProperty$kABChildLabel$kABCreationDateProperty$kABDatabaseChangedExternallyNotification$kABDatabaseChangedNotification$kABDeletedRecords$kABDepartmentProperty$kABEmailHomeLabel$kABEmailProperty$kABEmailWorkLabel$kABFatherLabel$kABFirstNamePhoneticProperty$kABFirstNameProperty$kABFriendLabel$kABGroupNameProperty$kABGroupRecordType@^{__CFString=}$kABHomeLabel$kABHomePageLabel$kABHomePageProperty$kABICQHomeLabel$kABICQInstantProperty$kABICQWorkLabel$kABInsertedRecords$kABJabberHomeLabel$kABJabberInstantProperty$kABBirthdayComponentsProperty$kABOtherDateComponentsProperty$kABInstantMessageProperty$kABInstantMessageUsernameKey$kABInstantMessageServiceKey$kABInstantMessageServiceAIM$kABInstantMessageServiceFacebook$kABInstantMessageServiceGaduGadu$kABInstantMessageServiceGoogleTalk$kABInstantMessageServiceICQ$kABInstantMessageServiceJabber$kABInstantMessageServiceMSN$kABInstantMessageServiceQQ$kABInstantMessageServiceSkype$kABInstantMessageServiceYahoo$kABSocialProfileProperty$kABSocialProfileURLKey$kABSocialProfileUsernameKey$kABSocialProfileUserIdentifierKey$kABSocialProfileServiceKey$kABSocialProfileServiceTwitter$kABSocialProfileServiceFacebook$kABSocialProfileServiceLinkedIn$kABSocialProfileServiceFlickr$kABSocialProfileServiceMySpace$kABJabberWorkLabel$kABMobileMeLabel$kABJobTitleProperty$kABLastNamePhoneticProperty$kABLastNameProperty$kABMSNHomeLabel$kABMSNInstantProperty$kABMSNWorkLabel$kABMaidenNameProperty$kABManagerLabel$kABMiddleNamePhoneticProperty$kABMiddleNameProperty$kABModificationDateProperty$kABMotherLabel$kABNicknameProperty$kABNoteProperty$kABOrganizationProperty$kABOtherDatesProperty$kABOtherLabel$kABParentLabel$kABPartnerLabel$kABPersonFlags$kABPersonRecordType@^{__CFString=}$kABPhoneHomeFAXLabel$kABPhoneHomeLabel$kABPhoneiPhoneLabel$kABPhoneMobileLabel$kABPhoneMainLabel$kABPhonePagerLabel$kABPhoneProperty$kABPhoneWorkFAXLabel$kABPhoneWorkLabel$kABRelatedNamesProperty$kABSisterLabel$kABSpouseLabel$kABSuffixProperty$kABTitleProperty$kABUIDProperty$kABURLsProperty$kABUpdatedRecords$kABWorkLabel$kABYahooHomeLabel$kABYahooInstantProperty$kABYahooWorkLabel$ABAddressBookErrorDomain$ABMultiValueIdentifiersErrorKey$'''
enums = '''$kABDateComponentsProperty@8$ABAddRecordsError@1001$ABRemoveRecordsError@1002$ABPropertyValueValidationError@1012$ABPropertyUnsupportedBySourceError@1013$ABPropertyReadOnlyError@1014$ABMultipleValueSelection@2$kABShowAsResource@2$kABShowAsRoom@3$ABNoValueSelection@0$ABSingleValueSelection@1$kABArrayProperty@5$kABBitsInBitFieldMatch@11$kABContainsSubString@7$kABContainsSubStringCaseInsensitive@8$kABDataProperty@7$kABDateProperty@4$kABDefaultNameOrdering@0$kABDefaultNameOrdering@0$kABDictionaryProperty@6$kABDoesNotContainSubString@12$kABDoesNotContainSubStringCaseInsensitive@13$kABEqual@0$kABEqualCaseInsensitive@6$kABErrorInProperty@0$kABFirstNameFirst@32$kABFirstNameFirst@32$kABGreaterThan@4$kABGreaterThanOrEqual@5$kABIntegerProperty@2$kABLastNameFirst@16$kABLastNameFirst@16$kABLessThan@2$kABLessThanOrEqual@3$kABMultiArrayProperty@261$kABMultiDataProperty@263$kABMultiDateProperty@260$kABMultiDateComponentsProperty@264$kABMultiDictionaryProperty@262$kABMultiIntegerProperty@258$kABMultiRealProperty@259$kABMultiStringProperty@257$kABMultiValueMask@256$kABNameOrderingMask@56$kABNameOrderingMask@56$kABNotEqual@1$kABNotEqualCaseInsensitive@14$kABNotWithinIntervalAroundToday@19$kABNotWithinIntervalAroundTodayYearless@20$kABNotWithinIntervalFromToday@23$kABNotWithinIntervalFromTodayYearless@24$kABPickerAllowGroupSelection@4$kABPickerAllowMultipleSelection@8$kABPickerMultipleValueSelection@2$kABPickerSingleValueSelection@1$kABPrefixMatch@9$kABPrefixMatchCaseInsensitive@10$kABRealProperty@3$kABSearchAnd@0$kABSearchOr@1$kABShowAsCompany@1$kABShowAsCompany@1$kABShowAsMask@7$kABShowAsMask@7$kABShowAsPerson@0$kABShowAsPerson@0$kABStringProperty@1$kABSuffixMatch@15$kABSuffixMatchCaseInsensitive@16$kABWithinIntervalAroundToday@17$kABWithinIntervalAroundTodayYearless@18$kABWithinIntervalFromToday@21$kABWithinIntervalFromTodayYearless@22$kEventABPeoplePickerDisplayedPropertyChanged@4$kEventABPeoplePickerGroupDoubleClicked@5$kEventABPeoplePickerGroupSelectionChanged@1$kEventABPeoplePickerNameDoubleClicked@6$kEventABPeoplePickerNameSelectionChanged@2$kEventABPeoplePickerValueSelectionChanged@3$kEventClassABPeoplePicker@1633841264$kEventParamABPickerRef@1633841264$'''
misc.update({})
functions = {'ABMultiValueReplaceValue': (sel32or64('B^{__ABMultiValue=}@l', 'B^{__ABMultiValue=}@q'),), 'ABPickerSetDelegate': ('v^{OpaqueABPicker=}^{OpaqueHIObjectRef=}',), 'ABAddRecord': ('B^{__ABAddressBookRef=}@',), 'ABPickerClearSearchField': ('v^{OpaqueABPicker=}',), 'ABPickerSelectGroup': ('v^{OpaqueABPicker=}^{__ABGroup=}B',), 'ABCopyDefaultCountryCode': ('^{__CFString=}^{__ABAddressBookRef=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABPickerGetAttributes': (sel32or64('L^{OpaqueABPicker=}', 'I^{OpaqueABPicker=}'),), 'ABSave': ('B^{__ABAddressBookRef=}',), 'ABPersonCreateWithVCardRepresentation': ('^{__ABPerson=}^{__CFData=}', '', {'retval': {'type': b'^{__ABPerson=}', 'already_cfretained': True}}), 'ABGroupAddMember': ('B^{__ABGroup=}^{__ABPerson=}',), 'ABPersonCreateSearchElement': (sel32or64('^{__ABSearchElementRef=}^{__CFString=}^{__CFString=}^{__CFString=}@l', '^{__ABSearchElementRef=}^{__CFString=}^{__CFString=}^{__CFString=}@q'), '', {'retval': {'type': b'^{__ABSearchElementRef=}', 'already_cfretained': True}}), 'ABMultiValueRemove': (sel32or64('B^{__ABMultiValue=}l', 'B^{__ABMultiValue=}q'),), 'ABSearchElementMatchesRecord': ('B^{__ABSearchElementRef=}@',), 'ABRecordCopyRecordType': ('^{__CFString=}@', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABPickerSelectIdentifier': ('v^{OpaqueABPicker=}^{__ABPerson=}^{__CFString=}B',), 'ABMultiValueCopyPrimaryIdentifier': ('^{__CFString=}^{__ABMultiValue=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABMultiValueIndexForIdentifier': (sel32or64('l^{__ABMultiValue=}^{__CFString=}', 'q^{__ABMultiValue=}^{__CFString=}'),), 'ABPickerSelectRecord': ('v^{OpaqueABPicker=}@B',), 'ABMultiValueCreateMutableCopy': ('^{__ABMultiValue=}^{__ABMultiValue=}', '', {'retval': {'type': b'^{__ABMultiValue=}', 'already_cfretained': True}}), 'ABRecordRemoveValue': ('B@^{__CFString=}',), 'ABPickerCopySelectedGroups': ('^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABMultiValueCopyIdentifierAtIndex': (sel32or64('^{__CFString=}^{__ABMultiValue=}l', '^{__CFString=}^{__ABMultiValue=}q'), '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABCancelLoadingImageDataForTag': (sel32or64('vl', 'vq'),), 'ABCopyArrayOfMatchingRecords': ('^{__CFArray=}^{__ABAddressBookRef=}^{__ABSearchElementRef=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABPickerRemoveProperty': ('v^{OpaqueABPicker=}^{__CFString=}',), 'ABMultiValueCount': (sel32or64('l^{__ABMultiValue=}', 'q^{__ABMultiValue=}'),), 'ABPickerCopySelectedIdentifiers': ('^{__CFArray=}^{OpaqueABPicker=}^{__ABPerson=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABGroupCreate': ('^{__ABGroup=}', '', {'retval': {'type': b'^{__ABGroup=}', 'already_cfretained': True}}), 'ABMultiValueCreateCopy': ('^{__ABMultiValue=}^{__ABMultiValue=}', '', {'retval': {'type': b'^{__ABMultiValue=}', 'already_cfretained': True}}), 'ABMultiValueAdd': ('B^{__ABMultiValue=}@^{__CFString=}^^{__CFString}', '', {'arguments': {0: {'type': b'^{__ABMultiValue=}'}, 1: {'type': b'@'}, 2: {'type': b'^{__CFString=}'}, 3: {'type': b'^^{__CFString}', 'type_modifier': b'o'}}}), 'ABHasUnsavedChanges': ('B^{__ABAddressBookRef=}',), 'ABMultiValueReplaceLabel': (sel32or64('B^{__ABMultiValue=}^{__CFString=}l', 'B^{__ABMultiValue=}^{__CFString=}q'),), 'ABGroupCopyParentGroups': ('^{__CFArray=}^{__ABGroup=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABGroupSetDistributionIdentifier': ('B^{__ABGroup=}^{__ABPerson=}^{__CFString=}^{__CFString=}',), 'ABPickerDeselectRecord': ('v^{OpaqueABPicker=}@',), 'ABGroupCreateSearchElement': (sel32or64('^{__ABSearchElementRef=}^{__CFString=}^{__CFString=}^{__CFString=}@l', '^{__ABSearchElementRef=}^{__CFString=}^{__CFString=}^{__CFString=}@q'), '', {'retval': {'type': b'^{__ABSearchElementRef=}', 'already_cfretained': True}}), 'ABCopyRecordTypeFromUniqueId': ('^{__CFString=}^{__ABAddressBookRef=}^{__CFString=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABRemoveRecord': ('B^{__ABAddressBookRef=}@',), 'ABGroupCopyDistributionIdentifier': ('^{__CFString=}^{__ABGroup=}^{__ABPerson=}^{__CFString=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABPersonCopyImageData': ('^{__CFData=}^{__ABPerson=}', '', {'retval': {'type': b'^{__CFData=}', 'already_cfretained': True}}), 'ABPickerDeselectGroup': ('v^{OpaqueABPicker=}^{__ABGroup=}',), 'ABGroupRemoveGroup': ('B^{__ABGroup=}^{__ABGroup=}',), 'ABRemoveProperties': (sel32or64('l^{__ABAddressBookRef=}^{__CFString=}^{__CFArray=}', 'q^{__ABAddressBookRef=}^{__CFString=}^{__CFArray=}'),), 'ABGroupCopyArrayOfAllSubgroups': ('^{__CFArray=}^{__ABGroup=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABMultiValueCreate': ('^{__ABMultiValue=}', '', {'retval': {'type': b'^{__ABMultiValue=}', 'already_cfretained': True}}), 'ABPickerSelectInAddressBook': ('v^{OpaqueABPicker=}',), 'ABGroupCopyArrayOfAllMembers': ('^{__CFArray=}^{__ABGroup=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABSearchElementCreateWithConjunction': (sel32or64('^{__ABSearchElementRef=}l^{__CFArray=}', '^{__ABSearchElementRef=}q^{__CFArray=}'), '', {'retval': {'type': b'^{__ABSearchElementRef=}', 'already_cfretained': True}}), 'ABMultiValueCopyValueAtIndex': (sel32or64('@^{__ABMultiValue=}l', '@^{__ABMultiValue=}q'), '', {'retval': {'type': b'@', 'already_cfretained': True}}), 'ABPersonSetImageData': ('B^{__ABPerson=}^{__CFData=}',), 'ABCreateFormattedAddressFromDictionary': ('^{__CFString=}^{__ABAddressBookRef=}^{__CFDictionary=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABRecordSetValue': ('B@^{__CFString=}@',), 'ABPickerGetDelegate': ('^{OpaqueHIObjectRef=}^{OpaqueABPicker=}',), 'ABPersonCreate': ('^{__ABPerson=}', '', {'retval': {'type': b'^{__ABPerson=}', 'already_cfretained': True}}), 'ABCopyArrayOfAllPeople': ('^{__CFArray=}^{__ABAddressBookRef=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABPickerCopyProperties': ('^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABMultiValueSetPrimaryIdentifier': ('B^{__ABMultiValue=}^{__CFString=}',), 'ABPickerCopyDisplayedProperty': ('^{__CFString=}^{OpaqueABPicker=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABPickerCopySelectedRecords': ('^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABGroupAddGroup': ('B^{__ABGroup=}^{__ABGroup=}',), 'ABLocalizedPropertyOrLabel': ('@@', '', {'retval': {'type': b'@', 'already_cfretained': True}}), 'ABMultiValueCreateMutable': ('^{__ABMultiValue=}', '', {'retval': {'type': b'^{__ABMultiValue=}', 'already_cfretained': True}}), 'ABRecordCreateCopy': ('@@', '', {'retval': {'type': b'@', 'already_cfretained': True}}), 'ABGetMe': ('^{__ABPerson=}^{__ABAddressBookRef=}',), 'ABPickerSetFrame': (sel32or64('v^{OpaqueABPicker=}^{_NSRect={_NSPoint=ff}{_NSSize=ff}}', 'v^{OpaqueABPicker=}^{CGRect={CGPoint=dd}{CGSize=dd}}'), '', {'arguments': {0: {'type': b'^{OpaqueABPicker=}'}, 1: {'type': sel32or64(b'^{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'^{CGRect={CGPoint=dd}{CGSize=dd}}'), 'type_modifier': b'n'}}}), 'ABAddPropertiesAndTypes': (sel32or64('l^{__ABAddressBookRef=}^{__CFString=}^{__CFDictionary=}', 'q^{__ABAddressBookRef=}^{__CFString=}^{__CFDictionary=}'),), 'ABCopyRecordForUniqueId': ('@^{__ABAddressBookRef=}^{__CFString=}', '', {'retval': {'type': b'@', 'already_cfretained': True}}), 'ABSetMe': ('v^{__ABAddressBookRef=}^{__ABPerson=}',), 'ABRecordCopyValue': ('@@^{__CFString=}', '', {'retval': {'type': b'@', 'already_cfretained': True}}), 'ABTypeOfProperty': (sel32or64('l^{__ABAddressBookRef=}^{__CFString=}^{__CFString=}', 'q^{__ABAddressBookRef=}^{__CFString=}^{__CFString=}'),), 'ABMultiValueInsert': (sel32or64('B^{__ABMultiValue=}@^{__CFString=}l^^{__CFString}', 'B^{__ABMultiValue=}@^{__CFString=}q^^{__CFString}'), '', {'arguments': {0: {'type': b'^{__ABMultiValue=}'}, 1: {'type': b'@'}, 2: {'type': b'^{__CFString=}'}, 3: {'type': sel32or64(b'l', b'q')}, 4: {'type': b'^^{__CFString}', 'type_modifier': b'o'}}}), 'ABPickerAddProperty': ('v^{OpaqueABPicker=}^{__CFString=}',), 'ABMultiValueCopyLabelAtIndex': (sel32or64('^{__CFString=}^{__ABMultiValue=}l', '^{__CFString=}^{__ABMultiValue=}q'), '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABPickerChangeAttributes': ('v^{OpaqueABPicker=}LL',), 'ABPickerDeselectAll': ('v^{OpaqueABPicker=}',), 'ABBeginLoadingImageDataForClient': (sel32or64('l^{__ABPerson=}^?^v', 'q^{__ABPerson=}^?^v'), '', {'arguments': {0: {'type': b'^{__ABPerson=}'}, 1: {'callable': {'retval': {'type': b'^v'}, 'arguments': {0: {'type': b'@'}, 1: {'type': sel32or64(b'l', b'q')}, 2: {'type': b'^v'}}}, 'type': b'^?'}, 2: {'type': b'^v'}}}), 'ABGetSharedAddressBook': ('^{__ABAddressBookRef=}',), 'ABRecordIsReadOnly': ('B@',), 'ABPickerIsVisible': ('B^{OpaqueABPicker=}',), 'ABRecordCopyUniqueId': ('^{__CFString=}@', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABCopyArrayOfAllGroups': ('^{__CFArray=}^{__ABAddressBookRef=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABPickerCreate': ('^{OpaqueABPicker=}', '', {'retval': {'type': b'^{OpaqueABPicker=}', 'already_cfretained': True}}), 'ABGroupRemoveMember': ('B^{__ABGroup=}^{__ABPerson=}',), 'ABPickerDeselectIdentifier': ('v^{OpaqueABPicker=}^{__ABPerson=}^{__CFString=}',), 'ABPickerSetColumnTitle': ('v^{OpaqueABPicker=}^{__CFString=}^{__CFString=}',), 'ABPickerCopySelectedValues': ('^{__CFArray=}^{OpaqueABPicker=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABPickerGetFrame': (sel32or64('v^{OpaqueABPicker=}^{_NSRect={_NSPoint=ff}{_NSSize=ff}}', 'v^{OpaqueABPicker=}^{CGRect={CGPoint=dd}{CGSize=dd}}'), '', {'arguments': {0: {'type': b'^{OpaqueABPicker=}'}, 1: {'type': sel32or64(b'^{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'^{CGRect={CGPoint=dd}{CGSize=dd}}'), 'type_modifier': b'o'}}}), 'ABMultiValuePropertyType': (sel32or64('l^{__ABMultiValue=}', 'q^{__ABMultiValue=}'),), 'ABPersonCopyVCardRepresentation': ('^{__CFData=}^{__ABPerson=}', '', {'retval': {'type': b'^{__CFData=}', 'already_cfretained': True}}), 'ABCopyArrayOfPropertiesForRecordType': ('^{__CFArray=}^{__ABAddressBookRef=}^{__CFString=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABPickerCopyColumnTitle': ('^{__CFString=}^{OpaqueABPicker=}^{__CFString=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABPickerSetVisibility': ('v^{OpaqueABPicker=}B',), 'ABPersonCopyParentGroups': ('^{__CFArray=}^{__ABPerson=}', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'ABCopyLocalizedPropertyOrLabel': ('^{__CFString=}^{__CFString=}', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'ABPickerEditInAddressBook': ('v^{OpaqueABPicker=}',), 'ABPickerSetDisplayedProperty': ('v^{OpaqueABPicker=}^{__CFString=}',)}
cftypes = []
cftypes.append(('ABAddressBookRef', '^{__ABAddressBookRef=}', None, 'ABAddressBook'))
cftypes.append(('ABGroupRef', '^{__ABGroup=}', None, 'ABGroup'))
cftypes.append(('ABMultiValueRef', '^{__ABMultiValue=}', None, 'ABMultiValue'))
cftypes.append(('ABMutableMultiValueRef', '^{__ABMultiValue=}', None, 'ABMutableMultiValue'))
cftypes.append(('ABPersonRef', '^{__ABPerson=}', None, 'ABPerson'))
cftypes.append(('ABPickerRef', '^{OpaqueABPicker=}', None, 'ABPeoplePickerView'))
cftypes.append(('ABSearchElementRef', '^{__ABSearchElementRef=}', None, 'ABSearchElement'))
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('ABAddressBook', b'addRecord:', {'retval': {'type': b'Z'}})
    r('ABAddressBook', b'addRecord:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('ABAddressBook', b'hasUnsavedChanges', {'retval': {'type': b'Z'}})
    r('ABAddressBook', b'removeRecord:', {'retval': {'type': b'Z'}})
    r('ABAddressBook', b'removeRecord:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r('ABAddressBook', b'save', {'retval': {'type': b'Z'}})
    r('ABAddressBook', b'saveAndReturnError:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r('ABGroup', b'addMember:', {'retval': {'type': b'Z'}})
    r('ABGroup', b'addSubgroup:', {'retval': {'type': b'Z'}})
    r('ABGroup', b'removeMember:', {'retval': {'type': b'Z'}})
    r('ABGroup', b'removeSubgroup:', {'retval': {'type': b'Z'}})
    r('ABGroup', b'setDistributionIdentifier:forProperty:person:', {'retval': {'type': b'Z'}})
    r('ABMutableMultiValue', b'removeValueAndLabelAtIndex:', {'retval': {'type': b'Z'}})
    r('ABMutableMultiValue', b'replaceLabelAtIndex:withLabel:', {'retval': {'type': b'Z'}})
    r('ABMutableMultiValue', b'replaceValueAtIndex:withValue:', {'retval': {'type': b'Z'}})
    r('ABMutableMultiValue', b'setPrimaryIdentifier:', {'retval': {'type': b'Z'}})
    r('ABPeoplePickerView', b'allowsGroupSelection', {'retval': {'type': b'Z'}})
    r('ABPeoplePickerView', b'allowsMultipleSelection', {'retval': {'type': b'Z'}})
    r('ABPeoplePickerView', b'selectGroup:byExtendingSelection:', {'arguments': {3: {'type': b'Z'}}})
    r('ABPeoplePickerView', b'selectIdentifier:forPerson:byExtendingSelection:', {'arguments': {4: {'type': b'Z'}}})
    r('ABPeoplePickerView', b'selectRecord:byExtendingSelection:', {'arguments': {3: {'type': b'Z'}}})
    r('ABPeoplePickerView', b'setAllowsGroupSelection:', {'arguments': {2: {'type': b'Z'}}})
    r('ABPeoplePickerView', b'setAllowsMultipleSelection:', {'arguments': {2: {'type': b'Z'}}})
    r('ABPeoplePickerView', b'setGroupDoubleAction:', {'arguments': {2: {'sel_of_type': b'v@:@'}}})
    r('ABPeoplePickerView', b'setNameDoubleAction:', {'arguments': {2: {'sel_of_type': b'v@:@'}}})
    r('ABPerson', b'setImageData:', {'retval': {'type': b'Z'}})
    r('ABRecord', b'isReadOnly', {'retval': {'type': b'Z'}})
    r('ABRecord', b'removeValueForProperty:', {'retval': {'type': b'Z'}})
    r('ABRecord', b'setValue:forProperty:', {'retval': {'type': b'Z'}})
    r('ABRecord', b'setValue:forProperty:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type_modifier': b'o'}}})
    r('ABSearchElement', b'matchesRecord:', {'retval': {'type': b'Z'}})
    r('NSObject', b'shouldEnableActionForPerson:identifier:', {'retval': {'type': b'Z'}})
    r('ABPersonView', b'editing', {'retval': {'type': b'Z'}})
    r('ABPersonView', b'setEditing:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)
protocols={'ABActionDelegate': objc.informal_protocol('ABActionDelegate', [objc.selector(None, 'actionProperty', '@@:', isRequired=False), objc.selector(None, 'performActionForPerson:identifier:', 'v@:@@', isRequired=False), objc.selector(None, 'shouldEnableActionForPerson:identifier:', 'Z@:@@', isRequired=False), objc.selector(None, 'titleForPerson:identifier:', '@@:@@', isRequired=False)])}
