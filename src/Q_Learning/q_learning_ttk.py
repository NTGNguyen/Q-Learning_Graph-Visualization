"""Visualize Q-learning process"""
import numpy as np
from numpy import matrix, zeros

from ..Graph import CWindow


class QLearningTTK:
    def __init__(self, environment: CWindow, number_of_nodes: int, edges_list: list[list[int]], edges_list_after_handle: dict[int, list[int]], end_node: int):
        self.environment = environment
        self.number_of_nodes = number_of_nodes
        self.edges_list = edges_list
        self.Q_Table = matrix(
            np.zeros(shape=(number_of_nodes, number_of_nodes)))
        self.Q_Table -= 100
        self.edges_list_after_handle = edges_list_after_handle
        for i in range(number_of_nodes):
            for edge in edges_list_after_handle[i]:
                self.Q_Table[edge, i] = 0
                self.Q_Table[i, edge] = 0
        self.R_Table = matrix(
            np.zeros(shape=(number_of_nodes, number_of_nodes)))
        for x in edges_list_after_handle[end_node]:
            self.R_table[x, end_node] = 100

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
            sample = self.edges_list_after_handle[start_node]
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
