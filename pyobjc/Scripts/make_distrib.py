#!/usr/bin/env python

import sys
import getopt
import os
import errno
import buildpkg
import shutil

USAGE='Usage: %s [-p python | --with-python=%s] [-h|--help] [-o release-dir|--output-directory=release-dir]\n'%(
	sys.argv[0], sys.executable)

PYTHON=sys.executable

def package_version():
	fp = open('Modules/objc/pyobjc.h', 'r')  
	for ln in fp.readlines():
		if ln.startswith('#define OBJC_VERSION'):
			fp.close()
                        break
	return ln.split()[-1][1:-1]

	raise ValueError, "Version not found"

packageVersion = package_version()
if (len(packageVersion) < 3) or (len(packageVersion) > 7):
        raise ValueError, "Version 'found' (%s), but seems preposterously short or long." % packageVersion

BUILDDIR='release-dir'
OUTPUTDIR='release-dir/PyObjC-%s' % package_version()

def escquotes(val):
	return val.replace("'", "'\"'\"'")

try:
	opts, args = getopt.getopt(
		sys.argv[1:],
		'p:h?o:', ['with-python=', 'help', 'output-directory='])
except getopt.error, msg:
	sys.stderr.write('%s: %s\n'%(sys.argv[0], msg))
	sys.stderr.write(USAGE)
	sys.exit(1)

for key, value in opts:
	if key in [ '-h', '-?', '--help' ]:
		sys.stdout.write(USAGE)
		sys.exit(0)
	elif key in [ '-p', '--with-python' ]:
		PYTHON=value
	elif key in [ '-o', '--output-directory' ]:
		BUILDDIR=value
	else:
		raise ValueError, "Unsupported option: %s=%s"%(key, value)

def makeDir(basedir, *path):
        base = basedir
        for p in path:
                base = os.path.join(base, p)
                try:
                        os.mkdir(base)
                except OSError, e:
                        if e.errno <> errno.EEXIST: raise


if not os.path.exists(BUILDDIR):
        apply(makeDir, ["."] + BUILDDIR.split(os.sep))

if not os.path.exists(OUTPUTDIR):
        apply(makeDir, ["."] + OUTPUTDIR.split(os.sep))


if PYTHON==sys.executable:
	PYTHONVER='.'.join(map(str, sys.version_info[:2]))
	PYTHONPATH=sys.path
else:
	fd = os.popen("'%s' -c 'import sys;print \".\".join(map(str, sys.version_info[:2]))'"%(
		escquotes(PYTHON)))
	PYTHONVER=fd.readline().strip()
	fd = os.popen("'%s' -c 'import sys;print \"\\n\".join(sys.path)'"%(
		escquotes(PYTHON)))
	PYTHONPATH=map(lambda x:x[:-1], fd.readlines())


basedir = ''
for p in PYTHONPATH:
	if p.endswith('lib/python%s'%PYTHONVER):
		basedir = os.path.split(os.path.split(p)[0])[0]
		break

if not basedir:
	sys.stderr.write("%s: Cannot determine basedir\n"%(sys.argv[0]))
	sys.exit(1)

print "Running: '%s' setup.py sdist -d '%s'"%(
			escquotes(PYTHON), escquotes(OUTPUTDIR))
fd = os.popen("'%s' setup.py sdist -d '%s'"%(
			escquotes(PYTHON), escquotes(OUTPUTDIR)), 'r')
for ln in fd.xreadlines():
	sys.stdout.write(ln)

print "Running: '%s' setup.py install --prefix='%s/package%s'"%(
	escquotes(PYTHON), escquotes(BUILDDIR), escquotes(basedir))
fd = os.popen("'%s' setup.py install --prefix='%s/package%s'"%(
	escquotes(PYTHON), escquotes(BUILDDIR), escquotes(basedir)), 'r')
for ln in fd.xreadlines():
	sys.stdout.write(ln)

print "Copying readme and license"
shutil.copyfile("ReadMe.txt", os.path.join(OUTPUTDIR, "ReadMe.txt"))
shutil.copyfile("License.txt", os.path.join(OUTPUTDIR, "License.txt"))
shutil.copyfile("ChangeLog", os.path.join(OUTPUTDIR, "ChangeLog"))

print "Setting up developer templates"

nastyFiles = ['.DS_Store', '.gdb_history']
def killNasties(irrelevant, dirName, names):
        for aName in names:
                if aName in nastyFiles:
                        os.remove( os.path.join(dirName, aName) )
        if dirName.find(".pbproj") > 0:
                for aName in names:
                        if aName.find(".pbxuser") > 0:
                                os.remove( os.path.join(dirName, aName) )
	if dirName[-3:] == 'CVS':
		while len(names): del names[0]
		shutil.rmtree(dirName)

basedir = '%s/package'%(BUILDDIR)

makeDir(basedir, 'Developer', 'ProjectBuilder Extras', 'Project Templates', 'Application')
templateDestination = os.path.join(basedir, 'Developer', 'ProjectBuilder Extras',
                                   'Project Templates', 'Application', 'Cocoa-Python Application')
shutil.copytree('Project Templates/Cocoa-Python Application', templateDestination)

print "Setting up developer examples"

makeDir(basedir, 'Developer', 'Examples')
examplesDestination = os.path.join(basedir, 'Developer', 'Examples', 'PyObjC')
shutil.copytree('Examples', examplesDestination)

print "Setting up some documentation"
makeDir(basedir, 'Developer', 'Documentation')
docsDestination = os.path.join(basedir, 'Developer', 'Documentation', 'PyObjC')
shutil.copytree('Doc', docsDestination)

os.path.walk(templateDestination, killNasties, None)
os.path.walk(examplesDestination, killNasties, None)
os.path.walk(docsDestination, killNasties, None)

print 'Building package'
pm = buildpkg.PackageMaker('PyObjC', package_version(), 
"""\
Python <-> Objective-C bridge that supports building full featured Cocoa
applications.
""")
pm.build(os.path.join(basedir), 
	resources=os.path.join(os.getcwd(), 'Installer Package', 'Resources'),
	OutputDir=os.path.join(os.getcwd(), OUTPUTDIR),
	Version=package_version(),
	NeedsAuthorization="YES",
	Relocatable="NO",
        RootVolumeOnly="YES")

print "Done, don't forget to test the output!"
