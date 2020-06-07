import unittest
from Productarray import productarray

class TestProductArray(unittest.TestCase):

    def testValidCase(self):
        arr = [5, 2, 4, 0, 1]
        self.assertEqual(productarray(arr), [0, 0, 0, 40, 0])

    def testExampleCase(self):
        arr = [1,2,3,4,5]
        self.assertEqual(productarray(arr), [120, 60, 40, 30, 24])

    def testEdgeCase(self):
        arr = [1]
        self.assertEqual(productarray(arr), [0])


if __name__ == "__main__":
    unittest.main()