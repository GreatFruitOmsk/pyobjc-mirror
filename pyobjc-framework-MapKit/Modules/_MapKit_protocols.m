/*
 * This file is generated by objective.metadata
 *
 * Last update: Sun Aug 10 14:29:53 2014
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1009
    p = PyObjC_IdToPython(@protocol(MKAnnotation)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MKMapViewDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MKOverlay)); Py_XDECREF(p);
#endif /* defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1009 */
#if defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(MKLocalSearchCompleterDelegate)); Py_XDECREF(p);
#endif
}
