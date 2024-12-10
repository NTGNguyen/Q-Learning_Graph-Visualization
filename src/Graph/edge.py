from tkinter import *
from typing import TYPE_CHECKING

from ttkbootstrap import *

if TYPE_CHECKING:
    from frame_graph import FrameGraph
    from node import Node


class Edge(Canvas):
    def __init__(self, parent: FrameGraph, start_node: Node, end_node: Node):
        super().__init__(parent)
        self.configure(bg="black")
        self.create_line()
        self.get
