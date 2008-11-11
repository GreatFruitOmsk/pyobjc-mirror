import unittest
from CoreFoundation import *
import errno, time, os, socket


class TestStream (unittest.TestCase):
    def testConstants(self):
        self.failUnless(kCFStreamStatusNotOpen == 0)
        self.failUnless(kCFStreamStatusOpening == 1)
        self.failUnless(kCFStreamStatusOpen == 2)
        self.failUnless(kCFStreamStatusReading == 3) 
        self.failUnless(kCFStreamStatusWriting == 4)
        self.failUnless(kCFStreamStatusAtEnd == 5)
        self.failUnless(kCFStreamStatusClosed == 6)
        self.failUnless(kCFStreamStatusError == 7)

        self.failUnless(kCFStreamEventNone == 0)
        self.failUnless(kCFStreamEventOpenCompleted == 1)
        self.failUnless(kCFStreamEventHasBytesAvailable == 2)
        self.failUnless(kCFStreamEventCanAcceptBytes == 4)
        self.failUnless(kCFStreamEventErrorOccurred == 8)
        self.failUnless(kCFStreamEventEndEncountered == 16)

        self.failUnless(kCFStreamErrorDomainCustom == -1)
        self.failUnless(kCFStreamErrorDomainPOSIX == 1)
        self.failUnless(kCFStreamErrorDomainMacOSStatus == 2)

        self.failUnless(isinstance(kCFStreamPropertyDataWritten, unicode))
        self.failUnless(isinstance(kCFStreamPropertyAppendToFile, unicode))
        self.failUnless(isinstance(kCFStreamPropertyFileCurrentOffset, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketNativeHandle, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketRemoteHostName, unicode))
        self.failUnless(isinstance(kCFStreamPropertySocketRemotePortNumber, unicode))

    def testStructs(self):
        o = CFStreamError()
        self.failUnless(hasattr(o, 'domain'))
        self.failUnless(hasattr(o, 'error'))


    def testGetTypeID(self):
        v = CFReadStreamGetTypeID()
        self.failUnless(isinstance(v, (int, long)))
        
        v = CFWriteStreamGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testReadStream(self):
        strval = "hello world"
        stream = CFReadStreamCreateWithBytesNoCopy(None,
                strval, len(strval), kCFAllocatorNull)
        self.failUnless(isinstance(stream, CFReadStreamRef))

        r, buf = CFReadStreamRead(stream, None, 10)
        self.assertEquals(r, -1)
        self.assertEquals(buf, '')

        err  = CFReadStreamCopyError(stream)
        self.failUnless(err is None or isinstance(err, CFErrorRef))

        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        r = CFReadStreamOpen(stream)
        self.failUnless(r is True)

        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusOpen)

        r = CFReadStreamHasBytesAvailable(stream)
        self.failUnless(r is True)

        r, buf = CFReadStreamRead(stream, None, 5)
        self.assertEquals(r, 5)
        self.assertEquals(buf, "hello")

        r, buf = CFReadStreamRead(stream, None, 10)
        self.assertEquals(r, 6)
        self.assertEquals(buf, " world")

        r = CFReadStreamHasBytesAvailable(stream)
        self.failUnless(r is False)

        r = CFReadStreamClose(stream)
        self.failUnless(r is None)
        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusClosed)


        del stream

        stream = CFReadStreamCreateWithFile(None, 
                    CFURLCreateWithString(None, u"file:///etc/shells", None))
        self.failUnless(isinstance(stream, CFReadStreamRef))
        r = CFReadStreamOpen(stream)
        self.failUnless(r is True)

        status = CFReadStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusOpen)

        r, buf = CFReadStreamRead(stream, None, 5)
        self.assertEquals(r, 5)
        self.failUnless(isinstance(buf, str))

        buf, numBytes = CFReadStreamGetBuffer(stream, 20, None)
        if buf is objc.NULL:
            self.assertEquals(numBytes, 0)
        else:
            self.failUnless(isinstance(buf, str))
            self.assertEquals(numBytes, len(buf))

        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 5)

        r = CFReadStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 10)
        self.failUnless(r is True)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 10)

        err = CFReadStreamGetError(stream)
        self.failUnless(isinstance(err, CFStreamError))
        self.failUnless(err.domain == 0)
        self.failUnless(err.error == 0)
        

    def testWriteStream(self):
        import array
        a = array.array('c', " "*20)

        stream = CFWriteStreamCreateWithBuffer(None, a, 20)
        self.failUnless(isinstance(stream, CFWriteStreamRef))

        r = CFWriteStreamOpen(stream)
        self.failUnless(r is True)

        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusOpen)

        b = CFWriteStreamCanAcceptBytes(stream)
        self.failUnless(b is True)

        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, 15)

        self.assertEquals(a[0], '0')
        self.assertEquals(a[1], '1')
        self.assertEquals(a[9], '9')

        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, -1)

        err = CFWriteStreamCopyError(stream)
        self.failUnless(isinstance(err, CFErrorRef))

        err = CFWriteStreamGetError(stream)
        self.failUnless(isinstance(err, CFStreamError))
        self.failUnless(err.domain == kCFStreamErrorDomainPOSIX)
        self.failUnless(err.error == errno.ENOMEM)


        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusError)


        del stream


        stream = CFWriteStreamCreateWithAllocatedBuffers(None, None)
        self.failUnless(isinstance(stream, CFWriteStreamRef))

        r = CFWriteStreamOpen(stream)
        self.failUnless(r is True)

        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, 15)

        buf = CFWriteStreamCopyProperty(stream, kCFStreamPropertyDataWritten)
        self.failUnless(isinstance(buf, CFDataRef))
        buf = CFDataGetBytes(buf, (0, CFDataGetLength(buf)), None)
        self.failUnless(isinstance(buf, str))
        self.assertEquals(buf, '0123456789ABCDE')

        CFWriteStreamClose(stream)
        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusClosed)

        del stream


        stream = CFWriteStreamCreateWithFile(None, 
                CFURLCreateWithString(None, u"file:///tmp/pyobjc.test.txt", None))
        self.failUnless(isinstance(stream, CFWriteStreamRef))

        r = CFWriteStreamOpen(stream)
        self.failUnless(r is True)

        n = CFWriteStreamWrite(stream, "0123456789ABCDE", 15)
        self.assertEquals(n, 15)

        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 15)

        r = CFReadStreamSetProperty(stream, kCFStreamPropertyFileCurrentOffset, 10)
        self.failUnless(r is True)
        val = CFReadStreamCopyProperty(stream, kCFStreamPropertyFileCurrentOffset)
        self.assertEquals(val, 10)

        CFWriteStreamClose(stream)
        status = CFWriteStreamGetStatus(stream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusClosed)

        data = open('/tmp/pyobjc.test.txt', 'rb').read()
        self.assertEquals(data, '0123456789ABCDE')
        os.unlink('/tmp/pyobjc.test.txt')

    def testStreamPair(self):
        readStream, writeStream = CFStreamCreateBoundPair(None, None, None, 1024*1024)
        self.failUnless(isinstance(readStream, CFReadStreamRef))
        self.failUnless(isinstance(writeStream, CFWriteStreamRef))

        # Make sure we actually have streams instead of random pointers.
        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        del readStream, writeStream

    def testSockets(self):
        sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sd.connect(('www.apple.com', 80))

        readStream, writeStream = CFStreamCreatePairWithSocket(None,
                sd.fileno(), None, None)

        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        del readStream, writeStream, sd

        readStream, writeStream = CFStreamCreatePairWithSocketToHost(None,
                "www.apple.com", 80, None, None)

        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        del readStream, writeStream


        # Note: I don't expect anyone to actually use this api, building
        # struct sockaddr buffers by hand is madness in python.
        ip = socket.gethostbyname('www.apple.com')
        ip = map(int, ip.split('.'))

        import struct
        sockaddr = struct.pack('>BBHBBBB', 16, socket.AF_INET, 80, *ip)

        signature = CFSocketSignature(
                protocolFamily=socket.AF_INET,
                socketType=socket.SOCK_STREAM,
                protocol=0,
                address=buffer(sockaddr))

        readStream, writeStream = CFStreamCreatePairWithPeerSocketSignature(
                None, signature, None, None)

        status = CFReadStreamGetStatus(readStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

        status = CFWriteStreamGetStatus(writeStream)
        self.failUnless(isinstance(status, (int, long)))
        self.assertEquals(status, kCFStreamStatusNotOpen)

    def testReadSocketASync(self):
        # CFReadStreamSetClient
        # CFReadStreamScheduleWithRunLoop
        #CFReadStreamUnscheduleFromRunLoop
        self.fail("read socket async")

    def testWriteSocketAsync(self):
        # CFWriteStreamSetClient
        # CFWriteStreamScheduleWithRunLoop
        #CFWriteStreamUnscheduleFromRunLoop
        self.fail("write socket async")


if __name__ == "__main__":
    unittest.main()
