from collections import deque  
dq = deque()
dq = deque([1, 2, 3, 4])
# 2. Removing Elements:
# pop(): Removes and returns the rightmost element.
dq.pop()  # Removes and returns the rightmost element (5)
print(dq)  # Output: deque([0, 1, 2, 3, 4])

# popleft(): Removes and returns the leftmost element.
dq.popleft()  # Removes and returns the leftmost element (0)
print(dq)  # Output: deque([1, 2, 3, 4])