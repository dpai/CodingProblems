""" Hi, here's your problem today. This problem was recently asked by Amazon:

Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.

Here's a starting point: """

## The bruteforce solution is to take each value from num2 and check if it is in num1 and put it in a set if found . O(nm) run time
## Put all elements of num1 in a set, then for each num2 element check if set has that number, add to output and remove from set . O(m+n) space O(n+m) run time
## Chosen solution - Sort num1 and then for each element in num2 check if in num1 using binary search, and put in set if found. O((m+n)logn) run time.

class Solution:

  def binary_search(self, num1, val):
      l = 0
      r = len(num1)-1

      while (l<=r):
          mid = int(l + (r-l)/2)
          if (num1[mid] == val):
              return True
          elif (num1[mid] > val):
              r = mid - 1
          else:
              l = mid + 1

      return False

  def intersection(self, nums1, nums2):
    # Fill this in.
    sorted(nums1)
    output = set()

    for i in nums2:
        if (self.binary_search(nums1, i)):
            output.add(i)

    return output

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]
print(Solution().intersection([1,2,2,1],[2,2]))
# [2]
print(Solution().intersection([1,2,4,5,6,1],[8,9,7]))
