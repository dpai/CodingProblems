# Hi, here's your problem today. This problem was recently asked by Uber:

# Given a string s and a character c, find the distance for all characters in the string to the character c in the string s. 
# You can assume that the character c will appear at least once in the string.

# Here's an example and some starter code:

## Insight - Tried to do it in 1 pass using a 2 pointer approach. Have the first pointer move ahead until it finds the character c
## then have the second pointer increment as it compares the distance between the character c and the current location and populates the
## result. The time complexity is O(n) and space complexity is O(n)

import math

def shortest_dist(s, c):
  # Fill this in.
    sz = len(s)
    result = [math.inf]*sz

    left = 0  ## Bug found - had set it at -1
    right = 0
    prev_right = 0

    while (right < sz):
        
        if (s[right] == c):
            prev_right = left - 1
            while (left <= right): # Bug found - had set to less than 
                val = right - left
                result[left] = min(result[left], val)
                if (prev_right != -1): ## Bug Found - Did not compare with previous c. This is a big one.
                    result[left] = min(result[left], left - prev_right)
                left = left + 1
        right = right + 1
    
    prev_right = left-1 
    ## Bug found - was incrementing left by 1, I assumed left = right here.
    while (left < sz):
        val = left - prev_right
        result[left] = val
        left = left + 1

    return result

print(shortest_dist('helloworld', 'l'))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
print(shortest_dist('retstl', 'l'))
print(shortest_dist('reslrest', 'l'))
print(shortest_dist('lerstarstjl', 'l'))
