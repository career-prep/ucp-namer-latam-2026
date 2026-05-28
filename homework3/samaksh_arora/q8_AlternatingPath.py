# Alternating Path
# Data Structure: Graph
# Algorithm: BFS (BFS guarantees shortest path in unweighted graphs)
# Time Complexity: O(N + E) where N is the number of nodes and E is the number of edges
# Space Complexity: O(N + E) where N is the number of nodes and E is the number of edges

from collections import deque

def AlternatingPath(list_of_edges, origin_node, target_node):
    if not list_of_edges:
        return -1
    
    node_to_colorNeighbors_map = {}

    for source_node, destination, edge_color in list_of_edges:
        if source_node not in node_to_colorNeighbors_map:
            node_to_colorNeighbors_map[source_node] = set()
        if destination not in node_to_colorNeighbors_map:
            node_to_colorNeighbors_map[destination] = set()

        node_to_colorNeighbors_map[source_node].add((destination, edge_color))

    bfs_queue = deque()
    bfs_queue.append((origin_node, "blue", 0))
    bfs_queue.append((origin_node, "red", 0))

    set_of_visited_node_color_pairs = set()
    set_of_visited_node_color_pairs.add((origin_node, "blue"))
    set_of_visited_node_color_pairs.add((origin_node, "red"))

    while bfs_queue:
        current_node, last_edge_color, current_path_length = bfs_queue.popleft()
        if current_node == target_node:
            return current_path_length
        
        if current_node not in node_to_colorNeighbors_map:
            continue

        for neighboring_node, edge_color in node_to_colorNeighbors_map[current_node]:
            if edge_color == last_edge_color:
                continue

            if (neighboring_node, edge_color) not in set_of_visited_node_color_pairs:
                set_of_visited_node_color_pairs.add((neighboring_node, edge_color))
                bfs_queue.append((neighboring_node, edge_color, current_path_length + 1))
        
    return -1

edges = [
    ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
    ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
    ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")
]

print(AlternatingPath(edges, "A", "E"))  # expected: 4
print(AlternatingPath(edges, "E", "D"))  # expected: -1