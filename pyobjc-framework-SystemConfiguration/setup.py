'''
Wrappers for framework 'SystemConfiguration'.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension

VERSION="3.2a1"

setup(
    name='pyobjc-framework-SystemConfiguration',
    version="3.2.1",
    description = "Wrappers for the framework SystemConfiguration on Mac OS X",
    long_description=__doc__,
    packages = [ "SystemConfiguration" ],
    setup_requires = [
        'pyobjc-core>=3.2.1',
    ],
    install_requires = [
        'pyobjc-core>=3.2.1',
        'pyobjc-framework-Cocoa>=3.2.1',
    ],
    ext_modules = [
        Extension('SystemConfiguration._manual',
                 [ 'Modules/_manual.m' ],
        ),
    ],
)
