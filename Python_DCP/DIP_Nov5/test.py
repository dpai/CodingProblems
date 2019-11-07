import unittest
from rangeinsorted import Solution

class TestMaxDistinct(unittest.TestCase):

    def setUp(self):
        self.arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
        self.x = 8

    def test_input(self):
        self.assertEqual(Solution().getRange(self.arr, self.x), [8,9])

    def test_input_1(self):
        t = 2
        self.assertEqual(Solution().getRange(self.arr, t), [1, 4])

    def test_all_same(self):
        arr = [1,1,1,1,1,1,1,1]
        t1 = 2
        t = 1
        self.assertEqual(Solution().getRange(arr, t), [0, 7])
        self.assertEqual(Solution().getRange(arr, t1), -1)

    def test_1_list(self):
        arr = [2]
        x = 1
        y = 2
        z = 3
        self.assertEqual(Solution().getRange(arr, x), -1)
        self.assertEqual(Solution().getRange(arr, y), [0,0])
        self.assertEqual(Solution().getRange(arr, z), -1)


if __name__ == "__main__":
    unittest.main()