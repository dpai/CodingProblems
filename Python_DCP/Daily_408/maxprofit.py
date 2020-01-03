""" Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in 
chronological order and an integer k, return the maximum profit you can make from k buys and sells. 
You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3. """

## Insight: This is a recursion problem because I need to find all possible configurations of 
## K buys and sells from the array and report what generates the maximum profit. However, since 
## there is overlap between the execution paths I can find a dynamic programming solution which 
## will be much faster than recursion. Following is the dynamic programmin solution that takes
## O(nk) space and O(nk) time. 
## Note no profit comes out to be 0 instead of a negative value or loss.
## Also an array for which K buys and sells is not valid also outputs 0. 
## Note2: The sz_len value is very important. This is to ascertain that if K is not valid 
## for the array it should show profit as 0 and not show the evaluated profit for valid part 
## of K. Now it is possible to in advanced check if K is valid for the array or not, but I 
## chose not to do so.  

def maxprofit(arr, K):
    sz = len(arr)

    output = [[0] * (sz+1) for i in range(K+1)]

    for i in range(sz-1, -1, -1):
        for k in range(1, K+1):
            sz_len = sz - 2*(k-1)
            ### The recursion is here
            ## f(i,k) = Given a array starting at i and need k buys and sells, return the max profit.
            for j in range(i+1,sz_len):
                output[k][i] = max(output[k][i], (arr[j] - arr[i]) + output[k-1][j+1])
        output[k][i] = max(output[k][i], output[k][i+1])
        
    return output[K][0]

if __name__ == "__main__":
    arr = [5, 2, 4, 0, 1]
    K = 2
    print("Max Profit "  + str(maxprofit(arr,K)))