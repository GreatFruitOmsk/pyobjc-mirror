from CoreFoundation import *
from PyObjCTools.TestSupport import *

class TestCFTree (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFTreeRef)

    def testCreation(self):
        context = object()
        tree = CFTreeCreate(None, context)

        self.assert_(isinstance(tree, CFTreeRef))

        self.assert_(CFTreeGetContext(tree) is context)
        CFTreeSetContext(tree, 42)
        self.assertEqual(CFTreeGetContext(tree), 42)



    def testCreateTree(self):
        root = CFTreeCreate(None, "root")

        for child in range(10):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        self.assertEqual(CFTreeGetContext(CFTreeGetFirstChild(root)), 0)

        def compare(l, r, context):
            return -cmp(CFTreeGetContext(l), CFTreeGetContext(r))

        CFTreeSortChildren(root, compare, None)
        self.assertEqual(CFTreeGetContext(CFTreeGetFirstChild(root)), 9)


    def testTypeID(self):
        v = CFTreeGetTypeID()
        self.assertIsInstance(v, (int, long))
    def testQuerying(self):
        root = CFTreeCreate(None, "root")

        for child in range(2):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        p = CFTreeGetParent(root)
        self.assertIsObject(p, None)
        c = CFTreeGetFirstChild(root)
        self.assertIsInstance(c, CFTreeRef)
        c2 = CFTreeGetChildAtIndex(root, 0)
        self.assertIsObject(c, c2)
        p = CFTreeGetParent(c)
        self.assertIsObject(p, root)
        s = CFTreeGetNextSibling(c)
        self.assertIsInstance(s, CFTreeRef)
        p = CFTreeGetParent(s)
        self.assertIsObject(p, root)
        s2 = CFTreeGetChildAtIndex(root, 1)
        self.assertIsObject(s, s2)
        s = CFTreeGetNextSibling(s)
        self.assertIsObject(s, None)
        cnt = CFTreeGetChildCount(root)
        self.assertEqual(cnt, 2)

        cnt = CFTreeGetChildCount(c)
        self.assertEqual(cnt, 0)

        children = CFTreeGetChildren(root, None)
        self.assertIsInstance(children, (list, tuple))
        self.assertEqual(len(children), 2)

        r = CFTreeFindRoot(s2)
        self.assertIsObject(r, root)
    def testModification(self):
        root = CFTreeCreate(None, "root")

        for child in range(2):
            CFTreeAppendChild(root, CFTreeCreate(None, child))

        def applyFunc(node, context):
            context.append(CFTreeGetContext(node))

        l = []
        CFTreeApplyFunctionToChildren(root, applyFunc, l)
        self.assertEqual(len(l), 2)

        preChild = CFTreeCreate(None, "before")
        postChild = CFTreeCreate(None, "after")
        CFTreePrependChild(root, preChild)
        CFTreeAppendChild(root, postChild)

        self.assertEqual(CFTreeGetChildCount(root), 4)
        n = CFTreeGetChildAtIndex(root, 0)
        self.assertIsObject(n, preChild)
        n = CFTreeGetChildAtIndex(root, 3)
        self.assertIsObject(n, postChild)
        s = CFTreeCreate(None, "sibling")
        CFTreeInsertSibling(preChild, s)
        n = CFTreeGetChildAtIndex(root, 1)
        self.assertIsObject(n, s)
        self.assertEqual(CFTreeGetChildCount(root), 5)

        CFTreeRemove(s)
        self.assertEqual(CFTreeGetChildCount(root), 4)

        def compare(left, right, context):
            left = CFTreeGetContext(left)
            right = CFTreeGetContext(right)
            return -cmp(left, right)

        before = []
        after = []
        CFTreeApplyFunctionToChildren(root, applyFunc, before)
        CFTreeSortChildren(root, compare, None)
        CFTreeApplyFunctionToChildren(root, applyFunc, after)

        before.sort()
        before.reverse()
        self.assertEqual(before, after)

        CFTreeRemoveAllChildren(root)
        self.assertEqual(CFTreeGetChildCount(root), 0)








if __name__ == "__main__":
    main()
