from collections import deque 
dq = deque()
dq = deque([1, 2, 3, 4])
# 1. Appending Elements
# append(x): Adds x to the right end.
dq.append(5)  # Adds 5 to the right end
print(dq)  # Output: deque([1, 2, 3, 4, 5])

# appendleft(x): Adds x to the left end.
dq.appendleft(0)  # Adds 0 to the left end
print(dq)  # Output: deque([0, 1, 2, 3, 4, 5])