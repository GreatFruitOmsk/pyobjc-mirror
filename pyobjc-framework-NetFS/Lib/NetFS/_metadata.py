# This file is generated by objective.metadata
#
# Last update: Mon Jul 18 12:12:04 2016

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
constants = '''$$'''
enums = '''$ENETFSACCOUNTRESTRICTED@-5999$ENETFSNOAUTHMECHSUPP@-5997$ENETFSNOPROTOVERSSUPP@-5996$ENETFSNOSHARESAVAIL@-5998$ENETFSPWDNEEDSCHANGE@-5045$ENETFSPWDPOLICY@-5046$'''
misc.update({'kNetFSOpenURLMountKey': b'OpenURLMount'.decode("utf-8"), 'kNetFSMountPathKey': b'MountPath'.decode("utf-8"), 'kNAUIOptionNoUI': b'NoUI'.decode("utf-8"), 'kNetFSServerDisplayNameKey': b'ServerDisplayName'.decode("utf-8"), 'kNetFSAuthorityParamsKey': b'AuthorityParams'.decode("utf-8"), 'kNetFSMountFlagsKey': b'MountFlags'.decode("utf-8"), 'kNetFSSupportsKerberosKey': b'SupportsKerberos'.decode("utf-8"), 'kNetFSMountedMultiUserKey': b'MountedMultiUser'.decode("utf-8"), 'kNetFSHostKey': b'Host'.decode("utf-8"), 'kNetFSConnectedAsUserKey': b'MountedByUser'.decode("utf-8"), 'kNetFSHasPasswordKey': b'HasPassword'.decode("utf-8"), 'kNetFSSupportsGuestKey': b'SupportsGuest'.decode("utf-8"), 'kNetFSAlreadyMountedKey': b'AlreadyMounted'.decode("utf-8"), 'kNAUIOptionAllowUI': b'AllowUI'.decode("utf-8"), 'kNetFSMechTypesSupportedKey': b'MechTypesSupported'.decode("utf-8"), 'kNetFSMountedByUserKey': b'MountedByUser'.decode("utf-8"), 'kNetFSMountedWithAuthenticationInfoKey': b'MountedWithAuthenticationInfo'.decode("utf-8"), 'kNetFSAuthenticationInfoKey': b'AuthenticationInfo'.decode("utf-8"), 'kNetFSNoMountAuthenticationKey': b'NoMountAuthentication'.decode("utf-8"), 'kNetFSPrinterShareKey': b'PrinterShare'.decode("utf-8"), 'kNetFSUseKerberosKey': b'Kerberos'.decode("utf-8"), 'kNetFSMountAtMountDirKey': b'MountAtMountDir'.decode("utf-8"), 'kNAUIOptionForceUI': b'ForceUI'.decode("utf-8"), 'kNetFSGetAccessRightsKey': b'GetAccessRights'.decode("utf-8"), 'kNetFSPasswordKey': b'Password'.decode("utf-8"), 'kNetFSMountedByKerberosKey': b'MountedByKerberos'.decode("utf-8"), 'kNetFSSchemeKey': b'Scheme'.decode("utf-8"), 'kNetFSConnectedMultiUserKey': b'ConnectedMultiUser'.decode("utf-8"), 'kNetFSAccessRightsKey': b'AccessRights'.decode("utf-8"), 'kNetFSMountedByGuestKey': b'MountedByGuest'.decode("utf-8"), 'kNetFSSoftMountKey': b'SoftMount'.decode("utf-8"), 'kNetFSChangePasswordKey': b'ChangePassword'.decode("utf-8"), 'kNetFSUseGuestKey': b'Guest'.decode("utf-8"), 'kNetFSUseAuthenticationInfoKey': b'UseAuthenticationInfo'.decode("utf-8"), 'kNetFSPathKey': b'Path'.decode("utf-8"), 'kNetFSSupportsChangePasswordKey': b'SupportsChangePassword'.decode("utf-8"), 'kNetFSNoUserPreferencesKey': b'NoUserPreferences'.decode("utf-8"), 'kNetFSForceNewSessionKey': b'ForceNewSession'.decode("utf-8"), 'kNAUIOptionKey': b'UIOption'.decode("utf-8"), 'kNetFSConnectedAsGuestKey': b'MountedByGuest'.decode("utf-8"), 'kNetFSConnectedWithAuthenticationInfoKey': b'ConnectedWithAuthenticationInfo'.decode("utf-8"), 'kNetFSDisplayNameKey': b'DisplayName'.decode("utf-8"), 'kNetFSAlternatePortKey': b'AlternatePort'.decode("utf-8"), 'kNetFSAllowLoopbackKey': b'AllowLoopback'.decode("utf-8"), 'kNetFSMountedURLKey': b'MountedURL'.decode("utf-8"), 'kNetFSGuestOnlyKey': b'GuestOnly'.decode("utf-8"), 'kNetFSAllowSubMountsKey': b'AllowSubMounts'.decode("utf-8"), 'kNetFSUserNameKey': b'UserName'.decode("utf-8"), 'kNetFSIsHiddenKey': b'IsHidden'.decode("utf-8")})
functions={'NetFSMountURLProbe': (b'^{__CFString=}^{__CFString=}',), 'NetFSMountURLAsync': (b'i^{__CFURL=}^{__CFURL=}^{__CFString=}^{__CFString=}^{__CFDictionary=}^{__CFDictionary=}^^v^{dispatch_queue_s=}@?', '', {'arguments': {8: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': '^v'}, 1: {'type': 'i'}, 2: {'type': '^v'}, 3: {'type': '@'}}}}, 6: {'type_modifier': 'o'}}}), 'NetFSMountURLSync': (b'i^{__CFURL=}^{__CFURL=}^{__CFString=}^{__CFString=}^{__CFDictionary=}^{__CFDictionary=}^^{__CFArray=}', '', {'arguments': {6: {'type_modifier': 'o'}}}), 'NetFSMountURLCancel': (b'i^v',), 'NetFSCopyURLForRemountingVolume': (b'^{__CFURL=}^{__CFURL=}', '', {'retval': {'already_cfretained': True}}), 'NetFSCFStringtoCString': (b'^t^{__CFString=}', '', {'retval': {'c_array_delimited_by_null': True}})}
expressions = {}

# END OF FILE
