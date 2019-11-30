""" Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance. 
That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, coins are o, and empty spaces are . (top left is 0, 0):

---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------

return (0, 4), since that coin is closest. This map would be represented in our question as:

Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)] """

#Insight - This was a easy problem. Have a gird and find the location of the closest coin is basically running a Breadth first search on a graph
#where the cells are nodes and neighbor set is the edges. Whenever we find a coin, we know that is closest to the location.
#Note the assumption here that the grid is not bounded in the positive direction and starting at (0,0), ie no negative indexes on cell
#We need to initially look if there are coins on the grid to not risk infinite loop.

def closestCoin(myPos, coins_on_grid):
    if len(coins_on_grid) == 0:
        return None
         
    queue = []

    neighbors = [(0,1), (0,-1), (1,0), (-1,0)]

    queue.append((myPos))

    visited = set()

    while len(queue) != 0:
        curPos = queue[0]
        del queue[0]
        if (curPos in visited):
            continue
        visited.add(curPos)
        
        for i in range(len(neighbors)):
            newPos = tuple([sum(x) for x in zip(curPos,neighbors[i])])
            if (newPos[0] < 0 or newPos[1] < 0):
                continue
            if (newPos in coins_on_grid):
                return newPos
            queue.append(newPos)

    return None

if __name__ == "__main__":
    myPos = (0,2)
    Coins = [(0, 4), (1, 0), (2, 0), (3, 2)] 
    print("Closest Coin is ", closestCoin(myPos, Coins))
