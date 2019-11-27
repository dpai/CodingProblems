#Hi, here's your problem today. This problem was recently asked by Twitter:

#Given a string with the initial condition of dominoes, where:

#. represents that the domino is standing still
#L represents that the domino is falling to the left side
#R represents that the domino is falling to the right side

#Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

#Example:
#Input:  ..R...L..R.
#Output: ..RR.LL..RR
#Here is your starting point:

class Solution(object):
  def make_one(self, st, en, output):
    while (st < en):
      output[st] = 'R'
      output[en] = 'L'
      st = st + 1
      en = en - 1

  def pushDominoes(self, dominoes):
    # Fill this in.
    start = 0
    sz = len(dominoes)
    output = ['.'] * sz
    for en in range(sz):
      if dominoes[en] == 'L':
        if (dominoes[start] == 'R'):
          self.make_one(start, en, output)
        else:
          ### Note: Python r-value should have same number of elements as the slice range in l-value index.
          output[start:en+1] = 'L' * (en - start + 1)
        start = en
      elif dominoes[en] == 'R':
        output[en] = 'R'
        start = en

    if (dominoes[start] == 'R'):
      ### Note: Python r-value should have same number of elements as the slice range in l-value index.
      output[start:] = 'R' * (sz - start)

    return ''.join(output) 

if __name__ == "__main__":
  print(Solution().pushDominoes('..R...L..R.'))
  # ..RR.LL..RR
  print(Solution().pushDominoes('......'))
  print(Solution().pushDominoes('....L'))
  print(Solution().pushDominoes('R....'))
  print(Solution().pushDominoes('..R..'))
  print(Solution().pushDominoes('..L..'))
  print(Solution().pushDominoes('R.........L'))
  print(Solution().pushDominoes('L.........R'))