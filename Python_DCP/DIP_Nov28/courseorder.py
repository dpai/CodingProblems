""" Hi, here's your problem today. This problem was recently asked by Google:

You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

Example:

{
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}


This input should return the order that we need to take these courses:

 ['CSC100', 'CSC200', 'CSCS300']


Here's your starting point: """

def helper(stack, course_to_prereqs, cur, visited):
    if cur in visited:
        return

    neighbors = course_to_prereqs[cur]

    visited.add(cur)
    for e in neighbors:
        helper(stack, course_to_prereqs, e, visited)

    stack.append(cur)

def courses_to_take(course_to_prereqs):
  # Fill this in.
  stack = []
  visited = set()
  
  for i in course_to_prereqs.keys():
      helper(stack, course_to_prereqs, i, visited)

  return stack
    

if __name__ == "__main__":
    courses = {
    'CSC300': ['CSC100', 'CSC200'], 
    'CSC200': ['CSC100'], 
    'CSC100': []
    }
    print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']

# Insight - This is basically a topological sort problem on a graph and can be solved by maintaining a stack that will be populated
# only when all of its neighbors are visited when traversing the graph via DFS. Note that the input should be a DAG but I think can
# have more than 1 component. However, the solution does not detect cycles in the graph. It will be invalid if there is a cycle
# since you cannot determine order in that case.