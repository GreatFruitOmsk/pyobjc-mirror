import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import FinderSync


    class TestFinderSyncHelper (FinderSync.NSObject):
        def exportedObjectForMessageInterface_itemURL_error_(self, mi, iu, err): pass
        def valuesForAttributes_forItemWithURL_completion_(self, at, iu, com): pass
        def makeListenerEndpointForServiceName_itemURL_andReturnError_(self, a, b, c): pass


    class TestFinderSync (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(FinderSync.FIFinderSyncController, objc.objc_class)
            self.assertIsInstance(FinderSync.FIFinderSync, objc.objc_class)

        @min_os_level("10.10")
        def testProtocols(self):
            self.assertIsInstance(objc.protocolNamed("FIFinderSync"), objc.formal_protocol)

            self.assertArgHasType(TestFinderSyncHelper.exportedObjectForMessageInterface_itemURL_error_, 2, b'o^@')
            self.assertArgIsBlock(TestFinderSyncHelper.valuesForAttributes_forItemWithURL_completion_, 2, b'v@@')

            self.assertArgIsOut(TestFinderSyncHelper.makeListenerEndpointForServiceName_itemURL_andReturnError_, 2)

        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(FinderSync.FIMenuKindContextualMenuForItems, 0)
            self.assertEqual(FinderSync.FIMenuKindContextualMenuForContainer, 1)
            self.assertEqual(FinderSync.FIMenuKindContextualMenuForSidebar, 2)
            self.assertEqual(FinderSync.FIMenuKindToolbarItemMenu, 3)

        @min_os_level("10.13")
        def testMethods(self):
            self.assertArgIsBlock(FinderSync.FIFinderSyncController.setLastUsedDate_forItemWithURL_completion_, 2, b'v@')
            self.assertArgIsBlock(FinderSync.FIFinderSyncController.setTagData_forItemWithURL_completion_, 2, b'v@')


if __name__ == "__main__":
    main()
