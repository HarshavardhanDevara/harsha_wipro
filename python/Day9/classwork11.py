from collections import deque  
dq = deque()
dq = deque([1, 2, 3, 4])
# 4. Rotating Deque:
# rotate(n): Rotates elements n steps to the right (negative for left rotation).
dq.rotate(2)  # Right rotation by 2 steps
print(dq)  # Output: deque([6, 7, -1, -2, 1, 2, 3, 4, 5])

dq.rotate(-1)  # Left rotation by 1 step
print(dq)  # Output: deque([7, -1, -2, 1, 2, 3, 4, 5, 6])