// This problem was asked by Amazon.

// Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
// You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
// If there's no way to break the text up, then return null.

// You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

// For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
// you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

// This is basically a greedy algorithm. Grab words as long as possible (limited by k) and then recurse on the remaining words.
// TC - O(N), SC - O(N) + Number of recursions (number of words) - approx O(N)

// PReviously I was keep track of min lines, which is not needed and unnecessarily recurses a lot of execution paths.

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

void splitlines(string &input, int idx, int k, vector<string> &result)
{
    if (idx >= input.size())
    {
        return;
    }

    int nSpace = input.find(' ', idx);
    if (nSpace == string::npos)
    {
        nSpace = input.size();
    }

    int pIdx = -1;
    while (nSpace - idx <= k)
    {
        pIdx = nSpace;
        if (nSpace == input.size())
            break; // Bug here

        nSpace = input.find(' ', nSpace + 1);

        if (nSpace == string::npos)
        {
            nSpace = input.size();
        }
    }
    if (pIdx == -1)
    {
        result.clear(); // Bug here.
        return;
    }
    result.push_back(input.substr(idx, pIdx - idx));
    splitlines(input, pIdx + 1, k, result);
}