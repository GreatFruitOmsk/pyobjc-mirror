
#
# This file is generated by 'create_byref_module.py'. Do not edit.
#
# Generated from 'AppKit.byref'.
#
#
from objc import set_signature_for_selector

set_signature_for_selector("NSInputManager", "getMarkedText:selectedRange:", "v@:o^@o^{_NSRange=II}")
set_signature_for_selector("NSToolbar", "_configSheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSEvent", "enterExitEventWithType:location:modifierFlags:timestamp:windowNumber:context:eventNumber:trackingNumber:userData:", "@52@4:8i12{_NSPoint=ff}16I24d36i40@44i48i52i56")
set_signature_for_selector("NSButton", "getPeriodicDelay:interval:", "v@:o^fo^f")
set_signature_for_selector("NSView", "addToolTipRect:owner:userData:", "i28@4:8{_NSRect={_NSPoint=ff}{_NSSize=ff}}12@28i32")
set_signature_for_selector("NSAlert", "didEndSheet:returnCode:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSSavePanel", "_runModalForDirectory:file:relativeToWindow:modalDelegate:didEndSelector:contextInfo:", "v28@4:8@12@16@20@24:28i32")
set_signature_for_selector("NSSavePanel", "beginSheetForDirectory:file:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v28@4:8@12@16@20@24:28i32")
set_signature_for_selector("NSSavePanel", "didEndSheet:returnCode:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSPageLayout", "_sheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSPageLayout", "beginSheetWithPrintInfo:modalForWindow:delegate:didEndSelector:contextInfo:", "v24@4:8@12@16@20:24i28")
set_signature_for_selector("NSPageLayout", "convertOldFactor:newFactor:", "v@:i^fo^f")
set_signature_for_selector("NSBitmapImageRep", "getCompression:factor:", "v@:o^io^f")
set_signature_for_selector("NSColor", "getCyan:magenta:yellow:black:alpha:", "v@:o^fo^fo^fo^f")
set_signature_for_selector("NSColor", "getHue:saturation:brightness:alpha:", "v@:o^fo^fo^fo^f")
set_signature_for_selector("NSColor", "getRed:green:blue:alpha:", "v@:o^fo^fo^fo^f")
set_signature_for_selector("NSColor", "getWhite:alpha:", "v@:o^fo^f")
set_signature_for_selector("NSWorkspace", "getFileSystemInfoForPath:isRemovable:isWritable:isUnmountable:description:type:", "c28@4:8@12o^c16o^c20o^c24o^@28o^@32")
set_signature_for_selector("NSWorkspace", "getInfoForFile:application:type:", "c16@4:8@12o^@16o^@20")
set_signature_for_selector("NSDocument", "_changeAlertDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSDocument", "_compatibility_canCloseDocumentWithDelegate:shouldCloseSelector:contextInfo:", "v16@4:8@12:16i20")
set_signature_for_selector("NSDocument", "_compatibility_doSavePanelSave:delegate:didSaveSelector:contextInfo:", "v20@4:8i12@16:20i24")
set_signature_for_selector("NSDocument", "_compatibility_shouldCloseWindowController:delegate:shouldCloseSelector:contextInfo:", "v20@4:8@12@16:20i24")
set_signature_for_selector("NSDocument", "_didEndCloseSheet:returnCode:closeContext:", "v16@4:8@12i16i20")
set_signature_for_selector("NSDocument", "_document:pageLayoutDidReturn:contextInfo:", "v16@4:8@12c16i20")
set_signature_for_selector("NSDocument", "_finishSaveDocumentTo:withType:forSaveOperation:withDelegate:didSaveSelector:contextInfo:", "v28@4:8@12@16i20@24:28i32")
set_signature_for_selector("NSDocument", "_pageLayout:didEndAndReturn:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSDocument", "_printOperation:didReturn:contextInfo:", "v16@4:8@12c16i20")
set_signature_for_selector("NSDocument", "_revertPanel:didConfirm:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSDocument", "_runAlertPanelForDocumentMoved:orDocumentRenamed:orDocumentInTrash:orDocumentUnavailable:thenSaveDocumentWithDelegate:didSaveSelector:contextInfo:", "v36@4:8c12c16c20c24@28:32i40")
set_signature_for_selector("NSDocument", "_savePanelDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSDocument", "canCloseDocumentWithDelegate:shouldCloseSelector:contextInfo:", "v16@4:8@12:16i20")
set_signature_for_selector("NSDocument", "runModalPageLayoutWithPrintInfo:delegate:didRunSelector:contextInfo:", "v20@4:8@12@16:20i24")
set_signature_for_selector("NSDocument", "runModalPrintOperation:delegate:didRunSelector:contextInfo:", "v20@4:8@12@16:20i24")
set_signature_for_selector("NSDocument", "runModalSavePanelForSaveOperation:delegate:didSaveSelector:contextInfo:", "v20@4:8i12@16:20i24")
set_signature_for_selector("NSDocument", "saveDocumentWithDelegate:didSaveSelector:contextInfo:", "v16@4:8@12:16i20")
set_signature_for_selector("NSDocument", "saveToFile:saveOperation:delegate:didSaveSelector:contextInfo:", "v24@4:8@12i16@20:24i28")
set_signature_for_selector("NSDocument", "shouldCloseWindowController:delegate:shouldCloseSelector:contextInfo:", "v20@4:8@12@16:20i24")
set_signature_for_selector("NSWindow", "_document:shouldClose:contextInfo:", "v16@4:8@12c16i20")
set_signature_for_selector("NSWindow", "_setTrackingRect:inside:owner:userData:", "i36@4:8{_NSRect={_NSPoint=ff}{_NSSize=ff}}12c28@32i40")
set_signature_for_selector("NSProgressPanel", "setCancellationDelegate:wasCancelledSelector:contextInfo:", "v16@4:8@12:16i20")
set_signature_for_selector("NSOpenPanel", "beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v36@4:8@12@16@20@24@28:32i40")
set_signature_for_selector("NSPrintOperation", "runOperationModalForWindow:delegate:didRunSelector:contextInfo:", "v20@4:8@12@16:20i24")
set_signature_for_selector("NSToolTipManager", "_setToolTip:forView:cell:rect:owner:ownerIsDisplayDelegate:userData:", "i48@4:8@12@16@20{_NSRect={_NSPoint=ff}{_NSSize=ff}}28@44c51i52")
set_signature_for_selector("NSToolTipManager", "setToolTipForView:rect:displayDelegate:userData:", "i36@4:8@12{_NSRect={_NSPoint=ff}{_NSSize=ff}}16@32i40")
set_signature_for_selector("NSToolTipManager", "setToolTipForView:rect:owner:userData:", "i36@4:8@12{_NSRect={_NSPoint=ff}{_NSSize=ff}}16@32i40")
set_signature_for_selector("NSMatrix", "getNumberOfRows:columns:", "v@:o^io^i")
set_signature_for_selector("NSMatrix", "getRow:column:forPoint:", "c@:o^io^i{_NSPoint=ff}")
set_signature_for_selector("NSMatrix", "getRow:column:ofCell:", "c@:o^io^i@")
set_signature_for_selector("NSMatrix", "view:frameForToolTip:point:userData:", "{_NSRect={_NSPoint=ff}{_NSSize=ff}}28@8:12@16i20{_NSPoint=ff}24i32")
set_signature_for_selector("NSMatrix", "view:stringForToolTip:point:userData:", "@24@4:8@12i16{_NSPoint=ff}20i28")
set_signature_for_selector("NSDocumentController", "_document:didSave:contextInfo:", "v16@4:8@12c16i20")
set_signature_for_selector("NSDocumentController", "closeAllDocumentsWithDelegate:didCloseAllSelector:contextInfo:", "v16@4:8@12:16i20")
set_signature_for_selector("NSDocumentController", "reviewUnsavedDocumentsWithAlertTitle:cancellable:delegate:didReviewAllSelector:contextInfo:", "v24@4:8@12c16@20:24i28")
set_signature_for_selector("NSConcretePrintOperation", "_printPanel:didEndAndReturn:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSConcretePrintOperation", "_progressPanelWasCancelled:contextInfo:", "v12@4:8@12i16")
set_signature_for_selector("NSConcretePrintOperation", "_progressPanel:didEndAndReturn:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSPrintPanel", "_sheetDidEnd:returnCode:contextInfo:", "v16@4:8@12i16i20")
set_signature_for_selector("NSPrintPanel", "beginSheetWithPrintInfo:modalForWindow:delegate:didEndSelector:contextInfo:", "v24@4:8@12@16@20:24i28")
set_signature_for_selector("NSApplication", "_commonBeginModalSessionForWindow:relativeToWindow:modalDelegate:didEndSelector:contextInfo:", "^{_NSModalSession=@@^{_NSModalSession}iciI^vi@@:^vi}24@4:8@12@16@20:24i28")
set_signature_for_selector("NSApplication", "beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:", "v@:@@@:i")
set_signature_for_selector("NSApplication", "contextID", "i4@4:8")
set_signature_for_selector("NSApplication", "openFile:ok:", "i12@4:8@12o^i16")
set_signature_for_selector("NSApplication", "openTempFile:ok:", "i12@4:8@12o^i16")
set_signature_for_selector("NSApplication", "runModalSession:", "i8@4:8^{_NSModalSession=@@^{_NSModalSession}iciI^vi@@:^vi}12")
