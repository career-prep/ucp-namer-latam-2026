# I went for brute force approach as I couldn't get the more optimal dp one
# O((r*c)^2) time complexity and constant space complexity (r and c are rows and columns)
def largestSquareOf1s_Intuitive(grid):
        
    rows = len(grid)
    cols = len(grid[0])
    max_side = 0
    
    for r in range(rows):
        for c in range(cols):
            
            if grid[r][c] == 1:
                possible_side = 1 
                is_square_valid = True
                
                while r + possible_side < rows and c + possible_side < cols and is_square_valid:
                    
                    for i in range(r, r + possible_side + 1):
                        if grid[i][c + possible_side] == 0:
                            is_square_valid = False
                            break
                            
                    for j in range(c, c + possible_side + 1):
                        if grid[r + possible_side][j] == 0:
                            is_square_valid = False
                            break
                    
                    if is_square_valid:
                        possible_side += 1
                
                max_side = max(max_side, possible_side)
                
    return max_side

# this took me around an hour

# Test Cases
test1 = largestSquareOf1s_Intuitive([[1,1,1],[1,1,1],[1,1,1]])
print(test1)

test2 = largestSquareOf1s_Intuitive([[1,0,1],[1,1,1],[1,1,0]])
print(test2)

test3 = largestSquareOf1s_Intuitive([[0,0],[0,0]])
print(test3)

test4 = largestSquareOf1s_Intuitive([[1]])
print(test4)
