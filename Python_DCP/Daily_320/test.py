import unittest
from maxdistinct import maxdistinct

class TestMaxDistinct(unittest.TestCase):

    def setUp(self):
        pass

    def test_length_1_string(self):
        inputstring = "a"
        self.assertEqual(maxdistinct(inputstring), 1)

    def test_repeated_string_1char(self):
        inputstring = "jjjjj"
        self.assertEqual(maxdistinct(inputstring), 1)

    def test_distinct_char_string(self):
        inputstring = "qwerty"
        self.assertEqual(maxdistinct(inputstring), 6)

    def test_with_full_string(self):
        inputstring = "darshan"
        self.assertEqual(maxdistinct(inputstring), 7)

    def test_with_substring(self):
        inputstring = "jiujitsu"
        self.assertEqual(maxdistinct(inputstring), 5)

    def test_different_lengths(self):
        inputstring = "darsffddddadfrs"
        self.assertEqual(maxdistinct(inputstring), 5)

    def test_string_in_middle(self):
        inputstring = "dddddabcdeddddd"
        self.assertEqual(maxdistinct(inputstring), 5)

    def test_one_character_last(self):
        inputstring = "bbbbbba"
        self.assertEqual(maxdistinct(inputstring), 2)

    def test_front_back_string(self):
        inputstring = "abbbba"
        self.assertEqual(maxdistinct(inputstring), 2)
if __name__ == "__main__":
    unittest.main()