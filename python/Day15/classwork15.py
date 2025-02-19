# InOrder 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def in_order_traversal(root):
    if root is None:
        return
 
    # Traverse the left subtree
    in_order_traversal(root.left)
 
    # Visit the root node
    print(root.data, end=" ")
 
    # Traverse the right subtree
    in_order_traversal(root.right)
 
 
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("In-Order Traversal: ", end="")
in_order_traversal(root)
print()
 

