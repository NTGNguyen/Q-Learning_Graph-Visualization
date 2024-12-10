"""Frame contains Graph to visualize the algorithm"""
import ttkbootstrap as tb
from typing import TYPE_CHECKING
from node import Node
from ttkbootstrap import *
from tkinter import *

if TYPE_CHECKING:
    from window import Window

class FrameGraph(Frame):
    """The FrameGraph Class inherits from tb.Frame"""
    def __init__(self,parent:'Window'):
        """The Initialization of FrameGraph Class

        Args:
            parent (Window): The parent(window) of this FrameGraph
        """
        super().__init__(parent)
        self.configure(bg="white") 
        self.pack(fill='both', expand=True)
        self.nodes_list:list[Node] = []

    def create_node(self):
        new_node:Node = Node(self,1)
        self.nodes_list.append(new_node)

    

