from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNTypes (TestCase):
        def testConstants(self):
            self.assertEqual(Vision.VNImageCropAndScaleOptionCenterCrop, 0)
            self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFit, 1)
            self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFill, 2)

        @min_os_level('10.13')
        def testConstants10_13(self):
            self.assertIsInstance(Vision.VNBarcodeSymbologyAztec, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyCODE39, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyCODE39Checksum, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyCODE39FullASCII, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyCODE39FullASCIIChecksum, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyCODE93, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyCODE93i, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyCODE128, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyDataMatrix, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyEAN8, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyEAN13, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyI2OF5, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyI2OF5Checksum, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyITF14, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyPDF417, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyQR, unicode)
            self.assertIsInstance(Vision.VNBarcodeSymbologyUPCE, unicode)

if __name__ == "__main__":
    main()
