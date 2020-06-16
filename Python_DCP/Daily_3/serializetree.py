# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

#Insight - Use a $ to serialize left subtree and # to serialize right subtree
# To unserialize, just traverse the string, when there is node, make a new one, when there is a $ increment, 
# and when there is a '#' return None. Edge case, when End of string , return None
# TC O(n) - for n is number of nodes.

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def serialize(root):
    if (root == None):
        return ''

    return '{}${}#{}'.format(root.val, serialize(root.left), serialize(root.right))
    # op = []
    # op.append(root.val)
    # op.append('$')
    # op.append(serialize(root.left))
    # op.append('#')
    # op.append(serialize(root.right))

    # return ''.join(op)

def deserialize(str1, idx):
    if (len(str1) == idx):
        return (None, idx)

    if (str1[idx] == '$'):
        idx = idx + 1
    if (str1[idx] == '#'):
        return (None, idx)
    
    n = Node(str1[idx])
    idx = idx + 1
    n.left, idx = deserialize(str1, idx)
    idx = idx + 1
    n.right, idx = deserialize(str1, idx)

    return (n, idx) 

if __name__ == "__main__":
    root = Node('a', Node('b', None, None), Node('c', None, None))
    print(root)
    stringtode = serialize(root)
    print(stringtode)
    
    head, n = deserialize(stringtode, 0)
    print(head)