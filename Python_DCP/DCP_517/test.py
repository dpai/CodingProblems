import unittest

from intersection import Node,find_intersection

class Testlinkedlistelements(unittest.TestCase):

    def testExampleCase(self):
        first = Node(3, Node(7, Node(8, Node(10))))
        second = Node(99, Node(1, Node(8, Node(10))))
        self.assertEqual(find_intersection(first, second), 8)

    def testunevenlengthcase(self):
        first = Node(3, Node(7, Node(8, Node(10))))
        second = Node(10)
        self.assertEqual(find_intersection(first, second), 10)

    def testsamelistcase(self):
        first = Node(3, Node(7, Node(8, Node(10))))
        self.assertEqual(find_intersection(first, first), 3)

    def testnointersectioncase(self):
        first = Node(3, Node(7, Node(8, Node(10))))
        second = Node(99, Node(81))
        self.assertEqual(find_intersection(first, second), None)
    

if __name__ == "__main__":
    unittest.main()