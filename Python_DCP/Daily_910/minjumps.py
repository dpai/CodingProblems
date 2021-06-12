# This problem was asked by Yelp.

# You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward 
# from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end 
# of the array.

# For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, 
# and then from 5 to 9.

## Insight - this is a recursion problem, but because the input does not change and with lot of overlapping problems it 
## can be solved using Dynamic Programming
## Recursion formula F(i) = 1 + min(forall (j = 1 to input[i]) [ F(i+j)], where i is the starting location to measure minimum jump 
## from, and F(i) is the minimum jumps starting at i.
## O(n^2)

def minjumps(ip_array):
    sz = len(ip_array)
    res = [-1]*len(ip_array)

    res[sz-1] = 0

    for l in range(sz-2, -1, -1):
        temp = sz+1
        for j in range(1, ip_array[l]+1):
            if (l+j < sz) and (ip_array[l+j] != 0):
                temp = min(temp, res[l+j])

        if (ip_array[l] != 0):
            res[l] = 1 + temp

    return res[0]

if __name__ == '__main__':
    ip_arry = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
    print(f"minimum jumps needed is {minjumps(ip_arry)}")
    ip_arry = [0,0,0,0]
    print(f"minimum jumps needed is {minjumps(ip_arry)}")
    ip_arry = [0]
    print(f"minimum jumps needed is {minjumps(ip_arry)}")
    ip_arry = [1,1]
    print(f"minimum jumps needed is {minjumps(ip_arry)}")
    ip_arry = [2,2,2,2,2,2,2,2,2]
    print(f"minimum jumps needed is {minjumps(ip_arry)}")
    ip_arry = [2,2,2,4,2,2,2,2]
    print(f"minimum jumps needed is {minjumps(ip_arry)}")