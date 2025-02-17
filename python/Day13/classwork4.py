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
 
    def AtEnd(self, data):
      ne=Node(data)
      last = self.head
      while(last.next):
         last = last.next
      last.next=ne
 
 
list = SLinkedList()
e1 = Node("1")
list.head=e1
e2 = Node("2")
e3 = Node("3")
# Link first Node to second node
e1.next= e2
# Link second Node to third node
e2.next= e3
list.listprint()  
print("Printing after insert at the begining")
list.AtBegining("0")
list.listprint()
print("Printing after insert at the End")
list.AtEnd("4")
list.listprint()