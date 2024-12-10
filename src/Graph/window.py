"""The Window shows Application"""
from tkinter import *

import ttkbootstrap as tb
from frame_graph import FrameGraph
from ttkbootstrap import *


class CWindow(Window):
    """The window class inherits from tb.Window"""

    def __init__(self):
        """Initialization of The window class"""
        super().__init__(themename="solar")
        self.geometry('1800x1200')
        self.title("Q-Learning Visualization")
        self.frame: FrameGraph = FrameGraph(self)
        self.frame.place(relwidth=0.7, relheight=1.0)
