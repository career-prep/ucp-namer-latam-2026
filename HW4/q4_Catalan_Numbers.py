import math
def catalan_numbers(num):
    res = []

    for i in range(num+1):
        catalan_num = math.factorial(2*i) // (math.factorial(i+1) * math.factorial(i))
        res.append(catalan_num)
    
    return res


print(catalan_numbers(5))
print(catalan_numbers(6))