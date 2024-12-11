"""Draw Graph with networkx and Find the shortest path behind the scene"""
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy import matrix

from ..utils import DEFAULT_EDGES_NETWORKX


class GraphNetworkX:
    """A class using to draw Graph with NetWorkX"""

    def __init__(self, edges: list[tuple[int, int]] = DEFAULT_EDGES_NETWORKX):
        """The Initialization of GraphNetworkX class

        Args:
            edges (list[tuple[int, int]], optional): List contains connections between two node. Defaults to DEFAULT_EDGES_NETWORKX.
        """
        self.edges = edges
        self.G = nx.Graph()
        self.G.add_edges_from(self.edges)
        self.pos = nx.spring_layout(self.G)

    def draw_graph(self):
        """Function to draw graph
        """
        nx.draw_networkx_nodes(self.G, self.pos)
        nx.draw_networkx_edges(self.G, self.pos)
        nx.draw_networkx_labels(self.G, self.pos)
        plt.show()


class GraphNetworkXForQLearning:
    """A Class using to run Q-Learning Algorithm in the graph behind the scene"""

    def __init__(self, G: GraphNetworkX, number_nodes: int, end_node_number: int):
        """The Initialization of GraphNetworkXForQLearning Class

        Args:
            G (GraphNetworkX): The Graph which this algorithm run on
            number_nodes (int): number of node in graph
            end_node_number (int): The target node
        """
        self.G = G
        self.number_nodes = number_nodes
        self.R: matrix = matrix(np.zeros(shape=(number_nodes, number_nodes)))
        for x in self.G.G[end_node_number]:
            self.R[x, end_node_number] = 100
        self.Q: matrix = matrix(np.zeros(shape=(number_nodes, number_nodes)))
        self.Q -= 100
        for node in self.G.G.nodes:
            for x in self.G.G[node]:
                self.Q[node, x] = 0
                self.Q[x, node] = 0

    def next_number(self, start_node: int, threshold: float) -> int:
        """Find next node to forward

        Args:
            start_node (int): From this node to
            threshold (float): Threshold for considering of two options

        Returns:
            int: number of next node
        """
        random_value = np.random.uniform(0, 1)
        if random_value < threshold:
            sample = self.G.G[start_node]
        else:
            sample = np.where(self.Q[start_node,] ==
                              np.max(self.Q[start_node,]))[1]
        next_node: int = int(np.random.choice(sample, 1))
        return next_node

    def updateQ(self, start_node: int, next_node: int, learning_rate: float, discount: float) -> None:
        """Update Q-table of in each step

        Args:
            start_node (int): From this node to
            next_node (int): Next node espected to forwar
            learning_rate (float): learning rate of learning
            discount (float): discount of learning
        """
        max_index = np.where(self.Q[next_node,] ==
                             np.max(self.Q[next_node,]))[1]
        if max_index.shape[0] > 1:
            max_index = int(np.random.choice(max_index, size=1))
        else:
            max_index = int(max_index)
        max_value: int = self.Q[next_node, max_index]
        self.Q[start_node, next_node] = int(
            (1 - learning_rate)*self.Q[start_node, next_node]+learning_rate*(self.R[start_node, next_node] + discount * max_value))

    def learn(self, threshold: float, learning_rate: float, discount: float) -> None:
        """Learning process

        Args:
            threshold (float): Threshold for considering of two options
            learning_rate (float): learning rate of learning
            discount (float): discount of learning
        """
        for _ in range(50000):
            start: int = np.random.randint(0, 11)
            next_node: int = self.next_number(start, threshold)
            self.updateQ(start, next_node, learning_rate, discount)

    def shortest_path(self, start_node: int, end_node: int) -> list[int]:
        """Find shortest_path after trainning

        Args:
            start_node (int): start from
            end_node (int): target node

        Returns:
            list[int]: list contains each node illustating to shortest path
        """
        path: list[int] = [start_node]
        next_node = np.argmax(self.Q[start_node,])
        path.append(next_node)
        while next_node != end_node:
            next_node = np.argmax(self.Q[next_node,])
            path.append(next_node)
        return path
