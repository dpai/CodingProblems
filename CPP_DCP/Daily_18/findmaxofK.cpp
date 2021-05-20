// This problem was asked by Google.

// Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

// For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

//     10 = max(10, 5, 2)
//     7 = max(5, 2, 7)
//     8 = max(2, 7, 8)
//     8 = max(7, 8, 7)

// Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
// You can simply print them out as you compute them.

// NAive solution is to choose element as start and capture next k-1 elements and find max . O(nk)
// Intermediate solution - Add to the map, the current element as key and the value as the index.
// Erase from map when only if the key to be removed from the left, has the same index value as the current index. Last element of the map is the max value.
// O(nlogk) with O(k) space
// Optimal solution that was asked. Maintain a queue. Since we traverse to the right, only elements to the right of the max value of any k elements can
// potentially be the max element. So always maintain the max value at the front of the queue at any time. In other words if current element is bigger
// than all elements in the queue, the queue will be emptied and the current element is added.
// O(n) and O(k)

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void findmaxOfK(vector<int> &ip, int k)
{
    queue<int> q;
    int maxv = ip[0];
    q.push(ip[0]);
    vector<int> result;

    for (int i = 1; i < ip.size(); i++)
    {
        if (i > k - 1) // Bug here - should be k-1
        {
            cout << q.front() << " ";
            q.pop();
        }
        q.push(ip[i]);
        while (q.front() < ip[i])
        {
            q.pop();
        }
    }
    cout << q.front() << "\n";
}
