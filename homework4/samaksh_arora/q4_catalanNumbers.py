#Samaksh Arora
#Question 4 - Catalan Numbers
#Dynamic programming (Tabulation)
#Time Complexity: O(n)
#Space Complexity: O(n)
#Time Spent: >40 minutes


def getCatalanNumbers(n):
    # Create a table to store results from C(0) to C(n)
    table = [0] * (n + 1)

    # Base case
    table[0] = 1

    for i in range(1, n + 1):
        table[i] = table[i - 1] * 2 * (2 * i - 1) // (i + 1)

    return table

#Test Cases
assert getCatalanNumbers(1) == [1, 1]
assert getCatalanNumbers(5) == [1, 1, 2, 5, 14, 42]

assert getCatalanNumbers(0) == [1] 
assert getCatalanNumbers(3) == [1, 1, 2, 5]
