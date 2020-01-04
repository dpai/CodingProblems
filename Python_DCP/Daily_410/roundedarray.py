""" Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

You are given an array X of floating-point numbers x1, x2, ... xn. 
These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

    The rounded sums of both arrays should be equal.

    The absolute pairwise difference between elements is minimized. 
    In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.

For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than [1, 2, 5], 
which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1. """

import math

def helper(i, inputarray, outputarray, absdiffarray, final_result):
    if (i == len(inputarray)):
        floatsum = int(sum(inputarray))
        opsum = sum(outputarray)
        absdiffsum = sum(absdiffarray)
        if (floatsum != opsum):
            return final_result
        if (len(final_result) != 0):
            if (absdiffsum < final_result[0]):
                final_result = (absdiffsum, outputarray.copy())
        else:
            final_result = (absdiffsum, outputarray.copy())
        return final_result

    outputarray[i] = math.floor(inputarray[i])
    absdiffarray[i] = abs(inputarray[i] - outputarray[i])
    final_result = helper(i+1, inputarray, outputarray, absdiffarray, final_result)
    outputarray[i] = math.ceil(inputarray[i])
    absdiffarray[i] = abs(inputarray[i] - outputarray[i])
    final_result = helper(i+1, inputarray, outputarray, absdiffarray, final_result)
    return final_result
        
def roundinputarray(inputarr):
    outputarray = [0]*len(inputarr)
    absdiffarray = [0]*len(inputarr)
    final_result = ()
    final_result = helper(0, inputarr, outputarray, absdiffarray, final_result)

    return final_result[1]

if __name__ == "__main__":
    arr = [1.3, 2.3, 4.4]
    print("Rounded array " + str(roundinputarray(arr)))
    arr = [4.4]
    print("Rounded array " + str(roundinputarray(arr)))