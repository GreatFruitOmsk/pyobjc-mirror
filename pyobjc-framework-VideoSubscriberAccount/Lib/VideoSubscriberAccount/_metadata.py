# This file is generated by objective.metadata
#
# Last update: Wed Jun  6 20:54:51 2018

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
enums = '''$VSSubscriptionAccessLevelFreeWithAccount@1$VSSubscriptionAccessLevelPaid@2$VSSubscriptionAccessLevelUnknown@0$'''
misc.update({})
expressions = {}

# END OF FILE
