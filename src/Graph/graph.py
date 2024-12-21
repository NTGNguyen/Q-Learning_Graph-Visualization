"""The Graph"""
import random
from typing import Any

import matplotlib.pyplot as plt
import networkx as nx
from networkx import Graph


class GraphRandomGenerate:
    """The Graph class contains their elements"""

    def __init__(self, default_node_color: str = 'skyblue', default_edge_color: str = 'black'):
        """The Initialization of this class

        Args:
            default_node_color (str, optional): color of all the nodes in the first. Defaults to 'skyblue'.
            default_edge_color (str, optional): color of all the edges in the first. Defaults to 'black'.
        """
        self.num_nodes: int = random.randint(10, 15)
        self.G: Graph = nx.gnp_random_graph(self.num_nodes, 0.4)
        self.pos = nx.spring_layout(self.G)
        self.node_colors: list[str] = [
            default_node_color for _ in range(len(self.G.nodes))]
        self.edge_colors: list[str] = [
            default_edge_color for _ in range(len(self.G.edges))]
        self.node_collection: plt.Collection
        self.edge_collection: plt.Collection
        self.canvas: Any

    def change_node_color(self, node_number: int) -> None:
        """Change node color with specific number of node

        Args:
            node_number (int): The node number
        """
        if not self.G:
            return
        node_id = list(self.G.nodes)[node_number]
        self.node_colors[node_number] = "red"
        self.node_collection.set_facecolor(self.node_colors)
        self.canvas.draw_idle()

    def change_edge_color(self, first_node_number: int, second_node_number: int) -> None:
        """Change edge color with specific number of two nodes in connection

        Args:
            first_node_number (int): number of first node in connection
            second_node_number (int): number of second node in connection
        """
        edge_index = list(self.G.edges).index((first_node_number, second_node_number)if (
            first_node_number, second_node_number) in self.G.edges else (second_node_number, first_node_number))
        self.edge_colors[edge_index] = "red"
        self.edge_collection.set_edgecolor(self.edge_colors)
        self.canvas.draw_idle()
