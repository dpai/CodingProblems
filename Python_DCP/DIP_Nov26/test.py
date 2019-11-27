import unittest

from removekthelement import Node,remove_kth_from_linked_list

class Testlinkedlistelements(unittest.TestCase):

    def testExampleCase(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        expected = Node(1, Node(2, Node(4, Node(5))))
        head = remove_kth_from_linked_list(head, 3)
        self.assertEqual(str(expected), str(head))

    def test2lengthCase(self):
        head = Node(1, Node(2))
        expected = Node(2)
        head = remove_kth_from_linked_list(head, 2)
        self.assertEqual(str(expected), str(head))

    def test1lengthCase(self):
        head = Node(1)
        expected = None
        self.assertEqual(str(expected), str(remove_kth_from_linked_list(head, 1)))

    def testremovelastCase(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        expected = Node(1, Node(2, Node(3, Node(4))))
        self.assertEqual(str(expected), str(remove_kth_from_linked_list(head, 1)))

    def testoutofboundsCase(self):
        head = Node(1, Node(2))
        expected = Node(1, Node(2))
        self.assertEqual(str(expected), str(remove_kth_from_linked_list(head, 3)))

if __name__ == "__main__":
    unittest.main()