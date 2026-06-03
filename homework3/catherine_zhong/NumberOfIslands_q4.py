#time complexity: O(nm)
#data structure & algorithm: DFS

def NumberOfIslands(map):
    if not map:
        return 0

    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                dfs(map, i, j)
                count += 1

    return count

def dfs(map, i, j):
    if i < 0 or j < 0 or i >= len(map) or j >= len(map[0]) or map[i][j] == 0:
        return

    map[i][j] = 0
    dfs(map, i-1, j)
    dfs(map, i+1, j)
    dfs(map, i, j-1)
    dfs(map, i, j+1)

#testcases
#empty matrix
map1 = []
print(f"empty matrix: {NumberOfIslands(map1)}")
#no island matrix
map2 = [[0,0,0],[0,0,0]]
print(f"no island matrix: {NumberOfIslands(map2)}")

#all island matrix
map3 = [[1,1,1],[1,1,1]]
print(f"all island matrix: {NumberOfIslands(map3)}")

#diagonal islands
map4 = [[1,0,1],[0,1,0]]
print(f"diagonal island matrix: {NumberOfIslands(map4)}")

#time spent: 20 min

