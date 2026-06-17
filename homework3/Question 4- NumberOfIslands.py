def NumberOfIslands(graph):
    visited = set()
    islands = 0
    for node in graph:
        if node not in visited:
            islands += 1
            q = [node]
            while q:
                current = q.pop(0)
                if current in visited:
                    continue
                visited.add(current)
                for neighbor in graph[current]:
                    q.append(neighbor)
    return islands

def grid_to_adjacency(grid):
    rows = len(grid)
    cols = len(grid[0])
    graph = {}
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                node = row * cols + col
                graph[node] = set()
    return graph

print(NumberOfIslands(grid_to_adjacency([
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
])))