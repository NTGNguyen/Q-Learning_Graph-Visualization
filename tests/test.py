
from ..src import CWindow, coordinate_random

new_window = CWindow()
x1, y1 = coordinate_random(
    new_window.frame.winfo_width, new_window.frame.winfo_height)
x2, y2 = coordinate_random(0.7*1800, 1200)
new_window.frame.create_node(1)
new_window.frame.create_node(2)

new_window.mainloop()
