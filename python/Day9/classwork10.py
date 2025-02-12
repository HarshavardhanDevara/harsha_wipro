from collections import deque  
dq = deque()
dq = deque([1, 2, 3, 4])
# 3. Extending Deque:
# extend(iterable): Adds elements from an iterable to the right.
dq.extend([5, 6, 7])  # Adds elements 5, 6, 7 to the right end
print(dq)  # Output: deque([1, 2, 3, 4, 5, 6, 7])

# extendleft(iterable): Adds elements from an iterable to the left (in reverse order).
dq.extendleft([-2, -1])  # Adds elements -2, -1 to the left end in reverse order
print(dq)  # Output: deque([-1, -2, 1, 2, 3, 4, 5, 6, 7])