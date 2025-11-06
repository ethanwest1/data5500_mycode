'''
This Python progam takes the edges in a graph from a file, 
generates the graph,
saves the graph visualization to a file, 
and traverses the paths in the graph and calculates the path weights
'''

import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations


import os

# Run this install commands the first time, then comment out these lines (or delete them)
# Note: these commands could also be run in a terminal.  Running them here, so the entire program below works
# os.system("sudo pip3 install networkx")
# os.system("sudo apt-get install python3-matplotlib")

import matplotlib
matplotlib.use('Agg') # putting matplolib into server-only mode, no GUI

import matplotlib.pyplot as plt
import networkx as nx
from networkx.classes.function import path_weight



############################################################
# Loading edges of the Graph from a file: example_graph.png
curr_dir = os.path.dirname(__file__) # get the current directory of this file

edges_fil = curr_dir + "/" + "lotostg.txt" # dirname and __file__ (this file) returns the current folder
graph_visual_fil = curr_dir + "/" + "graph_visual.png"

file = open(edges_fil) 

g = nx.DiGraph() # created directed graph



############################################################
# STEP 1 - Create Graph
# get all edges from the txt file
# edges = []

# for line in file.readlines():
#     node1, node2, weight = line.split(",")
#     weight = int(weight)
#     edges.append((node1, node2, weight)) # add edge to a list of tuples
    
# print(edges)
# g.add_weighted_edges_from(edges) 

# example of adding the edges to a graph one at a time
# code above adds all the edges to the graph at once
# for e in edges:
#     g.add_edge(e[0], e[1], weight=e[2])

# print all nodes
print(g.nodes)

#Saving graph as an image, for review
pos=nx.circular_layout(g) # pos = nx.nx_agraph.graphviz_layout(G)
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig(graph_visual_fil)



###########################################################
# STEP 2 - Traverse Graph 
# for each node pair, find paths between them
# calculate the path weight, 
# for n1, n2 in permutations(g.nodes,2): #permutations returns all pairs
#     print("all existing paths from", n1, "to", n2, ":")
    
#     # all_simple_paths function below returns each path as a list
#     # the graph can be accessed with the nodes as keys, like a dictionary
#     # g['v0']['v1']['weight'] returns 2, the weight of that edge
#     # iterating through the edges in a path, you can calculate the weight of the entire path
    
#     for path in nx.all_simple_paths(g, source=n1, target=n2):
#         print(path) # print each path
#         path_weight = 0
        
#         # iterating through each edge in the path and adding edge weight to total path weight
#         for i in range(len(path) - 1):
#             path_weight += g[path[i]][path[i+1]]['weight']
#         print("path_weight: ", path_weight)
        


#############STEPS ABOVE BUT BY ETHAN ################
#Step 1
g = nx.DiGraph()

edges = []
for line in file.readlines():
    line = line.strip()
    node1, node2, time =line.split(",")
    time = float(time)
    edges.append((node1, node2, time))
print(edges)
g.add_weighted_edges_from(edges) #adds the edges to the graphs

# STEP 2 - Traverse Graph  
for n1, n2 in permutations(g.nodes,2): #permutations returns all pairs
    print("all existing paths from", n1, "to", n2, ":")
    
    # all_simple_paths function below returns each path as a list
    # the graph can be accessed with the nodes as keys, like a dictionary
    # g['v0']['v1']['weight'] returns 2, the weight of that edge
    # iterating through the edges in a path, you can calculate the weight of the entire path
    
    for path in nx.all_simple_paths(g, source=n1, target=n2):
        print(path) # print each path
        path_weight = 0

        # iterating through each edge in the path and adding edge weight to total path weight
        for i in range(len(path) - 1):
            path_weight += g[path[i]][path[i+1]]['weight']

        print("path_weight: ", path_weight)
            
#Shortest path logic
shortest_path = nx.shortest_path(g,'lg','sg', weight='weight')
shortest_path_weight = nx.shortest_path_length(g, 'lg', 'sg', weight= 'weight')
print()
print('Shortest path: ', shortest_path)
print('Shortest path weight: ',shortest_path_weight)

        