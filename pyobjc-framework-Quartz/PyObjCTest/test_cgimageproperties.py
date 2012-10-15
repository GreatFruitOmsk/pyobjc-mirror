
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str

class TestCGImageProperties (TestCase):

    def testConstants(self):
        self.assertIsInstance(kCGImagePropertyTIFFDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyGIFDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyJFIFDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyExifDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyPNGDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyRawDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFDictionary, unicode)

    
        self.assertIsInstance(kCGImagePropertyFileSize, unicode)
        self.assertIsInstance(kCGImagePropertyPixelHeight, unicode)
        self.assertIsInstance(kCGImagePropertyPixelWidth, unicode)
        self.assertIsInstance(kCGImagePropertyDPIHeight, unicode)
        self.assertIsInstance(kCGImagePropertyDPIWidth, unicode)
        self.assertIsInstance(kCGImagePropertyDepth, unicode)
        self.assertIsInstance(kCGImagePropertyOrientation, unicode)
        self.assertIsInstance(kCGImagePropertyIsFloat, unicode)
        self.assertIsInstance(kCGImagePropertyIsIndexed, unicode)
        self.assertIsInstance(kCGImagePropertyHasAlpha, unicode)
        self.assertIsInstance(kCGImagePropertyColorModel, unicode)
        self.assertIsInstance(kCGImagePropertyProfileName, unicode)
        self.assertIsInstance(kCGImagePropertyColorModelRGB, unicode)
        self.assertIsInstance(kCGImagePropertyColorModelGray, unicode)
        self.assertIsInstance(kCGImagePropertyColorModelCMYK, unicode)
        self.assertIsInstance(kCGImagePropertyColorModelLab, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFCompression, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFPhotometricInterpretation, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFDocumentName, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFImageDescription, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFMake, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFModel, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFOrientation, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFXResolution, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFYResolution, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFResolutionUnit, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFSoftware, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFTransferFunction, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFDateTime, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFArtist, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFHostComputer, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFCopyright, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFWhitePoint, unicode)
        self.assertIsInstance(kCGImagePropertyTIFFPrimaryChromaticities, unicode)
        self.assertIsInstance(kCGImagePropertyJFIFVersion, unicode)
        self.assertIsInstance(kCGImagePropertyJFIFXDensity, unicode)
        self.assertIsInstance(kCGImagePropertyJFIFYDensity, unicode)
        self.assertIsInstance(kCGImagePropertyJFIFDensityUnit, unicode)
        self.assertIsInstance(kCGImagePropertyJFIFIsProgressive, unicode)
        self.assertIsInstance(kCGImagePropertyExifExposureTime, unicode)
        self.assertIsInstance(kCGImagePropertyExifFNumber, unicode)
        self.assertIsInstance(kCGImagePropertyExifExposureProgram, unicode)
        self.assertIsInstance(kCGImagePropertyExifSpectralSensitivity, unicode)
        self.assertIsInstance(kCGImagePropertyExifISOSpeedRatings, unicode)
        self.assertIsInstance(kCGImagePropertyExifOECF, unicode)
        self.assertIsInstance(kCGImagePropertyExifVersion, unicode)
        self.assertIsInstance(kCGImagePropertyExifDateTimeOriginal, unicode)
        self.assertIsInstance(kCGImagePropertyExifDateTimeDigitized, unicode)
        self.assertIsInstance(kCGImagePropertyExifComponentsConfiguration, unicode)
        self.assertIsInstance(kCGImagePropertyExifCompressedBitsPerPixel, unicode)
        self.assertIsInstance(kCGImagePropertyExifShutterSpeedValue, unicode)
        self.assertIsInstance(kCGImagePropertyExifApertureValue, unicode)
        self.assertIsInstance(kCGImagePropertyExifBrightnessValue, unicode)
        self.assertIsInstance(kCGImagePropertyExifExposureBiasValue, unicode)
        self.assertIsInstance(kCGImagePropertyExifMaxApertureValue, unicode)
        self.assertIsInstance(kCGImagePropertyExifSubjectDistance, unicode)
        self.assertIsInstance(kCGImagePropertyExifMeteringMode, unicode)
        self.assertIsInstance(kCGImagePropertyExifLightSource, unicode)
        self.assertIsInstance(kCGImagePropertyExifFlash, unicode)
        self.assertIsInstance(kCGImagePropertyExifFocalLength, unicode)
        self.assertIsInstance(kCGImagePropertyExifSubjectArea, unicode)
        self.assertIsInstance(kCGImagePropertyExifMakerNote, unicode)
        self.assertIsInstance(kCGImagePropertyExifUserComment, unicode)
        self.assertIsInstance(kCGImagePropertyExifSubsecTime, unicode)
        self.assertIsInstance(kCGImagePropertyExifSubsecTimeOrginal, unicode)
        self.assertIsInstance(kCGImagePropertyExifSubsecTimeDigitized, unicode)
        self.assertIsInstance(kCGImagePropertyExifFlashPixVersion, unicode)
        self.assertIsInstance(kCGImagePropertyExifColorSpace, unicode)
        self.assertIsInstance(kCGImagePropertyExifPixelXDimension, unicode)
        self.assertIsInstance(kCGImagePropertyExifPixelYDimension, unicode)
        self.assertIsInstance(kCGImagePropertyExifRelatedSoundFile, unicode)
        self.assertIsInstance(kCGImagePropertyExifFlashEnergy, unicode)
        self.assertIsInstance(kCGImagePropertyExifSpatialFrequencyResponse, unicode)
        self.assertIsInstance(kCGImagePropertyExifFocalPlaneXResolution, unicode)
        self.assertIsInstance(kCGImagePropertyExifFocalPlaneYResolution, unicode)
        self.assertIsInstance(kCGImagePropertyExifFocalPlaneResolutionUnit, unicode)
        self.assertIsInstance(kCGImagePropertyExifSubjectLocation, unicode)
        self.assertIsInstance(kCGImagePropertyExifExposureIndex, unicode)
        self.assertIsInstance(kCGImagePropertyExifSensingMethod, unicode)
        self.assertIsInstance(kCGImagePropertyExifFileSource, unicode)
        self.assertIsInstance(kCGImagePropertyExifSceneType, unicode)
        self.assertIsInstance(kCGImagePropertyExifCFAPattern, unicode)
        self.assertIsInstance(kCGImagePropertyExifCustomRendered, unicode)
        self.assertIsInstance(kCGImagePropertyExifExposureMode, unicode)
        self.assertIsInstance(kCGImagePropertyExifWhiteBalance, unicode)
        self.assertIsInstance(kCGImagePropertyExifDigitalZoomRatio, unicode)
        self.assertIsInstance(kCGImagePropertyExifFocalLenIn35mmFilm, unicode)
        self.assertIsInstance(kCGImagePropertyExifSceneCaptureType, unicode)
        self.assertIsInstance(kCGImagePropertyExifGainControl, unicode)
        self.assertIsInstance(kCGImagePropertyExifContrast, unicode)
        self.assertIsInstance(kCGImagePropertyExifSaturation, unicode)
        self.assertIsInstance(kCGImagePropertyExifSharpness, unicode)
        self.assertIsInstance(kCGImagePropertyExifDeviceSettingDescription, unicode)
        self.assertIsInstance(kCGImagePropertyExifSubjectDistRange, unicode)
        self.assertIsInstance(kCGImagePropertyExifImageUniqueID, unicode)
        self.assertIsInstance(kCGImagePropertyExifGamma, unicode)
        self.assertIsInstance(kCGImagePropertyGIFLoopCount, unicode)
        self.assertIsInstance(kCGImagePropertyGIFDelayTime, unicode)
        self.assertIsInstance(kCGImagePropertyGIFImageColorMap, unicode)
        self.assertIsInstance(kCGImagePropertyGIFHasGlobalColorMap, unicode)
        self.assertIsInstance(kCGImagePropertyPNGGamma, unicode)
        self.assertIsInstance(kCGImagePropertyPNGInterlaceType, unicode)
        self.assertIsInstance(kCGImagePropertyPNGXPixelsPerMeter, unicode)
        self.assertIsInstance(kCGImagePropertyPNGYPixelsPerMeter, unicode)
        self.assertIsInstance(kCGImagePropertyPNGsRGBIntent, unicode)
        self.assertIsInstance(kCGImagePropertyPNGChromaticities, unicode)
        self.assertIsInstance(kCGImagePropertyGPSVersion, unicode)
        self.assertIsInstance(kCGImagePropertyGPSLatitudeRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSLatitude, unicode)
        self.assertIsInstance(kCGImagePropertyGPSLongitudeRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSLongitude, unicode)
        self.assertIsInstance(kCGImagePropertyGPSAltitudeRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSAltitude, unicode)
        self.assertIsInstance(kCGImagePropertyGPSTimeStamp, unicode)
        self.assertIsInstance(kCGImagePropertyGPSSatellites, unicode)
        self.assertIsInstance(kCGImagePropertyGPSStatus, unicode)
        self.assertIsInstance(kCGImagePropertyGPSMeasureMode, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDOP, unicode)
        self.assertIsInstance(kCGImagePropertyGPSSpeedRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSSpeed, unicode)
        self.assertIsInstance(kCGImagePropertyGPSTrackRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSTrack, unicode)
        self.assertIsInstance(kCGImagePropertyGPSImgDirectionRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSImgDirection, unicode)
        self.assertIsInstance(kCGImagePropertyGPSMapDatum, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestLatitudeRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestLatitude, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestLongitudeRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestLongitude, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestBearingRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestBearing, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestDistanceRef, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDestDistance, unicode)
        self.assertIsInstance(kCGImagePropertyGPSProcessingMethod, unicode)
        self.assertIsInstance(kCGImagePropertyGPSAreaInformation, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDateStamp, unicode)
        self.assertIsInstance(kCGImagePropertyGPSDifferental, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCObjectTypeReference, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCObjectAttributeReference, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCObjectName, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCEditStatus, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCEditorialUpdate, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCUrgency, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCSubjectReference, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCCategory, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCSupplementalCategory, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCFixtureIdentifier, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCKeywords, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContentLocationCode, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContentLocationName, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCReleaseDate, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCReleaseTime, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCExpirationDate, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCExpirationTime, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCSpecialInstructions, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCActionAdvised, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCReferenceService, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCReferenceDate, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCReferenceNumber, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCDateCreated, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCTimeCreated, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCDigitalCreationDate, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCDigitalCreationTime, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCOriginatingProgram, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCProgramVersion, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCObjectCycle, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCByline, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCBylineTitle, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCCity, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCSubLocation, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCProvinceState, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCCountryPrimaryLocationCode, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCCountryPrimaryLocationName, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCOriginalTransmissionReference, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCHeadline, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCCredit, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCSource, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCCopyrightNotice, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContact, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCCaptionAbstract, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCWriterEditor, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCImageType, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCImageOrientation, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCLanguageIdentifier, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCStarRating, unicode)



    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCGImagePropertyMakerCanonDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonDictionary, unicode)
        self.assertIsInstance(kCGImageProperty8BIMDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyDNGDictionary, unicode)
        self.assertIsInstance(kCGImageProperty8BIMLayerNames, unicode)
        self.assertIsInstance(kCGImagePropertyDNGVersion, unicode)
        self.assertIsInstance(kCGImagePropertyDNGBackwardVersion, unicode)
        self.assertIsInstance(kCGImagePropertyDNGUniqueCameraModel, unicode)
        self.assertIsInstance(kCGImagePropertyDNGLocalizedCameraModel, unicode)
        self.assertIsInstance(kCGImagePropertyDNGCameraSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyDNGLensInfo, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFDescription, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFFirmware, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFOwnerName, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFImageName, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFImageFileName, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFReleaseMethod, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFReleaseTiming, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFRecordID, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFSelfTimingTime, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFCameraSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFImageSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFContinuousDrive, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFFocusMode, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFMeteringMode, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFShootingMode, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFLensModel, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFLensMaxMM, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFLensMinMM, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFWhiteBalanceIndex, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFFlashExposureComp, unicode)
        self.assertIsInstance(kCGImagePropertyCIFFMeasuredEV, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonISOSetting, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonColorMode, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonQuality, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonWhiteBalanceMode, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonSharpenMode, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonFocusMode, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonFlashSetting, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonISOSelection, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonFlashExposureComp, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonImageAdjustment, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonLensAdapter, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonLensType, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonLensInfo, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonFocusDistance, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonDigitalZoom, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonShootingMode, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonCameraSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyMakerNikonShutterCount, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonOwnerName, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonCameraSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonImageSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonFlashExposureComp, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonContinuousDrive, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonLensModel, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonFirmware, unicode)
        self.assertIsInstance(kCGImagePropertyMakerCanonAspectRatioInfo, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxLensInfo, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxLensModel, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxLensID, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxLensSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxImageNumber, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxFlashCompensation, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxOwnerName, unicode)
        self.assertIsInstance(kCGImagePropertyExifAuxFirmware, unicode)
        self.assertIsInstance(kCGImagePropertyMakerMinoltaDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyMakerFujiDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyMakerOlympusDictionary, unicode)
        self.assertIsInstance(kCGImagePropertyMakerPentaxDictionary, unicode)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCGImagePropertyIPTCCreatorContactInfo, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCRightsUsageTerms, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCScene, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoCity, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoCountry, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoAddress, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoPostalCode, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoStateProvince, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoEmails, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoPhones, unicode)
        self.assertIsInstance(kCGImagePropertyIPTCContactInfoWebURLs, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kCGImagePropertyExifCameraOwnerName, unicode)
        self.assertIsInstance(kCGImagePropertyExifBodySerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyExifLensSpecification, unicode)
        self.assertIsInstance(kCGImagePropertyExifLensMake, unicode)
        self.assertIsInstance(kCGImagePropertyExifLensModel, unicode)
        self.assertIsInstance(kCGImagePropertyExifLensSerialNumber, unicode)
        self.assertIsInstance(kCGImagePropertyGIFUnclampedDelayTime, unicode)
        self.assertIsInstance(kCGImagePropertyPNGAuthor, unicode)
        self.assertIsInstance(kCGImagePropertyPNGCopyright, unicode)
        self.assertIsInstance(kCGImagePropertyPNGCreationTime, unicode)
        self.assertIsInstance(kCGImagePropertyPNGDescription, unicode)
        self.assertIsInstance(kCGImagePropertyPNGModificationTime, unicode)
        self.assertIsInstance(kCGImagePropertyPNGSoftware, unicode)
        self.assertIsInstance(kCGImagePropertyPNGTitle, unicode)

if __name__ == "__main__":
    main()
