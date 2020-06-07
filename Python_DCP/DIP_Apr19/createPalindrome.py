# Hi, here's your problem today. This problem was recently asked by Google:

# Given a string, determine if you can remove any character to create a palindrome.

# Here's some examples and some starter code:

### Based on how I understand this question, it is asking if I can remove any 1 character to create a palindrome.
## On this assumption the second test case output is incorrect. The provided solution is O(N).
## Start from outside in. Any mismatch, I have 2 cases, skip character on the right and skip character on the left. 

def check_palindrome(s, l, r):
  while (l <= r):
    if (s[l] != s[r]):
      return False
    l = l + 1
    r = r - 1
  return True

def create_palindrome(s):
  # Fill this in.
  l = 0
  r = len(s) - 1
  while (l <= r):
    if (s[l] != s[r]):
      if (check_palindrome(s, l+1, r) or check_palindrome(s, l, r-1)):
        return True
      else:
        return False
    l = l + 1
    r = r - 1
  return True

print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False