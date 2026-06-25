def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return  n * factorial(n-1)

def main(num):
    res = []
    for i in range(num+1):
        first = factorial(i * 2)
        second = factorial(i+1)
        third = factorial(i)
        val = first //(second * third)
        res.append(val)

    return res

print(main(1))
