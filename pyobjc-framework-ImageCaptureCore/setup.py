'''
Wrappers for the "ImageCaptureCore" framework on Mac OS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup
setup(
    name='pyobjc-framework-ImageCaptureCore',
    version="3.0.4",
    description = "Wrappers for the framework ImageCaptureCore on Mac OS X",
    long_description=__doc__,
    packages = [ "ImageCaptureCore" ],
    setup_requires = [
        'pyobjc-core>=3.0.4',
    ],
    install_requires = [
        'pyobjc-core>=3.0.4',
        'pyobjc-framework-Cocoa>=3.0.4',
    ],
)
