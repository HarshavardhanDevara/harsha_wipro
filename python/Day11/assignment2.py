# Assignment 2 : python script to create empty stack , add some elements ,
# pop top most value  , print elements of stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        print("Stack elements:", self.stack)

# Create an empty stack
my_stack = Stack()

# Adding some elements
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(25)

# Pop the topmost value
popped_value = my_stack.pop()
print(f"Popped value: {popped_value}")

# Print elements of the stack
my_stack.print_stack()