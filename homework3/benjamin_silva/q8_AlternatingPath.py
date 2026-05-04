from collections import defaultdict, deque

def alternatingPath(origin, destination, edges):
    blue_graph = defaultdict(set)
    red_graph = defaultdict(set)
    for a, b, color in edges:
        if color == "blue":
            blue_graph[a].add(b)
        else:
            red_graph[a].add(b)

    visited = set()
    queue = deque()

    queue.append((origin, "blue", 0))
    queue.append((origin, "red", 0))
    visited.add((origin, "blue"))
    visited.add((origin, "red"))

    while queue:
        node, color, length = queue.popleft()

        if node == destination:
            return length
        
        next_color = "red" if color == "blue" else "blue"
        next_graph = red_graph if next_color == "red" else blue_graph

        for neighbor in next_graph[node]:
            if (neighbor, next_color) not in visited:
                visited.add((neighbor, next_color))
                queue.append((neighbor, next_color, length + 1))

    return -1

if __name__ == "__main__":

    edges1 = [
        ("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
        ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
        ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")
    ]

    print("Test 1 (expect 4):", alternatingPath("A", "E", edges1))

    print("Test 2 (expect -1):", alternatingPath("E", "D", edges1))