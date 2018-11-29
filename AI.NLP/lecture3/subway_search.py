

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

def build_graph(lines):
    for line in lines:
        i = 0
        while i < len(line) - 1:
            G.add_edge(line[i],line[i+1])