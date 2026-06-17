#Time: O(rows * cols), where each cell is visited at most once
#Space: O(rows * cols) in worst case (recursion stack)

import unittest

def number_of_islands(matrix) -> int:

    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != 1:
            return
        
        matrix[r][c] = 0
        for r_offset, c_offset in [(0,1),(1,0),(-1,0),(0,-1)]:
            dfs(r + r_offset,c + c_offset)

    rows = len(matrix)
    cols = len(matrix[0])
    num_of_islands = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                num_of_islands += 1
                dfs(r,c)
    return num_of_islands


#Tests
class TestNumberOfIslands(unittest.TestCase):

    def test_single_island(self):
        grid = [[1,1,0],[1,1,0],[0,0,0]]
        self.assertEqual(number_of_islands(grid), 1)

    def test_multiple_islands(self):
        grid = [[1,0,1],[0,1,0],[1,0,1]]
        self.assertEqual(number_of_islands(grid), 5)

    def test_no_islands(self):
        grid = [[0,0],[0,0]]
        self.assertEqual(number_of_islands(grid), 0)

    def test_one_cell(self):
        grid = [[1]]
        self.assertEqual(number_of_islands(grid), 1)


if __name__ == "__main__":
    unittest.main()

#Time-taken: 10 minutes