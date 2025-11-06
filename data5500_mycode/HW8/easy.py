# Ethan Westenskow

# Write a Python function that takes a NetworkX graph as input and returns the number of nodes in the graph.

import networkx as nx
import os

curr_dir = os.path.dirname(__file__)
edges_fil = curr_dir + '/' + 'lotostg.txt'

g = nx.DiGraph()
file = open(edges_fil)

#Add edges to graph
num_lines = 0
edges = []
for line in file.readlines():
    node1, node2, weight = line.split(",")
    weight = float(weight)
    edges.append((node1,node2,weight))
    num_lines += 1
g.add_weighted_edges_from(edges) #actually adds the edges to the graph

print('Nodes: ')
print(g.nodes)
print('Total Nodes: ', len(g.nodes))

#NO CHATGPT WAS USED FOR THIS :)



