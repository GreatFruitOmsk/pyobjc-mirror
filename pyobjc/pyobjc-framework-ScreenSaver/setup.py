''' 
Wrappers for framework 'ScreenSaver'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension
try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-ScreenSaver',
    version='2.2b2',
    description = "Wrappers for the framework ScreenSaver on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "ScreenSaver" ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.2b1',
        'pyobjc-framework-Cocoa>=2.2b1',
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    ext_modules = [
        Extension('ScreenSaver._inlines',
            [ 'Modules/_ScreenSaver_inlines.m' ],
            extra_link_args=['-framework', 'ScreenSaver']),
    ],
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('ScreenSaver'),
    zip_safe = False,
)
