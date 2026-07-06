# Method: Dynamic Programming (Tabulation)
# Space Complexity: O(N)
# Time Complexity: O(N)
# Total Time Taken: 20 mins
# Use dynamic programing tabulation to perform a bottom up calculation approach of the formula such 
# that the current number depends on the calculation of the previous number. Use dynamic programming so you don't need to recalculate everytime.

def CatalanNumbers(num):
    DP = [0] * (num + 1)

    DP[0] = 1

    for i in range(1, num + 1):
        DP[i] = (2 * (2 * i - 1) * DP[i - 1]) // (i + 1)
    return DP

print(CatalanNumbers(5))
print(CatalanNumbers(1))
print(CatalanNumbers(15))