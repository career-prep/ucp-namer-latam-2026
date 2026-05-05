from collections import deque

"""
ideas: use bfs and expand when the node is 1
        track visited node using a visited set
        


"""

# matrix is a 2d array
def number_of_islands(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return 0

    rows= len(matrix)
    cols= len(matrix[0])

    visited= set()
    island_count= 0
    
    #helper function
    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        visited.add((r, c))

        while queue:
            node = queue.popleft()

            node_row= node[0]
            node_col= node[1]

            directions= [(-1, 0), (1, 0), (0, -1), (0, 1)]           
            for direction in directions:
                row_direction= direction[0]
                col_direction= direction[1]

                neighbor_row= node_row + row_direction
                neighbor_col= node_col + col_direction

                #if the row and col in range and =1 and not visited
                if  0<=neighbor_row<rows and 0<= neighbor_col<cols and matrix[neighbor_row][neighbor_col]==1 and (neighbor_row, neighbor_col) not in visited:
                    visited.add((neighbor_row, neighbor_col))
                    queue.append((neighbor_row, neighbor_col))


    for r in range(rows):
        for c in range(cols):
            node= matrix[r][c]
            if node== 1 and (r, c) not in visited:
                bfs(r,c)
                island_count+=1
    
    return island_count



