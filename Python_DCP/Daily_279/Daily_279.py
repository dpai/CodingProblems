#A classroom consists of N students, whose friendships can be represented in an adjacency list. 
# For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

#{0: [1, 2],
# 1: [0, 5],
# 2: [0],
# 3: [6],
# 4: [],
# 5: [1],
# 6: [3]} 

# Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations.
# In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

# Given a friendship list such as the one above, determine the number of friend groups in the class.

def helper(adjlist, visited, i):
    visited[i] = 1
    n = adjlist[i]

    sz = len(n)

    for j in range(0, sz):
        if visited[n[j]] == 0:
            helper(adjlist, visited, n[j])

def nmbeofgroups(adjlist):
    sz = len(adjlist)
    visited = [0] * sz
    count = 0
    for i in range(0, sz):
        if visited[i] == 0:
            helper(adjlist, visited, i)
            count += 1
    
    return count

if __name__ == "__main__":
    adjlist = {}
    adjlist[0] = [1,2]
    adjlist[1] = [0,5]
    adjlist[2] = [0,]
    adjlist[3] = [6,]
    adjlist[4] = []
    adjlist[5] = [1,]
    adjlist[6] = [3,]

    group = nmbeofgroups(adjlist)
    print("Number of groups is {}".format(group))