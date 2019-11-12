import unittest
from check_nondecreasing import checkPossibility

class TestNonDecreasingArray(unittest.TestCase):

    def testExampleCase(self):
        self.assertEqual(True, checkPossibility([13, 4, 7]))
        self.assertEqual(False, checkPossibility([5,1,3,2,5]))

    def testNonePCase(self):
        self.assertEqual(True, checkPossibility([1,2,3,4,5]))

    def testPZeroCase(self):
        self.assertEqual(True, checkPossibility([4, 1, 2]))
        self.assertEqual(True, checkPossibility([3, 2, 4]))

    def testPMinus2Case(self):
        self.assertEqual(True, checkPossibility([3, 7, 2]))

    def testChangePCase(self):
        self.assertEqual(True, checkPossibility([2, 4, 3, 4, 5]))

    def testChangePplus1Case(self):
        self.assertEqual(True, checkPossibility([3, 3, 2, 4]))

if __name__ == "__main__":
    unittest.main()