"""Frame contains Graph to visualize the algorithm"""
from typing import TYPE_CHECKING

from ttkbootstrap import *

from ..utils import CHECK_IMPORT_LATER
from .edge import Edge
from .node import Node

if TYPE_CHECKING:
    from .window import Window

if CHECK_IMPORT_LATER:
    from tkinter import *


class FrameGraph(Frame):
    """The FrameGraph Class inherits from tb.Frame"""

    def __init__(self, parent: 'Window'):
        """The Initialization of FrameGraph Class

        Args:
            parent (Window): The parent(window) of this FrameGraph
        """
        super().__init__(parent)
        self.pack(fill='both', expand=True)
        self.configure(bg="white")

        self.nodes_list: list[Node] = []
        self.edges_list: list[Edge] = []

    def create_node(self, k: int, x: float, y: float) -> None:
        """Create a node

        Args:
            k (int): Number name of the node
            x (float): x-co of this node
            y (float): y-co of this node
        """
        new_node: Node = Node(self, k, x, y)
        self.nodes_list.append(new_node)

    def create_nodes(self, n: int, coordinate_list: list[list[float]]) -> None:
        """Create n nodes with a minimum distance of 100 units between them

        Args:
            n (int): Number of nodes
        """
        for i in range(n):
            self.create_node(i, coordinate_list[i][0], coordinate_list[i][1])

    def create_edge(self, first_node_number: int, second_node_number: int, coordinate_list: list[list[float]]) -> None:
        """Create a edge

        Args:
            first_node_number (int): first node number in connection
            second_node_number (int): second node number in connection
            coordinate_list (list[list[float]]): List contains coordinate(x,y)
        """
        new_edge: Edge = Edge(self, first_node_number,
                              second_node_number, coordinate_list)
        self.edges_list.append(new_edge)

    def create_edges(self, connections_list: list[list[int]], coordinate_list: list[list[float]]) -> None:
        """Create edges

        Args:
            connections_list (list[list[int]]): List contains connection of two node(a,b)
            coordinate_list (list[list[float]]): List contains coordinate(x,y)
        """
        done: list[list[int]] = []
        for connection in connections_list:
            first_node_number, second_node_number = connection
            if [first_node_number, second_node_number] in done | [second_node_number, first_node_number] in done:
                continue
            self.create_edge(first_node_number,
                             second_node_number, coordinate_list)
