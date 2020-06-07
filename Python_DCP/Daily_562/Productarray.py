# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
#  If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# Naive solution is O(n^2)
# a 2-pass solution is O(n)
# Forward pass -> At any index i, we save the result of the accumalated product of 0->i-1
# Backward pass -> For any index i, we multiply the accumalated value at i with accumalated product from i+1 -> n
# For this solution I am not considering product which causes number to overflow. 

def productarray(arr):
    sz = len(arr)
    if sz == 1:
        return [0]
    
    op = sz * [1]
    for i in range(1,sz):
        op[i] = op[i-1] * arr[i-1]

    val = 1
    for i in reversed(range(0,sz-1)):
        val = val * arr[i+1]
        op[i] = op[i] * val

    return op

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print("Output is " + str(productarray(arr))) 
    arr = [3,2,1]
    print("Output is " + str(productarray(arr))) 
