#Hi, here's your problem today. This problem was recently asked by Twitter:

#A palindrome is a sequence of characters that reads the same backwards and forwards. 
# Given a string, s, find the longest palindromic substring in s.

class Solution: 
    def palindrome(self, left, right, s):
        inter = ""
        while (left >= 0) and (right < len(s)):
            if (s[left] == s[right]):
                inter = s[left:right+1]
                left = left - 1
                right = right + 1
                continue
            else:
                break
        return inter
                

    def longestPalindrome(self, s):
      # Fill this in.
      result = ""

      for mid in range(0, len(s)):
          inter = self.palindrome(mid, mid, s) ## Odd length palindrome
          if (len(result) < len(inter)):
              result = inter
          inter = self.palindrome(mid, mid+1, s) ## even length palindrome
          if (len(result) < len(inter)):
              result = inter
      return result
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
s = "banana"
print(str(Solution().longestPalindrome(s)))
s = "million"
print(str(Solution().longestPalindrome(s)))
s = "a"
print(str(Solution().longestPalindrome(s)))
s = "abc"
print(str(Solution().longestPalindrome(s)))