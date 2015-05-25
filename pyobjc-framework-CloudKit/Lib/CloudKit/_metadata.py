# This file is generated by objective.metadata
#
# Last update: Mon May 25 15:34:23 2015

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
constants = '''$CKErrorDomain$CKErrorRetryAfterKey$CKOwnerDefaultName$CKPartialErrorsByItemIDKey$CKQueryOperationMaximumResults@Q$CKRecordChangedErrorAncestorRecordKey$CKRecordChangedErrorClientRecordKey$CKRecordChangedErrorServerRecordKey$CKRecordTypeUserRecord$CKRecordZoneDefaultName$'''
enums = '''$CKAccountStatusAvailable@1$CKAccountStatusCouldNotDetermine@0$CKAccountStatusNoAccount@3$CKAccountStatusRestricted@2$CKApplicationPermissionStatusCouldNotComplete@1$CKApplicationPermissionStatusDenied@2$CKApplicationPermissionStatusGranted@3$CKApplicationPermissionStatusInitialState@0$CKApplicationPermissionUserDiscoverability@1$CKErrorAssetFileModified@17$CKErrorAssetFileNotFound@16$CKErrorBadContainer@5$CKErrorBadDatabase@24$CKErrorBatchRequestFailed@22$CKErrorChangeTokenExpired@21$CKErrorConstraintViolation@19$CKErrorIncompatibleVersion@18$CKErrorInternalError@1$CKErrorInvalidArguments@12$CKErrorLimitExceeded@27$CKErrorMissingEntitlement@8$CKErrorNetworkFailure@4$CKErrorNetworkUnavailable@3$CKErrorNotAuthenticated@9$CKErrorOperationCancelled@20$CKErrorPartialFailure@2$CKErrorPermissionFailure@10$CKErrorQuotaExceeded@25$CKErrorRequestRateLimited@7$CKErrorResultsTruncated@13$CKErrorServerRecordChanged@14$CKErrorServerRejectedRequest@15$CKErrorServiceUnavailable@6$CKErrorUnknownItem@11$CKErrorUserDeletedZone@28$CKErrorZoneBusy@23$CKErrorZoneNotFound@26$CKNotificationTypeQuery@1$CKNotificationTypeReadNotification@3$CKNotificationTypeRecordZone@2$CKQueryNotificationReasonRecordCreated@1$CKQueryNotificationReasonRecordDeleted@3$CKQueryNotificationReasonRecordUpdated@2$CKRecordSaveAllKeys@2$CKRecordSaveChangedKeys@1$CKRecordSaveIfServerRecordUnchanged@0$CKRecordZoneCapabilityAtomic@2$CKRecordZoneCapabilityFetchChanges@1$CKReferenceActionDeleteSelf@1$CKReferenceActionNone@0$CKSubscriptionOptionsFiresOnRecordCreation@1$CKSubscriptionOptionsFiresOnRecordDeletion@4$CKSubscriptionOptionsFiresOnRecordUpdate@2$CKSubscriptionOptionsFiresOnce@8$CKSubscriptionTypeQuery@1$CKSubscriptionTypeRecordZone@2$'''
misc.update({})
aliases = {'CK_UNIT_TESTS_EXTERN': 'CK_EXTERN'}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'CKContainer', b'accountStatusWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'q'}, 2: {'type': b'@'}}}}}})
    r(b'CKContainer', b'discoverAllContactUserInfosWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKContainer', b'discoverUserInfoWithEmailAddress:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKContainer', b'discoverUserInfoWithUserRecordID:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKContainer', b'fetchUserRecordIDWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKContainer', b'requestApplicationPermission:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'q'}, 2: {'type': b'@'}}}}}})
    r(b'CKContainer', b'statusForApplicationPermission:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'q'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'deleteRecordWithID:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'deleteRecordZoneWithID:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'deleteSubscriptionWithID:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'fetchAllRecordZonesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'fetchAllSubscriptionsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'fetchRecordWithID:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'fetchRecordZoneWithID:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'fetchSubscriptionWithID:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'performQuery:inZoneWithID:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'saveRecord:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'saveRecordZone:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDatabase', b'saveSubscription:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKDiscoverAllContactsOperation', b'discoverAllContactsCompletionBlock', {'retval': {'callable': {'retval': {'type': b'@'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'CKDiscoverAllContactsOperation', b'setDiscoverAllContactsCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'@'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CKDiscoverUserInfosOperation', b'discoverUserInfosCompletionBlock', {'retval': {'callable': {'retval': {'type': b'@'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'CKDiscoverUserInfosOperation', b'setDiscoverUserInfosCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'@'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKFetchNotificationChangesOperation', b'fetchNotificationChangesCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'CKFetchNotificationChangesOperation', b'moreComing', {'retval': {'type': b'Z'}})
    r(b'CKFetchNotificationChangesOperation', b'notificationChangedBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'CKFetchNotificationChangesOperation', b'setFetchNotificationChangesCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKFetchNotificationChangesOperation', b'setNotificationChangedBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CKFetchRecordChangesOperation', b'fetchRecordChangesCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}})
    r(b'CKFetchRecordChangesOperation', b'moreComing', {'retval': {'type': b'Z'}})
    r(b'CKFetchRecordChangesOperation', b'perRecordProgressBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'd'}}}}})
    r(b'CKFetchRecordChangesOperation', b'recordChangedBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'CKFetchRecordChangesOperation', b'recordWithIDWasDeletedBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'CKFetchRecordChangesOperation', b'setFetchRecordChangesCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}}})
    r(b'CKFetchRecordChangesOperation', b'setPerRecordProgressBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'd'}}}}}})
    r(b'CKFetchRecordChangesOperation', b'setRecordChangedBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CKFetchRecordChangesOperation', b'setRecordWithIDWasDeletedBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CKFetchRecordZonesOperation', b'fetchRecordZonesCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'CKFetchRecordZonesOperation', b'setFetchRecordZonesCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKFetchRecordsOperation', b'fetchRecordsCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'CKFetchRecordsOperation', b'perRecordCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}})
    r(b'CKFetchRecordsOperation', b'perRecordProgressBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'd'}}}}})
    r(b'CKFetchRecordsOperation', b'setFetchRecordsCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKFetchRecordsOperation', b'setPerRecordCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}}})
    r(b'CKFetchRecordsOperation', b'setPerRecordProgressBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'd'}}}}}})
    r(b'CKFetchSubscriptionsOperation', b'fetchSubscriptionCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'CKFetchSubscriptionsOperation', b'setFetchSubscriptionCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKMarkNotificationsReadOperation', b'markNotificationsReadCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'CKMarkNotificationsReadOperation', b'setMarkNotificationsReadCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKModifyBadgeOperation', b'modifyBadgeCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'CKModifyBadgeOperation', b'setModifyBadgeCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CKModifyRecordZonesOperation', b'modifyRecordZonesCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}})
    r(b'CKModifyRecordZonesOperation', b'setModifyRecordZonesCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}}})
    r(b'CKModifyRecordsOperation', b'atomic', {'retval': {'type': b'Z'}})
    r(b'CKModifyRecordsOperation', b'modifyRecordsCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}})
    r(b'CKModifyRecordsOperation', b'perRecordCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'CKModifyRecordsOperation', b'perRecordProgressBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'd'}}}}})
    r(b'CKModifyRecordsOperation', b'setAtomic:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CKModifyRecordsOperation', b'setModifyRecordsCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}}})
    r(b'CKModifyRecordsOperation', b'setPerRecordCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'CKModifyRecordsOperation', b'setPerRecordProgressBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'd'}}}}}})
    r(b'CKModifySubscriptionsOperation', b'modifySubscriptionsCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}})
    r(b'CKModifySubscriptionsOperation', b'setModifySubscriptionsCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}}}})
    r(b'CKNotification', b'isPruned', {'retval': {'type': b'Z'}})
    r(b'CKNotificationInfo', b'setShouldBadge:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CKNotificationInfo', b'setShouldSendContentAvailable:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CKNotificationInfo', b'shouldBadge', {'retval': {'type': b'Z'}})
    r(b'CKNotificationInfo', b'shouldSendContentAvailable', {'retval': {'type': b'Z'}})
    r(b'CKOperation', b'allowsCellularAccess', {'retval': {'type': b'Z'}})
    r(b'CKOperation', b'setAllowsCellularAccess:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CKOperation', b'setUsesBackgroundSession:', {'arguments': {2: {'type': b'Z'}}})
    r(b'CKOperation', b'usesBackgroundSession', {'retval': {'type': b'Z'}})
    r(b'CKQueryNotification', b'isPublicDatabase', {'retval': {'type': b'Z'}})
    r(b'CKQueryOperation', b'queryCompletionBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'CKQueryOperation', b'recordFetchedBlock', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}})
    r(b'CKQueryOperation', b'setQueryCompletionBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'CKQueryOperation', b'setRecordFetchedBlock:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
