class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
 
class SLinkedList:     #linked is a collection of nodes , connecting to each other. One way traversal is allowed , not two way
    def __init__(self):
      self.head = None
 
    def listprint(self):
      a = self.head
      while a is not None:
         print(a.data)
         a=a.next
 
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