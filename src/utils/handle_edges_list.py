def handle_edges_list(edges_list: list[list[int]], number_of_nodes: int) -> dict[int, list[int]]:
    edges_dict: dict[int, list[int]] = {}
    for i in range(number_of_nodes):
        edges_dict[i] = []
        for edge in edges_list:
            if i == edge[0] and edge[1] not in edges_dict[i]:
                edges_dict[i].append(edge[1])
            if i == edge[1] and edge[0] not in edges_dict[i]:
                edges_dict[i].append(edge[0])
    return edges_dict
