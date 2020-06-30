# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Implement auto-completion. Given a large set of words (for instance 1,000,000 words) and then a single word prefix, 
# find all words that it can complete to.

# Build a Trie, then do a depth first search after the prefix string is found in the trie. 
# TC O(nm) for building the trie, when n is number of words, and m is the length of the words
# TC O(nm) for autocomplete, since we will need to traverse the entire trie

class Node(object):
    def __init__(self):
        self.neighbors = {}
        self.wordend = False

class Solution:
    def build(self, data):
      self.trie = Node()
      for s in data:
          toproot = self.trie
          for x in s:
              if x not in toproot.neighbors:
                  toproot.neighbors[x] = Node()
              toproot = toproot.neighbors[x]
          toproot.wordend = True

    def compose(self, node, expected, output):
        if (node.wordend):
            output.append(expected)

        for key, value in node.neighbors.items():
            self.compose(value, expected + key, output)
    
    def autocomplete(self, word):
    # Fill this in.
        output = []
        toproot = self.trie
        for w in word:
            if (w not in toproot.neighbors):
                return output
            toproot = toproot.neighbors[w]
        
        self.compose(toproot, word, output)

        return output

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']
print(s.autocomplete('door'))
print(s.autocomplete('de'))
print(s.autocomplete(''))