from PyObjCTools.TestSupport import *

import AVFoundation

AVAudioEngineManualRenderingBlock = objc._C_NSInteger + objc._C_NSInteger + b'...' + b'o^@'


class TestAVAudioEngine (TestCase):
    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAudioEngine.startAndReturnError_, 0)
        self.assertResultIsBOOL(AVFoundation.AVAudioEngine.isRunning)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioEngine.isAutoShutdownEnabled)
        self.assertArgIsBOOL(AVFoundation.AVAudioEngine.setAutoShutdownEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVAudioEngine.enableManualRenderingMode_format_maximumFrameCount_error_)
        self.assertArgIsOut(AVFoundation.AVAudioEngine.enableManualRenderingMode_format_maximumFrameCount_error_, 3)

        self.assertArgIsOut(AVFoundation.AVAudioEngine.renderOffline_toBuffer_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAudioEngine.isInManualRenderingMode)

        self.assertResultIsBlock(AVFoundation.AVAudioEngine.manualRenderingBlock, AVAudioEngineManualRenderingBlock)

    @min_os_level('10.10')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVAudioEngineConfigurationChangeNotification, unicode)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingErrorInvalidMode, -80800)
        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingErrorInitialized, -80801)
        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingErrorNotRunning , -80802)

        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingStatusError, -1)
        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingStatusSuccess, 0)
        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingStatusInsufficientDataFromInputNode, 1)
        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingStatusCannotDoInCurrentContext, 2)

        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingModeOffline, 0)
        self.assertEqual(AVFoundation.AVAudioEngineManualRenderingModeRealtime, 1)



if __name__ == "__main__":
    main()
