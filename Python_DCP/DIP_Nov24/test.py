import unittest
from dominoes import Solution

class TestDominoes(unittest.TestCase):

    def setUp(self):
        pass

    def test_example_string(self):
        inputstring = "..R...L..R."
        self.assertEqual(Solution().pushDominoes(inputstring), "..RR.LL..RR")

    def test_nochange(self):
        inputstring = "......"
        self.assertEqual(Solution().pushDominoes(inputstring), "......")
        input2 = "RRRR"
        self.assertEqual(Solution().pushDominoes(input2), "RRRR")

    def test_L_on_right(self):
        inputstring = "....L"
        self.assertEqual(Solution().pushDominoes(inputstring), "LLLLL")

    def test_R_on_left(self):
        inputstring = "R...."
        self.assertEqual(Solution().pushDominoes(inputstring), "RRRRR")

    def test_in_middle(self):
        inputstring = "..R.."
        self.assertEqual(Solution().pushDominoes(inputstring), "..RRR")

    def test_balanced(self):
        inputstring = "R.........L"
        self.assertEqual(Solution().pushDominoes(inputstring), "RRRRR.LLLLL")

    def test_unbalanced(self):
        inputstring = "L.........R"
        self.assertEqual(Solution().pushDominoes(inputstring), "L.........R")



if __name__ == "__main__":
    unittest.main()