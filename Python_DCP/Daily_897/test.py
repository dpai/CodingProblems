import unittest
from queuebystack import queue_stack

class TestQueuAsStack(unittest.TestCase):

    def testExampleCase(self):
        arr = [-5, -3, 2, 3]
        q = queue_stack()
        q.enqueue(arr[0])
        self.assertEqual(q.dequeue(), -5)
        q.enqueue(arr[1])
        self.assertEqual(q.dequeue(), -3)
        q.enqueue(arr[2])
        self.assertEqual(q.dequeue(), 2)
        q.enqueue(arr[3])
        self.assertEqual(q.dequeue(), 3)

    def testSecondExample(self):
        arr = [-10, -8, -5, -1]
        q = queue_stack()
        q.enqueue(arr[0])
        self.assertEqual(q.dequeue(), -10)
        q.enqueue(arr[1])
        self.assertEqual(q.dequeue(), -8)
        q.enqueue(arr[2])
        self.assertEqual(q.dequeue(), -5)
        q.enqueue(arr[3])
        self.assertEqual(q.dequeue(), -1)

    def testNoneCase(self):
        arr = []
        q = queue_stack()
        self.assertEqual(q.dequeue(), None)

if __name__ == "__main__":
    unittest.main()