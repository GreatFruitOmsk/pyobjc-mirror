''' 
Wrappers for framework 'SystemConfiguration'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension

setup(
    name='pyobjc-framework-SystemConfiguration',
    version="2.3",
    description = "Wrappers for the framework SystemConfiguration on Mac OS X",
    packages = [ "SystemConfiguration" ],
    install_requires = [ 
        'pyobjc-core>=2.3',
        'pyobjc-framework-Cocoa>=2.3',
    ],
    ext_modules = [
        Extension('SystemConfiguration._manual',
                 [ 'Modules/_manual.m' ],
        ),
    ],
)
