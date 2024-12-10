"""A Node class to config the node in Graph"""
from ttkbootstrap import *
from tkinter import *
from typing import TYPE_CHECKING



if TYPE_CHECKING:
    from .frame_graph import FrameGraph


class Node(Canvas):
    """The Node class inherits from Canvas"""

    def __init__(self, parent: 'FrameGraph', number: int,x:float ,y:float):
        """The initialization of Node Class

        Args:
            parent (FrameGraph): Parent for this Node
            number (int): The number(name) of this node
            x (int): The x-co of the center of this node
            y (int): The y-co of the center of this node
        """
        super().__init__(parent, width=60, height=60, bg="white", highlightthickness=0)
        self.x = x
        self.y = y
        self.number = number
        self.configure(bg="white")
        self.create_oval(0,0,60,60, fill="blue", outline="#F8F9FA")
        self.create_text(30, 30, text=str(number), font=("Arial", 20, "bold"))
        self.pack()
        self.place(x = x - 30,y = y - 30)
        
        
        

    def get_center(self)-> tuple[float,float]:
        """Get center of Node

        Returns:
            tuple[float,float]: x_center_pos and y_center_pos
        """
        return self.x,self.y
    
    
