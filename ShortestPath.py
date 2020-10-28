import pandas as pd
import networkx as nx
import numpy as np
from networkx.readwrite import json_graph
import json

#with open('data1.json') as json_file:
#    data = json.load(json_file)

#G = json_graph.node_link_graph(data)

edges = pd.read_csv('edges.csv')
nodes = pd.read_csv('nodes.csv')

G = nx.DiGraph()
for i in nodes['osmid']:
    G.add_node(i)
for i in range(len(edges)):
    G.add_edge(edges.iloc[i]['u'], edges.iloc[i]['v'], weight = edges.iloc[i]['length'])

def get_all_shortest_paths(node_id):
    return nx.single_source_dijkstra(G, id)

def get_shortest_path_to(start, end):
    path = nx.dijkstra_path(G, start, end, 'weight')
    cost = 0
    for i in range(len(path) - 1):
        cost += G[path[i]][path[i+1]]['weight']
    return (path, cost)
