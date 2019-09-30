#This problem was asked by Google.

#Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. 
# For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].
# This is not the optimal solution. 
import math
import pprint

def closestPoints(arr):
    sz = len(arr)
    res = []
    maxdist = math.inf
    for i in range(0, sz-1):
        for j in range(i+1, sz):
            x, y = arr[i]
            x1, y1 = arr[j]

            dist = max(abs(x1 - x), abs(y1 - y))
            if (dist < maxdist):
                maxdist = dist
                res = [(x, y), (x1,y1)]

    return res

if __name__ == "__main__":
    arr = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
    pprint.pprint(closestPoints(arr))