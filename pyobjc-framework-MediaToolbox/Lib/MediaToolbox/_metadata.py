# This file is generated by objective.metadata
#
# Last update: Tue Sep  4 22:31:30 2018

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
enums = '''$kMTAudioProcessingTapCallbacksVersion_0@0$kMTAudioProcessingTapCreationFlag_PostEffects@2$kMTAudioProcessingTapCreationFlag_PreEffects@1$kMTAudioProcessingTapFlag_EndOfStream@512$kMTAudioProcessingTapFlag_StartOfStream@256$'''
misc.update({})
functions={'MTAudioProcessingTapGetSourceAudio': (sel32or64(b'l^{opaqueMTAudioProcessingTap=}l^{AudioBufferList=L[1{AudioBuffer=LL^v}]}^I^{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}^l', b'i^{opaqueMTAudioProcessingTap=}q^{AudioBufferList=I[1{AudioBuffer=II^v}]}^I^{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}^q'), '', {'arguments': {3: {'type_modifier': 'o'}, 4: {'type_modifier': 'o'}, 5: {'type_modifier': 'o'}}}), 'MTAudioProcessingTapGetTypeID': (sel32or64(b'L', b'Q'),), 'MTRegisterProfessionalVideoWorkflowFormatReaders': (b'v',), 'MTCopyLocalizedNameForMediaType': (sel32or64(b'^{__CFString=}L', b'^{__CFString=}I'), '', {'retval': {'already_cfretained': True}}), 'MTCopyLocalizedNameForMediaSubType': (sel32or64(b'^{__CFString=}LL', b'^{__CFString=}II'), '', {'retval': {'already_cfretained': True}})}
cftypes=[('MTAudioProcessingTapRef', b'^{opaqueMTAudioProcessingTap=}', 'MTAudioProcessingTapGetTypeID', None)]
expressions = {}

# END OF FILE
