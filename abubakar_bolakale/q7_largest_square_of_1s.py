def maximal_square(matrix: list[list[int]]) -> int:
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])
    
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
                
    return max_side


if __name__ == "__main__":
    mat1 = [
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 1, 1]
    ]
    assert maximal_square(mat1) == 2

    mat2 = [
        [0, 1, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 0, 0]
    ]
    assert maximal_square(mat2) == 3

    assert maximal_square([]) == 0
    assert maximal_square([[0, 0], [0, 0]]) == 0

    assert maximal_square([[1]]) == 1
    assert maximal_square([[1, 1], [1, 1]]) == 2
    assert maximal_square([[1, 0, 1]]) == 1
    assert maximal_square([[1], [0], [1]]) == 1

    all_ones = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert maximal_square(all_ones) == 3

    print("All LargestSquareOf1s tests passed!")
