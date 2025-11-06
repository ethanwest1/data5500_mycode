#Ethan Westenskow
import networkx as nx
import os

curr_dir = os.path.dirname(__file__)
edges_fil = curr_dir + '/' + 'sample_graph.txt'
g = nx.DiGraph()

edges = []
file = open(edges_fil)
for line in file.readlines():
    line = line.strip()
    node1, node2 = line.split(' ')
    edges.append((node1, node2))

g.add_edges_from(edges)
# print(g.nodes)

#Node Degree > 5 logic:
total = 0
qualifying_nodes = []
for node in g.nodes:
    if g.degree(node) > 5:
        total += 1
        qualifying_nodes.append(node)

print()
print(f'There are a total of {total} nodes that have a degree greater than 5.\n')
print('Those nodes are: \n', qualifying_nodes)

######################################################################################
# ------------------------------------------------------------
# QUESTIONS ASKED DURING CHAT
# ------------------------------------------------------------

# I need help understanding this question.
# 
# 2. Write a Python function that takes a NetworkX graph as input 
# and returns the number of nodes in the graph that have a degree greater than 5

# ------------------------------------------------------------

# give me a .txt file that I can use for this problem.

# ------------------------------------------------------------

# Does this code satisfy the question? 
#
# #Ethan Westenskow
# import networkx as nx
# import os
#
# curr_dir = os.path.dirname(__file__)
# edges_fil = curr_dir + '/' + 'sample_graph.txt'
# g = nx.DiGraph()
#
# edges = []
# file = open(edges_fil)
# for line in file.readlines():
#     line = line.strip()
#     node1, node2 = line.split(' ')
#     edges.append((node1, node2))
#
# g.add_edges_from(edges)
# print(g.nodes)
#
# #Node Degree > 5 logic:
# total = 0
# qualifying_nodes = []
# for node in g.nodes:
#     if g.degree(node) > 5:
#         total += 1
#         qualifying_nodes.append(node)
#         
# print(f'There are a total of {total} nodes that have a degree greater than 5.')
# print('Those nodes are: ', qualifying_nodes)

# ------------------------------------------------------------

# give me another sample_graph.txt with even more nodes

# ------------------------------------------------------------

# Give me one with hundreds of nodes

# ------------------------------------------------------------

# Give me a summary of the questions that I asked you during this chat

# ------------------------------------------------------------


