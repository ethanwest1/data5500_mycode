# Write a Python function to insert a value into a binary search tree. 
# The function should take the root of the tree and the value to be inserted as parameters.

class Node:  #Creates the base node structure.
    def __init__(self, key): #creates node with no children.
        self.key = key
        self.left = None
        self.right = None
    
def insert_bst(root, value): 
    if root is None: #Base Case, stops the recursion
        return Node(value)
    elif value < root.key: # Creates the node to the left if it's less than the root.
        root.left = insert_bst(root.left, value)
    elif value > root.key: # Creates the node to the right if it's greater than the root.
        root.right = insert_bst(root.right, value)
    else: # Deals with duplicates by simply returning the root.
        return root
    return root

#__Test and ChatGPT stuff below...






#___ Test
values = [5, 2, 3, 4, 7, 6, 1]

root = None
for value in values:
    root = insert_bst(root, value)

print('Root', root.key)
print('Left', root.left.key)
print('Right', root.right.key)


#My chatgpt stuff is below. 
"""
────────────────────────────────────────────────────────────
🧠  QUESTIONS I ASKED WHILE LEARNING BINARY SEARCH TREES
────────────────────────────────────────────────────────────

1️⃣  Understanding the problem
------------------------------
- Write a Python function to insert a value into a binary search tree. 
  The function should take the root of the tree and the value to be inserted as parameters.
- I don’t fully understand the concepts necessary to complete it so let’s get that down before I attempt it.
- How is the root determined?

2️⃣  Concept building
---------------------
- What other concepts do I need to know before attempting this problem?
- Is a node simply a Python object data type?
- Give me the Python basics of a class.

3️⃣  Planning & design
----------------------
- Do I create my insert function within the Node class?
- Give me the pseudocode for this problem. I'd like to do recursion.

4️⃣  Coding stage
-----------------
- This is what I'm thinking of doing: I'll define a class with 3 functions.
  The first function will compare the value to the root, the other functions will assign the value 
  to either the left or right until it comes to a node that equals None.
- How does this look so far? (several iterations of code review)
- How does this look now? (multiple refinements of syntax and logic)

5️⃣  Testing & debugging
------------------------
- How do I test this?
- Give me just one thing of code that I can copy and paste to test my code. 
  Make the output nice to look at.
- How would I write code to test this?
- Can you display it vertically?
- Give me the most simple test code for my code ever.
- How would I change this to have it create the tree from a list?
- That didn't display for the entire list.
- What's wrong with this test code?

6️⃣  Reflection
---------------
- Give me a summary of the questions that I asked you to help me figure out this problem.
- Give me a copy and paste format for my Python code of all of the questions that I asked you during our conversation.

────────────────────────────────────────────────────────────
✅  Notes:
This session covered:
• Understanding BST structure (root, left, right)
• Recursive insertion logic
• Python class & object basics
• Testing from a list and traversals
• Debugging and printing the full tree

────────────────────────────────────────────────────────────
"""