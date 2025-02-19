class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            pass    
 
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
 
# Example usage:
dll = DoublyLinkedList()
dll.append(1)
print("Forward traversal of the doubly linked list:")
dll.traverse_forward()  # Output: 1 <-> 2 <-> 3 <-> 4 <-> None