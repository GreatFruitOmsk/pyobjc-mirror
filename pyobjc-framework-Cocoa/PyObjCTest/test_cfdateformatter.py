from PyObjCTools.TestSupport import *
from CoreFoundation import *



class TestDateFormatter (TestCase):
    def testTypeID(self):
        self.assertIsInstance(CFDateGetTypeID(), (int, long))

    def testConstants(self):
        self.assertEqual(kCFDateFormatterNoStyle , 0)
        self.assertEqual(kCFDateFormatterShortStyle , 1)
        self.assertEqual(kCFDateFormatterMediumStyle , 2)
        self.assertEqual(kCFDateFormatterLongStyle , 3)
        self.assertEqual(kCFDateFormatterFullStyle , 4)
        self.assertIsInstance(kCFDateFormatterIsLenient, unicode)
        self.assertIsInstance(kCFDateFormatterTimeZone, unicode)
        self.assertIsInstance(kCFDateFormatterCalendarName, unicode)
        self.assertIsInstance(kCFDateFormatterDefaultFormat, unicode)
        self.assertIsInstance(kCFDateFormatterTwoDigitStartDate, unicode)
        self.assertIsInstance(kCFDateFormatterDefaultDate, unicode)
        self.assertIsInstance(kCFDateFormatterCalendar, unicode)
        self.assertIsInstance(kCFDateFormatterEraSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterMonthSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterShortMonthSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterWeekdaySymbols, unicode)
        self.assertIsInstance(kCFDateFormatterShortWeekdaySymbols, unicode)
        self.assertIsInstance(kCFDateFormatterAMSymbol, unicode)
        self.assertIsInstance(kCFDateFormatterPMSymbol, unicode)
        self.assertIsInstance(kCFDateFormatterLongEraSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterVeryShortMonthSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterStandaloneMonthSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterShortStandaloneMonthSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterVeryShortStandaloneMonthSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterVeryShortWeekdaySymbols, unicode)
        self.assertIsInstance(kCFDateFormatterStandaloneWeekdaySymbols, unicode)
        self.assertIsInstance(kCFDateFormatterShortStandaloneWeekdaySymbols, unicode)
        self.assertIsInstance(kCFDateFormatterVeryShortStandaloneWeekdaySymbols, unicode)
        self.assertIsInstance(kCFDateFormatterQuarterSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterShortQuarterSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterStandaloneQuarterSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterShortStandaloneQuarterSymbols, unicode)
        self.assertIsInstance(kCFDateFormatterGregorianStartDate, unicode)

        self.assertEqual(kCFISO8601DateFormatWithYear, 1 << 0)
        self.assertEqual(kCFISO8601DateFormatWithMonth, 1 << 1)
        self.assertEqual(kCFISO8601DateFormatWithWeekOfYear, 1 << 2)
        self.assertEqual(kCFISO8601DateFormatWithDay, 1 << 4)
        self.assertEqual(kCFISO8601DateFormatWithTime, 1 << 5)
        self.assertEqual(kCFISO8601DateFormatWithTimeZone, 1 << 6)
        self.assertEqual(kCFISO8601DateFormatWithSpaceBetweenDateAndTime, 1 << 7)
        self.assertEqual(kCFISO8601DateFormatWithDashSeparatorInDate, 1 << 8)
        self.assertEqual(kCFISO8601DateFormatWithColonSeparatorInTime, 1 << 9)
        self.assertEqual(kCFISO8601DateFormatWithColonSeparatorInTimeZone, 1 << 10)
        self.assertEqual(kCFISO8601DateFormatWithFractionalSeconds, 1 << 11)
        self.assertEqual(kCFISO8601DateFormatWithFullDate, kCFISO8601DateFormatWithYear | kCFISO8601DateFormatWithMonth | kCFISO8601DateFormatWithDay | kCFISO8601DateFormatWithDashSeparatorInDate)
        self.assertEqual(kCFISO8601DateFormatWithFullTime, kCFISO8601DateFormatWithTime | kCFISO8601DateFormatWithColonSeparatorInTime | kCFISO8601DateFormatWithTimeZone | kCFISO8601DateFormatWithColonSeparatorInTimeZone)
        self.assertEqual(kCFISO8601DateFormatWithInternetDateTime, kCFISO8601DateFormatWithFullDate | kCFISO8601DateFormatWithFullTime)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCFDateFormatterDoesRelativeDateFormattingKey, unicode)

    @min_os_level('10.6')
    def testFunction10_6(self):
        self.assertResultIsCFRetained(CFDateFormatterCreateDateFormatFromTemplate)
        r = CFDateFormatterCreateDateFormatFromTemplate(None, "%Y-%m-%d", 0, None)
        self.assertIsInstance(r, unicode)

    @min_os_level('10.12')
    def testFunctions10_12(self):
        self.assertResultIsCFRetained(CFDateFormatterCreateISO8601Formatter)

    def testTypes(self):
        self.assertIsCFType(CFDateFormatterRef)

        self.assertIsInstance(CFDateFormatterGetTypeID(), (int, long))

    def testInspection(self):
        locale = CFLocaleCopyCurrent()
        self.assertIsInstance(locale, CFLocaleRef)

        date = CFDateCreate(None, CFAbsoluteTimeGetCurrent())
        self.assertIsInstance(date, NSDate)

        self.assertResultIsCFRetained(CFDateFormatterCreate)
        fmt = CFDateFormatterCreate(None, locale, kCFDateFormatterShortStyle, kCFDateFormatterLongStyle)
        self.assertIsInstance(fmt, CFDateFormatterRef)
        v = CFDateFormatterGetLocale(fmt)
        self.assertEqual(CFLocaleGetIdentifier(locale), CFLocaleGetIdentifier(v))

        v = CFDateFormatterGetDateStyle(fmt)
        self.assertEqual(v, kCFDateFormatterShortStyle)

        v = CFDateFormatterGetTimeStyle(fmt)
        self.assertEqual(v, kCFDateFormatterLongStyle)

        v = CFDateFormatterGetFormat(fmt)
        self.assertIsInstance(v, unicode)
        CFDateFormatterSetFormat(fmt, v[:-1])
        v2 = CFDateFormatterGetFormat(fmt)
        self.assertEqual(v[:-1], v2)

        v = CFDateFormatterCreateStringWithDate(None, fmt, date)
        self.assertIsInstance(v, unicode)
        v = CFDateFormatterCreateStringWithAbsoluteTime(None, fmt, CFAbsoluteTimeGetCurrent())
        self.assertIsInstance(v, unicode)
        dt, rng = CFDateFormatterCreateDateFromString(None, fmt, v, (0, len(v)))
        self.assertIsInstance(dt, NSDate)
        self.assertIsInstance(rng, CFRange)
        ok, rng, abstime = CFDateFormatterGetAbsoluteTimeFromString(fmt, v, (0, len(v)), None)
        self.assertIs(ok, True)
        self.assertIsInstance(rng, CFRange)
        self.assertIsInstance(abstime, float)
        self.assertResultIsCFRetained(CFDateFormatterCopyProperty)
        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterCalendarName)
        self.assertIsInstance(v, unicode)
        CFDateFormatterSetProperty(fmt, kCFDateFormatterCalendarName, b"gregorian".decode('latin1'))
        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterCalendarName)
        self.assertIsInstance(v, unicode)
        self.assertEqual(v , b"gregorian".decode('latin1'))
        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterIsLenient)
        self.assertTrue(v is True or v is False)
        CFDateFormatterSetProperty(fmt, kCFDateFormatterIsLenient, True)
        v2 = CFDateFormatterCopyProperty(fmt, kCFDateFormatterIsLenient)
        self.assertIs(v2, True)

if __name__ == "__main__":
    main()
