"""Q-Learning with networkx"""
from typing import TYPE_CHECKING
import networkx as nx
import numpy as np
import random
from numpy import matrix
import time
if TYPE_CHECKING:
    from ..Graph import MainWindow


class QLearningNX:
    """The QLearning with networkx"""

    def __init__(self, Window: 'MainWindow', G: nx.Graph, target_node_number: int):
        """The Initialization of QLearningNX class

        Args:
            Window (MainWindow): The main window
            G (nx.Graph): Graph
            target_node_number (int): target node(final node)
        """
        self.window: 'MainWindow' = Window
        self.G = G
        self.R: matrix = np.matrix(np.zeros(
            shape=(self.G.number_of_nodes(), self.G.number_of_nodes())))
        for x in self.G[target_node_number]:
            self.R[x, 10] = 100
        self.Q: matrix = np.matrix(np.zeros(
            shape=(self.G.number_of_nodes(), self.G.number_of_nodes())))
        self.Q -= 100
        for node in self.G.nodes:
            for x in G[node]:
                self.Q[node, x] = 0
                self.Q[x, node] = 0

    def next_number(self, start_node_number: int, threshold: float) -> int:
        """Find next node number step

        Args:
            start_node_number (int): From this node to next node
            threshold (float): The threshole

        Returns:
            int: the next node number
        """
        random_value: float = random.uniform(0, 1)
        if random_value < threshold:
            sample = list(self.G.neighbors(start_node_number))
        else:
            sample = np.where(self.Q[start_node_number,] == np.max(
                self.Q[start_node_number,]))[0]
        next_node: int = int(np.random.choice(sample, 1))
        return next_node

    def update_Q(self, node1: int, node2: int, lr: float, discount: float) -> None:
        """Update Q table

        Args:
            node1 (int): first node
            node2 (int): second node
            lr (float): learning rate
            discount (float): discount
        """
        max_index = np.where(self.Q[node2,] == np.max(self.Q[node2]))[1]
        if max_index.shape[0] > 1:
            max_index: int = int(np.random.choice(max_index, size=1))
        else:
            max_index: int = int(max_index)
        max_value = self.Q[node2, max_index]
        self.Q[node1, node2] = int(
            (1-lr)*self.Q[node1, node2] + lr*(self.R[node1, node2]+discount*max_value))

    def run_epoch(self, threshold: float, lr: float, discount: float) -> None:
        """Action in each epoch

        Args:
            threshold (float): threshold
            lr (float): learning rate
            discount (float): discount
        """
        if self.epoch < 50000:
            self.epoch += 1
            self.window.epoch_label.update_epoch(self.epoch)
            start_node: int = np.random.randint(0, self.G.number_of_nodes())
            next_node = self.next_number(start_node, threshold)
            self.update_Q(start_node, next_node, lr, discount)
            self.window.after(100, self.run_epoch, threshold, lr, discount)

    def learn(self, threshold: float, lr: float, discount: float) -> None:
        """Learn algorithm

        Args:
            threshold (float): The threshold
            lr (float): learning rate
            discount (float): discount
        """
        self.epoch = 0
        self.run_epoch(threshold, lr, discount)
