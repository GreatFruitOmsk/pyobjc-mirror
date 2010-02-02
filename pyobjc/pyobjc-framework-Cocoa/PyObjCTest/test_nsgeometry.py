from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation


class TestNSGeometry (TestCase):
    def testConstants(self):
        self.assertEqual(NSMinXEdge, 0)
        self.assertEqual(NSMinYEdge, 1)
        self.assertEqual(NSMaxXEdge, 2)
        self.assertEqual(NSMaxYEdge, 3)

        self.assertEqual(NSZeroPoint, NSPoint())
        self.assertEqual(NSZeroSize, NSSize())
        self.assertEqual(NSZeroRect, NSRect())

    def testInlines(self):
        self.assertEqual(NSMakePoint(1, 2), NSPoint(1, 2))
        self.assertEqual(NSMakeSize(4, 5), NSSize(4, 5))
        self.assertEqual(NSMakeRect(1, 2, 3, 4), NSRect(NSPoint(1, 2), NSSize(3, 4)))

        rect = NSRect(NSPoint(1,2), NSSize(4,6))
        self.assertEqual(NSMaxX(rect), 5)
        self.assertEqual(NSMaxY(rect), 8)
        self.assertEqual(NSMidX(rect), 3)
        self.assertEqual(NSMidY(rect), 5)
        self.assertEqual(NSMinX(rect), 1)
        self.assertEqual(NSMinY(rect), 2)
        self.assertEqual(NSWidth(rect), 4)
        self.assertEqual(NSHeight(rect), 6)
       
        # Cannot test these here, need to be tested in the Quartz unittests
        self.assertHasAttr(Foundation, 'NSRectFromCGRect')
        self.assertHasAttr(Foundation, 'NSRectToCGRect')
        self.assertHasAttr(Foundation, 'NSPointFromCGPoint')
        self.assertHasAttr(Foundation, 'NSPointToCGPoint')
        self.assertHasAttr(Foundation, 'NSSizeFromCGSize')
        self.assertHasAttr(Foundation, 'NSSizeToCGSize')
    def testFunctions(self):
        p1 = NSPoint(1, 2)
        p2 = NSPoint(3, 4)
        
        s1 = NSSize(4, 5)
        s2 = NSSize(7, 8)

        r0 = NSRect(NSPoint(9, 10), NSSize(0, 0))
        r1 = NSRect(NSPoint(0, 1), NSSize(4, 5))
        r2 = NSRect(NSPoint(4.5, 5.5), NSSize(7.5, 8.5))



        self.assertIsObject(NSEqualPoints(p1, p1), True)
        self.assertIsObject(NSEqualPoints(p1, p2), False)
        self.assertIsObject(NSEqualSizes(s1, s1), True)
        self.assertIsObject(NSEqualSizes(s1, s2), False)
        self.assertIsObject(NSEqualRects(r1, r1), True)
        self.assertIsObject(NSEqualRects(r1, r2), False)
        self.assertIsObject(NSIsEmptyRect(r0), True)
        self.assertIsObject(NSIsEmptyRect(r1), False)
        ra = NSInsetRect(r1, 2, 3)
        self.assertEqual(ra, NSRect(NSPoint(2, 4), NSSize(0, -1)))

        ra = NSIntegralRect(r2)
        self.assertEqual(ra, NSRect(NSPoint(4, 5), NSSize(8, 9)))

        ra = NSUnionRect(r1, r2)
        self.assertEqual(ra, NSRect(NSPoint(0, 1), NSSize(12, 13)))

        ra = NSIntersectionRect(r1, r2)
        self.assertEqual(ra, NSRect(NSPoint(0, 0), NSSize(0, 0)))

        ra = NSOffsetRect(r1, 5, 6)
        self.assertEqual(ra, NSRect(NSPoint(5, 7), NSSize(4,5)))

        slice, rem = NSDivideRect(r2, None, None, 1.5, NSMaxYEdge)
        self.assertEqual(slice, NSRect(NSPoint(4.5, 12.5), NSSize(7.5, 1.5))) 
        self.assertEqual(rem, NSRect(NSPoint(4.5, 5.5), NSSize(7.5, 7.0)))

        self.assertIsObject(NSPointInRect(p1, r1), True)
        self.assertIsObject(NSMouseInRect(p1, r1, False), True)
        self.assertIsObject(NSMouseInRect(p2, r2, True), False)
        self.assertIsObject(NSContainsRect(r1, r2), False)
        self.assertIsObject(NSIntersectsRect(r1, r2), False)
        self.assertEqual(NSStringFromPoint(p1), u'{1, 2}')
        self.assertEqual(NSStringFromSize(s1), u'{4, 5}')
        self.assertEqual(NSStringFromRect(r1),  u'{{0, 1}, {4, 5}}')
        v = NSPointFromString('{1, 2}')
        self.assertEqual(v, p1)
        v = NSSizeFromString('{4,5}')
        self.assertEqual(v, s1)
        v = NSRectFromString(u'{   {0,1}  , {  4, 5}}')
        self.assertEqual(v, r1)

    def testValueMethods(self):
        v = NSValue.valueWithPoint_(NSPoint(2, 3))
        w = v.pointValue()
        self.assertIsInstance(w, NSPoint)
        self.assertEqual(w, (2,3))

        w = v.sizeValue()
        self.assertIsInstance(w, NSSize)
        self.assertEqual(w, (2,3))

        v = NSValue.valueWithSize_(NSSize(9, 8))
        w = v.sizeValue()
        self.assertIsInstance(w, NSSize)
        self.assertEqual(w, (9,8))

        v = NSValue.valueWithRect_(NSRect(NSPoint(9, 10), NSSize(11, 12)))
        w = v.rectValue()
        self.assertIsInstance(w, NSRect)
        self.assertEqual(w, ((9,10),(11,12)))

        self.assertArgHasType(NSValue.valueWithPoint_, 0, NSPoint.__typestr__)
        self.assertResultHasType(NSValue.pointValue, NSPoint.__typestr__)
        self.assertArgHasType(NSValue.valueWithSize_, 0, NSSize.__typestr__)
        self.assertResultHasType(NSValue.sizeValue, NSSize.__typestr__)
        self.assertArgHasType(NSValue.valueWithRect_, 0, NSRect.__typestr__)
        self.assertResultHasType(NSValue.rectValue, NSRect.__typestr__)


    def testCoderMethods(self):
        self.assertArgHasType(NSCoder.encodePoint_, 0, NSPoint.__typestr__)
        self.assertResultHasType(NSCoder.decodePoint, NSPoint.__typestr__)
        self.assertArgHasType(NSCoder.encodeSize_, 0, NSSize.__typestr__)
        self.assertResultHasType(NSCoder.decodeSize, NSSize.__typestr__)
        self.assertArgHasType(NSCoder.encodeRect_, 0, NSRect.__typestr__)
        self.assertResultHasType(NSCoder.decodeRect, NSRect.__typestr__)


if __name__ == "__main__":
    main()
