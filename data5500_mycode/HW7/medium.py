# Implement a Python function to search for a value in a binary search tree.
#  The method should take the root of the tree and the value to be searched as parameters.
#  It should return True if the value is found in the tree, and False otherwise.

#My BST code from easy.py
class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
def insert_bst(root, value):
    if root is None:
        return Node(value)
    elif root.key > value:
        root.left = insert_bst(root.left, value)
    elif root.key < value:
        root.right = insert_bst(root.right, value)
    else:
        return root
    return root

    # Build a small tree: 7, 3, 9, 1, 5
root = None
for v in [7, 3, 9, 1, 5]:
    root = insert_bst(root, v)

print(root.key, root.left.key, root.right.key)  # Expect: 7 3 9
print("Tree built for problem.")

##_____Answer!!!
target = 4 #change this number to whatever you'd like to search for.
node = root #pulls the tree in

def search_bst(node, target):
    while node is not None:
        if target == node.key:
            return True
        elif target < node.key:
            node = node.left
        else:
            node = node.right
    return False

print(search_bst(node, target))







#____ ChatGPT convo below:
# Conversation Log (Ethan's Messages)
# ------------------------------------------------------------
# Act as a tutor helping me figure out this question. 
# I want to understand the concepts so don't just give me the answer. 
# I need to understand the concepts more before I attempt the problem. 
# What questions do you have for me?
#
# 1. Implement a Python function to search for a value in a binary search tree. 
#    The method should take the root of the tree and the value to be searched as parameters. 
#    It should return True if the value is found in the tree, and False otherwise.
# 2. Python
# 3. Starting from scratch
#
# How does this bst code look? 
#
# class Node:
#     def __init__(key, value):
#         self.key = key
#         self.right = None
#         self.left = None
# def insert_bst(root, value):
#     if root.key is None:
#         return root
#     elif root.key > value:
#         root.left = insert_bst(root, value)
#     elif root.key < value:
#         root.right = insert_bst(root, value)
#     else:
#         return root
#     return root
#
# Does this bst work to create a tree that we will use for this problem?
#
# Help me fix my code rather than just giving me the correct code.
#
# Here's my code:
# class Node:
#     def __init__(key, value):
#         self.key = key
#         self.right = None
#         self.left = None
# def insert_bst(root, value):
#     if root.key is None:
#         return Node(value)
#     elif root.key > value:
#         root.left = insert_bst(root, value)
#     elif root.key < value:
#         root.right = insert_bst(root, value)
#     else:
#         return root
#