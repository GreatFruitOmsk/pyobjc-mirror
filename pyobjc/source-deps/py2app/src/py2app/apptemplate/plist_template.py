import sys
__all__ = ['infoPlistDict']

def infoPlistDict(CFBundleExecutable, plist={}):
    CFBundleExecutable = unicode(CFBundleExecutable)
    version = sys.version[:3]
    pdict = dict(
        CFBundleDevelopmentRegion=u'English',
        CFBundleDisplayName=plist.get('CFBundleName', CFBundleExecutable),
        CFBundleExecutable=CFBundleExecutable,
        CFBundleIconFile=CFBundleExecutable,
        CFBundleIdentifier=u'org.pythonmac.unspecified.%s' % (u''.join(CFBundleExecutable.split()),),
        CFBundleInfoDictionaryVersion=u'6.0',
        CFBundleName=CFBundleExecutable,
        CFBundlePackageType=u'APPL',
        CFBundleShortVersionString=plist.get('CFBundleVersion', u'0.0'),
        CFBundleSignature=u'????',
        CFBundleVersion=u'0.0',
        LSHasLocalizedDisplayName=False,
        NSAppleScriptEnabled=False,
        NSHumanReadableCopyright=u'Copyright not specified',
        NSMainNibFile=u'MainMenu',
        NSPrincipalClass=u'NSApplication',
        PyMainFileNames=[u'__boot__'],
        PyResourcePackages=[
            u'Python',
            u'Python/lib-dynload',
            u'Python/site-packages',
            u'Python/site-packages.zip',
        ],
        PyRuntimeLocations=[(s % version) for s in [
            u'@executable_path/../Frameworks/Python.framework/Versions/%s/Python',
            u'~/Library/Frameworks/Python.framework/Versions/%s/Python',
            u'/Library/Frameworks/Python.framework/Versions/%s/Python',
            u'/Network/Library/Frameworks/Python.framework/Versions/%s/Python',
            u'/System/Library/Frameworks/Python.framework/Versions/%s/Python',
        ]],
    )
    pdict.update(plist)
    return pdict
