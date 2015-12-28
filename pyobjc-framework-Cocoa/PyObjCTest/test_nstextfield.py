from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSTextField (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSTextField.drawsBackground)
        self.assertArgIsBOOL(NSTextField.setDrawsBackground_, 0)
        self.assertResultIsBOOL(NSTextField.isBordered)
        self.assertArgIsBOOL(NSTextField.setBordered_, 0)
        self.assertResultIsBOOL(NSTextField.isBezeled)
        self.assertArgIsBOOL(NSTextField.setBezeled_, 0)
        self.assertResultIsBOOL(NSTextField.isEditable)
        self.assertArgIsBOOL(NSTextField.setEditable_, 0)
        self.assertResultIsBOOL(NSTextField.isSelectable)
        self.assertArgIsBOOL(NSTextField.setSelectable_, 0)
        self.assertResultIsBOOL(NSTextField.textShouldBeginEditing_)
        self.assertResultIsBOOL(NSTextField.textShouldEndEditing_)
        self.assertResultIsBOOL(NSTextField.acceptsFirstResponder)
        self.assertResultIsBOOL(NSTextField.allowsEditingTextAttributes)
        self.assertArgIsBOOL(NSTextField.setAllowsEditingTextAttributes_, 0)
        self.assertResultIsBOOL(NSTextField.importsGraphics)
        self.assertArgIsBOOL(NSTextField.setImportsGraphics_, 0)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSTextField.allowsDefaultTighteningForTruncation)
        self.assertArgIsBOOL(NSTextField.setAllowsDefaultTighteningForTruncation_, 0)

    @min_sdk_level('10.6')
    def testProtocols(self):
        objc.protocolNamed('NSTextFieldDelegate')

if __name__ == "__main__":
    main()
