class Node:
    def __init__(self, dataval=None):
      self.data = dataval
      self.next = None
class SLinkedList:
    def __init__(self):
      self.head = None
    def listprint(self):
      a = self.head
      while a is not None:
         print (a.data)
         a=a.next
    def AtBegining(self,data):
      nb = Node(data)
      # Update the new nodes next val to existing node
      nb.next = self.head
      self.head = nb
 
    def Inbetween(self,mn,data):
         nn = Node(data)
         nn.next = mn.next
         mn.next= nn
     # Update a node's value
    def update(self, old_value, new_value):
        temp = self.head   # points to the first node 
        while temp:
            if temp.data == old_value:
                temp.data = new_value
                return
            temp = temp.next
        print(f"Value {old_value} not found in list.")
 
    
 
 
    def AtEnd(self, data):
      ne=Node(data)
      last = self.head
      while(last.next):
         last = last.next
      last.next=ne
list = SLinkedList()
e1 = Node("10")
list.head=e1
e2 = Node("20")
e3 = Node("30")
# Link first Node to second node
e1.next= e2
# Link second Node to third node
e2.next= e3
list.listprint()  
print("Printing after insert at the begining")
list.AtBegining("0")
list.listprint()
print("Printing after insert at the End")
list.AtEnd("40")
list.listprint()
print("\n Updating  the data \n")
list.update("30","35")  # old value is 30 and new value is 35
list.listprint()