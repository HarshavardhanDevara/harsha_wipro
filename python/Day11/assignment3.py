# Assigment 3 :  Create an empty queue using class , 
# add and remove elements  and print  elements
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def print_queue(self):
        print(self.queue)

# Create an empty queue
q = Queue()
# Add elements to the queue
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
# Print elements of the queue
q.print_queue()  
# Remove elements from the queue
q.dequeue()      #11 removed
q.print_queue()  
q.dequeue()        #22 
q.print_queue() 
q.dequeue()        #33
q.print_queue()  
# Check if the queue is empty
if q.is_empty():
    print("Queue is empty")

