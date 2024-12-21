"""Some Frames"""
from tkinter import BOTH, X, ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .window import MainWindow


class MainFrame(ttk.Frame):
    """The MainFrame Class inherits from ttk.Frame"""

    def __init__(self, parent: 'MainWindow'):
        """The initialization of MainFrame

        Args:
            parent (MainWindow): the master's window of this frame
            padding (str, optional): padding of this frame. Defaults to "10".
        """
        super().__init__(parent, padding="10")
        self.pack(fill=BOTH, expand=True)


class GraphFrame(ttk.Frame):
    """The GraphFrame Class inherit from ttk.Frame"""

    def __init__(self, parent: MainFrame):
        """The initialization of GraphFrame

        Args:
            parent (MainWindow): The master's frame of this frame
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        self.pack(fill=BOTH, expand=True)


class ButtonFrame(ttk.Frame):
    """The Frame contains buttons"""

    def __init__(self, parent: MainFrame):
        """The initialization of ButtonFrame

        Args:
            parent (MainFrame) : The master of button frame
        """
        super().__init__(parent)
        self.pack(fill=X)
