class Node:

    def __init__(self, data):

        self.data = data

        self.next = None
 
class CircularLinkedList:

    def __init__(self):

        self.head=None
 
 
    def insert_at_beginning(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node

            new_node.next = self.head

        else:

            curr = self.head

            while curr.next != self.head:

                curr = curr.next

            curr.next = new_node

            new_node.next = self.head

            self.head = new_node
 
    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node

            new_node.next = self.head

        else:

            curr = self.head

            while curr.next != self.head:

                curr = curr.next

            curr.next = new_node

            new_node.next = self.head
 
    def traverse(self):

        if self.head is None:

            print("List is empty!")

            return

        curr = self.head

        while True:

            print(curr.data, end=" ")

            curr = curr.next

            if curr == self.head:

                break

        print()
 
    def search(self, data):

        if self.head is None:

            print("List is empty!")

            return False

        curr = self.head

        while True:

            if curr.data == data:

                return True

            curr = curr.next

            if curr == self.head:

                break

        return False
 
# Testing the Circular Linked List

cll = CircularLinkedList()

cll.insert_at_beginning(10)

cll.insert_at_beginning(20)

cll.traverse()