#This problem was asked by Microsoft.

#Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k. 
# For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

def find3k(arr, K):
    finalsort = sorted(arr)

    for left in range(0,len(arr)-2):
        mid = left + 1
        right = len(arr) - 1

        while mid < right:
            tot = finalsort[left] + finalsort[mid] + finalsort[right]
            if tot == K:
                return True
            elif tot > K:
                right = right - 1
            else:
                mid = mid + 1

    return False


if __name__ == "__main__":
    arr = [20, 303, 3, 4 , 25]
    print("Answer is " + str(find3k(arr, 49)))
    print("Answer is " + str(find3k(arr, 50)))
    arr = [0,0,1]
    print("Answer is " + str(find3k(arr, 1)))
    arr = [0, 0, 0]
    print("Answer is " + str(find3k(arr, 4)))
