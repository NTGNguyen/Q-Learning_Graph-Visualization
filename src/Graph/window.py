"""The Window shows Application"""
from ttkbootstrap import *
from tkinter import *


from .frame_graph import FrameGraph

from ..utils import WIDTH_WINDOW, HEIGHT_WINDOW


class CWindow(Window):
    """The window class inherits from tb.Window"""

    def __init__(self):
        """Initialization of The window class"""
        super().__init__(themename="solar")
        self.geometry(f'{WIDTH_WINDOW}x{HEIGHT_WINDOW}')
        self.title("Q-Learning Visualization")
        self.frame: FrameGraph = FrameGraph(self)
        self.frame.place(relwidth=0.7, relheight=1.0)
