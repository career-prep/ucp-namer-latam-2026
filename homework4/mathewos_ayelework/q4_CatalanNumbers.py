# technique: dynamic programming - tabulation
# time complexity: O(n)
# space complexity: O(n)
# time taken: 15 mins

import math

def catalanNumbers(n):
    result = []
    for i in range(n + 1):
        catalan = math.factorial(2 * i) // (math.factorial(i + 1) * math.factorial(i))
        result.append(catalan)
    return result


print(catalanNumbers(1))   # [1, 1]
print(catalanNumbers(5))   # [1, 1, 2, 5, 14, 42]
print(catalanNumbers(0))   # [1]
