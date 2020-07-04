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

#include <problem.h>
#include <string>

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