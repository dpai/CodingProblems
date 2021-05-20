#include <iostream>
#include <vector>
#include <memory>
using namespace std;

extern int FindInversions(const vector<int> &arr);
extern void findmaxOfK(vector<int> &ip, int k);
extern void splitlines(string &input, int idx, int k, vector<string> &result);

template <class T>
void printVector(vector<T> arr)
{
    for (auto &i : arr)
    {
        cout << i << "\n";
    }
    cout << "\n";
}

int main()
{
    vector<int> arr{2, 4, 1, 3, 5};

    cout << "Inversions : " << FindInversions(arr) << endl;

    cout << "Inversions : " << FindInversions({5, 4, 3, 2, 1}) << endl;

    cout << "Inversions : " << FindInversions({5, 1, 2, 3, 4}) << endl;

    cout << "Inversions : " << FindInversions({5}) << endl;

    vector<int> ip = {10, 5, 2, 7, 8, 7};
    findmaxOfK(ip, 3);
    ip = {7, 7, 7, 7, 7};
    findmaxOfK(ip, 1);

    string str("Mocks");
    vector<string> result;
    splitlines(str, 0, 4, result);
    printVector(result);

    return 0;
}