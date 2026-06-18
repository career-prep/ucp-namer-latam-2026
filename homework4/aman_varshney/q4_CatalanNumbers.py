# spent 15 minutes
# tabulation
# TC - O(n^2)
# SC - O(n)


def catalan_numbers(n: int) -> list[int]:
    """Return Catalan numbers C(0) through C(n)"""
    result = [0] * (n+1)
    result[0] = 1 # C(0) = 1

    for i in range(1, n+1):
        for j in range(i):
            result[i] += result[j] * result[i-1-j]

    return result



def run_tests() -> None:
    print("Running tests")
    assert catalan_numbers(1) == [1, 1]
    assert catalan_numbers(5) == [1, 1, 2, 5, 14, 42]
    print("All tests passed")

if __name__ == "__main__":
    run_tests()
