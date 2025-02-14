# import queue
# # Instantiate the Queue object
# q = queue.Queue()
# # Insert elements 1 to 5 in the queue
# for i in range(1, 6):
#     q.put(i)
# print('Now, q.qsize() =', q.qsize())
# # Empty queue
# q.empty()
# print('After emptying, size =', q.qsize())
# for i in range(q.qsize()):
#     print(q.get())

import queue
# Instantiate the Queue object
q = queue.Queue()
# Insert elements 1 to 5 in the queue
for i in range(1, 6):
    q.put(i)
print('Now, q.qsize() =', q.qsize())
 
for i in range(q.qsize()):
    print(q.get())
# Empty queue
q.empty()
print('After emptying, size =', q.qsize())
for i in range(q.qsize()):
    print(q.get())
print(q.empty())