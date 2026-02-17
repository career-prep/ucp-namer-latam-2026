# Time complexity: O(log n)
# Space complexity: O(1)

# Technique: Binary search variation

def MissingInteger(arr, n):
    if n < 1:
        return None
    
    if n == 1:
        return 1
    
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == mid + 1:
            low = mid + 1
        
        else:
            high = mid - 1

    return low + 1


if __name__ == '__main__':
    inputArr = [1, 2, 3, 4, 6, 7]
    n = 7
    # inputArr = [1]
    # n = 2
    # inputArr = []
    # n = 1
    # inputArr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # n = 12
    # inputArr = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
    # n = 12
    print("Input Array:", inputArr)
    print("Output:", MissingInteger(inputArr, n))

# ~ time spent: 20 minutes