import unittest
from findmincover import findmincover
import random

class TestQueuAsStack(unittest.TestCase):

    def testExampleCase(self):
        intervals = [(0, 3), (2, 6), (3, 4), (6, 9)]
        res = random.sample(intervals, len(intervals))
        self.assertEqual(findmincover(res), (3,6))
        
    def testSecondExample(self):
        intervals = [(0, 3), (5, 8), (10,19), (20, 21)]
        res = random.sample(intervals, len(intervals))
        self.assertEqual(findmincover(res), (3, 20))

    def testOneInterval(self):
        intervals = [(0, 3)]
        self.assertEqual(findmincover(intervals), (0, 0))

    def testIntervalsSameStart(self):
        intervals = [(0, 5), (0, 1), (0, 2), (0, 3)]
        res = random.sample(intervals, len(intervals))
        self.assertEqual(findmincover(res), (0, 0))

    def testIntervalSameEnd(self):
        intervals = [(0, 5), (1, 5), (2, 5), (3, 5)]
        self.assertEqual(findmincover(intervals), (3, 3))

    def testMultipleOverlap(self):
        intervals = [(0, 7), (1,3), (6, 10), (8, 9), (9, 10)]
        res = random.sample(intervals, len(intervals))
        self.assertEqual(findmincover(res), (3, 9))

if __name__ == "__main__":
    unittest.main()