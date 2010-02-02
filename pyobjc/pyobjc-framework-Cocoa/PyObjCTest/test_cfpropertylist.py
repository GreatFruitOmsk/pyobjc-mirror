from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestPropertyList (TestCase):
    def testFunctions(self):
        dta = CFPropertyListCreateXMLData(None, {u"key": 42, u"key2": 1})
        self.assertIsInstance(dta, CFDataRef)
        self.assertArgIsOut(CFPropertyListCreateFromXMLData, 3)
        v, err = CFPropertyListCreateFromXMLData(None, dta, 0, None)
        self.assertIsObject(err, None)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertIsIn('key', v)
        self.assertIsIn('key2', v)
        self.assertEqual(v['key'] , 42)
        self.assertEqual(v['key2'] , True)
        v = CFPropertyListCreateDeepCopy(None, {u"key": 42, u"key2": True}, 0)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertIsIn('key', v)
        self.assertIsIn('key2', v)
        self.assertEqual(v['key'] , 42)
        self.assertEqual(v['key2'] , True)
        valid = CFPropertyListIsValid({u"key": 42, u"key2": True}, kCFPropertyListBinaryFormat_v1_0)
        self.assertIsObject(valid, True)
    def testStreams(self):

        stream = CFWriteStreamCreateWithAllocatedBuffers(kCFAllocatorDefault, kCFAllocatorDefault)
        r = CFWriteStreamOpen(stream)
        self.assertTrue(r)

        value = {u'key1': 42, u'key2': 1}

        self.assertArgIsOut(CFPropertyListWriteToStream, 3)
        rval, errorString = CFPropertyListWriteToStream(value, stream, 
                kCFPropertyListXMLFormat_v1_0, None)
        self.assertIsInstance(rval, (int, long))
        self.assertTrue(rval)
        self.assertIsObject(errorString, None)
        buf = CFWriteStreamCopyProperty(stream, kCFStreamPropertyDataWritten)
        self.assertIsInstance(buf, CFDataRef)
        buf = CFDataGetBytes(buf, (0, CFDataGetLength(buf)), None)
        self.assertIsInstance(buf, str)
        self.assertIsIn('<key>key1</key>', buf)
        self.assertIsIn('<integer>42</integer>', buf)
        self.assertIsIn('<key>key2</key>', buf)
        self.assertIsIn('<integer>1</integer>', buf)
        stream = CFReadStreamCreateWithBytesNoCopy(None, buf, len(buf), kCFAllocatorNull)
        r = CFReadStreamOpen(stream)
        self.assertTrue(r)

        self.assertArgIsOut(CFPropertyListCreateFromStream, 4)
        self.assertArgIsOut(CFPropertyListCreateFromStream, 5)
        res, format, errorString = CFPropertyListCreateFromStream(None, stream, 0, 0, None, None)
        self.assertEqual(format, kCFPropertyListXMLFormat_v1_0)
        self.assertIsObject(errorString, None)
        self.assertEqual(res, value)



    def testConstants(self):
        self.assertEqual(kCFPropertyListImmutable , 0)
        self.assertEqual(kCFPropertyListMutableContainers , 1)
        self.assertEqual(kCFPropertyListMutableContainersAndLeaves , 2)
        self.assertEqual(kCFPropertyListOpenStepFormat , 1)
        self.assertEqual(kCFPropertyListXMLFormat_v1_0 , 100)
        self.assertEqual(kCFPropertyListBinaryFormat_v1_0 , 200)
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFPropertyListReadCorruptError, 3840)
        self.assertEqual(kCFPropertyListReadUnknownVersionError, 3841)
        self.assertEqual(kCFPropertyListReadStreamError, 3842)
        self.assertEqual(kCFPropertyListWriteStreamError, 3851)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        dta = CFPropertyListCreateXMLData(None, {u"key": 42, u"key2": 1})
        self.assertIsInstance(dta, CFDataRef)
        bytes = CFDataGetBytes(dta, (0, CFDataGetLength(dta)), None)
        self.assertIsNotObject(bytes, None)
        self.assertResultIsCFRetained(CFPropertyListCreateWithData)
        self.assertArgIsOut(CFPropertyListCreateWithData, 3)
        self.assertArgIsOut(CFPropertyListCreateWithData, 4)
        v, fmt, err = CFPropertyListCreateWithData(None, dta, 0, None, None)
        self.assertIsNotObject(v, None)
        self.assertIsInstance(fmt, (int, long))
        self.assertIsObject(err, None)
        stream = CFReadStreamCreateWithBytesNoCopy(None, bytes, len(bytes), kCFAllocatorNull)
        CFReadStreamOpen(stream)

        self.assertResultIsCFRetained(CFPropertyListCreateWithStream)
        self.assertArgIsOut(CFPropertyListCreateWithStream, 4)
        self.assertArgIsOut(CFPropertyListCreateWithStream, 5)
        v, fmt, err = CFPropertyListCreateWithStream(None, stream, len(bytes), 0, None, None)
        self.assertIsNotObject(v, None)
        self.assertIsInstance(fmt, (int, long))
        self.assertIsObject(err, None)
        import array
        buf = array.array('b', ' '*1024)

        stream = CFWriteStreamCreateWithBuffer(None, buf, 1024)
        CFWriteStreamOpen(stream)

        self.assertArgIsOut(CFPropertyListWrite, 4)
        cnt, err = CFPropertyListWrite({'key':42}, stream, kCFPropertyListBinaryFormat_v1_0, 0, None)
        self.assertNotEqual(cnt, 0)
        self.assertEqual(err, None)

        self.assertResultIsCFRetained(CFPropertyListCreateData)
        self.assertArgIsOut(CFPropertyListCreateData, 4)
        dta, err = CFPropertyListCreateData(None, {'key':'value'}, kCFPropertyListBinaryFormat_v1_0, 0, None)
        self.assertIsInstance(dta, CFDataRef)
        self.assertEqual(err, None)



if __name__ == "__main__":
    main()
