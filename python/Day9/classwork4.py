from collections import deque  # Import deque from the collections module


class Stack:
    # Initialize the stack with an empty deque
    def __init__(self):
        self.stack = deque()

    # Method to add an element to the top of the stack
    def push(self, data):
        self.stack.append(data)  # Append the data to the deque

    # Method to remove and return the top element of the stack
    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"  # Remove and return the top element if the stack is not empty

    # Method to return the top element of the stack without removing it
    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"  # Return the top element if the stack is not empty

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0  # Return True if the stack is empty, otherwise False

    # Method to display the elements of the stack
    def display(self):
        print(list(self.stack))  # Print the deque as a list

# Usage example
s = Stack()  # Create an instance of the Stack class
s.push(5)  # Push the value 5 onto the stack
s.push(15)  # Push the value 15 onto the stack
s.display()  # Display the current elements of the stack, Output: [5, 15]
print(s.pop())  # Pop the top element from the stack and print it, Output: 15
s.display()  # Display the current elements of the stack after pop, Output: [5]
print(s.peek())  # Peek at the top element of the stack and print it, Output: 5
s.display()  # Display the current elements of the stack after peek, Output: [5]