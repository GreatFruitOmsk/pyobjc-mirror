import os
import sys
from distutils.util import spawn
from distutils.version import LooseVersion
from distutils.dir_util import mkpath
try:
    set
except NameError:
    from sets import Set as set

def adminperms(src, verbose=0, dry_run=0):
    try:
        spawn(['/usr/bin/chgrp', '-R', 'admin', src])
        spawn(['/bin/chmod', '-R', 'g+w', src])
    except:
        return False
    return True

def mkbom(src, pkgdir, verbose=0, dry_run=0, TOOL='/usr/bin/mkbom'):
    """
    Create a bill-of-materials (BOM) for the given src directory and store it
    to the given pkg directory
    """
    dest = os.path.join(pkgdir, 'Contents', 'Archive.bom')
    mkpath(os.path.dirname(dest), verbose=verbose, dry_run=dry_run)
    spawn([TOOL, src, dest], verbose=verbose, dry_run=dry_run)

def pax(src, pkgdir, verbose=0, dry_run=0, TOOL='/bin/pax'):
    """
    Create a pax gzipped cpio archive of the given src directory and store it
    to the given pkg directory

    returns size of archive
    """
    dest = os.path.realpath(os.path.join(pkgdir, 'Contents', 'Archive.pax.gz'))
    mkpath(os.path.dirname(dest), verbose=verbose, dry_run=dry_run)
    pwd = os.path.realpath(os.getcwd())
    os.chdir(src)
    try:
        spawn([TOOL, '-w', '-f', dest, '-x', 'cpio', '-z', '.'])
    finally:
        os.chdir(pwd)
    return os.stat(dest).st_size

def unicode_path(path, encoding=sys.getfilesystemencoding()):
    if isinstance(path, unicode):
        return path
    return unicode(path, encoding)

def walk_files(path):
    for root, dirs, files in os.walk(path):
        for fn in files:
            yield os.path.join(root, fn)

def get_gid(name):
    for line in os.popen('/usr/bin/nidump group .'):
        fields = line.split(':')
        if fields[0] == name:
            return int(fields[2])
    raise ValueError, 'group %s not found' % (name,)

def find_root(path, base='/'):
    """
    Return the list of files, the archive directory, and the destination path
    """
    files = list(walk_files(path))
    common = os.path.dirname(os.path.commonprefix(files))
    prefix = os.path.join(base, common[len(os.path.join(path, '')):])
    #while not os.path.exists(prefix):
    #    common = os.path.dirname(common)
    #    prefix = os.path.dirname(prefix)
    prefix = os.path.realpath(prefix)
    return files, common, prefix

def admin_writable(path):
    gid = get_gid('admin')
    while not os.path.exists(path):
        path = os.path.dirname(path)
    s = os.stat(path)
    mode = s.st_mode
    return (mode & 00002) or (s.st_gid == gid and mode & 00020)

def reduce_size(files):
    return sum([os.stat(fn).st_size for fn in files])
