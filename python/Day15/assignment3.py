# Task 1:
# 1. create  class node for the Dll  Data, prev ,next
# 2. create class   for Dll  head is None and Tail is None
# 3. Add a Node.   dll1.append(10)  
# 4. Find the length of Dll
# 5. Search an Element in a Doubly Linked List in Python:

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Dll:
    def __init__(self ):
        self.head=None
        self.tail=None
    def isEmpty(self):
        if self.head is None:
           return True
        else:
           return False
    def length(self):
        cnt=0
        temp=self.head
        while temp is not None:
            cnt=cnt+1
            temp=temp.next 
    def search(self , value):
        foung=False
        while temp is not None:
            if temp.data==value:
               found=True 
               break 
            else: 
               temp=temp.next 
               return found 
    def add(self,data ):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            pass
dll=Dll() 
#n1=Node(10)
dll.add(10)
if dll.isEmpty():
    print("Empty Double linked List")
else:
    print("Not an Empty Double Linked List")
# node is created but this node is not added to dll and hence length is zero 
 