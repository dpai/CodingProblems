import unittest
from smallestindex import smallestIndexSameAsNumber

class TestSmallestIndex(unittest.TestCase):

    def testExampleCase(self):
        arr = [-5, -3, 2, 3]
        self.assertEqual(smallestIndexSameAsNumber(arr), 2)

    def testLeftNoneCase(self):
        arr = [-10, -8, -5, -1]
        self.assertEqual(smallestIndexSameAsNumber(arr), None)

    def testRightNoneCase(self):
        arr = [2, 3, 4, 5]
        self.assertEqual(smallestIndexSameAsNumber(arr), None)

    def testLeftmostCase(self):
        arr = [-10, -9, -6, -4, 4]
        self.assertEqual(smallestIndexSameAsNumber(arr), 4)
    
    def testRightMostCase(self):
        arr = [0, 5, 34, 67, 100]
        self.assertEqual(smallestIndexSameAsNumber(arr), 0)

if __name__ == "__main__":
    unittest.main()