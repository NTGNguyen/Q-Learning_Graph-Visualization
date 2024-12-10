"""A Edge class to config the Edge in Graph"""
from tkinter import *
from typing import TYPE_CHECKING

from ttkbootstrap import *

if TYPE_CHECKING:
    from frame_graph import FrameGraph
    from node import Node


class Edge(Canvas):
    """The Edge class inherit from Canvas"""

    def __init__(self, parent: 'FrameGraph', first_node_number: int, second_node_number: int, coordinate_list: list[list[float]]):
        """The Initialization of Edge class

        Args:
            parent (FrameGraph): The parent(Frame) of this Edge
            first_node (Node): The first node of the connection
            second_node (Node): The second node of the connection
        """
        super().__init__(parent, highlightthickness=0)
        self.first_node_number: int = first_node_number
        self.second_node_number: int = second_node_number
        x1, y1 = coordinate_list[first_node_number]
        x2, y2 = coordinate_list[second_node_number]
        print(x1, y1, x2, y2)
        min_width = 1
        min_height = 1
        self.configure(
            width=max(abs(x1 - x2), min_width),
            height=max(abs(y1 - y2), min_height),
            bg="white",
            highlightthickness=0
        )
        self.pack()
        self.place(x=min(x1, x2), y=min(y1, y2))
        line_x1, line_y1 = x1 - min(x1, x2), y1 - min(y1, y2)
        line_x2, line_y2 = x2 - min(x1, x2), y2 - min(y1, y2)
        self.create_line(line_x1, line_y1, line_x2,
                         line_y2, fill="black", width=2)
