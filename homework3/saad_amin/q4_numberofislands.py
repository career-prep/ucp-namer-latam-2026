#Time Complexity: O(R * C)
#Space Complexity: O(R * C)
#Technique: Graphs(DFS)

def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if grid[r][c] == 0:
            return

        if (r, c) in visited:
            return

        visited.add((r, c))

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                count += 1
                dfs(r, c)

    return count

def test_num_islands():

    grid1 = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    print(num_islands(grid1), "Expected: 3")

    grid2 = [
        [1, 0, 0],
        [0, 0, 0]
    ]
    print(num_islands(grid2), "Expected: 1")


    grid3 = [
        [0, 0],
        [0, 0]
    ]
    print(num_islands(grid3), "Expected: 0")
    
test_num_islands()

#Time: 15 min
