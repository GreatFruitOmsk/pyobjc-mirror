# This file is generated by objective.metadata
#
# Last update: Mon Sep 24 11:18:48 2012

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$$'''
enums = '''$$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSServerNotificationCenter', b'addObserver:selector:name:object:', {'arguments': {3: {'type': ':', 'sel_of_type': b'v@:@'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
