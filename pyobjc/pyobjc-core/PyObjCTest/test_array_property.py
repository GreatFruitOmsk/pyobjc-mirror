from PyObjCTools.TestSupport import *
import objc
import collections

NSObject = objc.lookUpClass('NSObject')
NSIndexSet = objc.lookUpClass('NSIndexSet')
NSMutableIndexSet = objc.lookUpClass('NSMutableIndexSet')

class TestArrayPropertyHelper (NSObject):
    array = objc.array_property()
    roArray = objc.array_property(read_only=True)

from test_object_property import OCObserve

class TestArrayProperty (TestCase):
    def _testMissing(self):
        self.fail("Implement tests")

    def testGetting(self):
        # Check that default value is an empty value
        # Check that value is a proxy object
        o = TestArrayPropertyHelper.alloc().init()

        v = o.array
        self.failUnlessIsInstance(v, collections.MutableSequence)

        self.failUnlessEqual(len(v), 0)

        v.append(1)
        self.failUnlessEqual(len(v), 1)

        self.assertEquals(type(v).__name__, 'array_proxy')

    def testSetting(self):
        # Set value, check that 
        # (1) value gets copied
        # (2) accessing the property result in proxy
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')
        try:
            self.assertEquals(len(observer.values), 0)
            self.assertEquals(len(o.array), 0)
            self.assertEquals(len(observer.values), 0)
            o.array = l
            self.assertEquals(len(observer.values), 1)


            self.assertEquals(len(o.array), 3)

            # This shouldn't affect the property
            l.append(4)
            self.assertEquals(len(o.array), 3)

            self.assertEquals(len(l), 4)
            o.array.append(5)
            self.assertEquals(len(l), 4)

        finally:
            observer.unregister(o, 'array')



    def testGetSetItem(self):
        # Use __getitem__, __setitem__ interface and check
        # that the correct KVO events get emitted.
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        # FIXME: the call to len shouldn't be necessary
        len(o.array)
        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            self.assertEquals(len(observer.values), 0)

            o.array.append(1)

            self.assertEquals(len(observer.values), 1)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertEquals(observer.values[-1][-1]['new'], [1])


            self.assertEquals(o.array[0], 1)
            o.array[0] = 4
            self.assertEquals(o.array[0], 4)
            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertEquals(observer.values[-1][-1]['old'], [1])
            self.assertEquals(observer.values[-1][-1]['new'], [4])

        finally:
            observer.unregister(o, 'array')

    def testGetSetSlice(self):
        # Same as testGetSetItem, but using slice
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndexesInRange_((0, 3))
            IS2 = NSIndexSet.alloc().initWithIndexesInRange_((1, 2))
            IS3 = NSMutableIndexSet.alloc().init()
            IS3.addIndex_(0)
            IS3.addIndex_(2)
            self.assertEquals(len(observer.values), 0)

            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('indexes', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], [1, 2, 3])


            self.assertEquals(o.array[0], 1)
            o.array[1:3] = [4, 5]
            self.assertEquals(o.array[1], 4)
            self.assertEquals(o.array[2], 5)
            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS2)
            self.assertEquals(observer.values[-1][-1]['old'], [2, 3])
            self.assertEquals(observer.values[-1][-1]['new'], [4, 5])

            self.assertEquals(o.array[0], 1)
            o.array[0:3:2] = [9, 10]
            self.assertEquals(o.array[0], 9)
            self.assertEquals(o.array[1], 4)
            self.assertEquals(o.array[2], 10)
            self.assertEquals(len(observer.values), 3)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS3)
            self.assertEquals(observer.values[-1][-1]['old'], [1, 5])
            self.assertEquals(observer.values[-1][-1]['new'], [9, 10])

        finally:
            observer.unregister(o, 'array')

    def testInsert(self):
        # Use insert method and check that the correct
        # KVO events get emitted
        # Same as testGetSetItem, but using slice
        observer = OCObserve.alloc().init()
        l = [1, 2, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            IS1 = NSIndexSet.alloc().initWithIndex_(4)
            self.assertEquals(len(observer.values), 0)

            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEquals(o.array[0], 1)


            o.array.insert(0, 'a')
            self.assertEquals(o.array[0], 'a')
            self.assertEquals(len(o.array), 4)

            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], ['a'])

            o.array.insert(4, 'b')
            self.assertEquals(o.array[4], 'b')
            self.assertEquals(len(o.array), 5)

            self.assertEquals(len(observer.values), 3)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS1)
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], ['b'])

        finally:
            observer.unregister(o, 'array')

    def testPop(self):
        # Use pop method and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            IS2 = NSIndexSet.alloc().initWithIndex_(2)
            self.assertEquals(len(observer.values), 0)

            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEquals(o.array[0], 1)


            v = o.array.pop(0)
            self.assertEquals(v, 1)
            self.assertEquals(o.array[0], 2)
            self.assertEquals(len(o.array), 3)

            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], [1])

            v = o.array.pop(2)
            self.assertEquals(v, 4)
            self.assertEquals(len(o.array), 2)

            self.assertEquals(len(observer.values), 3)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS2)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], [4])

        finally:
            observer.unregister(o, 'array')

    def testDelItem(self):
        # Use __delitem__and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndex_(0)
            IS2 = NSIndexSet.alloc().initWithIndex_(2)
            self.assertEquals(len(observer.values), 0)

            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEquals(o.array[0], 1)


            del o.array[0]
            self.assertEquals(o.array[0], 2)
            self.assertEquals(len(o.array), 3)

            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], [1])

            del o.array[2]
            self.assertEquals(len(o.array), 2)

            self.assertEquals(len(observer.values), 3)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS2)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], [4])

        finally:
            observer.unregister(o, 'array')

    def testDelSlice(self):
        # As testDelItem, but using slices
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSMutableIndexSet.alloc().init()
            IS.addIndex_(0)
            IS.addIndex_(2)
            self.assertEquals(len(observer.values), 0)

            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEquals(o.array[0], 1)


            del o.array[0:4:2]
            self.assertEquals(o.array[0], 2)
            self.assertEquals(o.array[1], 4)
            self.assertEquals(len(o.array), 2)

            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertNotIn('new', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['old'], [1, 3])

        finally:
            observer.unregister(o, 'array')

    def testExtend(self):
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        l2 = ['a', 'b', 'c']
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertEquals(o.array[0], 1)

            o.array.extend(l2)

            self.assertEquals(len(o.array), 7)
            self.assertEquals(o.array[4], 'a')

            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], NSIndexSet.alloc().initWithIndexesInRange_((4, 3)))
            self.assertNotIn('old', observer.values[-1][-1])
            self.assertEquals(observer.values[-1][-1]['new'], ['a', 'b', 'c'])

        finally:
            observer.unregister(o, 'array')

    def testIAdd(self):
        observer = OCObserve.alloc().init()
        l = [1, 2, 3, 4]
        l2 = ['a', 'b', 'c']
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertEquals(o.array[0], 1)

            o.array += l2

            self.assertEquals(len(o.array), 7)
            self.assertEquals(o.array[4], 'a')

            #self.assertEquals(len(observer.values), 3)
            #self.assertEquals(observer.values[-2][-1]['indexes'], NSIndexSet.alloc().initWithIndexesInRange_((4, 3)))
            #self.assertNotIn('old', observer.values[-2][-1])
            #self.assertEquals(observer.values[-2][-1]['new'], ['a', 'b', 'c'])

            self.assertEquals(len(observer.values), 2)
            self.assertNotIn('indexes', observer.values[-1][-1])

        finally:
            observer.unregister(o, 'array')

    def testIMul(self):
        observer = OCObserve.alloc().init()
        l = [1, 2]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            o.array = l

            self.assertEquals(len(observer.values), 1)
            self.assertEquals(o.array[0], 1)

            o.array *= 3

            self.assertEquals(len(o.array), 6)
            self.assertEquals(o.array[0], 1)
            self.assertEquals(o.array[1], 2)
            self.assertEquals(o.array[2], 1)
            self.assertEquals(o.array[3], 2)
            self.assertEquals(o.array[4], 1)
            self.assertEquals(o.array[5], 2)

            #self.assertEquals(len(observer.values), 3)
            #self.assertEquals(observer.values[-2][-1]['indexes'], NSIndexSet.alloc().initWithIndexesInRange_((2, 4)))
            #self.assertNotIn('old', observer.values[-2][-1])
            #self.assertEquals(observer.values[-2][-1]['new'], [1, 2, 1, 2])

            self.assertEquals(len(observer.values), 2)
            self.assertNotIn('indexes', observer.values[-1][-1])

        finally:
            observer.unregister(o, 'array')


    def testSort(self):
        # Use sort method and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [2, 4, 1, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndexesInRange_((0, 4))
            self.assertEquals(len(observer.values), 0)

            orig_l = l[:]
            o.array = l


            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEquals(o.array[0], 2)

            o.array.sort()

            self.assertEquals(o.array[0], 1)
            self.assertEquals(o.array[1], 2)
            self.assertEquals(o.array[2], 3)
            self.assertEquals(o.array[3], 4)
            self.assertEquals(len(o.array), 4)

            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertEquals(observer.values[-1][-1]['old'], l)
            self.assertEquals(observer.values[-1][-1]['new'], [1,2,3,4])
            self.assertEquals(orig_l, l)

        finally:
            observer.unregister(o, 'array')

    def testReverse(self):
        # Use reverse method and check that the correct
        # KVO events get emitted
        observer = OCObserve.alloc().init()
        l = [2, 4, 1, 3]
        o = TestArrayPropertyHelper.alloc().init()
        observer.register(o, 'array')

        try:
            IS = NSIndexSet.alloc().initWithIndexesInRange_((0, 4))
            self.assertEquals(len(observer.values), 0)

            orig_l = l[:]
            o.array = l


            self.assertEquals(len(observer.values), 1)
            self.assertNotIn('indexes', observer.values[-1][-1])

            self.assertEquals(o.array[0], 2)

            o.array.reverse()

            self.assertEquals(o.array[0], 3)
            self.assertEquals(o.array[1], 1)
            self.assertEquals(o.array[2], 4)
            self.assertEquals(o.array[3], 2)
            self.assertEquals(len(o.array), 4)

            self.assertEquals(len(observer.values), 2)
            self.assertEquals(observer.values[-1][-1]['indexes'], IS)
            self.assertEquals(observer.values[-1][-1]['old'], l)
            self.assertEquals(observer.values[-1][-1]['new'], [3, 1, 4, 2])
            self.assertEquals(orig_l, l)

        finally:
            observer.unregister(o, 'array')

    def testObjCAccessors(self):
        # Check that the right ObjC array accessors are defined and work properly
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"setArray:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"array"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"countOfArray"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"objectInArrayAtIndex:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"insertObject:inArrayAtIndex:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"removeObjectFromArrayAtIndex:"))
        self.assertTrue(TestArrayPropertyHelper.instancesRespondToSelector_(b"replaceObjectInArrayAtIndex:withObject:"))

        o = TestArrayPropertyHelper.alloc().init()
        self.assertEquals(0, o.pyobjc_instanceMethods.countOfArray())
        self.assertRaises(AttributeError, getattr, o, 'countOfArray')

        o.pyobjc_instanceMethods.insertObject_inArrayAtIndex_('a', 0)
        self.assertEquals(1, o.pyobjc_instanceMethods.countOfArray())
        self.assertEquals('a', o.array[0])
        self.assertEquals('a', o.pyobjc_instanceMethods.objectInArrayAtIndex_(0))
        o.pyobjc_instanceMethods.replaceObjectInArrayAtIndex_withObject_(0, 'b')
        self.assertEquals('b', o.array[0])
        o.pyobjc_instanceMethods.removeObjectFromArrayAtIndex_(0)
        self.assertEquals(0, o.pyobjc_instanceMethods.countOfArray())


    # Verify docs and/or implementation to check for other
    # mutating methods

    def testReadingMethods(self):
        # Check that all read-only methods work as well

        o = TestArrayPropertyHelper.alloc().init()
        o.array = [1, 2, 3, 4]

        self.assertNotIsInstance(o.array, list)

        self.assertEquals(o.array, [1,2,3,4])
        self.assertNotEquals(o.array, [1,2,3,4, 5])
        

        self.assertTrue(o.array < [1,2,3,4,5])
        self.assertTrue(o.array <= [1,2,3,4,5])
        self.assertTrue(o.array <= [1,2,3,4])
        self.assertTrue(o.array >= [1,2,3,4])
        self.assertTrue(o.array > [1,2,3])

        self.assertEquals(o.array.count(1), 1)
        self.assertEquals(o.array.index(4), 3)

    def testMutatingReadonlyProperty(self):
        # Check that trying to mutate a read-only property
        # will raise an exception
        o = TestArrayPropertyHelper.alloc().init()

        o._roArray = [1, 2, 3]

        self.assertEquals(list(o.roArray), [1,2,3])

        self.assertRaises(ValueError, o.roArray.append,1)
        self.assertRaises(ValueError, o.roArray.extend, [1,2])
        self.assertRaises(ValueError, o.roArray.sort)
        self.assertRaises(ValueError, o.roArray.reverse)
        try:
            o.roArray[0] = 2
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            del o.roArray[0]
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            o.roArray += [4]
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            o.roArray *= 4
        except ValueError:
            pass
        else:
            self.fail("TypeError not raised")


    def testMutatingReadonlyPropertyObjC(self):
        # Check that trying to mutate a read-only property
        # from ObjC will raise an exception
        o = TestArrayPropertyHelper.alloc().init()
        o._roArray = [1,2,3]
        self.assertEquals(3, o.pyobjc_instanceMethods.countOfRoArray())
        self.assertRaises(AttributeError, getattr, o, 'countOfRoArray')

        try:
            o.pyobjc_instanceMethods.insertObject_inRoArrayAtIndex_('a', 0)
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        self.assertEquals(3, o.pyobjc_instanceMethods.countOfRoArray())
        self.assertEquals(1, o.pyobjc_instanceMethods.objectInRoArrayAtIndex_(0))
        try:
            o.pyobjc_instanceMethods.replaceObjectInRoArrayAtIndex_withObject_(0, 'b')
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

        try:
            o.pyobjc_instanceMethods.removeObjectFromRoArrayAtIndex_(0)
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")



if __name__ == "__main__":
    main()
