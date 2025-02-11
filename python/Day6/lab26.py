#Basic Queue Implementation Using List
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return an item from the front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue"""
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2