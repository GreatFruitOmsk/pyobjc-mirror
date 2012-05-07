from PyObjCTools.TestSupport import *
from Foundation import *

class Presenter (NSObject):
    def relinquishPresentedItemToReader_(self, reader): pass
    def relinquishPresentedItemToWriter_(self, reader): pass

class TestNSFilePresenter (TestCase):
    @min_os_level('10.7')
    def testProtocols(self):
        self.assertArgIsBlock(Presenter.relinquishPresentedItemToReader_, 0,
                b'v@?') # FIXME: Cannot test exact signature at this time
        self.assertArgIsBlock(Presenter.relinquishPresentedItemToWriter_, 0,
                b'v@?') # FIXME: Cannot test exact signature at this time

        self.assertArgIsBlock(Presenter.savePresentedItemChangesWithCompletionHandler_, 0, b'v@')
        self.assertArgIsBlock(Presenter.accommodatePresentedItemDeletionWithCompletionHandler_, 0, b'v@')
        self.assertArgIsBlock(Presenter.accommodatePresentedSubitemDeletionAtURL_completionHandler_, 1, b'v@')

if __name__ == "__main__":
    main()
