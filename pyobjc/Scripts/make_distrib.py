#!/usr/bin/env python

import sys
import getopt
import os
import buildpkg
import shutil

USAGE='Usage: %s [-p python | --with-python=%s] [-h|--help] [-o release-dir|--output-directory=release-dir]\n'%(
	sys.argv[0], sys.executable)

PYTHON=sys.executable
OUTPUTDIR='release-dir'

def package_version():
	fp = open('Modules/objc/pyobjc.h', 'r')  
	for ln in fp.readlines():
		if ln.startswith('#define OBJC_VERSION'):
			fp.close()
	return ln.split()[-1][1:-1]

	raise ValueError, "Version not found"


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
		OUTPUTDIR=value
	else:
		raise ValueError, "Unsupported option: %s=%s"%(key, value)

if not os.path.exists(OUTPUTDIR):
	try:
		os.mkdir(OUTPUTDIR)
	except os.error, msg:
		sys.stderr.write("%s: Cannot create %s: %s\n"%(
			sys.argv[0], OUTPUTDIR, msg))
		sys.exit(1)


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
	escquotes(PYTHON), escquotes(OUTPUTDIR), escquotes(basedir))
fd = os.popen("'%s' setup.py install --prefix='%s/package%s'"%(
	escquotes(PYTHON), escquotes(OUTPUTDIR), escquotes(basedir)), 'r')
for ln in fd.xreadlines():
	sys.stdout.write(ln)

print "Setting up developer templates"

basedir = '%s/package'%(OUTPUTDIR)
os.mkdir(os.path.join(basedir, 'Developer'))
os.mkdir(os.path.join(basedir, 'Developer', 'ProjectBuilder Extras'))
os.mkdir(os.path.join(basedir, 'Developer', 'ProjectBuilder Extras', 'Project Templates'))
os.mkdir(os.path.join(basedir, 'Developer', 'ProjectBuilder Extras', 'Project Templates', 'Application'))
shutil.copytree('Project Templates/Cocoa-Python Application', os.path.join(basedir, 'Developer', 'ProjectBuilder Extras', 'Project Templates', 'Application', 'Cocoa-Python Application'))

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
	Relocatable="NO")

print "Done, don't forget to test the output!"
