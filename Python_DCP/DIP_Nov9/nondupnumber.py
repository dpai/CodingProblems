#Hi, here's your problem today. This problem was recently asked by Facebook:

#By the way, check out our NEW project AlgoPro (http://algopro.com) for over 60+ video coding sessions with ex-Google/ex-Facebook engineers.

#Given a list of numbers, where every number shows up twice except for one number, find that one number.

#Example:

#Input: [4, 3, 2, 4, 1, 3, 2]
#Output: 1

#Here's the function signature:

def singleNumber(nums):
  # Fill this in.
  if (len(nums) == 0):
      return None

  if (len(nums) % 2 == 0):
      return None

  nums = sorted(nums)
  sz = len(nums)-1

  for i in range(0,sz,2):
      if (nums[i] != nums[i+1]):
          return nums[i]

  return nums[sz]


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1


#Challenge: Find a way to do this using O(1) memory.

# The obvious way to do this was to scan through the array and save the integer in a hashmap if not present and remove it
# when it is. After the scan is done, whatever is left in the hashmap is the non duplicate number.
# This can lead to a O(n) worst space in the worst case. 
# To do it in O(1) memory, a good way is to sort the array. Then as you scan through the array using a span of 2, 
# check for the ith entry and the (i+1) entry. If not same , that is the number . Else continue.
# Note that I assume there is no invalid input. If there is invalid input then O(1) memory may not be possible.
