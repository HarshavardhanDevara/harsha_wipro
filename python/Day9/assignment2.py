# Assignment 2 :
# create stack using list . do some operations like  push ,pop , peek and 
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from stack")
            return item
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Top item is {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack elements are:", self.stack)
if __name__ == "__main__":
    s = Stack()
    s.push(44)
    s.push(12)
    s.push(22)
    s.push(92)
    s.push(64)
    s.push(88)
    s.display()
    s.peek()
    s.pop()
    s.display()
    s.pop()
    s.pop()
    s.pop()
    s.display()
