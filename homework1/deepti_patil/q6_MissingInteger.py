def missing_integer(n: int, arr: list[int]) -> int:
    """
    Given n and a sorted array of size n-1 containing numbers from 1..n
    with exactly one missing, return the missing number.

    Time Complexity: O(log n)
        - Binary search on the sorted array.
    Space Complexity: O(1)
        - Uses constant extra space.
    """

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Expected value at index mid is mid + 1 (since numbers should start at 1)
        if arr[mid] == mid + 1:
            # Missing number must be to the right
            left = mid + 1
        else:
            # We found a mismatch; missing number is at mid or to the left
            right = mid - 1

    # left ends at the first index where arr[index] != index + 1
    # So the missing number is left + 1
    return left + 1


# Examples
print(missing_integer(7, [1, 2, 3, 4, 6, 7]))                 # 5
print(missing_integer(2, [1]))                               # 2
print(missing_integer(12, [1,2,3,4,5,6,7,8,10,11,12]))        # 9

