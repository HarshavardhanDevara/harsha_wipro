import queue
# Instantiate the Queue object
q = queue.Queue()
# Insert elements 1 to 5 in the queue
for i in range(1, 6):
    q.put(i)
print('Now, q.qsize() =', q.qsize())
# Now, the queue looks like this:
# (First) 1 <- 2 <- 3 <- 4 <- 5
 
for i in range(q.qsize()):
    print(q.get())