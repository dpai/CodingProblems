""" Hi, here's your problem today. This problem was recently asked by Apple:

Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.

Example:
Input:
words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

Output: False
Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

Example 2:
Input:
words = ["zyx", "zyxw", "zyxwy"],
order="zyxwvutsrqponmlkjihgfedcba"

Output: True
Explanation: The words are in increasing alphabetical order

Here's a starting point: """

## Insight: At first I thouht this was a graph problem where I need to do a topological sort. But I realized since the order
## is given this should simply be a word compare. Yor compare every 2 adjacent words and see if they are in the right order.
## If all possible adjacent words dod not violate order, return true else false. O(n*m) where n is number of words and m is
## length of each word. Note that to find the index is another O(p) order, but I think if we are only using alphabets this
## can be considered a constant amount of work. Otherwise we need to make a dictionary with the letter as key and the index 
## as value.

def checkorder(w1, w2, order):
    sz = len(w1)
    sz1 = len(w2)

    minsz = min(sz, sz1)

    for i in range(minsz):
        if (w1[i] == w2[i]):
            continue
        w1idx = order.index(w1[i])
        w2idx = order.index(w2[i])
        return (w1idx < w2idx)

    if (sz == sz1):
        return True

    if (minsz == sz):
        return True

    return False

def isSorted(words, order):
  # Fill this in.
  sz = len(words)
  for i in range(sz-1):
      word1 = words[i]
      word2 = words[i+1]
      if (checkorder(word1, word2, order) == False):
          return False
  return True
      

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True