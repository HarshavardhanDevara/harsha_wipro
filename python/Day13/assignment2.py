# Assignment-2:
# create linked list with nodes  with data 10 ,20 , 30 and 40.
# we need to add a new node after given node , lets say 35 after 30
# data must be obtained from console , we must add new node after given the node
# lets say
#   10  20   30   40   50
#   read value from console lets say x=30 and new data node with data 35
# so new list is
#   10  20  30   35  40  50

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_after(self, prev_data, new_data):
        temp = self.head
        while temp:
            if temp.data == prev_data:
                new_node = Node(new_data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"Node with data {prev_data} not found.")

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Creating the linked list
ll = LinkedList()
for value in [10, 20, 30, 40, 50]:
    ll.append(value)

# Display the original list
print("Original list:")
ll.display()

# Taking user input to insert new node
target = int(input("Enter the node after which to insert: "))
new_value = int(input("Enter the new node value: "))
ll.insert_after(target, new_value)

# Display the updated list
print("Updated list:")
ll.display()
