// This problem was asked by Google.
 
//We can determine how "out of order" an array A is by counting the number of inversions it has. 
//Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

//Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

//You may assume each element in the array is distinct.

//For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
//The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

//Insight: The O(N^2) solution is obvious since it basically compares at every pair of numbers.
//To make a faster implementation the number of compares should be reduced.
//So my initial thought process was to iterate from the back and remember the max and min of values I have seen.
//So for every new number I compare with the max and min to decide if there is a overlap. But it still did not help improve from O(N^2).
//Then it clicked that if I maintain a binary search tree intead of min and max, then I will need only log(n) comparisons to get my answer 
//for each element.
//Every node in the binary search tree will record how many elements are to its left. Keep a running total of the number of inversions
//as you insert a new node in the tree. Note, the binary search tree should be generated back to front.
//TC = O(nlogn) SC=O(n)
#include <iostream>
#include <memory>
#include <vector>
using namespace std;

struct Node {
    int value;
    int left_cnt = 0;
    shared_ptr<Node> left = nullptr;
    shared_ptr<Node> right = nullptr;
};

void InsertTree(shared_ptr<Node>& head, shared_ptr<Node>& current)
{
    if (head == nullptr)
    {
        head = current;
        return;
    }

    if (head->value < current->value)
    {
        current->left_cnt = head->left_cnt + 1;
        InsertTree(head->right, current);
    }
    else
    {
        head->left_cnt += 1;
        InsertTree(head->left, current);
    }
}

int FindInversions(const vector<int>& arr)
{
    int total = 0;
    shared_ptr<Node> head = nullptr;
    for (auto itr = arr.rbegin(); itr != arr.rend(); itr++)
    {
        shared_ptr<Node> current = make_shared<Node>();
        current->value = *itr;
        InsertTree(head, current);
        total += current->left_cnt;
    }
    return total;
}