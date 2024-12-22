"""A label to show epoch in current time"""

from tkinter import LEFT, ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .frame import ButtonFrame


class EpochLabel(ttk.Label):
    """The EpochLabel inherits from ttk.Label"""

    def __init__(self, parent: "ButtonFrame"):
        """The Initialization of this class

        Args:
            parent (ButtonFrame): The parent of this class
        """
        super().__init__(parent, text="Epoch:0/50000")
        self.pack(side=LEFT, padx=5, pady=5)

    def update_epoch(self, new_epoch: int) -> None:
        """Update new epoch

        Args:
            new_epoch (int): new epoch
        """
        self.configure(text=f"Epoch:{new_epoch}/5000")
