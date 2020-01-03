import unittest
from maxprofit import maxprofit

class TestMaxProfits(unittest.TestCase):

    def testExampleCase(self):
        arr = [5, 2, 4, 0, 1]
        K = 2
        self.assertEqual(maxprofit(arr, K), 3)

    def testNonValidCase(self):
        arr = [5, 2, 4, 0, 1]
        K = 3
        self.assertEqual(maxprofit(arr, K), 0)

    def testLastValueHighCase(self):
        arr = [6,5,4,3,2,7]
        K = 2
        self.assertEqual(maxprofit(arr,K), 4)
        K = 3
        self.assertEqual(maxprofit(arr,K), 3)
        K = 1
        self.assertEqual(maxprofit(arr,K), 5)

    def testNoProfit(self):
        arr = [6,5,4,3,2,1]
        K = 2
        self.assertEqual(maxprofit(arr,K), 0)

    def testNoValid2(self):
        arr = [3,7]
        K = 2
        self.assertEqual(maxprofit(arr,K), 0)

    def testConcreteExample(self):
        arr = [6, 9, 2, 3, 5, 4, 7, 16]
        K = 2
        self.assertEqual(maxprofit(arr,K), 17)
        K = 3
        self.assertEqual(maxprofit(arr,K), 18)
        K = 4
        self.assertEqual(maxprofit(arr,K), 12)
        K = 5
        self.assertEqual(maxprofit(arr,K), 0)

    def testEdgeCase(self):
        arr = [1]
        K = 1
        self.assertEqual(maxprofit(arr,K), 0)


if __name__ == "__main__":
    unittest.main()