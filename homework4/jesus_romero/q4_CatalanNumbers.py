# Runtime:
# Time: O(n^2)
# Space: O(n)
# Implementation time: 20 min


def catalan_numbers(n):
    #1. Handle edge case
    if n < 0:
        return []

    #2. Declare variables
    catalan = [0] * (n + 1)
    catalan[0] = 1

    #3. Compute Catalan numbers
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]

    #4. Return result
    return catalan


def Test_CatalanNumbers():
    #1. Declare test cases
    test_cases = [1, 5]

    #2. Run tests
    for n in test_cases:
        result = catalan_numbers(n)

        print(f"Input: {n}")
        print("Output:", result)
        print()


if __name__ == "__main__":
    Test_CatalanNumbers()