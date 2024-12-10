"""Some useful function regarding coordinate"""
import math
import random as rd


def coordinate_random(max_width_frame: int, max_height_frame: int) -> tuple[float, float]:
    """The random function to random coordinate of point(x,y)

    Args:
        max_width_frame (int): max width of frame
        max_height_frame (int): max height of frame

    Returns:
        tuple(float,float): The (x,y) coordinate
    """
    x: float = rd.uniform(0, max_width_frame)
    y: float = rd.uniform(0, max_height_frame)
    return x, y


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Caculate distance between two nodes

    Args:
        x1 (float): x1
        y1 (float): y1
        x2 (float): x2
        y2 (float): y2

    Returns:
        float: distance of two nodes
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def coordinate_list_random(k: int, max_width: float, max_height: float, min_distance: float = 100) -> list[list[float]]:
    """Random the coordinate of k nodes

    Args:
        k (int): number of nodes
        max_width (float): Max of x
        max_height (float): Max of y
        min_distance (float, optional): Min distance between each two nodes. Defaults to 100.

    Returns:
        list[list[float]]: The list contains coordinate of k nodes
    """
    coordinate_list = []
    for _ in range(k):
        while True:
            x, y = coordinate_random(max_width, max_height)
            if all(distance(x, y, cx, cy) >= min_distance for cx, cy in coordinate_list):
                coordinate_list.append([x, y])
                break
    return coordinate_list
