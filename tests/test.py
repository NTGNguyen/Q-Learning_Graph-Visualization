import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import random

# Global variables to store the graph, layout, and plot elements
G = None
pos = None
node_colors = []
edge_colors = []
canvas = None
ax = None
node_collection = None
edge_collection = None


def draw_random_graph():
    global G, pos, node_colors, edge_colors, canvas, ax, node_collection, edge_collection

    # Clear existing graph
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # Create a random graph
    num_nodes = random.randint(5, 10)
    # Random graph with edge probability 0.4
    G = nx.gnp_random_graph(num_nodes, 0.4)
    pos = nx.spring_layout(G)  # Layout for graph nodes
    # Default color for all nodes
    node_colors = ['skyblue' for _ in range(len(G.nodes))]
    # Default color for all edges
    edge_colors = ['black' for _ in range(len(G.edges))]

    # Create the Matplotlib figure and axis
    fig, ax = plt.subplots(figsize=(5, 4))
    nx.draw(
        G, pos, ax=ax, with_labels=True,
        node_color=node_colors, edge_color=edge_colors,
        node_size=500, font_size=10
    )

    # Extract node and edge collections for updating
    node_collection = ax.collections[0]
    edge_collection = ax.collections[1]

    # Set the title
    ax.set_title("Random Graph", fontsize=12)

    # Embed the Matplotlib figure into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    canvas.draw()


def change_random_node_color():
    global node_colors, node_collection, canvas

    # Ensure the graph exists
    if not G:
        return

    # Select a random node
    random_node = random.choice(list(G.nodes))
    # Change the color of the selected node
    node_colors[random_node] = random_color()

    # Update node colors in the collection
    node_collection.set_facecolor(node_colors)
    canvas.draw_idle()  # Redraw the canvas more efficiently


def change_random_edge_color():
    global edge_colors, edge_collection, canvas

    # Ensure the graph exists
    if not G:
        return

    # Select a random edge
    random_edge_index = random.randint(0, len(G.edges) - 1)
    # Change the color of the selected edge
    edge_colors[random_edge_index] = random_color()

    # Update edge colors in the collection
    edge_collection.set_edgecolor(edge_colors)
    canvas.draw_idle()  # Redraw the canvas more efficiently


def random_color():
    """Generate a random color."""
    return f'#{random.randint(0, 0xFFFFFF):06x}'


# Create the main Tkinter window
root = tk.Tk()
root.title("Interactive Node-Edge Graph")

# Create a ttk Frame for the graph
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# Add ttk Buttons to interact with the graph
button_frame = ttk.Frame(main_frame)
button_frame.pack(fill=tk.X)

draw_button = ttk.Button(
    button_frame, text="Draw Random Graph", command=draw_random_graph)
draw_button.pack(side=tk.LEFT, padx=5, pady=5)

node_button = ttk.Button(
    button_frame, text="Change Node Color", command=change_random_node_color)
node_button.pack(side=tk.LEFT, padx=5, pady=5)

edge_button = ttk.Button(
    button_frame, text="Change Edge Color", command=change_random_edge_color)
edge_button.pack(side=tk.LEFT, padx=5, pady=5)

# Frame for displaying the graph
graph_frame = ttk.Frame(main_frame, borderwidth=2, relief="solid")
graph_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
