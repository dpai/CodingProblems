# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given 3 sorted lists, find the intersection of those 3 lists.

# Here's an example and some starter code.

## Insight: The main part is how to solve the intersection between lists. Since the lists are sorted, we can 
## have 3 pointers for the 3 lists. If the values pointed to are the same, we have a 3-way intersection. If not
## increment the pointers for the values that are lower than the maximum value. This allows one-pass O(n) algorithm.
## Expecially good if the lists are very long. Note that if I had done a 2-way intersection and used the intersected 
## list to compare with the 3rd list, that will be a 2-pass O(n)
## Another note is that if the number of lists was variable, then the 2-pass technique is a much better option in
## my opinion, since we then do not need to maintain variable list of pointers which will be cumbersome.

def intersection(list1, list2, list3):
  # Fill this in.
  l1size = len(list1)
  l2size = len(list2)
  l3size = len(list3)

  l1p = 0
  l2p = 0
  l3p = 0

  result = []

  while ((l1p < l1size) and (l2p < l2size) and (l3p < l3size)):
      maxval = max(list1[l1p], list2[l2p], list3[l3p])
      if ((list1[l1p] == list2[l2p]) and (list1[l1p] == list3[l3p])):
          result.append(maxval)
          l1p = l1p + 1
          l2p = l2p + 1
          l3p = l3p + 1
      else:
          if (maxval > list1[l1p]):
              l1p = l1p + 1
          if (maxval > list2[l2p]):
              l2p = l2p + 1
          if (maxval > list3[l3p]):
              l3p = l3p + 1

  return result
  
print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]
print(intersection([1, 2, 7, 8], [1, 2, 7, 8], [5, 6, 7, 8]))
# [7, 8]
print(intersection([2, 8, 11, 15, 20, 28, 32, 45], [11, 13, 28, 45], [5, 6, 11, 18, 19, 23, 28, 30, 37, 41, 45]))
# [11, 28, 45]