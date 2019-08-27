import unittest
from charactermap import characterMap

class TestKPair(unittest.TestCase):

    def setUp(self):
        pass

    def test_unique_maps(self):
        s1 = "abcdefgh"
        s2 = "defghijk"
        self.assertTrue(characterMap(s1, s2))

    def test_duplicate_maps(self):
        s1 = "abdcbcde"
        s2 = "yfdafadh"
        self.assertTrue(characterMap(s1, s2))

    def test_one_to_many(self):
        s1 = "abfgdhaa"
        s2 = "cfhdjsko"
        self.assertFalse(characterMap(s1, s2))

    def test_many_to_one(self):
        s1 = "ajbghrk"
        s2 = "aprssfj"
        self.assertFalse(characterMap(s1,s2))

    def test_many_to_many(self):
        s1 = "ahfjskaabdh"
        s2 = "dfffahjkplm"
        self.assertFalse(characterMap(s1,s2))

    def test_unequal_length_string(self):
        s1 = "iehrfe"
        s2 = "dfk"
        self.assertFalse(characterMap(s1,s2))

if __name__ == "__main__":
    unittest.main()