# This problem was asked by Google.

# Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
# If there are multiple smallest sets, return any of them.

# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.

## I have assumed the intervals are all sorted on the starting interval. If not we can simply sort before we do this 
## Insight - The first insight was that the starting point of the last interval is the end point of the cover. How to find the start 
# of the cover. Basically we keep track of which interval has the smallest endpoint. We compare it with the current interval's starting 
# point. If starting point is bigger we choose the smallest endpoint at the start of the cover. This is the invariant we maintain as
# we traverse the loop.
# TC = O(n) SC = O(1) , If we have to sort then it is O(nlogn)
# Updated - If current interval is greater than the end cover point, only then update the end cover point. This update will ensure
# the input intervals can be out of order

def findmincover(intervals):
    min_int = -1
    max_int = -1
    min_en = -1
    for k, v in intervals:
        if min_int == -1:
            min_int = k
            max_int = k
            min_en = v
            continue

        max_int = max(k, max_int)
        min_en = min(min_en, v)
        min_int = min(max_int, min_en)

    return (min_int, max_int)

if __name__ == '__main__':
    intervals = [(0, 3), (2, 6), (3, 4), (6, 9)]
    print(f"Min cover for intervals is {findmincover(intervals)}")

