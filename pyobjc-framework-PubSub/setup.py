'''
Wrappers for the "PubSub" framework on MacOSX 10.5 or later.  This framework
offers developers a way to subscribe to web feeds (RSS, Atom) from their
applications.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

Note that this framework is deprecated in OSX 10.9
'''
from pyobjc_setup import setup

VERSION="3.2a1"

setup(
    min_os_level='10.5',
    name='pyobjc-framework-PubSub',
    version="3.3a0",
    description = "Wrappers for the framework PubSub on Mac OS X",
    long_description=__doc__,
    packages = [ "PubSub" ],
    setup_requires = [
        'pyobjc-core>=3.3a0',
    ],
    install_requires = [
        'pyobjc-core>=3.3a0',
        'pyobjc-framework-Cocoa>=3.3a0',
    ],
)
