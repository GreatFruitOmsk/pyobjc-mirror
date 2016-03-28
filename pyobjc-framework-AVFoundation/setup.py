'''
Wrappers for the "AVFoundation" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-AVFoundation',
    version=VERSION,
    description = "Wrappers for the framework AVFoundation on Mac OS X",
    long_description=__doc__,
    packages = [ "AVFoundation" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
        'pyobjc-framework-Quartz>=' + VERSION,
    ],
    min_os_level="10.7",
    ext_modules = [
        Extension('AVFoundation._inlines',
            [ 'Modules/_AVFoundation_inlines.m' ],
            extra_link_args=['-framework', 'AVFoundation']),
        Extension("AVFoundation._AVFoundation",
            [ "Modules/_AVFoundation.m" ],
            extra_link_args=["-framework", "AVFoundation"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_AVFoundation')
            ]
        ),
    ],
)
