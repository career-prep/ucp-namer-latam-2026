def catalan_numbers(n):
    table = [0] * (n + 1)
    table[0] = 1 

    for i in range(1, n + 1):
        numerator = 1
        for j in range(1, 2 * i + 1):
            numerator *= j
        denom1 = 1
        for j in range(1, i + 2):
            denom1 *= j
        denom2 = 1
        for j in range(1, i + 1):
            denom2 *= j
        table[i] = numerator // (denom1 * denom2)
    return table


if __name__ == "__main__":
    print(catalan_numbers(1))  # [1, 1]
    print(catalan_numbers(5))  # [1, 1, 2, 5, 14, 42]
    print(catalan_numbers(0))  # [1]

    # Time spent: 40