from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAccessibilityHelper (NSObject):
    def accessibilityIsAttributeSettable_(self, arg):
        return 1

    def accessibilityIsIgnored(self):
        return 1

    def accessibilityHitTest_(self, pt):
        pass

    def accessibilitySetOverrideValue_forAttribute_(self, v, a):
        return 1

    def accessibilityNotifiesWhenDestroyed(self): pass

    def accessibilityIndexOfChild_(self, c): return 1
    def accessibilityArrayAttributeCount_(self, c): return 1
    def accessibilityArrayAttributeValues_index_maxCount_(self, v, i, c): return None

class TestNSAccessibility (TestCase):
    def testInformal(self):
        self.assertResultIsBOOL(TestNSAccessibilityHelper.accessibilityIsAttributeSettable_)
        self.assertResultIsBOOL(TestNSAccessibilityHelper.accessibilityIsIgnored)
        self.assertArgHasType(TestNSAccessibilityHelper.accessibilityHitTest_, 0, NSPoint.__typestr__)
        self.assertResultIsBOOL(TestNSAccessibilityHelper.accessibilitySetOverrideValue_forAttribute_)
        self.assertResultIsBOOL(TestNSAccessibilityHelper.accessibilityNotifiesWhenDestroyed)
        self.assertResultHasType(TestNSAccessibilityHelper.accessibilityIndexOfChild_, objc._C_NSUInteger)
        self.assertResultHasType(TestNSAccessibilityHelper.accessibilityArrayAttributeCount_, objc._C_NSUInteger)
        self.assertResultHasType(TestNSAccessibilityHelper.accessibilityArrayAttributeCount_, objc._C_NSUInteger)
        self.assertArgHasType(TestNSAccessibilityHelper.accessibilityArrayAttributeValues_index_maxCount_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSAccessibilityHelper.accessibilityArrayAttributeValues_index_maxCount_, 2, objc._C_NSUInteger)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSWorkspace.accessibilityDisplayShouldIncreaseContrast)
        self.assertResultIsBOOL(NSWorkspace.accessibilityDisplayShouldDifferentiateWithoutColor)
        self.assertResultIsBOOL(NSWorkspace.accessibilityDisplayShouldReduceTransparency)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSWorkspace.accessibilityDisplayShouldReduceMotion)
        self.assertResultIsBOOL(NSWorkspace.accessibilityDisplayShouldInvertColors)

    @min_os_level('10.10')
    def testFunctions10_10(self):
        NSAccessibilityFrameInView # Existence
        NSAccessibilityPointInView # Existence

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSWorkspaceAccessibilityDisplayOptionsDidChangeNotification, unicode)

    def testFunction(self):
        v = NSAccessibilityRoleDescription(NSAccessibilityButtonRole, None)
        self.assertIsInstance(v, unicode)

        b = NSButton.alloc().init()
        v = NSAccessibilityRoleDescriptionForUIElement(b)
        self.assertIsInstance(v, unicode)

        v = NSAccessibilityActionDescription(NSAccessibilityIncrementAction)
        self.assertIsInstance(v, unicode)

        self.assertRaises(objc.error, NSAccessibilityRaiseBadArgumentException, b, "attribute", "value")


        v = NSAccessibilityUnignoredAncestor(b)
        self.assertIs(v, None)
        v = NSAccessibilityUnignoredDescendant(b)
        self.assertIsInstance(b, NSView)

        v = NSAccessibilityUnignoredChildren([b])
        self.assertIsInstance(v, NSArray)

        v = NSAccessibilityUnignoredChildrenForOnlyChild(b)
        self.assertIsInstance(v, NSArray)

        v = NSAccessibilityPostNotification(b, "hello")
        self.assertIs(v, None)


    def testConstants(self):
        self.assertEqual(NSAccessibilityAnnotationPositionFullRange, 0)
        self.assertEqual(NSAccessibilityAnnotationPositionStart, 1)
        self.assertEqual(NSAccessibilityAnnotationPositionEnd, 2)

        self.assertIsInstance(NSAccessibilityErrorCodeExceptionInfo, unicode)
        self.assertIsInstance(NSAccessibilityRoleAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRoleDescriptionAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySubroleAttribute, unicode)
        self.assertIsInstance(NSAccessibilityHelpAttribute, unicode)
        self.assertIsInstance(NSAccessibilityValueAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMinValueAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMaxValueAttribute, unicode)
        self.assertIsInstance(NSAccessibilityEnabledAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFocusedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityParentAttribute, unicode)
        self.assertIsInstance(NSAccessibilityChildrenAttribute, unicode)
        self.assertIsInstance(NSAccessibilityWindowAttribute, unicode)
        self.assertIsInstance(NSAccessibilityTopLevelUIElementAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedChildrenAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVisibleChildrenAttribute, unicode)
        self.assertIsInstance(NSAccessibilityPositionAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySizeAttribute, unicode)
        self.assertIsInstance(NSAccessibilityContentsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityTitleAttribute, unicode)
        self.assertIsInstance(NSAccessibilityDescriptionAttribute, unicode)
        self.assertIsInstance(NSAccessibilityShownMenuAttribute, unicode)
        self.assertIsInstance(NSAccessibilityValueDescriptionAttribute, unicode)
        self.assertIsInstance(NSAccessibilityPreviousContentsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityNextContentsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityHeaderAttribute, unicode)
        self.assertIsInstance(NSAccessibilityEditedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityTabsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityHorizontalScrollBarAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVerticalScrollBarAttribute, unicode)
        self.assertIsInstance(NSAccessibilityOverflowButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityIncrementButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityDecrementButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFilenameAttribute, unicode)
        self.assertIsInstance(NSAccessibilityExpandedAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySplittersAttribute, unicode)
        self.assertIsInstance(NSAccessibilityDocumentAttribute, unicode)
        self.assertIsInstance(NSAccessibilityURLAttribute, unicode)
        self.assertIsInstance(NSAccessibilityIndexAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRowCountAttribute, unicode)
        self.assertIsInstance(NSAccessibilityColumnCountAttribute, unicode)
        self.assertIsInstance(NSAccessibilityOrderedByRowAttribute, unicode)
        self.assertIsInstance(NSAccessibilityTitleUIElementAttribute, unicode)
        self.assertIsInstance(NSAccessibilityServesAsTitleForUIElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLinkedUIElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedTextRangeAttribute, unicode)
        self.assertIsInstance(NSAccessibilityNumberOfCharactersAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVisibleCharacterRangeAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySharedTextUIElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySharedCharacterRangeAttribute, unicode)
        self.assertIsInstance(NSAccessibilityInsertionPointLineNumberAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedTextRangesAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLineForIndexParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRangeForLineParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityStringForRangeParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRangeForPositionParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRangeForIndexParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityBoundsForRangeParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRTFForRangeParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityStyleRangeForIndexParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityAttributedStringForRangeParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFontTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityForegroundColorTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityBackgroundColorTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityUnderlineColorTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityStrikethroughColorTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityUnderlineTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySuperscriptTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityStrikethroughTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityShadowTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityAttachmentTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLinkTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMisspelledTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMarkedMisspelledTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFontNameKey, unicode)
        self.assertIsInstance(NSAccessibilityFontFamilyKey, unicode)
        self.assertIsInstance(NSAccessibilityVisibleNameKey, unicode)
        self.assertIsInstance(NSAccessibilityFontSizeKey, unicode)
        self.assertIsInstance(NSAccessibilityMainAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMinimizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityCloseButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityZoomButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMinimizeButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityToolbarButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityProxyAttribute, unicode)
        self.assertIsInstance(NSAccessibilityGrowAreaAttribute, unicode)
        self.assertIsInstance(NSAccessibilityModalAttribute, unicode)
        self.assertIsInstance(NSAccessibilityDefaultButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityCancelButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMenuBarAttribute, unicode)
        self.assertIsInstance(NSAccessibilityWindowsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFrontmostAttribute, unicode)
        self.assertIsInstance(NSAccessibilityHiddenAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMainWindowAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFocusedWindowAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFocusedUIElementAttribute, unicode)
        self.assertIsInstance(NSAccessibilityOrientationAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVerticalOrientationValue, unicode)
        self.assertIsInstance(NSAccessibilityHorizontalOrientationValue, unicode)
        self.assertIsInstance(NSAccessibilityColumnTitlesAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySearchButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySearchMenuAttribute, unicode)
        self.assertIsInstance(NSAccessibilityClearButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRowsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVisibleRowsAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedRowsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityColumnsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVisibleColumnsAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedColumnsAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySortDirectionAttribute, unicode)
        self.assertIsInstance(NSAccessibilityAscendingSortDirectionValue, unicode)
        self.assertIsInstance(NSAccessibilityDescendingSortDirectionValue, unicode)
        self.assertIsInstance(NSAccessibilityUnknownSortDirectionValue, unicode)
        self.assertIsInstance(NSAccessibilityDisclosingAttribute, unicode)
        self.assertIsInstance(NSAccessibilityDisclosedRowsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityDisclosedByRowAttribute, unicode)
        self.assertIsInstance(NSAccessibilityDisclosureLevelAttribute, unicode)
        self.assertIsInstance(NSAccessibilityAllowedValuesAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLabelUIElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLabelValueAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMatteHoleAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMatteContentUIElementAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMarkerUIElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMarkerValuesAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMarkerGroupUIElementAttribute, unicode)
        self.assertIsInstance(NSAccessibilityUnitsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityUnitDescriptionAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMarkerTypeAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMarkerTypeDescriptionAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLeftTabStopMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityRightTabStopMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityCenterTabStopMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityDecimalTabStopMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityHeadIndentMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityTailIndentMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityFirstLineIndentMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityUnknownMarkerTypeValue, unicode)
        self.assertIsInstance(NSAccessibilityInchesUnitValue, unicode)
        self.assertIsInstance(NSAccessibilityCentimetersUnitValue, unicode)
        self.assertIsInstance(NSAccessibilityPointsUnitValue, unicode)
        self.assertIsInstance(NSAccessibilityPicasUnitValue, unicode)
        self.assertIsInstance(NSAccessibilityUnknownUnitValue, unicode)
        self.assertIsInstance(NSAccessibilityPressAction, unicode)
        self.assertIsInstance(NSAccessibilityIncrementAction, unicode)
        self.assertIsInstance(NSAccessibilityDecrementAction, unicode)
        self.assertIsInstance(NSAccessibilityConfirmAction, unicode)
        self.assertIsInstance(NSAccessibilityPickAction, unicode)
        self.assertIsInstance(NSAccessibilityCancelAction, unicode)
        self.assertIsInstance(NSAccessibilityRaiseAction, unicode)
        self.assertIsInstance(NSAccessibilityShowMenuAction, unicode)
        self.assertIsInstance(NSAccessibilityDeleteAction, unicode)
        self.assertIsInstance(NSAccessibilityMainWindowChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityFocusedWindowChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityFocusedUIElementChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityApplicationActivatedNotification, unicode)
        self.assertIsInstance(NSAccessibilityApplicationDeactivatedNotification, unicode)
        self.assertIsInstance(NSAccessibilityApplicationHiddenNotification, unicode)
        self.assertIsInstance(NSAccessibilityApplicationShownNotification, unicode)
        self.assertIsInstance(NSAccessibilityWindowCreatedNotification, unicode)
        self.assertIsInstance(NSAccessibilityWindowMovedNotification, unicode)
        self.assertIsInstance(NSAccessibilityWindowResizedNotification, unicode)
        self.assertIsInstance(NSAccessibilityWindowMiniaturizedNotification, unicode)
        self.assertIsInstance(NSAccessibilityWindowDeminiaturizedNotification, unicode)
        self.assertIsInstance(NSAccessibilityDrawerCreatedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySheetCreatedNotification, unicode)
        self.assertIsInstance(NSAccessibilityUIElementDestroyedNotification, unicode)
        self.assertIsInstance(NSAccessibilityValueChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityTitleChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityResizedNotification, unicode)
        self.assertIsInstance(NSAccessibilityMovedNotification, unicode)
        self.assertIsInstance(NSAccessibilityCreatedNotification, unicode)
        self.assertIsInstance(NSAccessibilityHelpTagCreatedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySelectedTextChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityRowCountChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySelectedChildrenChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySelectedRowsChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySelectedColumnsChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityUnknownRole, unicode)
        self.assertIsInstance(NSAccessibilityButtonRole, unicode)
        self.assertIsInstance(NSAccessibilityRadioButtonRole, unicode)
        self.assertIsInstance(NSAccessibilityCheckBoxRole, unicode)
        self.assertIsInstance(NSAccessibilitySliderRole, unicode)
        self.assertIsInstance(NSAccessibilityTabGroupRole, unicode)
        self.assertIsInstance(NSAccessibilityTextFieldRole, unicode)
        self.assertIsInstance(NSAccessibilityStaticTextRole, unicode)
        self.assertIsInstance(NSAccessibilityTextAreaRole, unicode)
        self.assertIsInstance(NSAccessibilityScrollAreaRole, unicode)
        self.assertIsInstance(NSAccessibilityPopUpButtonRole, unicode)
        self.assertIsInstance(NSAccessibilityMenuButtonRole, unicode)
        self.assertIsInstance(NSAccessibilityTableRole, unicode)
        self.assertIsInstance(NSAccessibilityApplicationRole, unicode)
        self.assertIsInstance(NSAccessibilityGroupRole, unicode)
        self.assertIsInstance(NSAccessibilityRadioGroupRole, unicode)
        self.assertIsInstance(NSAccessibilityListRole, unicode)
        self.assertIsInstance(NSAccessibilityScrollBarRole, unicode)
        self.assertIsInstance(NSAccessibilityValueIndicatorRole, unicode)
        self.assertIsInstance(NSAccessibilityImageRole, unicode)
        self.assertIsInstance(NSAccessibilityMenuBarRole, unicode)
        self.assertIsInstance(NSAccessibilityMenuRole, unicode)
        self.assertIsInstance(NSAccessibilityMenuItemRole, unicode)
        self.assertIsInstance(NSAccessibilityColumnRole, unicode)
        self.assertIsInstance(NSAccessibilityRowRole, unicode)
        self.assertIsInstance(NSAccessibilityToolbarRole, unicode)
        self.assertIsInstance(NSAccessibilityBusyIndicatorRole, unicode)
        self.assertIsInstance(NSAccessibilityProgressIndicatorRole, unicode)
        self.assertIsInstance(NSAccessibilityWindowRole, unicode)
        self.assertIsInstance(NSAccessibilityDrawerRole, unicode)
        self.assertIsInstance(NSAccessibilitySystemWideRole, unicode)
        self.assertIsInstance(NSAccessibilityOutlineRole, unicode)
        self.assertIsInstance(NSAccessibilityIncrementorRole, unicode)
        self.assertIsInstance(NSAccessibilityBrowserRole, unicode)
        self.assertIsInstance(NSAccessibilityComboBoxRole, unicode)
        self.assertIsInstance(NSAccessibilitySplitGroupRole, unicode)
        self.assertIsInstance(NSAccessibilitySplitterRole, unicode)
        self.assertIsInstance(NSAccessibilityColorWellRole, unicode)
        self.assertIsInstance(NSAccessibilityGrowAreaRole, unicode)
        self.assertIsInstance(NSAccessibilitySheetRole, unicode)
        self.assertIsInstance(NSAccessibilityHelpTagRole, unicode)
        self.assertIsInstance(NSAccessibilityMatteRole, unicode)
        self.assertIsInstance(NSAccessibilityRulerRole, unicode)
        self.assertIsInstance(NSAccessibilityRulerMarkerRole, unicode)
        self.assertIsInstance(NSAccessibilitySortButtonRole, unicode)
        self.assertIsInstance(NSAccessibilityLinkRole, unicode)
        self.assertIsInstance(NSAccessibilityDisclosureTriangleRole, unicode)
        self.assertIsInstance(NSAccessibilityGridRole, unicode)
        self.assertIsInstance(NSAccessibilityUnknownSubrole, unicode)
        self.assertIsInstance(NSAccessibilityCloseButtonSubrole, unicode)
        self.assertIsInstance(NSAccessibilityZoomButtonSubrole, unicode)
        self.assertIsInstance(NSAccessibilityMinimizeButtonSubrole, unicode)
        self.assertIsInstance(NSAccessibilityToolbarButtonSubrole, unicode)
        self.assertIsInstance(NSAccessibilityTableRowSubrole, unicode)
        self.assertIsInstance(NSAccessibilityOutlineRowSubrole, unicode)
        self.assertIsInstance(NSAccessibilitySecureTextFieldSubrole, unicode)
        self.assertIsInstance(NSAccessibilityStandardWindowSubrole, unicode)
        self.assertIsInstance(NSAccessibilityDialogSubrole, unicode)
        self.assertIsInstance(NSAccessibilitySystemDialogSubrole, unicode)
        self.assertIsInstance(NSAccessibilityFloatingWindowSubrole, unicode)
        self.assertIsInstance(NSAccessibilitySystemFloatingWindowSubrole, unicode)
        self.assertIsInstance(NSAccessibilityIncrementArrowSubrole, unicode)
        self.assertIsInstance(NSAccessibilityDecrementArrowSubrole, unicode)
        self.assertIsInstance(NSAccessibilityIncrementPageSubrole, unicode)
        self.assertIsInstance(NSAccessibilityDecrementPageSubrole, unicode)
        self.assertIsInstance(NSAccessibilitySearchFieldSubrole, unicode)
        self.assertIsInstance(NSAccessibilityTextAttachmentSubrole, unicode)
        self.assertIsInstance(NSAccessibilityTextLinkSubrole, unicode)
        self.assertIsInstance(NSAccessibilityTimelineSubrole, unicode)
        self.assertIsInstance(NSAccessibilityRelevanceIndicatorRole, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSAccessibilityUnknownOrientationValue, unicode)
        self.assertIsInstance(NSAccessibilityWarningValueAttribute, unicode)
        self.assertIsInstance(NSAccessibilityCriticalValueAttribute, unicode)
        self.assertIsInstance(NSAccessibilityPlaceholderValueAttribute, unicode)
        self.assertIsInstance(NSAccessibilitySelectedCellsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVisibleCellsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRowHeaderUIElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityColumnHeaderUIElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityCellForColumnAndRowParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRowIndexRangeAttribute, unicode)
        self.assertIsInstance(NSAccessibilityColumnIndexRangeAttribute, unicode)
        self.assertIsInstance(NSAccessibilityHorizontalUnitsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVerticalUnitsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityHorizontalUnitDescriptionAttribute, unicode)
        self.assertIsInstance(NSAccessibilityVerticalUnitDescriptionAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLayoutPointForScreenPointParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityLayoutSizeForScreenSizeParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityScreenPointForLayoutPointParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityScreenSizeForLayoutSizeParameterizedAttribute, unicode)
        self.assertIsInstance(NSAccessibilityHandlesAttribute, unicode)
        self.assertIsInstance(NSAccessibilityRowExpandedNotification, unicode)
        self.assertIsInstance(NSAccessibilityRowCollapsedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySelectedCellsChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityUnitsChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySelectedChildrenMovedNotification, unicode)
        self.assertIsInstance(NSAccessibilitySortButtonRole, unicode)
        self.assertIsInstance(NSAccessibilityLevelIndicatorRole, unicode)
        self.assertIsInstance(NSAccessibilityCellRole, unicode)
        self.assertIsInstance(NSAccessibilityLayoutAreaRole, unicode)
        self.assertIsInstance(NSAccessibilityLayoutItemRole, unicode)
        self.assertIsInstance(NSAccessibilityHandleRole, unicode)
        self.assertIsInstance(NSAccessibilitySortButtonSubrole, unicode)
        self.assertIsInstance(NSAccessibilityRatingIndicatorSubrole, unicode)
        self.assertIsInstance(NSAccessibilityContentListSubrole, unicode)
        self.assertIsInstance(NSAccessibilityDefinitionListSubrole, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(NSAccessibilityAutocorrectedTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityFullScreenButtonAttribute, unicode)
        self.assertIsInstance(NSAccessibilityPopoverRole, unicode)
        self.assertIsInstance(NSAccessibilityFullScreenButtonSubrole, unicode)
        self.assertIsInstance(NSAccessibilityIdentifierAttribute, unicode)
        self.assertIsInstance(NSAccessibilityAnnouncementRequestedNotification, unicode)
        self.assertIsInstance(NSAccessibilityAnnouncementKey, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(NSAccessibilityExtrasMenuBarAttribute, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSAccessibilityContainsProtectedContentAttribute, unicode)
        self.assertIsInstance(NSAccessibilityShowAlternateUIAction, unicode)
        self.assertIsInstance(NSAccessibilityShowDefaultUIAction, unicode)
        self.assertIsInstance(NSAccessibilityLayoutChangedNotification, unicode)
        self.assertIsInstance(NSAccessibilityToggleSubrole, unicode)
        self.assertIsInstance(NSAccessibilitySwitchSubrole, unicode)
        self.assertIsInstance(NSAccessibilityDescriptionListSubrole, unicode)
        self.assertIsInstance(NSAccessibilityUIElementsKey, unicode)
        self.assertIsInstance(NSAccessibilityPriorityKey, unicode)

        self.assertEqual(NSAccessibilityPriorityLow, 10)
        self.assertEqual(NSAccessibilityPriorityMedium, 50)
        self.assertEqual(NSAccessibilityPriorityHigh, 90)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSAccessibilityActivationPointAttribute, unicode)

        self.assertIsInstance(NSAccessibilitySharedFocusElementsAttribute, unicode)
        self.assertIsInstance(NSAccessibilityAlternateUIVisibleAttribute, unicode)

        self.assertEqual(NSAccessibilityOrientationUnknown, 0)
        self.assertEqual(NSAccessibilityOrientationVertical, 1)
        self.assertEqual(NSAccessibilityOrientationHorizontal, 2)

        self.assertEqual(NSAccessibilitySortDirectionUnknown, 0)
        self.assertEqual(NSAccessibilitySortDirectionAscending, 1)
        self.assertEqual(NSAccessibilitySortDirectionDescending, 2)

        self.assertEqual(NSAccessibilityRulerMarkerTypeUnknown, 0)
        self.assertEqual(NSAccessibilityRulerMarkerTypeTabStopLeft, 1)
        self.assertEqual(NSAccessibilityRulerMarkerTypeTabStopRight, 2)
        self.assertEqual(NSAccessibilityRulerMarkerTypeTabStopCenter, 3)
        self.assertEqual(NSAccessibilityRulerMarkerTypeTabStopDecimal, 4)
        self.assertEqual(NSAccessibilityRulerMarkerTypeIndentHead, 5)
        self.assertEqual(NSAccessibilityRulerMarkerTypeIndentTail, 6)
        self.assertEqual(NSAccessibilityRulerMarkerTypeIndentFirstLine, 7)

        self.assertEqual(NSAccessibilityUnitsUnknown, 0)
        self.assertEqual(NSAccessibilityUnitsInches, 1)
        self.assertEqual(NSAccessibilityUnitsCentimeters, 2)
        self.assertEqual(NSAccessibilityUnitsPoints, 3)
        self.assertEqual(NSAccessibilityUnitsPicas, 4)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(NSAccessibilityListItemPrefixTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityListItemIndexTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityListItemLevelTextAttribute, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(NSAccessibilityRequiredAttribute, unicode)
        self.assertIsInstance(NSAccessibilityMenuBarItemRole, unicode)
        self.assertIsInstance(NSAccessibilityTextAlignmentAttribute, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(NSAccessibilityAnnotationLabel, unicode)
        self.assertIsInstance(NSAccessibilityAnnotationElement, unicode)
        self.assertIsInstance(NSAccessibilityAnnotationLocation, unicode)

        self.assertIsInstance(NSAccessibilityLanguageTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityCustomTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityAnnotationTextAttribute, unicode)
        self.assertIsInstance(NSAccessibilityPageRole, unicode)
        self.assertIsInstance(NSAccessibilityTabButtonSubrole, unicode)
        self.assertIsInstance(NSAccessibilityCollectionListSubrole, unicode)
        self.assertIsInstance(NSAccessibilitySectionListSubrole, unicode)

    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertIsInstance(NSAccessibilityPostNotificationWithUserInfo, objc.function)

    @min_os_level('10.9')
    def testFunctions10_9(self):
        self.assertArgIsBOOL(NSAccessibilitySetMayContainProtectedContent, 0)
        self.assertResultIsBOOL(NSAccessibilitySetMayContainProtectedContent)

if __name__ == "__main__":
    main()
