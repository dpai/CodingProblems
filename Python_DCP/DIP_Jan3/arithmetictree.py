""" Hi, here's your problem today. This problem was recently asked by Apple:

You are given a binary tree representation of an arithmetic expression. In this tree, 
each leaf is an integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.

Write a function that takes this tree and evaluates the expression.

Example:

    *
   / \
  +    +
 / \  / \
3  2  4  5


This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.

Here's a starting point: """

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
  if (root.left is None and root.right is None):
      return root.val

  leftval = evaluate(root.left)
  rightval = evaluate(root.right)

  if (root.val == PLUS):
      return leftval + rightval
  if (root.val == MINUS):
      return leftval - rightval
  if (root.val == TIMES):
      return leftval*rightval
  if (root.val == DIVIDE):
      return leftval/rightval


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45

tree1 = Node(1)
print(evaluate(tree1))
# 1
