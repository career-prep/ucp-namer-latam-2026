# spent < 10 min
# binary search
# Time Complexity - O(logn) 
# Space Complexity - O(1)


def missingInteger(arr, n):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # in a perfect array (no missing), arr[mid] = mid+1
        if arr[mid] == mid + 1: # left half is fine and missing in right half
            low = mid + 1
        else: 
            high = mid - 1

    return low + 1
    
    
if __name__ == "__main__":
    input_arrs = [
        [1,2,3,4],
        [1,2,3,4,6,7],
        [1],
        [1,2,3,4,5,6,7,8,10,11,12]
    ]
    input_ns = [
        5,
        7,
        2,
        12
    ]
    expected = [
        5,
        5,
        2,
        9
    ]
    
    for i in range(len(input_arrs)):
        print("expected:", expected[i])
        print("actual:", missingInteger(input_arrs[i], input_ns[i]))
        print()
    
    
if __name__ == "__main__":
    input_arrs = [
        [1,2,3,4],
        [1,2,3,4,6,7],
        [1],
        [1,2,3,4,5,6,7,8,10,11,12]
    ]
    input_ns = [
        5,
        7,
        2,
        12
    ]
    expected = [
        5,
        5,
        2,
        9
    ]
    
    for i in range(len(input_arrs)):
        print("expected:", expected[i])
        print("actual:", missingInteger(input_arrs[i], input_ns[i]))
        print()