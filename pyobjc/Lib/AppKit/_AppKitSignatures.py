from objc import setSignatureForSelector

setSignatureForSelector("NSFocusState", "clip:", "@@:n^{_NSRect={_NSPoint=ff}{_NSSize=ff}}")
setSignatureForSelector("NSSurface", "surfaceID", "i@:")
setSignatureForSelector("NSInputManager", "getMarkedText:selectedRange:", "v@:o^@o^{_NSRange=II}")
setSignatureForSelector("NSToolbar", "_configSheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSAlert", "didEndAlert:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSEvent", "enterExitEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:trackingNumber:userData:", "@52@4:8i12{_NSPoint=ff}16I24d36i40@44i48i52i56")
setSignatureForSelector("NSEvent", "userData", "i@:")
setSignatureForSelector("NSPSMatrix", "invTransformRect:", "@@:N^{_NSRect={_NSPoint=ff}{_NSSize=ff}}")
setSignatureForSelector("NSPSMatrix", "invTransform:", "@@:N^{_NSPoint=ff}")
setSignatureForSelector("NSPSMatrix", "transformRect:", "@@:N^{_NSRect={_NSPoint=ff}{_NSSize=ff}}")
setSignatureForSelector("NSPSMatrix", "transform:", "@@:N^{_NSPoint=ff}")
setSignatureForSelector("NSButton", "getPeriodicDelay:interval:", "v@:o^fo^f")
setSignatureForSelector("NSView", "addToolTipRect:owner:userData:", "i28@4:8{_NSRect={_NSPoint=ff}{_NSSize=ff}}12@28i32")
setSignatureForSelector("NSView", "addTrackingRect:owner:userData:assumeInside:", "i@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}@ic")
setSignatureForSelector("NSAlert", "didEndSheet:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSSavePanel", "_runModalForDirectory:file:relativeToWindow:modalDelegate:didEndSelector:contextInfo:", "v28@4:8@12@16@20@24:28i32")
setSignatureForSelector("NSSavePanel", "beginSheetForDirectory:file:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v28@4:8@12@16@20@24:28i32")
setSignatureForSelector("NSSavePanel", "didEndSheet:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSPageLayout", "_sheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSPageLayout", "beginSheetWithPrintInfo:modalForWindow:delegate:didEndSelector:contextInfo:", "v24@4:8@12@16@20:24i28")
setSignatureForSelector("NSPageLayout", "convertOldFactor:newFactor:", "v@:n^fo^f")
setSignatureForSelector("NSBitmapImageRep", "getCompression:factor:", "v@:o^io^f")
setSignatureForSelector("NSColor", "getCyan:magenta:yellow:black:alpha:", "v@:o^fo^fo^fo^fo^f")
setSignatureForSelector("NSColor", "getHue:saturation:brightness:alpha:", "v@:o^fo^fo^fo^f")
setSignatureForSelector("NSColor", "getRed:green:blue:alpha:", "v@:o^fo^fo^fo^f")
setSignatureForSelector("NSColor", "getWhite:alpha:", "v@:o^fo^f")
setSignatureForSelector("NSFont", "positionOfGlyph:precededByGlyph:isNominal:", "{_NSPoint=ff}@:IIo^c")
setSignatureForSelector("NSFont", "positionOfGlyph:struckOverGlyph:metricsExist:", "{_NSPoint=ff}@:IIo^c")
setSignatureForSelector("NSFont", "positionOfGlyph:struckOverRect:metricsExist:", "{_NSPoint=ff}@:I{_NSRect={_NSPoint=ff}{_NSSize=ff}}o^c")
setSignatureForSelector("NSFont", "positionOfGlyph:withRelation:toBaseGlyph:totalAdvancement:metricsExist:", "{_NSPoint=ff}@:IiIo^{_NSSize=ff}o^c")
setSignatureForSelector("NSWorkspace", "getFileSystemInfoForPath:isRemovable:isWritable:isUnmountable:description:type:", "c28@4:8@12o^c16o^c20o^c24o^@28o^@32")
setSignatureForSelector("NSWorkspace", "getInfoForFile:application:type:", "c@:@o^@o^@")
setSignatureForSelector("NSWorkspace", "performFileOperation:source:destination:files:tag:", "c@:@@@@o^i")
setSignatureForSelector("NSDocument", "_changeAlertDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSDocument", "_compatibility_canCloseDocumentWithDelegate:shouldCloseSelector:contextInfo:", "v16@4:8@12:16i20")
setSignatureForSelector("NSDocument", "_compatibility_doSavePanelSave:delegate:didSaveSelector:contextInfo:", "v20@4:8i12@16:20i24")
setSignatureForSelector("NSDocument", "_compatibility_shouldCloseWindowController:delegate:shouldCloseSelector:contextInfo:", "v20@4:8@12@16:20i24")
setSignatureForSelector("NSDocument", "_didEndCloseSheet:returnCode:closeContext:", "v16@4:8@12i16i20")
setSignatureForSelector("NSDocument", "_document:pageLayoutDidReturn:contextInfo:", "v16@4:8@12c16i20")
setSignatureForSelector("NSDocument", "_finishSaveDocumentTo:withType:forSaveOperation:withDelegate:didSaveSelector:contextInfo:", "v28@4:8@12@16i20@24:28i32")
setSignatureForSelector("NSDocument", "_pageLayout:didEndAndReturn:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSDocument", "_printOperation:didReturn:contextInfo:", "v16@4:8@12c16i20")
setSignatureForSelector("NSDocument", "_revertPanel:didConfirm:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSDocument", "_runAlertPanelForDocumentMoved:orDocumentRenamed:orDocumentInTrash:orDocumentUnavailable:thenSaveDocumentWithDelegate:didSaveSelector:contextInfo:", "v36@4:8c12c16c20c24@28:32i40")
setSignatureForSelector("NSDocument", "_savePanelDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSDocument", "canCloseDocumentWithDelegate:shouldCloseSelector:contextInfo:", "v16@4:8@12:16i20")
setSignatureForSelector("NSDocument", "runModalPageLayoutWithPrintInfo:delegate:didRunSelector:contextInfo:", "v20@4:8@12@16:20i24")
setSignatureForSelector("NSDocument", "runModalPrintOperation:delegate:didRunSelector:contextInfo:", "v20@4:8@12@16:20i24")
setSignatureForSelector("NSDocument", "runModalSavePanelForSaveOperation:delegate:didSaveSelector:contextInfo:", "v20@4:8i12@16:20i24")
setSignatureForSelector("NSDocument", "saveDocumentWithDelegate:didSaveSelector:contextInfo:", "v16@4:8@12:16i20")
setSignatureForSelector("NSDocument", "saveToFile:saveOperation:delegate:didSaveSelector:contextInfo:", "v24@4:8@12i16@20:24i28")
setSignatureForSelector("NSDocument", "shouldCloseWindowController:delegate:shouldCloseSelector:contextInfo:", "v20@4:8@12@16:20i24")
setSignatureForSelector("NSWindow", "_document:shouldClose:contextInfo:", "v16@4:8@12c16i20")
setSignatureForSelector("NSWindow", "_setTrackingRect:inside:owner:userData:", "i36@4:8{_NSRect={_NSPoint=ff}{_NSSize=ff}}12c28@32i40")
setSignatureForSelector("NSTypesetter", "layoutGlyphsInLayoutManager:startingAtGlyphIndex:maxNumberOfLineFragments:nextGlyphIndex:", "v@:@IIo^I")
setSignatureForSelector("NSCell", "getPeriodicDelay:interval:", "v@:o^fo^f")
setSignatureForSelector("NSProgressPanel", "setCancellationDelegate:wasCancelledSelector:contextInfo:", "v16@4:8@12:16i20")
setSignatureForSelector("NSLayoutManager", "characterRangeForGlyphRange:actualGlyphRange:", "{_NSRange=II}@:{_NSRange=II}o^{_NSRange=II}")
setSignatureForSelector("NSLayoutManager", "getFirstUnlaidCharacterIndex:glyphIndex:", "v@:o^Io^I")
setSignatureForSelector("NSLayoutManager", "glyphAtIndex:isValidIndex:", "I@:Io^c")
setSignatureForSelector("NSLayoutManager", "glyphIndexForPoint:inTextContainer:fractionOfDistanceThroughGlyph:", "I@:{_NSPoint=ff}@o^f")
setSignatureForSelector("NSLayoutManager", "glyphRangeForCharacterRange:actualCharacterRange:", "{_NSRange=II}@:{_NSRange=II}o^{_NSRange=II}")
setSignatureForSelector("NSLayoutManager", "invalidateGlyphsForCharacterRange:changeInLength:actualCharacterRange:", "v@:{_NSRange=II}io^{_NSRange=II}")
setSignatureForSelector("NSLayoutManager", "invalidateLayoutForCharacterRange:isSoft:actualCharacterRange:", "v@:{_NSRange=II}co^{_NSRange=II}")
setSignatureForSelector("NSLayoutManager", "lineFragmentRectForGlyphAtIndex:effectiveRange:", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:Io^{_NSRange=II}")
setSignatureForSelector("NSLayoutManager", "lineFragmentUsedRectForGlyphAtIndex:effectiveRange:", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:Io^{_NSRange=II}")
setSignatureForSelector("NSLayoutManager", "lineFragmentUsedRectForGlyphAtIndex:effectiveRange:allowLayout:", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:Io^{_NSRange=II}c")
setSignatureForSelector("NSLayoutManager", "temporaryAttributesAtCharacterIndex:effectiveRange:", "@@:Io^{_NSRange=II}")
setSignatureForSelector("NSLayoutManager", "textContainerForGlyphAtIndex:effectiveRange:", "@@:Io^{_NSRange=II}")
setSignatureForSelector("NSOpenPanel", "beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v36@4:8@12@16@20@24@28:32i40")
setSignatureForSelector("NSSavePanel", "beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v36@4:8@12@16@20@24@28:32i40")
setSignatureForSelector("NSPrintOperation", "runOperationModalForWindow:delegate:didRunSelector:contextInfo:", "v20@4:8@12@16:20i24")
setSignatureForSelector("NSSpellChecker", "checkSpellingOfString:startingAt:language:wrap:inSpellDocumentWithTag:wordCount:", "{_NSRange=II}@:@i@cio^i")
setSignatureForSelector("NSSpellChecker", "checkSpellingOfString:startingAt:language:wrap:inSpellDocumentWithTag:wordCount:reconnectOnError:", "{_NSRange=II}@:@i@cio^ic")
setSignatureForSelector("NSToolTipManager", "_setToolTip:forView:cell:rect:owner:ownerIsDisplayDelegate:userData:", "i48@4:8@12@16@20{_NSRect={_NSPoint=ff}{_NSSize=ff}}28@44c51i52")
setSignatureForSelector("NSToolTipManager", "setToolTipForView:rect:displayDelegate:userData:", "i36@4:8@12{_NSRect={_NSPoint=ff}{_NSSize=ff}}16@32i40")
setSignatureForSelector("NSToolTipManager", "setToolTipForView:rect:owner:userData:", "i36@4:8@12{_NSRect={_NSPoint=ff}{_NSSize=ff}}16@32i40")
setSignatureForSelector("NSMatrix", "getNumberOfRows:columns:", "v@:o^io^i")
setSignatureForSelector("NSMatrix", "getRow:column:forPoint:", "c@:o^io^i{_NSPoint=ff}")
setSignatureForSelector("NSMatrix", "getRow:column:ofCell:", "c@:o^io^i@")
setSignatureForSelector("NSMatrix", "view:frameForToolTip:point:userData:", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}28@8:12@16i20{_NSPoint=ff}24i32")
setSignatureForSelector("NSMatrix", "view:stringForToolTip:point:userData:", "@24@4:8@12i16{_NSPoint=ff}20i28")
setSignatureForSelector("NSDocumentController", "_document:didSave:contextInfo:", "v16@4:8@12c16i20")
setSignatureForSelector("NSDocumentController", "closeAllDocumentsWithDelegate:didCloseAllSelector:contextInfo:", "v16@4:8@12:16i20")
setSignatureForSelector("NSDocumentController", "reviewUnsavedDocumentsWithAlertTitle:cancellable:delegate:didReviewAllSelector:contextInfo:", "v24@4:8@12c16@20:24i28")
setSignatureForSelector("NSConcretePrintOperation", "_printPanel:didEndAndReturn:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSConcretePrintOperation", "_progressPanelWasCancelled:contextInfo:", "v12@4:8@12i16")
setSignatureForSelector("NSConcretePrintOperation", "_progressPanel:didEndAndReturn:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSPrintPanel", "_sheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSPrintPanel", "beginSheetWithPrintInfo:modalForWindow:delegate:didEndSelector:contextInfo:", "v24@4:8@12@16@20:24i28")
setSignatureForSelector("NSTextContainer", "lineFragmentRectForProposedRect:sweepDirection:movementDirection:remainingRect:", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}iio^{_NSRect={_NSPoint=ff}{_NSSize=ff}}")
setSignatureForSelector("NSApplication", "_commonBeginModalSessionForWindow:relativeToWindow:modalDelegate:didEndSelector:contextInfo:", "^{_NSModalSession=@@^{_NSModalSession}iciI^vi@@:^vi}24@4:8@12@16@20:24i28")
setSignatureForSelector("NSApplication", "beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v@:@@@:i")
setSignatureForSelector("NSAlert", "beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v@:@@@:i")
setSignatureForSelector("NSApplication", "contextID", "i4@4:8")
setSignatureForSelector("NSApplication", "openFile:ok:", "i12@4:8@12o^i16")
setSignatureForSelector("NSApplication", "openTempFile:ok:", "i12@4:8@12o^i16")
setSignatureForSelector("NSApplication", "runModalSession:", "i8@4:8^{_NSModalSession=@@^{_NSModalSession}iciI^vi@@:^vi}12")
setSignatureForSelector("NSView", "adjustPageHeightNew:top:bottom:limit:", "v@:o^ffff")
setSignatureForSelector("NSView", "adjustPageWidthNew:left:right:limit:", "v@:o^ffff")
setSignatureForSelector("NSView", "knowsPageRange:", "c@:o^{_NSRange=II}")
setSignatureForSelector("NSNib", "instantiateNibWithOwner:topLevelObjects:", "c@:@N^@")
setSignatureForSelector("NSWorkspace", "launchAppWithBundleIdentifier:options:additionalEventParamDescriptor:launchIdentifier:", "c24@0:4@8I12@16o^@20")
setSignatureForSelector("NSWorkspace", "openURLs:withAppBundleIdentifier:options:additionalEventParamDescriptor:launchIdentifiers:", "c28@0:4@8@12I16@20o^@24")
setSignatureForSelector("NSTextRulerOptions", "sheetDidEnd:returnCode:contextInfo:", "v@:@ii")
setSignatureForSelector("NSAlert", "beginSheetModalForWindow:modalDelegate:didEndSelector:contextInfo:", "v@:@@:i")
setSignatureForSelector("NSATSTypesetter", "characterRangeForGlyphRange:actualGlyphRange:", "{_NSRange=II}@:{_NSRange=II}o^{_NSRange=II}")
setSignatureForSelector("NSATSTypesetter", "glyphRangeForGlyphRange:actualGlyphRange:", "{_NSRange=II}@:{_NSRange=II}o^{_NSRange=II}")
setSignatureForSelector("NSATSTypesetter", "layoutParagraphAtPoint:", "I@:{_NSPoint=ff}")
setSignatureForSelector("NSATSTypesetter", "lineFragmentRectForProposedRect:remainingRect:", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}o^{_NSRect={_NSPoint=ff}{_NSSize=ff}}")
setSignatureForSelector("NSATSTypesetter", "getLineFragmentRect:usedRect:forParagraphSeparatorGlyphRange:atProposedOrigin:", "v@:o^{_NSRect={_NSPoint=ff}{_NSSize=ff}}o^{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSRange=II}{_NSPoint=ff}")
setSignatureForSelector("NSATSTypesetter", "glyphRangeForCharacterRange:actualCharacterRange:", "{_NSRange=II}@:{_NSRange=II}o^{_NSRange=II}")
setSignatureForSelector("NSSavePanel", "beginForDirectory:file:types:modelessDelegate:didEndSelector:contextInfo:", 'v@:@@@@:i')
setSignatureForSelector("NSOpenGLPixelFormat", "getValues:forAttribute:forVirtualScreen:", 'v@:o^lii')
setSignatureForSelector("NSSavePanel", "gotoSheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSNavFilepathInputController", "sheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
setSignatureForSelector("NSNavFilepathInputController", "beginSheetForSavePanel:withFilepath:didEndSelector:contextInfo:", 'v@:@@:i')
setSignatureForSelector("NSGraphicsContext", "graphicsPort", "^{CGContext=}@:")
#setSignatureForSelector("NSDocument", "initWithType:error:", "@@:@o^@")
