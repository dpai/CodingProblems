import unittest
from findmincover import findmincover

class TestQueuAsStack(unittest.TestCase):

    def testExampleCase(self):
        intervals = [(0, 3), (2, 6), (3, 4), (6, 9)]
        self.assertEqual(findmincover(intervals), (3,6))
        
    def testSecondExample(self):
        intervals = [(0, 3), (5, 8), (10,19), (20, 21)]
        self.assertEqual(findmincover(intervals), (3, 20))

    def testOneInterval(self):
        intervals = [(0, 3)]
        self.assertEqual(findmincover(intervals), (3, 3))

    def testIntervalsSameStart(self):
        intervals = [(0, 5), (0, 1), (0, 2), (0, 3)]
        self.assertEqual(findmincover(intervals), (0, 0))

    def testIntervalSameEnd(self):
        intervals = [(0, 5), (1, 5), (2, 5), (3, 5)]
        self.assertEqual(findmincover(intervals), (3, 3))

    def testMultipleOverlap(self):
        intervals = [(0, 7), (1,3), (6, 10), (8, 9), (9, 10)]
        self.assertEqual(findmincover(intervals), (3, 9))

if __name__ == "__main__":
    unittest.main()