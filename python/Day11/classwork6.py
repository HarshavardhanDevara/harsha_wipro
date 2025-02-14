class MyQueue():
 
    # Using Python Lists as a Queue
    def __init__(self):
        self.queue = []
 

    def enqueue(self, value):
        # Inserting to the end of the queue
        self.queue.append(value)
    def dequeue(self):
         # Remove the furthest element from the top,
         # since the Queue is a FIFO structure
         return self.queue.pop(0)

my_q = MyQueue()
my_q.enqueue(2)
my_q.enqueue(5)
my_q.enqueue(7)
for i in my_q.queue:
    print(i)
print('Popped,', my_q.dequeue())
for i in my_q.queue:
    print(i)