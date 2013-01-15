/* 
 * This file is generated by objective.metadata
 *
 * Last update: Tue Jan 15 18:57:44 2013
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p;
    p = PyObjC_IdToPython(@protocol(NSCacheDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSConnectionDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSDiscardableContent)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSKeyedArchiverDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSKeyedUnarchiverDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSMachPortDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSMetadataQueryDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSNetServiceBrowserDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSNetServiceDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSPortDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSSpellServerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSStreamDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSXMLParserDelegate)); Py_XDECREF(p);
#if defined(MAC_OS_X_VERSION_10_5)
    p = PyObjC_IdToPython(@protocol(NSCoding)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSCopying)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSDecimalNumberBehaviors)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFastEnumeration)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSLocking)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSMutableCopying)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSObject)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSURLAuthenticationChallengeSender)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSURLHandleClient)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSURLProtocolClient)); Py_XDECREF(p);
#endif /* defined(MAC_OS_X_VERSION_10_5) */
#if defined(MAC_OS_X_VERSION_10_7)
    p = PyObjC_IdToPython(@protocol(NSFileManagerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSFilePresenter)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSURLConnectionDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSURLDownloadDelegate)); Py_XDECREF(p);
#endif /* defined(MAC_OS_X_VERSION_10_7) */
#if defined(MAC_OS_X_VERSION_10_8)
    p = PyObjC_IdToPython(@protocol(NSSecureCoding)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSURLConnectionDataDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSURLConnectionDownloadDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSUserNotificationCenterDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSXPCListenerDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(NSXPCProxyCreating)); Py_XDECREF(p);
#endif /* defined(MAC_OS_X_VERSION_10_8) */
}
