
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMAction (TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertIsVararg(AMAction.logMessageWithLevel_format_)
        self.assertIsArgIsFormat(AMAction.logMessageWithLevel_format_, 1)
        self.assertArgIsOut(AMAction.runWithInput_error_, 1)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsOut(AMAction.initWithContentsOfURL_error_, 1)
        self.assertArgIsBOOL(AMAction.initWithDefinition_fromArchive_, 1)
        self.assertResultIsBOOL(AMAction.ignoresInput)

    def testMethods(self):
        self.assertArgIsOut(AMAction.runWithInput_fromAction_error_, 2)
        self.assertResultIsBOOL(AMAction.isStopped)

if __name__ == "__main__":
    main()
