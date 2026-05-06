# dfs 
# spent 10-15 minutes
# TC - O(R*C)
# SC - O(1) 


def numberOfIslands(matrix: list[list[int]]) -> int:
    count = 0
    if not matrix: # empty case
        return count
    
    row_length = len(matrix)
    col_length = len(matrix[0])
    directions = [ [0,1], [1,0], [-1,0], [0,-1] ]
    
    # helper to traverse all possible directions and mark as seen
    def dfs(r, c):
        # out of bounds
        if r >= row_length or r < 0:
            return 
        if c >= col_length or c < 0:
            return 
        
        # mark as seen if island
        if matrix[r][c] == 0: 
            return 
        matrix[r][c] = 0
        
        # check neighbors
        for dx, dy in directions:
            dfs(r+dx, c+dy)
            
            
    for r in range(row_length):
        for c in range(col_length):
            if matrix[r][c] == 1: # island
                dfs(r, c) 
                count += 1
                
    return count



if __name__ == "__main__":
    # case 1
    matrix1 = [
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    print("Expected: 3")
    print("Actual :", numberOfIslands(matrix1))
    
    # case 2 
    matrix2 = [
        [1, 0, 0],
        [0, 0, 0],
    ]
    print("Expected: 1")
    print("Actual :", numberOfIslands(matrix2))