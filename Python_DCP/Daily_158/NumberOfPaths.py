## You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?
## Recursion - recurrence relation f(i,j) = f(i+i,j) + f(i,j+1) if (i,j) = 0 , base case f(n-1,m-1) = 1
## This can also be solved using DP,
## Both implementations are below.

def recursive_solution(i, j, grid):
    if i >= len(grid) or j >= len(grid[0]):
        return 0
    if grid[i][j] == 1:
        return 0
    if (i == len(grid)-1) and (j == len(grid[0])-1):
        if i == 0 and j == 0:
            return 0
        else:
            return 1

    return recursive_solution(i+1, j, grid) + recursive_solution(i, j+1, grid)

def iterative_solution(grid):
    row = len(grid)
    col = len(grid[0])

    output = [[0 for i in range(col+1)] for j in range(row+1)]

    if grid[row-1][col-1] == 0:
        if (row != 1 or col != 1):
            output[row-1][col-1] = 1

    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            if (i == row - 1) and (j == col - 1):
                continue
            if grid[i][j] != 1:
                output[i][j] = output[i+1][j] + output[i][j+1]

    return output[0][0]

if __name__ == "__main__":
    grid = [[0 for i in range(2)] for j in range(2)]

    # Recursion answer
    op1 = recursive_solution(0,0,grid)
    op2 = iterative_solution(grid)

    print("Recursive : Paths : "  + str(op1))
    print("Iterative : Paths : "  + str(op2))