"""The Graph"""
import random

import networkx as nx
from networkx import Graph


class GraphRandomGenerate:
    """The Graph class contains their elements"""

    def __init__(self, default_node_color: str = 'skyblue', default_edge_color: str = 'black'):
        """The initialization of GraphX class
        """
        self.num_nodes: int = random.randint(10, 15)
        self.G: Graph = nx.gnp_random_graph(self.num_nodes, 0.4)
        self.pos = nx.spring_layout(self.G)
        self.node_colors: list[str] = [
            default_node_color for _ in range(len(self.G.nodes))]
        self.edge_colors: list[str] = [
            default_edge_color for _ in range(len(self.G.edges))]
