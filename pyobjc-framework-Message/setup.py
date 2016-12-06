'''
Wrappers for the "Message" framework on MacOSX. This framework contains a
number of utilities for sending e-mail.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="3.2a1"

setup(
    name='pyobjc-framework-Message',
    version="3.2",
    description = "Wrappers for the framework Message on Mac OS X",
    long_description=__doc__,
    packages = [ "Message" ],
    setup_requires = [
        'pyobjc-core>=3.2',
    ],
    install_requires = [
        'pyobjc-core>=3.2',
        'pyobjc-framework-Cocoa>=3.2',
    ],
    max_os_level="10.8",
)
