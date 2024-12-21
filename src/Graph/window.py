"""The main window"""

import tkinter as tk
from ..utils import HEIGHT_WINDOW, WIDTH_WINDOW
from .frame import MainFrame, GraphFrame, ButtonFrame
from .button import DrawRandomButton


class MainWindow(tk.Tk):
    """MainWindow class inherits from tk.Tk"""

    def __init__(self, title: str):
        """The initialization of MainWindow class"""
        super().__init__()
        self.title(title)
        self.geometry(newGeometry=f"{WIDTH_WINDOW}x{HEIGHT_WINDOW}")
        self.minsize(WIDTH_WINDOW, HEIGHT_WINDOW)
        self.maxsize(WIDTH_WINDOW, HEIGHT_WINDOW)
        self.resizable(width=False, height=False)
        self.main_frame: MainFrame = MainFrame(self)
        self.graph_frame: GraphFrame = GraphFrame(self.main_frame)
        self.button_frame: ButtonFrame = ButtonFrame(self.main_frame)
        self.draw_random_button: DrawRandomButton = DrawRandomButton(
            self.button_frame, self.graph_frame)
