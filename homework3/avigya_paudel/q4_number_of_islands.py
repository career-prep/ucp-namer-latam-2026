# Time Taken: 25 minutes
# Time Complexity: O(ROWS X COLS)
# Space Complexity: O(ROWS X COLS) 
# Algorithm: DFS

def number_of_islands(matrix) -> int:
    """
    Count how many islands are in a 2D grid.

    An island is a group of connected 1s. Cells are connected only up, down,
    left, and right. 0s are water and are ignored.
    """
    ROWS, COLS = len(matrix), len(matrix[0])
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = set()
    count = 0
    
    def dfs(r,c):
        if (r,c) in visited:
            return
        visited.add((r,c))

        # Visit every land cell connected to the current one.
        for dr, dc in directions:
            r_new, c_new = r+dr, c+dc
            if 0 <= r_new < ROWS and 0 <= c_new < COLS and matrix[r_new][c_new] == 1:
                dfs(r_new, c_new) 
        return
        

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 1 and (r,c) not in visited:
                dfs(r,c)
                count += 1
    return count

if __name__ == "__main__":
    example_1 = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    example_2 = [
        [1, 0, 0],
        [0, 0, 0],
    ]

    print(number_of_islands(example_1))  # Expected: 3
    print(number_of_islands(example_2))  # Expected: 1