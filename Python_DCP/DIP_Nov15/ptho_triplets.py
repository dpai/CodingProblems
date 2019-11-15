#Hi, here's your problem today. This problem was recently asked by Uber:

#Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

#Example:
##Input: [3, 5, 12, 5, 13]
#Output: True
#Here, 5^2 + 12^2 = 13^2.

def findPythagoreanTriplets(nums):
  # Fill this in.
  nums = sorted(nums)
  en = len(nums)-1
  
  for i in range(en, 0, -1):
    left = 0
    right = i-1

    total = nums[i] * nums[i]

    while (left < right):
      l_value = nums[left]*nums[left] + nums[right]*nums[right]
      if (l_value == total):
        return True
      elif (l_value > total):
        right = right - 1
      else:
        left = left + 1
    
  return False
      
print(findPythagoreanTriplets([3, 12, 5, 13]))
# True