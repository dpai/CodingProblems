#Good morning! Here's your coding interview problem for today.

#This problem was asked by Amazon.

#Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. 
#Return null if there is no such index.

#For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, 
#we return 2 since it's the lowest index.

def smallestIndexSameAsNumber(arr):
    st = 0
    en = len(arr)
    cur = None

    while (st < en):
        mid = st + (en - st)//2
        if (arr[mid] < mid):
            st = mid + 1
        else:
            if (arr[mid] == mid):
                cur = mid
            en = mid - 1

    return cur

if __name__ == "__main__":
    arr = [-5, -3, 2, 3]
    print(smallestIndexSameAsNumber(arr))
    arr = [-10, -8, -5, -1]
    print(smallestIndexSameAsNumber(arr))
    arr = [2, 3, 4, 5]
    print(smallestIndexSameAsNumber(arr))
    arr = [-10, -9, -6, -4, 4]
    print(smallestIndexSameAsNumber(arr))
    arr = [0, 5, 34, 67, 100]
    print(smallestIndexSameAsNumber(arr))
