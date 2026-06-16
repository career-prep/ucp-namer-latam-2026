# tabulation
import math

def CatalanNumbers(n):

    # need an array of size n+1
    array = []
 
    for i in range(n+1):
        catalan = math.factorial(2 * i) // (math.factorial(i + 1) * math.factorial(i))
        array.append(str(catalan))

    answer = ', '.join(array)

    return answer

# n = 5
# output: 1, 1, 2, 5, 14, 42

# n = 0
# output: 1

# print(CatalanNumbers(n))
