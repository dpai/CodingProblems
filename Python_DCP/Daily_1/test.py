import unittest
from  findanyKPair import findanyKpair

def setup_module(module):
    print("This will print first")

class TestKPair(unittest.TestCase):

    def setUp(self):
        pass

    def test_2_length_input(self):
        input = [1,2]
        k1 = 3
        k2 = 5
        k3 = 1
        self.assertTrue(findanyKpair(input, k1))
        self.assertFalse(findanyKpair(input, k2))
        self.assertFalse(findanyKpair(input, k3))

    def test_1_length_input(self):
        input = [1]
        k1 = 1
        k2 = 5
        self.assertFalse(findanyKpair(input, k1))
        self.assertFalse(findanyKpair(input, k2))

    def test_variable_length(self):
        input = [ 1, 45,56,67,8,4,5,6,3]
        k1 = 4
        k2 = 9
        k3 = 1000
        self.assertTrue(findanyKpair(input, k1))
        self.assertTrue(findanyKpair(input, k2))
        self.assertFalse(findanyKpair(input, k3))

if __name__ == "__main__":
    unittest.main()