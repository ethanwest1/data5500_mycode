### TREES
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
        print(root.key, end=" ") 
        preorder(root.left)
        preorder(root.right)

#in-order
def inorder(root):
    if root is None:
        inorder(root.left)
        print(root.key, end=" ") 
        inorder(root.right)

#post-order
def postorder(root):
    if root is None: 
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ") 

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


### Recursion
#Factorial code
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)

### Python Dictionary / JSON
my_dict = {'fname': 'Ethan', 'lname': 'Westenskow', 'Age': 23}
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(my_dict[key])

#save to json
# import json
# with open('student.json', 'w') as f:
#     json.dump(student, f)


#bubble sort practice
lst = [47, 12, 89, 5, 63, 22, 78, 36, 91, 10]

for x in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
