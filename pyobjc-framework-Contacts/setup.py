'''
Wrappers for the "Contacts" framework on MacOS X 10.11.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-Contacts',
    min_os_level='10.11',
    version="3.3a0",
    description = "Wrappers for the framework Contacts on Mac OS X",
    long_description=__doc__,
    packages = [ "Contacts" ],
    setup_requires = [
        'pyobjc-core>=3.3a0',
    ],
    install_requires = [
        'pyobjc-core>=3.3a0',
        'pyobjc-framework-Cocoa>=3.3a0',
    ],
    ext_modules = [
        Extension("Contacts._Contacts",
            [ "Modules/_Contacts.m" ],
            extra_link_args=["-framework", "Contacts"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_Contacts')
            ]
        ),
    ],
)
