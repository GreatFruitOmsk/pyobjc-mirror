'''
Wrappers for the "MapKit" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

setup(
    name='pyobjc-framework-MapKit',
    version="3.1",
    description = "Wrappers for the framework MapKit on Mac OS X",
    packages = [ "MapKit" ],
    setup_requires = [
        'pyobjc-core>=3.1',
    ],
    install_requires = [
        'pyobjc-core>=3.1',
        'pyobjc-framework-Cocoa>=3.1',
    ],
    min_os_level="10.9",
)
