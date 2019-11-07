#Hi, here's your problem today. This problem was recently asked by AirBNB:

#Given a sorted array, A, with possibly duplicated elements, find the indices of the 
# first and last occurrences of a target element, x. Return -1 if the target is not found.

class Solution: 
  def lowerbound(self, st, en, arr, k):
    cur = -1
    while (st <= en):
      mid = int(st + (en - st)/2)
      if (arr[mid] == k):
        cur = mid
        en = mid - 1
      else:
        st = mid + 1
    return cur

  def upperbound(self, st, en, arr, k):
    cur = -1
    while (st <= en):
      mid = int(st + (en - st)/2)
      if (arr[mid] == k):
        cur = mid
        st = mid + 1
      else:
        en = mid - 1
    return cur

  def getRange(self, arr, target):
    # Fill this in.
    st = 0
    en = len(arr) - 1
    op_list = -1

    while (st <= en):
      mid = int(st + (en - st)/2)
      if (arr[mid] == target):
        l = self.lowerbound(st, mid-1, arr, target)
        r = self.upperbound(mid+1, en, arr, target)
        if (l == -1):
          l = mid
        if (r == -1):
          r = mid
        op_list = [l,r]
        break
      elif (arr[mid] < target):
        st = mid+1
      else:
        en = mid-1
    
    return op_list
  
if __name__ == "__main__":
  # Test program 
  arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
  x = 8
  print(Solution().getRange(arr, x))
  # [1, 4]