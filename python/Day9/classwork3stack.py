# Define the Stack class
class Stack:
    # Initialize the stack with an empty list
    def __init__(self):
        self.stack = []

    # Method to add an element to the top of the stack
    def push(self, data):
        self.stack.append(data)  # Append the data to the list

    # Method to remove and return the top element of the stack
    def pop(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.stack.pop()  # Remove and return the top element
        return "Stack is empty"  # Return a message if the stack is empty

    # Method to return the top element of the stack without removing it
    def peek(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.stack[-1]  # Return the top element
        return "Stack is empty"  # Return a message if the stack is empty

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0  # Return True if the stack is empty, otherwise False

    # Method to display the elements of the stack
    def display(self):
        print(self.stack)  # Print the list representing the stack

# Usage example
s = Stack()  # Create an instance of the Stack class
s.push(10)  # Push the value 10 onto the stack
s.push(20)  # Push the value 20 onto the stack
s.push(30)  # Push the value 30 onto the stack
s.push(40)  # Push the value 40 onto the stack
s.display()  # Display the current elements of the stack, Output: [10, 20, 30, 40]
print(s.pop())  # Pop(removes) the top element from the stack and print it, Output: 40
print(s.peek())  # Peek at the top element of the stack and print it, Output: 30
s.display()