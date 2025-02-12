from collections import deque 
dq = deque()
dq = deque([1, 2, 3, 4])
# 5. Limiting Deque Size:
# deque(iterable, maxlen=n): Creates a deque with a fixed maximum length.
dq = deque([1, 2, 3], maxlen=5)  # Max size = 5
print(dq)  # Output: deque([1, 2, 3], maxlen=5)

dq.append(4)
dq.append(5)
dq.append(6)  # Oldest element (1) is removed automatically
print(dq)  # Output: deque([2, 3, 4, 5, 6], maxlen=5)


