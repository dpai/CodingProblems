""" Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given the preorder and inorder traversals of a binary tree in the form of arrays. Write a function that reconstructs the tree represented by these traversals.

Example:
Preorder: [a, b, d, e, c, f, g]
Inorder: [d, b, e, a, f, c, g]

The tree that should be constructed from these traversals is:

    a
   / \
  b   c
 / \ / \
d  e f  g

Here's a start: """

#Insight: This is a tree traversal problem. The first element of the preorder is the root . You need to find the location of the current root element in the
#inorder array. Everything before it will be on left side on the root. Splice the left side contents and recurse. Splice the rest of the contents which will be 
#on right side of the current root and recurse. O(n) time run as all elements are touched once. 

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result


def reconstruct(preorder, inorder):
  # Fill this in.
  if (len(preorder) == 0):
    return None
  head = Node(preorder[0])
  fIdx= inorder.index(preorder[0])
  head.left = reconstruct(preorder[1:(1+fIdx)], inorder[0:fIdx])
  head.right = reconstruct(preorder[(1+fIdx):], inorder[(1+fIdx):])

  return head

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
# abcdefg

tree1 = reconstruct(['b', 'a', 'c'],
                   ['a','b','c'])
print(tree1)
# bac

bigtree = reconstruct(['1','2','5','7','8','6','9','3','4','10','11','13','14','12'],
                      ['7','5','8','2','9','6','1','4','3','14','13','11','10','12'])
print(bigtree)
# 1235641078911121314