""" Good morning! Here's your coding interview problem for today.

This problem was asked by Samsung.

A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:

A <--> B <--> C <--> plant
Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.

pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
} """

## Prims Algorithm implementation.

import heapq

def smallestconfigcost(pipes):
    heap = []

    heapq.heappush(heap, (0, 'plant'))
    visited = []
    smallestcost = 0

    while (len(heap) != 0):
        node = heap[0]
        heapq.heappop(heap)

        if (node[1] in visited):
            continue

        visited.append(node[1])
        smallestcost = smallestcost + node[0]

        neighbors = pipes[node[1]]

        for k, v in neighbors.items():
            heapq.heappush(heap,(v, k))

    return smallestcost

if __name__ == "__main__":
    pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
    }

    print("Smallest config is " + str(smallestconfigcost(pipes)))