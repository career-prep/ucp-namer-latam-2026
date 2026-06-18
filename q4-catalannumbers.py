import math

def CatalanNumbers(input):
    if input == 0:
        return 1

    dp = [0] * (input+1)
    dp[0] = 1

    for i in range(1, input+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - 1 - j]
    
    return dp

print(CatalanNumbers(1))
print(CatalanNumbers(5))