// #Hi, here's your problem today. This problem was recently asked by Twitter:

// #Given a string with the initial condition of dominoes, where:

// #. represents that the domino is standing still
// #L represents that the domino is falling to the left side
// #R represents that the domino is falling to the right side

// #Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

// #Example:
// #Input:  ..R...L..R.
// #Output: ..RR.LL..RR
// #Here is your starting point:

#include <string>
#include <iostream>

class Solution 
{
    public:
    void make_one(int st, int en, std::string& output)
    {
        while(st < en)
        {
            output[st] = 'R';
            output[en] = 'L';
            st++;
            en--;
        }
    }

    void pushDominoes(std::string& dominoes)
    {
        int start = 0;
        int sz = dominoes.size();

        for (int en = 0; en < sz; en++)
        {
            if (dominoes[en] == 'L')
            {
                if (dominoes[start] = 'R')
                    make_one(start, en, dominoes);
                else
                {
                    for (int i = start; i < en; i++)
                        dominoes[i] = 'L';
                }
                start = en;
            }
            else if (dominoes[en] == 'R')
            {
                dominoes[en] = 'R';
                start = en;
            }
        }

        if (dominoes[start] == 'R')
        {
            for (; start < sz; start++)
            {
                dominoes[start] = 'R';
            }
        }
    }
};

int main()
{
    std::string input = "..R...L..R.";
    Solution().pushDominoes(input);
    std::cout << input << '\n';
}

// if __name__ == "__main__":
//   print(Solution().pushDominoes('..R...L..R.'))
//   # ..RR.LL..RR
//   print(Solution().pushDominoes('......'))
//   print(Solution().pushDominoes('....L'))
//   print(Solution().pushDominoes('R....'))
//   print(Solution().pushDominoes('..R..'))
//   print(Solution().pushDominoes('..L..'))
//   print(Solution().pushDominoes('R.........L'))
//   print(Solution().pushDominoes('L.........R'))