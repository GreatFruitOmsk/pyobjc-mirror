
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTStringAttributes (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCTFontAttributeName, unicode)
        self.failUnlessIsInstance(kCTKernAttributeName, unicode)
        self.failUnlessIsInstance(kCTLigatureAttributeName, unicode)
        self.failUnlessIsInstance(kCTForegroundColorAttributeName, unicode)
        self.failUnlessIsInstance(kCTParagraphStyleAttributeName, unicode)
        self.failUnlessIsInstance(kCTUnderlineStyleAttributeName, unicode)
        self.failUnlessIsInstance(kCTVerticalFormsAttributeName, unicode)
        self.failUnlessIsInstance(kCTGlyphInfoAttributeName, unicode)
        self.failUnlessEqual(kCTUnderlineStyleNone,  0x00)
        self.failUnlessEqual(kCTUnderlineStyleSingle,  0x01)
        self.failUnlessEqual(kCTUnderlineStyleThick,  0x02)
        self.failUnlessEqual(kCTUnderlineStyleDouble,  0x09)
        self.failUnlessEqual(kCTUnderlinePatternSolid,  0x0000)
        self.failUnlessEqual(kCTUnderlinePatternDot,  0x0100)
        self.failUnlessEqual(kCTUnderlinePatternDash,  0x0200)
        self.failUnlessEqual(kCTUnderlinePatternDashDot,  0x0300)
        self.failUnlessEqual(kCTUnderlinePatternDashDotDot,  0x0400)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kCTForegroundColorFromContextAttributeName, unicode)
        self.failUnlessIsInstance(kCTSuperscriptAttributeName, unicode)
        self.failUnlessIsInstance(kCTUnderlineColorAttributeName, unicode)
        self.failUnlessIsInstance(kCTCharacterShapeAttributeName, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCTStrokeWidthAttributeName, unicode)
        self.failUnlessIsInstance(kCTStrokeColorAttributeName, unicode)


if __name__ == "__main__":
    main()
