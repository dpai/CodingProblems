#Hi, here's your problem today. This problem was recently asked by Facebook:

#Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

#Example:
#Input: [1, 3, 5, 3, 1, 3, 1, 5]
#Output: 4
#The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]

#Here's the solution signature:

def findSequence(seq):
  # Fill this in.
  l = 0
  r = 0
  mapper = {}
  max_unique = -1

  sz = len(seq)
  for r in range(sz):
      mapper[seq[r]] = r
      if len(mapper) > 2:
          max_unique = max(max_unique, r - l)
          k = min(mapper, key=mapper.get)
          l = mapper[k]+1
          del mapper[k]
  
  return max_unique

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4
print(findSequence([1,1,1,1]))