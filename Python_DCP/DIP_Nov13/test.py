import unittest

from maxinstack import MaxStack

class TestNonDecreasingArray(unittest.TestCase):

    def testExampleCase(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(2)
        self.assertEqual(3, s.max())
        s.pop()
        s.pop()
        self.assertEqual(2, s.max())

    def testEmptyStack(self):
        s = MaxStack()
        self.assertEqual(None, s.max())

    def testSecondExample(self):
        s = MaxStack()
        s.push(4)
        s.push(1)
        s.push(3)
        s.push(5)
        s.push(5)
        self.assertEqual(5, s.max())
        s.pop()
        self.assertEqual(5, s.max())
        s.pop()
        self.assertEqual(4, s.max())

if __name__ == "__main__":
    unittest.main()