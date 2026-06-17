"""
Time, Space complexities: O(log n), O(1)
Q6: MissingInteger
Given an integer n and a sorted array of integers of size n-1 which ontain all but 
one of the integers in  the range 1-n, find the missing integr
"""

def findMissingInteger(arr, n):
    # Edge Case If the last element is n-1, then n is missing
    if not arr or arr[-1] != n:
        return n

    # basically bin search
    #1. Declaration of pointers
    low = 0
    high = len(arr) - 1

    #2. Classic setup
    while low < high:
        mid = (low + high) // 2
        
        #3. If the value matches the expected index+1, left side is fine
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            #4. Value is larger than expected->gap is to the left
            high = mid
            
    return low + 1

def test_FMI():
    input_array = [1, 2, 3, 4, 6, 7]
    n = 7
    expected = 5
    result = findMissingInteger(input_array, n)
    assert result == expected, f"Expected {expected}, got {result}"

    input_array = [1]
    n = 2
    expected = 2
    result = findMissingInteger(input_array, n)
    assert result == expected, f"Expected {expected}, got {result}"

    input_array = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    n = 12
    expected = 9
    result = findMissingInteger(input_array, n)
    assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_FMI()