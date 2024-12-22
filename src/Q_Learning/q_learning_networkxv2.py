import random
from typing import TYPE_CHECKING

import networkx as nx
import numpy as np
from numpy import matrix

from src.Q_Learning.q_learning_networkx import QLearningNX

if TYPE_CHECKING:
    from ..Graph import MainWindow


class QLearningNXv2:
    """The QLearning version 2 with networkx"""

    def __init__(self, Window: 'MainWindow', G: nx.Graph, target_node_number: int):
        """The Inittialization of QLearningNXv2 class

        Args:
            Window (MainWindow): The main window
            G (nx.Graph): Graph
            target_node_number (int): The number of target node(final node to reach)
        """
        self.window = Window
        self.G = G
        self.target_node_number: int = target_node_number
        self.R: matrix = np.matrix(
            np.zeros(shape=(self.G.number_of_nodes(), self.G.number_of_nodes())))
        for x in self.G[target_node_number]:
            self.R[x, target_node_number] = 100
        self.Q: matrix = np.matrix(
            np.zeros(shape=(self.G.number_of_nodes(), self.G.number_of_nodes())))
        self.Q -= 100
        for node in self.G.nodes:
            for x in G[node]:
                self.Q[node, x] = 0
                self.Q[x, node] = 0
        self.epoch = 0

    def next_number(self, start_node_number: int, threshold: float) -> int:
        """Find next node number

        Args:
            start_node_number (int): From this node to next node
            threshold (float): The threshold

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
            node1 (int): first node number
            node2 (int): second node number 
            lr (float): learning rate
            discount (float): discount
        """
        max_index = np.where(self.Q[node2,] == np.max(self.Q[node2]))[1]
        if max_index.shape[0] > 1:
            max_index: int = int(np.random.choice(max_index, 1))
        else:
            max_index: int = int(max_index)
        max_value = self.Q[node2, max_index]
        self.Q[node1, node2] = int(
            (1-lr)*self.Q[node1, node2] + lr*(self.R[node1, node2] + discount * max_value))

    def run_epoch(self, threshold: float, lr: float, discount: float, target_node_number: int) -> None:
        """Action in each epoch until the target node in reached

        Args:
            threshold (float): threshold for exploration vs. exploitation
            lr (float): _description_
            discount (float): _description_
        """
        if self.epoch < 50000:
            self.epoch += 1
            self.window.epoch_label.update_epoch(self.epoch)

            start_node: int = np.random.randint(0, self.G.number_of_nodes())
            current_node = start_node
            while current_node != target_node_number:
                next_node = self.next_number(current_node, threshold)
                self.update_Q(current_node, next_node, lr, discount)
                current_node = next_node
            self.window.after(100, self.run_epoch, threshold,
                              lr, discount, target_node_number)

    def learn(self, threshold: float, lr: float, discount: float) -> None:
        """Learn algorithm

        Args:
            threshold (float): The threshold 
            lr (float): learning rate
            discount (float): Discount factor
        """
        self.epoch = 0
        self.run_epoch(threshold, lr, discount, self.target_node_number)
