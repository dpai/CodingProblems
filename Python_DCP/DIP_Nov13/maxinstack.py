#Hi, here's your problem today. This problem was recently asked by Twitter:

##By the way, check out our NEW project AlgoPro (http://algopro.com
#) for over 60+ video coding sessions with ex-Google/ex-Facebook engineers.

#Implement a class for a stack that supports all the regular functions (push, pop) and an additional function 
# of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
  def __init__(self):
    # Fill this in.
    self.stack = []
    self.maxstack = []

  def push(self, val):
    # Fill this in.
    self.stack.append(val)
    if len(self.maxstack) and val >= self.maxstack[-1]:
        self.maxstack.append(val)
    if len(self.maxstack) == 0:
        self.maxstack.append(val)

  def pop(self):
    # Fill this in.
    if len(self.stack):
        val = self.stack[-1]
        if val == self.maxstack[-1]:
            self.maxstack.pop()
        self.stack.pop()

  def max(self):
    # Fill this in.
    if len(self.maxstack):
        return self.maxstack[-1]

    return None