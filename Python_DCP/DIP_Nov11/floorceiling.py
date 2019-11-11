#Hi, here's your problem today. This problem was recently asked by Apple:

#By the way, check out our NEW project AlgoPro (http://algopro.com) for over 60+ video coding sessions with ex-Google/ex-Facebook engineers.

#Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. 
#If either does not exist, then print them as None.

#Here is the definition of a node for the tree.

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
    

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    # Fill this in.
    if (root_node is None):
        return (floor,ceil)

    if (root_node.value == k):
        floor = k
        ceil = k
        return (floor,ceil)

    if (root_node.value < k):
        return findCeilingFloor(root_node.right, k, root_node.value, ceil) 
    else:
        return findCeilingFloor(root_node.left, k, floor, root_node.value)


root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)
print(findCeilingFloor(root, 11))
# (10, 12)
print(findCeilingFloor(root, 7))
#(6,8)
print(findCeilingFloor(root, 10))
#(10,10)
print(findCeilingFloor(root, 15))
#(14, None)
print(findCeilingFloor(root, 1))
#(None, 2)