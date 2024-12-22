"""Some buttons"""
from tkinter import BOTH, LEFT, ttk
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from .graph import GraphRandomGenerate
from ..Q_Learning import QLearningNX

if TYPE_CHECKING:
    from .frame import ButtonFrame, GraphFrame
    from .window import MainWindow


class DrawRandomButton(ttk.Button):
    """The Button inherits from ttk.Button"""

    def __init__(self, parent: 'ButtonFrame', graph_frame: 'GraphFrame', window: 'MainWindow'):
        """The button to draw graph

        Args:
            parent (ButtonFrame): The Frame contains the Button
            graph_frame (GraphFrame): The Frame contains the graph
        """
        super().__init__(parent, text="Draw Random Graph", command=self.draw_random_graph)
        self.pack(side=LEFT, padx=5, pady=5)
        self.graph_frame: GraphFrame = graph_frame
        self.window = window

    def draw_random_graph(self):
        """Function to draw random graph
        """
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        self.Gr = GraphRandomGenerate()
        self.q_learning = QLearningNX(self.window, self.Gr.G, 9)
        fig, ax = plt.subplots(figsize=(5, 4))
        nx.draw(self.Gr.G, self.Gr.pos, ax=ax, with_labels=True, node_color=self.Gr.node_colors,
                edge_color=self.Gr.edge_colors, node_size=500, font_size=10)
        self.node_collection: plt.Collection = ax.collections[0]
        self.edge_collection: plt.Collection = ax.collections[1]
        self.Gr.node_collection = ax.collections[0]
        self.Gr.edge_collection = ax.collections[1]
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.Gr.canvas = self.canvas
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=BOTH, expand=True)
        self.canvas.draw()


class LearnButton(ttk.Button):
    """The button inherits from ttk.Button"""

    def __init__(self, parent: 'ButtonFrame', random_button: DrawRandomButton):
        """The Initialization of class

        Args:
            parent (ButtonFrame): The Button frame
            graph_q_le (QLearningNX): The algorithm
        """
        super().__init__(parent, text="Start learn",
                         command=self.blearn)
        self.random_button = random_button
        self.pack(side=LEFT, padx=5, pady=5)

    def blearn(self):
        self.random_button.q_learning.learn(0.5, 0.8, 0.8)
