# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def find_intersection(a, b):
    n1 = a
    n2 = b
    n3 = None
    n4 = None

    while (n1 is not None and n2 is not None):
        n1 = n1.next
        n2 = n2.next

    if (n1 is None):
        n3 = b
        n4 = a
    else:
        n3 = a
        n4 = b

    while (n1 is not None):
        n1 = n1.next
        n3 = n3.next

    while (n2 is not None):
        n2 = n2.next
        n3 = n3.next

    while (n3.val != n4.val):
        n3 = n3.next
        n4 = n4.next

        if (n3 is None or n4 is None):
            return None

    return n3.val

if __name__ == "__main__":
    first = Node(3, Node(7, Node(8, Node(10))))
    print(first)
    second = Node(99, Node(1, Node(8, Node(10))))
    print(second)
    print('The list intersect at ' + str(find_intersection(first, second)))

