# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions 
# required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: 
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

## Insight - This is a dynamic programming question. The recursion is 
## If f(i,j) - where i is the index into the first word, and j is the index into the second word
## f(i,j) = 1 + min(f(i+1,j+1) [Replace], f(i,j+1) [Add], f(i+1, j) [Delete]). (Contraint add 1 only if first[i] != second[j])
## Base case is when both strings are empty, the answer is 0
## TC O(nm) SC O(nm)
#import pprint

def editdistance(first, second):
    col = len(first)
    row = len(second)

    data = [[0] * (col+1) for i in range(row+1)]

    for i in range(col):
        data[row][i] = (col - i)
    for j in range(row):
        data[j][col] = (row - j)

    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            data[i][j] = min(data[i+1][j+1], data[i][j+1], data[i+1][j])
            if (first[j] != second[i]):   ## This is important case to understand. Edit happens only when letters mismatch.
                data[i][j] = data[i][j] + 1

#    pprint.pprint(data)

    return data[0][0]

if __name__ == "__main__":
    first = "kitten"
    second = "sitting"
    print("Number of substitutions needed " + str(editdistance(first, second)))
    # 3
    ## Check for empty strings
    first = ""
    second = ""
    print("Number of substitutions needed " + str(editdistance(first, second)))
    # 0
    ## No characters matching
    first = "xyz"
    second = "abc"
    print("Number of substitutions needed " + str(editdistance(first, second)))
    # 3
    ## Same strings
    first = "hello"
    second = "hello"
    print("Number of substitutions needed " + str(editdistance(first, second)))
    # 0
