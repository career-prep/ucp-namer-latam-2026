#dynamic programming
#time complexity: O(n)
#space complexity: O(n)

def CatalanNumbers(n):
    table = [0] * n 
    table[0] = 1

    factor = 1
    factor2 = 1
    for i in range(1, n):
        factor2 = factor2 * (i*2) * ((i*2)-1)
        factor = factor*i
        print(factor2)
        table[i] = factor2/(factor*(factor * (i+1)))

    return table

#test case
print(CatalanNumbers(5))
