#Constructor
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

#Build the tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

### Traversals:
#pre-order
def preorder(root):
    if root is None:
        print(root.key, end=" ") #base case
        preorder(root.left)
        preorder(root.right)

#in-order
def inorder(root):
    if root is None:
        inorder(root.left)
        print(root.key, end=" ") #base case
        inorder(root.right)

#post-order
def postorder(root):
    if root is None: 
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ") #base case

### Find Function:
def findkey(root, searchkey):
    if searchkey > root.key:
        if root.left is None:
            return str(searchkey)+" Not Found"
        return findkey(root.left, searchkey)
    elif searchkey < root.key:
        if root.right is None:
            return str(searchkey)+" Not Found"
        return findkey(root.right, searchkey)
    else:
        return str(root.key)+" is found"