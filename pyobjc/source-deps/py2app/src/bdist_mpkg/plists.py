import os
import sys
from plistlib import Plist
from distutils.version import LooseVersion
import tools

def common_info(name, version):
    # Keys that can appear in any package
    name, version = unicode(name), LooseVersion(version)
    return dict(
        CFBundleGetInfoString=u'%s %s' % (name, version.vstring),
        CFBundleIdentifier=u'org.pythonmac.unspecified.%s' % (name,),
        CFBundleName=name,
        CFBundleShortVersionString=version.vstring,
        IFMajorVersion=version.version[0],
        IFMinorRevision=version.version[1],
        IFPkgFormatVersion=0.10000000149011612,
        IFRequirementDicts=[path_requirement(u'/')],
    )
    return defaults

def pkg_info(name, version):
    d = common_info(name, version)
    # Keys that can only appear in single packages
    d.update(dict(
        IFPkgFlagAllowBackRev=False,
        IFPkgFlagAuthorizationAction=u'AdminAuthorization',
        IFPkgFlagDefaultLocation=u'/Library/Python/2.3',
        IFPkgFlagFollowLinks=True,
        IFPkgFlagInstallFat=False,
        IFPkgFlagIsRequired=False,
        IFPkgFlagOverwritePermissions=False,
        IFPkgFlagRelocatable=False,
        IFPkgFlagRestartAction=u'NoRestart',
        IFPkgFlagRootVolumeOnly=True,
        IFPkgFlagUpdateInstalledLangauges=False,
    ))
    return d

def path_requirement(SpecArgument, Level=u'requires', **kw):
    return dict(
        Level=Level,
        SpecType=u'file',
        SpecArgument=tools.unicode_path(SpecArgument),
        **kw
    )

FRIENDLY_PREFIX = {
    os.path.expanduser(u'~/Library/Frameworks') : u'User',
    u'/System/Library/Frameworks' : u'Apple',
    u'/Library/Frameworks' : u'System',
    u'/opt/local' : u'DarwinPorts',
    u'/usr/local' : u'Unix',
    u'/sw' : u'Fink',
}

def python_requirement(pkgname, prefix=None, version=None, **kw):
    if prefix is None:
        prefix = sys.prefix
    if version is None:
        version = sys.version[:3]
    prefix = os.path.realpath(prefix)
    fmwkprefix = os.path.dirname(os.path.dirname(prefix))
    is_framework = fmwkprefix.endswith('.framework')
    if is_framework:
        dprefix = os.path.dirname(fmwkprefix)
    else:
        dprefix = prefix
    dprefix = tools.unicode_path(dprefix)
    name = u'%s Python %s' % (FRIENDLY_PREFIX.get(dprefix, dprefix), version)
    kw.setdefault('LabelKey', name)
    title = u'%s requires %s to install.' % (pkgname, name,)
    kw.setdefault('TitleKey', title)
    kw.setdefault('MessageKey', title)
    return path_requirement(prefix, **kw)

def mpkg_info(name, version, packages=[]):
    d = common_info(name, version)
    # Keys that can appear only in metapackages
    npackages = []
    for p in packages:
        items = getattr(p, 'items', None)
        if items is not None:
            p = dict(items())
        else:
            if isinstance(p, basestring):
                p = [p]
            p = dict(zip((u'IFPkgFlagPackageLocation',u'IFPkgFlagPackageSelection'), p))
        npackages.append(p)
    d.update(dict(
        IFPkgFlagComponentDirectory=u'./Contents/Packages',
        IFPkgFlagPackageList=npackages,
    ))
    return d

def checkpath_plugin(path):
    if not isinstance(path, unicode):
        path = unicode(path, encoding)
    return dict(
        searchPlugin=u'CheckPath',
        path=path,
    )

def common_description(name, version):
    name, version = unicode(name), LooseVersion(version)
    return dict(
        IFPkgDescriptionTitle=name,
        IFPkgDescriptionVersion=version.vstring,
    )

def write(dct, path):
    p = Plist()
    p.update(dct)
    p.write(path)
