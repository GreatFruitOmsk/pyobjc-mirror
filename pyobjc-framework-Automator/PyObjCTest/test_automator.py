'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import Automator

class TestAutomator (TestCase):
    def testClasses(self):
        self.assert_( hasattr(Automator, 'AMAction') )
        self.assert_( isinstance(Automator.AMAction, objc.objc_class) )

        self.assert_( hasattr(Automator, 'AMAppleScriptAction') )
        self.assert_( isinstance(Automator.AMAppleScriptAction, objc.objc_class) )

    def testInformalProtocols(self):
        self.assertFalse(hasattr(Automator, 'protocols'))


if __name__ == "__main__":
    main()
