# Technique: Tabulation
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def catalan_numbers(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        total = 0

        for j in range(i):
            total += dp[j] * dp[i - 1 - j]

        dp[i] = total

    return dp


def main():
    print("n = 1:", catalan_numbers(1))
    print("n = 5:", catalan_numbers(5))


if __name__ == "__main__":
    main()
    
#Time : 30 min