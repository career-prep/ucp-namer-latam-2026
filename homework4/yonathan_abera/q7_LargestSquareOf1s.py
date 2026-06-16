# Technique: Dynamic programming (tabulation)
# Time Complexity: O(m * n)
# Space Complexity: O(n)

def largest_square_of_1s(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    prev = [0] * cols
    best = 0
    for i in range(rows):
        cur = [0] * cols
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    cur[j] = 1
                else:
                    cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
                best = max(best, cur[j])
        prev = cur
    return best

m1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
]
m2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0],
]
print(largest_square_of_1s(m1))
print(largest_square_of_1s(m2))
print(largest_square_of_1s([[0, 0], [0, 0]]))
print(largest_square_of_1s([[1]]))

# Time spent: 38
