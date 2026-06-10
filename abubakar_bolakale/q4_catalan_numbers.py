def get_catalan_numbers(n: int) -> list[int]:
    if n < 0:
        return []
    catalan = [0] * (n + 1)
    catalan[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
            
    return catalan


if __name__ == "__main__":
    assert get_catalan_numbers(5) == [1, 1, 2, 5, 14, 42]
    assert get_catalan_numbers(1) == [1, 1]
    assert get_catalan_numbers(0) == [1]
    assert get_catalan_numbers(-5) == []

    assert get_catalan_numbers(2) == [1, 1, 2]
    assert get_catalan_numbers(3) == [1, 1, 2, 5]
    assert get_catalan_numbers(4) == [1, 1, 2, 5, 14]
    assert get_catalan_numbers(6) == [1, 1, 2, 5, 14, 42, 132]

    print("All Catalan Numbers tests passed!")
