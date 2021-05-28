# This problem was asked by Apple.

# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: 
# enqueue, which inserts an element into the queue, and dequeue, which removes it.

## Below is the implementation. enqueue is O(1) and dequeue is O(N)

class queue_stack:
    enqueue_stack = []
    dequeue_stack = []

    def __init__(self):
        pass

    def enqueue(self, val):
        self.enqueue_stack.append(val)

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                return None
            
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack[-1])
                self.enqueue_stack.pop()

        val = self.dequeue_stack[-1]
        self.dequeue_stack.pop()
        return val

if __name__ == "__main__":
    q = queue_stack()

    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(9)
    q.enqueue(90)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
