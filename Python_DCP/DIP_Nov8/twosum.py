#Hi, here's your problem today. This problem was recently asked by Facebook:

#You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

#Example:
#Given [4, 7, 1 , -3, 2] and k = 5,
#return true since 4 + 1 = 5.

def two_sum(arr, k):
  # Fill this in.
  K_minus_list = []
  en = len(arr)

  for i in range(en):
      val = arr[i]
      if (val in K_minus_list):
          return True
      else:
          K_minus_list.append(k-val)

  return False

if __name__ == "__main__":
    print(two_sum([4,7,1,-3,2], 5))
# True

#Try to do it in a single pass of the list.