# This file is generated by objective.metadata
#
# Last update: Wed Jun  6 09:48:44 2018

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
constants = '''$kCFErrorDomainCGImageMetadata@^{__CFString=}$kCGImageAuxiliaryDataInfoData$kCGImageAuxiliaryDataInfoDataDescription$kCGImageAuxiliaryDataInfoMetadata$kCGImageAuxiliaryDataTypeDepth$kCGImageAuxiliaryDataTypeDisparity$kCGImageAuxiliaryDataTypePortraitEffectsMatte$kCGImageDestinationBackgroundColor@^{__CFString=}$kCGImageDestinationDateTime@^{__CFString=}$kCGImageDestinationEmbedThumbnail@^{__CFString=}$kCGImageDestinationImageMaxPixelSize@^{__CFString=}$kCGImageDestinationLossyCompressionQuality@^{__CFString=}$kCGImageDestinationMergeMetadata@^{__CFString=}$kCGImageDestinationMetadata@^{__CFString=}$kCGImageDestinationOptimizeColorForSharing$kCGImageDestinationOrientation@^{__CFString=}$kCGImageMetadataEnumerateRecursively@^{__CFString=}$kCGImageMetadataNamespaceDublinCore@^{__CFString=}$kCGImageMetadataNamespaceExif@^{__CFString=}$kCGImageMetadataNamespaceExifAux@^{__CFString=}$kCGImageMetadataNamespaceExifEX@^{__CFString=}$kCGImageMetadataNamespaceIPTCCore@^{__CFString=}$kCGImageMetadataNamespaceIPTCExtension$kCGImageMetadataNamespacePhotoshop@^{__CFString=}$kCGImageMetadataNamespaceTIFF@^{__CFString=}$kCGImageMetadataNamespaceXMPBasic@^{__CFString=}$kCGImageMetadataNamespaceXMPRights@^{__CFString=}$kCGImageMetadataPrefixDublinCore@^{__CFString=}$kCGImageMetadataPrefixExif@^{__CFString=}$kCGImageMetadataPrefixExifAux@^{__CFString=}$kCGImageMetadataPrefixExifEX@^{__CFString=}$kCGImageMetadataPrefixIPTCCore@^{__CFString=}$kCGImageMetadataPrefixIPTCExtension$kCGImageMetadataPrefixPhotoshop@^{__CFString=}$kCGImageMetadataPrefixTIFF@^{__CFString=}$kCGImageMetadataPrefixXMPBasic@^{__CFString=}$kCGImageMetadataPrefixXMPRights@^{__CFString=}$kCGImageMetadataShouldExcludeGPS@^{__CFString=}$kCGImageMetadataShouldExcludeXMP@^{__CFString=}$kCGImageProperty8BIMDictionary@^{__CFString=}$kCGImageProperty8BIMLayerNames@^{__CFString=}$kCGImageProperty8BIMVersion@^{__CFString=}$kCGImagePropertyAPNGDelayTime@^{__CFString=}$kCGImagePropertyAPNGLoopCount@^{__CFString=}$kCGImagePropertyAPNGUnclampedDelayTime@^{__CFString=}$kCGImagePropertyAuxiliaryData$kCGImagePropertyAuxiliaryDataType$kCGImagePropertyBytesPerRow$kCGImagePropertyCIFFCameraSerialNumber@^{__CFString=}$kCGImagePropertyCIFFContinuousDrive@^{__CFString=}$kCGImagePropertyCIFFDescription@^{__CFString=}$kCGImagePropertyCIFFDictionary@^{__CFString=}$kCGImagePropertyCIFFFirmware@^{__CFString=}$kCGImagePropertyCIFFFlashExposureComp@^{__CFString=}$kCGImagePropertyCIFFFocusMode@^{__CFString=}$kCGImagePropertyCIFFImageFileName@^{__CFString=}$kCGImagePropertyCIFFImageName@^{__CFString=}$kCGImagePropertyCIFFImageSerialNumber@^{__CFString=}$kCGImagePropertyCIFFLensMaxMM@^{__CFString=}$kCGImagePropertyCIFFLensMinMM@^{__CFString=}$kCGImagePropertyCIFFLensModel@^{__CFString=}$kCGImagePropertyCIFFMeasuredEV@^{__CFString=}$kCGImagePropertyCIFFMeteringMode@^{__CFString=}$kCGImagePropertyCIFFOwnerName@^{__CFString=}$kCGImagePropertyCIFFRecordID@^{__CFString=}$kCGImagePropertyCIFFReleaseMethod@^{__CFString=}$kCGImagePropertyCIFFReleaseTiming@^{__CFString=}$kCGImagePropertyCIFFSelfTimingTime@^{__CFString=}$kCGImagePropertyCIFFShootingMode@^{__CFString=}$kCGImagePropertyCIFFWhiteBalanceIndex@^{__CFString=}$kCGImagePropertyColorModel@^{__CFString=}$kCGImagePropertyColorModelCMYK@^{__CFString=}$kCGImagePropertyColorModelGray@^{__CFString=}$kCGImagePropertyColorModelLab@^{__CFString=}$kCGImagePropertyColorModelRGB@^{__CFString=}$kCGImagePropertyDNGActiveArea$kCGImagePropertyDNGAnalogBalance$kCGImagePropertyDNGAntiAliasStrength$kCGImagePropertyDNGAsShotICCProfile$kCGImagePropertyDNGAsShotNeutral$kCGImagePropertyDNGAsShotPreProfileMatrix$kCGImagePropertyDNGAsShotProfileName$kCGImagePropertyDNGAsShotWhiteXY$kCGImagePropertyDNGBackwardVersion@^{__CFString=}$kCGImagePropertyDNGBaselineExposure$kCGImagePropertyDNGBaselineExposureOffset$kCGImagePropertyDNGBaselineNoise$kCGImagePropertyDNGBaselineSharpness$kCGImagePropertyDNGBayerGreenSplit$kCGImagePropertyDNGBestQualityScale$kCGImagePropertyDNGBlackLevel$kCGImagePropertyDNGBlackLevelDeltaH$kCGImagePropertyDNGBlackLevelDeltaV$kCGImagePropertyDNGBlackLevelRepeatDim$kCGImagePropertyDNGCFALayout$kCGImagePropertyDNGCFAPlaneColor$kCGImagePropertyDNGCalibrationIlluminant1$kCGImagePropertyDNGCalibrationIlluminant2$kCGImagePropertyDNGCameraCalibration1$kCGImagePropertyDNGCameraCalibration2$kCGImagePropertyDNGCameraCalibrationSignature$kCGImagePropertyDNGCameraSerialNumber@^{__CFString=}$kCGImagePropertyDNGChromaBlurRadius$kCGImagePropertyDNGColorMatrix1$kCGImagePropertyDNGColorMatrix2$kCGImagePropertyDNGColorimetricReference$kCGImagePropertyDNGCurrentICCProfile$kCGImagePropertyDNGCurrentPreProfileMatrix$kCGImagePropertyDNGDefaultBlackRender$kCGImagePropertyDNGDefaultCropOrigin$kCGImagePropertyDNGDefaultCropSize$kCGImagePropertyDNGDefaultScale$kCGImagePropertyDNGDefaultUserCrop$kCGImagePropertyDNGDictionary@^{__CFString=}$kCGImagePropertyDNGExtraCameraProfiles$kCGImagePropertyDNGFixVignetteRadial$kCGImagePropertyDNGForwardMatrix1$kCGImagePropertyDNGForwardMatrix2$kCGImagePropertyDNGLensInfo@^{__CFString=}$kCGImagePropertyDNGLinearResponseLimit$kCGImagePropertyDNGLinearizationTable$kCGImagePropertyDNGLocalizedCameraModel@^{__CFString=}$kCGImagePropertyDNGMakerNoteSafety$kCGImagePropertyDNGMaskedAreas$kCGImagePropertyDNGNewRawImageDigest$kCGImagePropertyDNGNoiseProfile$kCGImagePropertyDNGNoiseReductionApplied$kCGImagePropertyDNGOpcodeList1$kCGImagePropertyDNGOpcodeList2$kCGImagePropertyDNGOpcodeList3$kCGImagePropertyDNGOriginalBestQualityFinalSize$kCGImagePropertyDNGOriginalDefaultCropSize$kCGImagePropertyDNGOriginalDefaultFinalSize$kCGImagePropertyDNGOriginalRawFileData$kCGImagePropertyDNGOriginalRawFileDigest$kCGImagePropertyDNGOriginalRawFileName$kCGImagePropertyDNGPreviewApplicationName$kCGImagePropertyDNGPreviewApplicationVersion$kCGImagePropertyDNGPreviewColorSpace$kCGImagePropertyDNGPreviewDateTime$kCGImagePropertyDNGPreviewSettingsDigest$kCGImagePropertyDNGPreviewSettingsName$kCGImagePropertyDNGPrivateData$kCGImagePropertyDNGProfileCalibrationSignature$kCGImagePropertyDNGProfileCopyright$kCGImagePropertyDNGProfileEmbedPolicy$kCGImagePropertyDNGProfileHueSatMapData1$kCGImagePropertyDNGProfileHueSatMapData2$kCGImagePropertyDNGProfileHueSatMapDims$kCGImagePropertyDNGProfileHueSatMapEncoding$kCGImagePropertyDNGProfileLookTableData$kCGImagePropertyDNGProfileLookTableDims$kCGImagePropertyDNGProfileLookTableEncoding$kCGImagePropertyDNGProfileName$kCGImagePropertyDNGProfileToneCurve$kCGImagePropertyDNGRawDataUniqueID$kCGImagePropertyDNGRawImageDigest$kCGImagePropertyDNGRawToPreviewGain$kCGImagePropertyDNGReductionMatrix1$kCGImagePropertyDNGReductionMatrix2$kCGImagePropertyDNGRowInterleaveFactor$kCGImagePropertyDNGShadowScale$kCGImagePropertyDNGSubTileBlockSize$kCGImagePropertyDNGUniqueCameraModel@^{__CFString=}$kCGImagePropertyDNGVersion@^{__CFString=}$kCGImagePropertyDNGWarpFisheye$kCGImagePropertyDNGWarpRectilinear$kCGImagePropertyDNGWhiteLevel$kCGImagePropertyDPIHeight@^{__CFString=}$kCGImagePropertyDPIWidth@^{__CFString=}$kCGImagePropertyDepth@^{__CFString=}$kCGImagePropertyExifApertureValue@^{__CFString=}$kCGImagePropertyExifAuxDictionary@^{__CFString=}$kCGImagePropertyExifAuxFirmware@^{__CFString=}$kCGImagePropertyExifAuxFlashCompensation@^{__CFString=}$kCGImagePropertyExifAuxImageNumber@^{__CFString=}$kCGImagePropertyExifAuxLensID@^{__CFString=}$kCGImagePropertyExifAuxLensInfo@^{__CFString=}$kCGImagePropertyExifAuxLensModel@^{__CFString=}$kCGImagePropertyExifAuxLensSerialNumber@^{__CFString=}$kCGImagePropertyExifAuxOwnerName@^{__CFString=}$kCGImagePropertyExifAuxSerialNumber@^{__CFString=}$kCGImagePropertyExifBodySerialNumber@^{__CFString=}$kCGImagePropertyExifBrightnessValue@^{__CFString=}$kCGImagePropertyExifCFAPattern@^{__CFString=}$kCGImagePropertyExifCameraOwnerName@^{__CFString=}$kCGImagePropertyExifColorSpace@^{__CFString=}$kCGImagePropertyExifComponentsConfiguration@^{__CFString=}$kCGImagePropertyExifCompressedBitsPerPixel@^{__CFString=}$kCGImagePropertyExifContrast@^{__CFString=}$kCGImagePropertyExifCustomRendered@^{__CFString=}$kCGImagePropertyExifDateTimeDigitized@^{__CFString=}$kCGImagePropertyExifDateTimeOriginal@^{__CFString=}$kCGImagePropertyExifDeviceSettingDescription@^{__CFString=}$kCGImagePropertyExifDictionary@^{__CFString=}$kCGImagePropertyExifDigitalZoomRatio@^{__CFString=}$kCGImagePropertyExifExposureBiasValue@^{__CFString=}$kCGImagePropertyExifExposureIndex@^{__CFString=}$kCGImagePropertyExifExposureMode@^{__CFString=}$kCGImagePropertyExifExposureProgram@^{__CFString=}$kCGImagePropertyExifExposureTime@^{__CFString=}$kCGImagePropertyExifFNumber@^{__CFString=}$kCGImagePropertyExifFileSource@^{__CFString=}$kCGImagePropertyExifFlash@^{__CFString=}$kCGImagePropertyExifFlashEnergy@^{__CFString=}$kCGImagePropertyExifFlashPixVersion@^{__CFString=}$kCGImagePropertyExifFocalLenIn35mmFilm@^{__CFString=}$kCGImagePropertyExifFocalLength@^{__CFString=}$kCGImagePropertyExifFocalPlaneResolutionUnit@^{__CFString=}$kCGImagePropertyExifFocalPlaneXResolution@^{__CFString=}$kCGImagePropertyExifFocalPlaneYResolution@^{__CFString=}$kCGImagePropertyExifGainControl@^{__CFString=}$kCGImagePropertyExifGamma@^{__CFString=}$kCGImagePropertyExifISOSpeed@^{__CFString=}$kCGImagePropertyExifISOSpeedLatitudeyyy@^{__CFString=}$kCGImagePropertyExifISOSpeedLatitudezzz@^{__CFString=}$kCGImagePropertyExifISOSpeedRatings@^{__CFString=}$kCGImagePropertyExifImageUniqueID@^{__CFString=}$kCGImagePropertyExifLensMake@^{__CFString=}$kCGImagePropertyExifLensModel@^{__CFString=}$kCGImagePropertyExifLensSerialNumber@^{__CFString=}$kCGImagePropertyExifLensSpecification@^{__CFString=}$kCGImagePropertyExifLightSource@^{__CFString=}$kCGImagePropertyExifMakerNote@^{__CFString=}$kCGImagePropertyExifMaxApertureValue@^{__CFString=}$kCGImagePropertyExifMeteringMode@^{__CFString=}$kCGImagePropertyExifOECF@^{__CFString=}$kCGImagePropertyExifPixelXDimension@^{__CFString=}$kCGImagePropertyExifPixelYDimension@^{__CFString=}$kCGImagePropertyExifRecommendedExposureIndex@^{__CFString=}$kCGImagePropertyExifRelatedSoundFile@^{__CFString=}$kCGImagePropertyExifSaturation@^{__CFString=}$kCGImagePropertyExifSceneCaptureType@^{__CFString=}$kCGImagePropertyExifSceneType@^{__CFString=}$kCGImagePropertyExifSensingMethod@^{__CFString=}$kCGImagePropertyExifSensitivityType@^{__CFString=}$kCGImagePropertyExifSharpness@^{__CFString=}$kCGImagePropertyExifShutterSpeedValue@^{__CFString=}$kCGImagePropertyExifSpatialFrequencyResponse@^{__CFString=}$kCGImagePropertyExifSpectralSensitivity@^{__CFString=}$kCGImagePropertyExifStandardOutputSensitivity@^{__CFString=}$kCGImagePropertyExifSubjectArea@^{__CFString=}$kCGImagePropertyExifSubjectDistRange@^{__CFString=}$kCGImagePropertyExifSubjectDistance@^{__CFString=}$kCGImagePropertyExifSubjectLocation@^{__CFString=}$kCGImagePropertyExifSubsecTime@^{__CFString=}$kCGImagePropertyExifSubsecTimeDigitized@^{__CFString=}$kCGImagePropertyExifSubsecTimeOrginal@^{__CFString=}$kCGImagePropertyExifSubsecTimeOriginal$kCGImagePropertyExifUserComment@^{__CFString=}$kCGImagePropertyExifVersion@^{__CFString=}$kCGImagePropertyExifWhiteBalance@^{__CFString=}$kCGImagePropertyFileContentsDictionary$kCGImagePropertyFileSize@^{__CFString=}$kCGImagePropertyGIFDelayTime@^{__CFString=}$kCGImagePropertyGIFDictionary@^{__CFString=}$kCGImagePropertyGIFHasGlobalColorMap@^{__CFString=}$kCGImagePropertyGIFImageColorMap@^{__CFString=}$kCGImagePropertyGIFLoopCount@^{__CFString=}$kCGImagePropertyGIFUnclampedDelayTime@^{__CFString=}$kCGImagePropertyGPSAltitude@^{__CFString=}$kCGImagePropertyGPSAltitudeRef@^{__CFString=}$kCGImagePropertyGPSAreaInformation@^{__CFString=}$kCGImagePropertyGPSDOP@^{__CFString=}$kCGImagePropertyGPSDateStamp@^{__CFString=}$kCGImagePropertyGPSDestBearing@^{__CFString=}$kCGImagePropertyGPSDestBearingRef@^{__CFString=}$kCGImagePropertyGPSDestDistance@^{__CFString=}$kCGImagePropertyGPSDestDistanceRef@^{__CFString=}$kCGImagePropertyGPSDestLatitude@^{__CFString=}$kCGImagePropertyGPSDestLatitudeRef@^{__CFString=}$kCGImagePropertyGPSDestLongitude@^{__CFString=}$kCGImagePropertyGPSDestLongitudeRef@^{__CFString=}$kCGImagePropertyGPSDictionary@^{__CFString=}$kCGImagePropertyGPSDifferental@^{__CFString=}$kCGImagePropertyGPSHPositioningError@^{__CFString=}$kCGImagePropertyGPSImgDirection@^{__CFString=}$kCGImagePropertyGPSImgDirectionRef@^{__CFString=}$kCGImagePropertyGPSLatitude@^{__CFString=}$kCGImagePropertyGPSLatitudeRef@^{__CFString=}$kCGImagePropertyGPSLongitude@^{__CFString=}$kCGImagePropertyGPSLongitudeRef@^{__CFString=}$kCGImagePropertyGPSMapDatum@^{__CFString=}$kCGImagePropertyGPSMeasureMode@^{__CFString=}$kCGImagePropertyGPSProcessingMethod@^{__CFString=}$kCGImagePropertyGPSSatellites@^{__CFString=}$kCGImagePropertyGPSSpeed@^{__CFString=}$kCGImagePropertyGPSSpeedRef@^{__CFString=}$kCGImagePropertyGPSStatus@^{__CFString=}$kCGImagePropertyGPSTimeStamp@^{__CFString=}$kCGImagePropertyGPSTrack@^{__CFString=}$kCGImagePropertyGPSTrackRef@^{__CFString=}$kCGImagePropertyGPSVersion@^{__CFString=}$kCGImagePropertyHasAlpha@^{__CFString=}$kCGImagePropertyHeight$kCGImagePropertyIPTCActionAdvised@^{__CFString=}$kCGImagePropertyIPTCByline@^{__CFString=}$kCGImagePropertyIPTCBylineTitle@^{__CFString=}$kCGImagePropertyIPTCCaptionAbstract@^{__CFString=}$kCGImagePropertyIPTCCategory@^{__CFString=}$kCGImagePropertyIPTCCity@^{__CFString=}$kCGImagePropertyIPTCContact@^{__CFString=}$kCGImagePropertyIPTCContactInfoAddress@^{__CFString=}$kCGImagePropertyIPTCContactInfoCity@^{__CFString=}$kCGImagePropertyIPTCContactInfoCountry@^{__CFString=}$kCGImagePropertyIPTCContactInfoEmails@^{__CFString=}$kCGImagePropertyIPTCContactInfoPhones@^{__CFString=}$kCGImagePropertyIPTCContactInfoPostalCode@^{__CFString=}$kCGImagePropertyIPTCContactInfoStateProvince@^{__CFString=}$kCGImagePropertyIPTCContactInfoWebURLs@^{__CFString=}$kCGImagePropertyIPTCContentLocationCode@^{__CFString=}$kCGImagePropertyIPTCContentLocationName@^{__CFString=}$kCGImagePropertyIPTCCopyrightNotice@^{__CFString=}$kCGImagePropertyIPTCCountryPrimaryLocationCode@^{__CFString=}$kCGImagePropertyIPTCCountryPrimaryLocationName@^{__CFString=}$kCGImagePropertyIPTCCreatorContactInfo@^{__CFString=}$kCGImagePropertyIPTCCredit@^{__CFString=}$kCGImagePropertyIPTCDateCreated@^{__CFString=}$kCGImagePropertyIPTCDictionary@^{__CFString=}$kCGImagePropertyIPTCDigitalCreationDate@^{__CFString=}$kCGImagePropertyIPTCDigitalCreationTime@^{__CFString=}$kCGImagePropertyIPTCEditStatus@^{__CFString=}$kCGImagePropertyIPTCEditorialUpdate@^{__CFString=}$kCGImagePropertyIPTCExpirationDate@^{__CFString=}$kCGImagePropertyIPTCExpirationTime@^{__CFString=}$kCGImagePropertyIPTCExtAboutCvTerm$kCGImagePropertyIPTCExtAboutCvTermCvId$kCGImagePropertyIPTCExtAboutCvTermId$kCGImagePropertyIPTCExtAboutCvTermName$kCGImagePropertyIPTCExtAboutCvTermRefinedAbout$kCGImagePropertyIPTCExtAddlModelInfo$kCGImagePropertyIPTCExtArtworkCircaDateCreated$kCGImagePropertyIPTCExtArtworkContentDescription$kCGImagePropertyIPTCExtArtworkContributionDescription$kCGImagePropertyIPTCExtArtworkCopyrightNotice$kCGImagePropertyIPTCExtArtworkCopyrightOwnerID$kCGImagePropertyIPTCExtArtworkCopyrightOwnerName$kCGImagePropertyIPTCExtArtworkCreator$kCGImagePropertyIPTCExtArtworkCreatorID$kCGImagePropertyIPTCExtArtworkDateCreated$kCGImagePropertyIPTCExtArtworkLicensorID$kCGImagePropertyIPTCExtArtworkLicensorName$kCGImagePropertyIPTCExtArtworkOrObject$kCGImagePropertyIPTCExtArtworkPhysicalDescription$kCGImagePropertyIPTCExtArtworkSource$kCGImagePropertyIPTCExtArtworkSourceInvURL$kCGImagePropertyIPTCExtArtworkSourceInventoryNo$kCGImagePropertyIPTCExtArtworkStylePeriod$kCGImagePropertyIPTCExtArtworkTitle$kCGImagePropertyIPTCExtAudioBitrate$kCGImagePropertyIPTCExtAudioBitrateMode$kCGImagePropertyIPTCExtAudioChannelCount$kCGImagePropertyIPTCExtCircaDateCreated$kCGImagePropertyIPTCExtContainerFormat$kCGImagePropertyIPTCExtContainerFormatIdentifier$kCGImagePropertyIPTCExtContainerFormatName$kCGImagePropertyIPTCExtContributor$kCGImagePropertyIPTCExtContributorIdentifier$kCGImagePropertyIPTCExtContributorName$kCGImagePropertyIPTCExtContributorRole$kCGImagePropertyIPTCExtControlledVocabularyTerm$kCGImagePropertyIPTCExtCopyrightYear$kCGImagePropertyIPTCExtCreator$kCGImagePropertyIPTCExtCreatorIdentifier$kCGImagePropertyIPTCExtCreatorName$kCGImagePropertyIPTCExtCreatorRole$kCGImagePropertyIPTCExtDataOnScreen$kCGImagePropertyIPTCExtDataOnScreenRegion$kCGImagePropertyIPTCExtDataOnScreenRegionD$kCGImagePropertyIPTCExtDataOnScreenRegionH$kCGImagePropertyIPTCExtDataOnScreenRegionText$kCGImagePropertyIPTCExtDataOnScreenRegionUnit$kCGImagePropertyIPTCExtDataOnScreenRegionW$kCGImagePropertyIPTCExtDataOnScreenRegionX$kCGImagePropertyIPTCExtDataOnScreenRegionY$kCGImagePropertyIPTCExtDigitalImageGUID$kCGImagePropertyIPTCExtDigitalSourceFileType$kCGImagePropertyIPTCExtDigitalSourceType$kCGImagePropertyIPTCExtDopesheet$kCGImagePropertyIPTCExtDopesheetLink$kCGImagePropertyIPTCExtDopesheetLinkLink$kCGImagePropertyIPTCExtDopesheetLinkLinkQualifier$kCGImagePropertyIPTCExtEmbdEncRightsExpr$kCGImagePropertyIPTCExtEmbeddedEncodedRightsExpr$kCGImagePropertyIPTCExtEmbeddedEncodedRightsExprLangID$kCGImagePropertyIPTCExtEmbeddedEncodedRightsExprType$kCGImagePropertyIPTCExtEpisode$kCGImagePropertyIPTCExtEpisodeIdentifier$kCGImagePropertyIPTCExtEpisodeName$kCGImagePropertyIPTCExtEpisodeNumber$kCGImagePropertyIPTCExtEvent$kCGImagePropertyIPTCExtExternalMetadataLink$kCGImagePropertyIPTCExtFeedIdentifier$kCGImagePropertyIPTCExtGenre$kCGImagePropertyIPTCExtGenreCvId$kCGImagePropertyIPTCExtGenreCvTermId$kCGImagePropertyIPTCExtGenreCvTermName$kCGImagePropertyIPTCExtGenreCvTermRefinedAbout$kCGImagePropertyIPTCExtHeadline$kCGImagePropertyIPTCExtIPTCLastEdited$kCGImagePropertyIPTCExtLinkedEncRightsExpr$kCGImagePropertyIPTCExtLinkedEncodedRightsExpr$kCGImagePropertyIPTCExtLinkedEncodedRightsExprLangID$kCGImagePropertyIPTCExtLinkedEncodedRightsExprType$kCGImagePropertyIPTCExtLocationCity$kCGImagePropertyIPTCExtLocationCountryCode$kCGImagePropertyIPTCExtLocationCountryName$kCGImagePropertyIPTCExtLocationCreated$kCGImagePropertyIPTCExtLocationGPSAltitude$kCGImagePropertyIPTCExtLocationGPSLatitude$kCGImagePropertyIPTCExtLocationGPSLongitude$kCGImagePropertyIPTCExtLocationIdentifier$kCGImagePropertyIPTCExtLocationLocationId$kCGImagePropertyIPTCExtLocationLocationName$kCGImagePropertyIPTCExtLocationProvinceState$kCGImagePropertyIPTCExtLocationShown$kCGImagePropertyIPTCExtLocationSublocation$kCGImagePropertyIPTCExtLocationWorldRegion$kCGImagePropertyIPTCExtMaxAvailHeight$kCGImagePropertyIPTCExtMaxAvailWidth$kCGImagePropertyIPTCExtModelAge$kCGImagePropertyIPTCExtOrganisationInImageCode$kCGImagePropertyIPTCExtOrganisationInImageName$kCGImagePropertyIPTCExtPersonHeard$kCGImagePropertyIPTCExtPersonHeardIdentifier$kCGImagePropertyIPTCExtPersonHeardName$kCGImagePropertyIPTCExtPersonInImage$kCGImagePropertyIPTCExtPersonInImageCharacteristic$kCGImagePropertyIPTCExtPersonInImageCvTermCvId$kCGImagePropertyIPTCExtPersonInImageCvTermId$kCGImagePropertyIPTCExtPersonInImageCvTermName$kCGImagePropertyIPTCExtPersonInImageCvTermRefinedAbout$kCGImagePropertyIPTCExtPersonInImageDescription$kCGImagePropertyIPTCExtPersonInImageId$kCGImagePropertyIPTCExtPersonInImageName$kCGImagePropertyIPTCExtPersonInImageWDetails$kCGImagePropertyIPTCExtProductInImage$kCGImagePropertyIPTCExtProductInImageDescription$kCGImagePropertyIPTCExtProductInImageGTIN$kCGImagePropertyIPTCExtProductInImageName$kCGImagePropertyIPTCExtPublicationEvent$kCGImagePropertyIPTCExtPublicationEventDate$kCGImagePropertyIPTCExtPublicationEventIdentifier$kCGImagePropertyIPTCExtPublicationEventName$kCGImagePropertyIPTCExtRating$kCGImagePropertyIPTCExtRatingRatingRegion$kCGImagePropertyIPTCExtRatingRegionCity$kCGImagePropertyIPTCExtRatingRegionCountryCode$kCGImagePropertyIPTCExtRatingRegionCountryName$kCGImagePropertyIPTCExtRatingRegionGPSAltitude$kCGImagePropertyIPTCExtRatingRegionGPSLatitude$kCGImagePropertyIPTCExtRatingRegionGPSLongitude$kCGImagePropertyIPTCExtRatingRegionIdentifier$kCGImagePropertyIPTCExtRatingRegionLocationId$kCGImagePropertyIPTCExtRatingRegionLocationName$kCGImagePropertyIPTCExtRatingRegionProvinceState$kCGImagePropertyIPTCExtRatingRegionSublocation$kCGImagePropertyIPTCExtRatingRegionWorldRegion$kCGImagePropertyIPTCExtRatingScaleMaxValue$kCGImagePropertyIPTCExtRatingScaleMinValue$kCGImagePropertyIPTCExtRatingSourceLink$kCGImagePropertyIPTCExtRatingValue$kCGImagePropertyIPTCExtRatingValueLogoLink$kCGImagePropertyIPTCExtRegistryEntryRole$kCGImagePropertyIPTCExtRegistryID$kCGImagePropertyIPTCExtRegistryItemID$kCGImagePropertyIPTCExtRegistryOrganisationID$kCGImagePropertyIPTCExtReleaseReady$kCGImagePropertyIPTCExtSeason$kCGImagePropertyIPTCExtSeasonIdentifier$kCGImagePropertyIPTCExtSeasonName$kCGImagePropertyIPTCExtSeasonNumber$kCGImagePropertyIPTCExtSeries$kCGImagePropertyIPTCExtSeriesIdentifier$kCGImagePropertyIPTCExtSeriesName$kCGImagePropertyIPTCExtShownEvent$kCGImagePropertyIPTCExtShownEventIdentifier$kCGImagePropertyIPTCExtShownEventName$kCGImagePropertyIPTCExtStorylineIdentifier$kCGImagePropertyIPTCExtStreamReady$kCGImagePropertyIPTCExtStylePeriod$kCGImagePropertyIPTCExtSupplyChainSource$kCGImagePropertyIPTCExtSupplyChainSourceIdentifier$kCGImagePropertyIPTCExtSupplyChainSourceName$kCGImagePropertyIPTCExtTemporalCoverage$kCGImagePropertyIPTCExtTemporalCoverageFrom$kCGImagePropertyIPTCExtTemporalCoverageTo$kCGImagePropertyIPTCExtTranscript$kCGImagePropertyIPTCExtTranscriptLink$kCGImagePropertyIPTCExtTranscriptLinkLink$kCGImagePropertyIPTCExtTranscriptLinkLinkQualifier$kCGImagePropertyIPTCExtVideoBitrate$kCGImagePropertyIPTCExtVideoBitrateMode$kCGImagePropertyIPTCExtVideoDisplayAspectRatio$kCGImagePropertyIPTCExtVideoEncodingProfile$kCGImagePropertyIPTCExtVideoShotType$kCGImagePropertyIPTCExtVideoShotTypeIdentifier$kCGImagePropertyIPTCExtVideoShotTypeName$kCGImagePropertyIPTCExtVideoStreamsCount$kCGImagePropertyIPTCExtVisualColor$kCGImagePropertyIPTCExtWorkflowTag$kCGImagePropertyIPTCExtWorkflowTagCvId$kCGImagePropertyIPTCExtWorkflowTagCvTermId$kCGImagePropertyIPTCExtWorkflowTagCvTermName$kCGImagePropertyIPTCExtWorkflowTagCvTermRefinedAbout$kCGImagePropertyIPTCFixtureIdentifier@^{__CFString=}$kCGImagePropertyIPTCHeadline@^{__CFString=}$kCGImagePropertyIPTCImageOrientation@^{__CFString=}$kCGImagePropertyIPTCImageType@^{__CFString=}$kCGImagePropertyIPTCKeywords@^{__CFString=}$kCGImagePropertyIPTCLanguageIdentifier@^{__CFString=}$kCGImagePropertyIPTCObjectAttributeReference@^{__CFString=}$kCGImagePropertyIPTCObjectCycle@^{__CFString=}$kCGImagePropertyIPTCObjectName@^{__CFString=}$kCGImagePropertyIPTCObjectTypeReference@^{__CFString=}$kCGImagePropertyIPTCOriginalTransmissionReference@^{__CFString=}$kCGImagePropertyIPTCOriginatingProgram@^{__CFString=}$kCGImagePropertyIPTCProgramVersion@^{__CFString=}$kCGImagePropertyIPTCProvinceState@^{__CFString=}$kCGImagePropertyIPTCReferenceDate@^{__CFString=}$kCGImagePropertyIPTCReferenceNumber@^{__CFString=}$kCGImagePropertyIPTCReferenceService@^{__CFString=}$kCGImagePropertyIPTCReleaseDate@^{__CFString=}$kCGImagePropertyIPTCReleaseTime@^{__CFString=}$kCGImagePropertyIPTCRightsUsageTerms@^{__CFString=}$kCGImagePropertyIPTCScene@^{__CFString=}$kCGImagePropertyIPTCSource@^{__CFString=}$kCGImagePropertyIPTCSpecialInstructions@^{__CFString=}$kCGImagePropertyIPTCStarRating@^{__CFString=}$kCGImagePropertyIPTCSubLocation@^{__CFString=}$kCGImagePropertyIPTCSubjectReference@^{__CFString=}$kCGImagePropertyIPTCSupplementalCategory@^{__CFString=}$kCGImagePropertyIPTCTimeCreated@^{__CFString=}$kCGImagePropertyIPTCUrgency@^{__CFString=}$kCGImagePropertyIPTCWriterEditor@^{__CFString=}$kCGImagePropertyImageCount$kCGImagePropertyImages$kCGImagePropertyIsFloat@^{__CFString=}$kCGImagePropertyIsIndexed@^{__CFString=}$kCGImagePropertyJFIFDensityUnit@^{__CFString=}$kCGImagePropertyJFIFDictionary@^{__CFString=}$kCGImagePropertyJFIFIsProgressive@^{__CFString=}$kCGImagePropertyJFIFVersion@^{__CFString=}$kCGImagePropertyJFIFXDensity@^{__CFString=}$kCGImagePropertyJFIFYDensity@^{__CFString=}$kCGImagePropertyMakerAppleDictionary@^{__CFString=}$kCGImagePropertyMakerCanonAspectRatioInfo@^{__CFString=}$kCGImagePropertyMakerCanonCameraSerialNumber@^{__CFString=}$kCGImagePropertyMakerCanonContinuousDrive@^{__CFString=}$kCGImagePropertyMakerCanonDictionary@^{__CFString=}$kCGImagePropertyMakerCanonFirmware@^{__CFString=}$kCGImagePropertyMakerCanonFlashExposureComp@^{__CFString=}$kCGImagePropertyMakerCanonImageSerialNumber@^{__CFString=}$kCGImagePropertyMakerCanonLensModel@^{__CFString=}$kCGImagePropertyMakerCanonOwnerName@^{__CFString=}$kCGImagePropertyMakerFujiDictionary@^{__CFString=}$kCGImagePropertyMakerMinoltaDictionary@^{__CFString=}$kCGImagePropertyMakerNikonCameraSerialNumber@^{__CFString=}$kCGImagePropertyMakerNikonColorMode@^{__CFString=}$kCGImagePropertyMakerNikonDictionary@^{__CFString=}$kCGImagePropertyMakerNikonDigitalZoom@^{__CFString=}$kCGImagePropertyMakerNikonFlashExposureComp@^{__CFString=}$kCGImagePropertyMakerNikonFlashSetting@^{__CFString=}$kCGImagePropertyMakerNikonFocusDistance@^{__CFString=}$kCGImagePropertyMakerNikonFocusMode@^{__CFString=}$kCGImagePropertyMakerNikonISOSelection@^{__CFString=}$kCGImagePropertyMakerNikonISOSetting@^{__CFString=}$kCGImagePropertyMakerNikonImageAdjustment@^{__CFString=}$kCGImagePropertyMakerNikonLensAdapter@^{__CFString=}$kCGImagePropertyMakerNikonLensInfo@^{__CFString=}$kCGImagePropertyMakerNikonLensType@^{__CFString=}$kCGImagePropertyMakerNikonQuality@^{__CFString=}$kCGImagePropertyMakerNikonSharpenMode@^{__CFString=}$kCGImagePropertyMakerNikonShootingMode@^{__CFString=}$kCGImagePropertyMakerNikonShutterCount@^{__CFString=}$kCGImagePropertyMakerNikonWhiteBalanceMode@^{__CFString=}$kCGImagePropertyMakerOlympusDictionary@^{__CFString=}$kCGImagePropertyMakerPentaxDictionary@^{__CFString=}$kCGImagePropertyNamedColorSpace$kCGImagePropertyOpenEXRAspectRatio@^{__CFString=}$kCGImagePropertyOpenEXRDictionary@^{__CFString=}$kCGImagePropertyOrientation@^{__CFString=}$kCGImagePropertyPNGAuthor@^{__CFString=}$kCGImagePropertyPNGChromaticities@^{__CFString=}$kCGImagePropertyPNGCompressionFilter$kCGImagePropertyPNGCopyright@^{__CFString=}$kCGImagePropertyPNGCreationTime@^{__CFString=}$kCGImagePropertyPNGDescription@^{__CFString=}$kCGImagePropertyPNGDictionary@^{__CFString=}$kCGImagePropertyPNGGamma@^{__CFString=}$kCGImagePropertyPNGInterlaceType@^{__CFString=}$kCGImagePropertyPNGModificationTime@^{__CFString=}$kCGImagePropertyPNGSoftware@^{__CFString=}$kCGImagePropertyPNGTitle@^{__CFString=}$kCGImagePropertyPNGXPixelsPerMeter@^{__CFString=}$kCGImagePropertyPNGYPixelsPerMeter@^{__CFString=}$kCGImagePropertyPNGsRGBIntent@^{__CFString=}$kCGImagePropertyPixelFormat$kCGImagePropertyPixelHeight@^{__CFString=}$kCGImagePropertyPixelWidth@^{__CFString=}$kCGImagePropertyProfileName@^{__CFString=}$kCGImagePropertyRawDictionary@^{__CFString=}$kCGImagePropertyTIFFArtist@^{__CFString=}$kCGImagePropertyTIFFCompression@^{__CFString=}$kCGImagePropertyTIFFCopyright@^{__CFString=}$kCGImagePropertyTIFFDateTime@^{__CFString=}$kCGImagePropertyTIFFDictionary@^{__CFString=}$kCGImagePropertyTIFFDocumentName@^{__CFString=}$kCGImagePropertyTIFFHostComputer@^{__CFString=}$kCGImagePropertyTIFFImageDescription@^{__CFString=}$kCGImagePropertyTIFFMake@^{__CFString=}$kCGImagePropertyTIFFModel@^{__CFString=}$kCGImagePropertyTIFFOrientation@^{__CFString=}$kCGImagePropertyTIFFPhotometricInterpretation@^{__CFString=}$kCGImagePropertyTIFFPrimaryChromaticities@^{__CFString=}$kCGImagePropertyTIFFResolutionUnit@^{__CFString=}$kCGImagePropertyTIFFSoftware@^{__CFString=}$kCGImagePropertyTIFFTileLength$kCGImagePropertyTIFFTileWidth$kCGImagePropertyTIFFTransferFunction@^{__CFString=}$kCGImagePropertyTIFFWhitePoint@^{__CFString=}$kCGImagePropertyTIFFXResolution@^{__CFString=}$kCGImagePropertyTIFFYResolution@^{__CFString=}$kCGImagePropertyThumbnailImages$kCGImagePropertyWidth$kCGImageSourceCreateThumbnailFromImageAlways@^{__CFString=}$kCGImageSourceCreateThumbnailFromImageIfAbsent@^{__CFString=}$kCGImageSourceCreateThumbnailWithTransform@^{__CFString=}$kCGImageSourceShouldAllowFloat@^{__CFString=}$kCGImageSourceShouldCache@^{__CFString=}$kCGImageSourceShouldCacheImmediately@^{__CFString=}$kCGImageSourceSubsampleFactor$kCGImageSourceThumbnailMaxPixelSize@^{__CFString=}$kCGImageSourceTypeIdentifierHint@^{__CFString=}$'''
enums = '''$IIO_HAS_IOSURFACE@1$IMAGEIO_PNG_ALL_FILTERS@248$IMAGEIO_PNG_FILTER_AVG@64$IMAGEIO_PNG_FILTER_NONE@8$IMAGEIO_PNG_FILTER_PAETH@128$IMAGEIO_PNG_FILTER_SUB@16$IMAGEIO_PNG_FILTER_UP@32$IMAGEIO_PNG_NO_FILTERS@0$kCGImageMetadataErrorBadArgument@2$kCGImageMetadataErrorConflictingArguments@3$kCGImageMetadataErrorPrefixConflict@4$kCGImageMetadataErrorUnknown@0$kCGImageMetadataErrorUnsupportedFormat@1$kCGImageMetadataTypeAlternateArray@4$kCGImageMetadataTypeAlternateText@5$kCGImageMetadataTypeArrayOrdered@3$kCGImageMetadataTypeArrayUnordered@2$kCGImageMetadataTypeDefault@0$kCGImageMetadataTypeInvalid@-1$kCGImageMetadataTypeString@1$kCGImageMetadataTypeStructure@6$kCGImagePropertyOrientationDown@3$kCGImagePropertyOrientationDownMirrored@4$kCGImagePropertyOrientationLeft@8$kCGImagePropertyOrientationLeftMirrored@5$kCGImagePropertyOrientationRight@6$kCGImagePropertyOrientationRightMirrored@7$kCGImagePropertyOrientationUp@1$kCGImagePropertyOrientationUpMirrored@2$kCGImageStatusComplete@0$kCGImageStatusIncomplete@-1$kCGImageStatusInvalidData@-4$kCGImageStatusReadingHeader@-2$kCGImageStatusUnexpectedEOF@-5$kCGImageStatusUnknownType@-3$'''
misc.update({})
functions={'CGImageMetadataSetValueMatchingImageProperty': (b'B^{CGImageMetadata=}^{__CFString=}^{__CFString=}@',), 'CGImageMetadataCreateFromXMPData': (b'^{CGImageMetadata=}^{__CFData=}', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceGetCount': (sel32or64(b'L^{CGImageSource=}', b'Q^{CGImageSource=}'),), 'CGImageSourceCreateWithData': (b'^{CGImageSource=}^{__CFData=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceCopyTypeIdentifiers': (b'^{__CFArray=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataCopyTagWithPath': (b'^{CGImageMetadataTag=}^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataGetTypeID': (sel32or64(b'L', b'Q'),), 'CGImageDestinationAddAuxiliaryDataInfo': (b'v^{CGImageDestination=}@@',), 'CGImageMetadataTagGetType': (b'i^{CGImageMetadataTag=}',), 'CGImageSourceGetStatus': (b'i^{CGImageSource=}',), 'CGImageMetadataCreateXMPData': (b'^{__CFData=}^{CGImageMetadata=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceCreateImageAtIndex': (sel32or64(b'^{CGImage=}^{CGImageSource=}L^{__CFDictionary=}', b'^{CGImage=}^{CGImageSource=}Q^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataTagCopyNamespace': (b'^{__CFString=}^{CGImageMetadataTag=}', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceCopyMetadataAtIndex': (sel32or64(b'^{CGImageMetadata=}^{CGImageSource=}L^{__CFDictionary=}', b'^{CGImageMetadata=}^{CGImageSource=}Q^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}}), 'CGImageDestinationCreateWithURL': (sel32or64(b'^{CGImageDestination=}^{__CFURL=}^{__CFString=}L^{__CFDictionary=}', b'^{CGImageDestination=}^{__CFURL=}^{__CFString=}Q^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}}), 'CGImageSourceRemoveCacheAtIndex': (sel32or64(b'v^{CGImageSource=}L', b'v^{CGImageSource=}Q'),), 'CGImageSourceCreateThumbnailAtIndex': (sel32or64(b'^{CGImage=}^{CGImageSource=}L^{__CFDictionary=}', b'^{CGImage=}^{CGImageSource=}Q^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}}), 'CGImageSourceCreateIncremental': (b'^{CGImageSource=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceCopyPropertiesAtIndex': (sel32or64(b'^{__CFDictionary=}^{CGImageSource=}L^{__CFDictionary=}', b'^{__CFDictionary=}^{CGImageSource=}Q^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}}), 'CGImageSourceUpdateData': (b'v^{CGImageSource=}^{__CFData=}B',), 'CGImageDestinationSetProperties': (b'v^{CGImageDestination=}^{__CFDictionary=}',), 'CGImageMetadataSetTagWithPath': (b'B^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}^{CGImageMetadataTag=}',), 'CGImageDestinationCreateWithDataConsumer': (sel32or64(b'^{CGImageDestination=}^{CGDataConsumer=}^{__CFString=}L^{__CFDictionary=}', b'^{CGImageDestination=}^{CGDataConsumer=}^{__CFString=}Q^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}}), 'CGImageDestinationCopyTypeIdentifiers': (b'^{__CFArray=}', '', {'retval': {'already_cfretained': True}}), 'CGImageDestinationCreateWithData': (sel32or64(b'^{CGImageDestination=}^{__CFData=}^{__CFString=}L^{__CFDictionary=}', b'^{CGImageDestination=}^{__CFData=}^{__CFString=}Q^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}}), 'CGImageSourceCopyAuxiliaryDataInfoAtIndex': (b'@^{CGImageSource=}L@', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceGetTypeID': (sel32or64(b'L', b'Q'),), 'CGImageDestinationAddImageAndMetadata': (b'v^{CGImageDestination=}^{CGImage=}^{CGImageMetadata=}^{__CFDictionary=}',), 'CGImageMetadataTagCreate': (b'^{CGImageMetadataTag=}^{__CFString=}^{__CFString=}^{__CFString=}i@', '', {'retval': {'already_cfretained': True}}), 'CGImageDestinationCopyImageSource': (b'B^{CGImageDestination=}^{CGImageSource=}^{__CFDictionary=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {3: {'already_cfretained': True, 'type_modifier': 'o', 'null_accepted': True}}}), 'CGImageSourceUpdateDataProvider': (b'v^{CGImageSource=}^{CGDataProvider=}B',), 'CGImageDestinationAddImage': (b'v^{CGImageDestination=}^{CGImage=}^{__CFDictionary=}',), 'CGImageMetadataRemoveTagWithPath': (b'B^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}',), 'CGImageSourceGetStatusAtIndex': (sel32or64(b'i^{CGImageSource=}L', b'i^{CGImageSource=}Q'),), 'CGImageSourceCreateWithURL': (b'^{CGImageSource=}^{__CFURL=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataTagCopyValue': (b'@^{CGImageMetadataTag=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataCopyTags': (b'^{__CFArray=}^{CGImageMetadata=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataCopyStringValueWithPath': (b'^{__CFString=}^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceGetType': (b'^{__CFString=}^{CGImageSource=}',), 'CGImageDestinationAddImageFromSource': (sel32or64(b'v^{CGImageDestination=}^{CGImageSource=}L^{__CFDictionary=}', b'v^{CGImageDestination=}^{CGImageSource=}Q^{__CFDictionary=}'),), 'CGImageDestinationGetTypeID': (sel32or64(b'L', b'Q'),), 'CGImageDestinationFinalize': (b'B^{CGImageDestination=}',), 'CGImageSourceCopyProperties': (b'^{__CFDictionary=}^{CGImageSource=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataTagGetTypeID': (sel32or64(b'L', b'Q'),), 'CGImageMetadataSetValueWithPath': (b'B^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}@',), 'CGImageMetadataCopyTagMatchingImageProperty': (b'^{CGImageMetadataTag=}^{CGImageMetadata=}^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataRegisterNamespaceForPrefix': (b'B^{CGImageMetadata=}^{__CFString=}^{__CFString=}^^{__CFError=}', '', {'arguments': {3: {'already_cfretained': True, 'type_modifier': 'o', 'null_accepted': True}}}), 'CGImageMetadataTagCopyPrefix': (b'^{__CFString=}^{CGImageMetadataTag=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataTagCopyName': (b'^{__CFString=}^{CGImageMetadataTag=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataEnumerateTagsUsingBlock': (b'v^{CGImageMetadata=}^{__CFString=}^{__CFDictionary=}@?', '', {'arguments': {3: {'callable': {'retval': {'type': b'B'}, 'arguments': {0: {'type': '^v'}, 1: {'type': '@'}, 2: {'type': '@'}}}}}}), 'CGImageMetadataCreateMutable': (b'^{CGImageMetadata=}', '', {'retval': {'already_cfretained': True}}), 'CGImageSourceCreateWithDataProvider': (b'^{CGImageSource=}^{CGDataProvider=}^{__CFDictionary=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataTagCopyQualifiers': (b'^{__CFArray=}^{CGImageMetadataTag=}', '', {'retval': {'already_cfretained': True}}), 'CGImageMetadataCreateMutableCopy': (b'^{CGImageMetadata=}^{CGImageMetadata=}', '', {'retval': {'already_cfretained': True}})}
aliases = {'IMAGEIO_AVAILABLE_STARTING': '__OSX_AVAILABLE_STARTING', 'IMAGEIO_AVAILABLE_BUT_DEPRECATED': '__OSX_AVAILABLE_BUT_DEPRECATED'}
cftypes=[('CGImageSourceRef', b'^{CGImageSource=}', 'CGImageSourceGetTypeID', None), ('CGImageDestinationRef', b'^{CGImageDestination=}', 'CGImageDestinationGetTypeID', None), ('CGImageMetadataTagRef', b'^{CGImageMetadataTag=}', 'CGImageMetadataTagGetTypeID', None), ('CGImageMetadataRef', b'^{CGImageMetadata=}', 'CGImageMetadataGetTypeID', None)]
expressions = {}

# END OF FILE
