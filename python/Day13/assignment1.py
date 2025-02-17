# Task 1 :
# 1. create 4 nodes n1 , n2, n3 and n4 with the values "Sun" ,"Mon" , "Tue" , "Wed"  and "Thu"  respectively.
# 2. create simple linked list with these four  nodes
# 3. print these nodes data from head to end
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
n1 = Node("Sun")
n2 = Node("Mon")
n3 = Node("Tue")
n4 = Node("Wed")
n5 = Node("Thu")

# Linking nodes to form a linked list
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Print the linked list
print_list(n1)
