

def box(input):
    n = len(input)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = input[i][0]

    for j in range(n):
        dp[0][j] = input[0][j]

    num = 0

    for i in range(1, n):
        for j in range(1, n):
            if input[i][j] == 1:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

            num = max(num, dp[i][j])

    return num

grid = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]
print(box(grid))

grid2 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
print(box(grid2))
