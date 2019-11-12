import unittest
from nondupnumber import singleNumber

class TestSingleNumber(unittest.TestCase):

    def testExampleCase(self):
        self.assertEqual(1, singleNumber([4, 3, 2, 4, 1, 3, 2]))

    def testLastNumber(self):
        self.assertEqual(30, singleNumber([2,5,6,7,8,8,7,6,5,2,30]))

    def testEmpty(self):
        self.assertEqual(None, singleNumber([]))

    def testInvalid(self):
        self.assertEqual(None, singleNumber([2,3,4,5,2,3,4,5]))

if __name__ == "__main__":
    unittest.main()