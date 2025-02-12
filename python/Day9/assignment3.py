# Assignment 3 :
# create stack using deque.
# do some opeations like append ,appendleft , pop , popleft , rotate left and right and print stack

from collections import deque

stack = deque()

stack.append('h')
stack.append('a')
stack.append('r')
print("Stack after append operations:", stack)

stack.appendleft('s')
stack.appendleft('h')
stack.appendleft('a')
print("Stack after appendleft operations:", stack)

stack.pop()
print("Stack after pop operation:", stack)

stack.popleft()
print("Stack after popleft operation:", stack)

stack.rotate(1)
print("Stack after rotate right operation:", stack)

stack.rotate(-2)
print("Stack after rotate left operation:", stack)