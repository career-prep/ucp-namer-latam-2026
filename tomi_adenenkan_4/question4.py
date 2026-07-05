

def main(num):
    if num < 0:
        return 0

    if num <= 1:
        return 0

    total = 0

    for i in range(1, num+1):
        left = main(i-1)
        right = main(n-i)
        total += (left * right)
    return total
                    
print(main(1))
