"""A Node class to config the node in Graph"""
from tkinter import *
from typing import TYPE_CHECKING

import ttkbootstrap as tb
from ttkbootstrap import *

if TYPE_CHECKING:
    from frame_graph import FrameGraph


class Node(Canvas):
    """The Node class inherits from Canvas"""

    def __init__(self, parent: 'FrameGraph', number: int):
        """The initialization of Node Class

        Args:
            parent (FrameGraph): Parent for this Node
            number (int): The number(name) of this node
        """
        super().__init__(parent, width=60, height=60, bg="white", highlightthickness=0)
        self.number = number
        self.configure(bg="white")
        self.create_oval(10, 10, 50, 50, fill="blue", outline="#F8F9FA")
        self.create_text(30, 30, text=str(number), font=("Arial", 20, "bold"))
        self.pack()
