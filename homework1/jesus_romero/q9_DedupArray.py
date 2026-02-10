"""
Given a sorted array of non neg integers, modify the array by removing duplicates
 so each element appears once. If arrays are static in your language of choice, 
 the remaining elements should appear in the left hand side of the array and the 
 extra space in the right hand should be padded with -1s
"""


def DedupArrayDynamic(arr):
    #1. Edge case
    if not arr:
        return []

    #2. Write pointer tracks where the next unique value belongs
    write_ptr = 1

    #3. Read pointer scans for unique values
    for read_ptr in range(1, len(arr)):
        if arr[read_ptr] != arr[read_ptr - 1]:
            arr[write_ptr] = arr[read_ptr]
            write_ptr += 1

    #4. Truncate the list to remove the "leftover" duplicates
    return arr[:write_ptr]

def test_dedup():
    input_array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    expected = [1, 2, 3, 4]
    result = DedupArrayDynamic(input_array)
    assert result == expected, f"Expected {expected}, got {result}"

    input_array = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
    expected = [0, 1, 4, 5, 8, 9, 10, 11, 15]
    result = DedupArrayDynamic(input_array)
    assert result == expected, f"Expected {expected}, got {result}"

    input_array = [1, 3, 4, 8, 10, 12]
    expected = [1, 3, 4, 8, 10, 12]
    result = DedupArrayDynamic(input_array)
    assert result == expected, f"Expected {expected}, got {result}"


if __name__ == "__main__":
    test_dedup()