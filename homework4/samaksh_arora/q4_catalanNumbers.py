#Samaksh Arora
#Question 4 - Catalan Numbers
#Dynamic programming (Tabulation)
#Time Complexity:
#Space Complexity:
#Time Spent:


def getCatalanNumbers(n):
    # Create a table to store results from C(0) to C(n)
    table = [0] * (n + 1)

    # Base case
    table[0] = 1

    # Fill the table using the mathematical formula: C(i) = C(i-1) * 2(2i-1) / (i+1)
    # This is O(n) instead of O(n^2)
    for i in range(1, n + 1):
        table[i] = table[i - 1] * 2 * (2 * i - 1) // (i + 1)

    return table

#Test Cases
assert getCatalanNumbers(1) == [1, 1]
assert getCatalanNumbers(5) == [1, 1, 2, 5, 14, 42]

assert getCatalanNumbers(0) == [1] 
assert getCatalanNumbers(3) == [1, 1, 2, 5]
