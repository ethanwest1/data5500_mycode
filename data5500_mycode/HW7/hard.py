# Explain the process of deleting a node from a binary search tree in Python. 
# Discuss how you would handle different cases, such as deleting a node with one, or two children. 
# Additionally, explain any potential challenges or edge cases that may arise during the deletion process and how you would address them. 

#__Answer:
To delete a node we first need to find the value within our tree, and then we have to figure
out where to place the node's children (if applicable) in order to maintain the order of
the tree. If the node has no children, then we don't need to worry because we can simply
delete it and return none to the parent to keep the integrity and sorted order of the tree.
If the node has one child node then the child node simply takes the place of the deleted 
node, which will maintain the structure and sorted order of the tree. If the node has 2 
children then we would choose the minimum node to the right subtree to replace the 
node that is being deleted, we then would have to delete the minimum node from the right 
subtree that we used to replace the deleted node. 