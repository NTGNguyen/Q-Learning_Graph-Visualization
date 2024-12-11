import pandas as pd

from src import (CWindow, GraphNetworkX, GraphNetworkXForQLearning,
                 coordinate_list_random)


def main():
    new_window = CWindow()
    coordinate_list = coordinate_list_random(10, 0.7*0.8*1800, 0.8*900)
    new_window.frame.create_edge(1, 2, coordinate_list)
    new_window.frame.create_nodes(10, coordinate_list)
    new_window.mainloop()
    # new_graph = GraphNetworkX()
    # graph = GraphNetworkXForQLearning(new_graph,10,9)
    # print(pd.DataFrame(graph.R))
    # print(pd.DataFrame(graph.Q))


if __name__ == "__main__":
    main()
