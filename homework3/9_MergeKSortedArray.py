# Data Structure: List
# Algorithm: Collect and Sort
# Time Complexity: O(N log N)
# Space Complexity: O(N)

def mergeKSortedArrays(k, arrays):
    if not arrays or k == 0:
        return []
    
    result = []
    
    for arr in arrays:
        for val in arr:
            result.append(val)
            
    result.sort()
    return result

def main():
    k1 = 2
    arrays1 = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
    print(f"Test Case 1 - Result: {mergeKSortedArrays(k1, arrays1)}")

    k2 = 3
    arrays2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
    print(f"Test Case 2 - Result: {mergeKSortedArrays(k2, arrays2)}")

if __name__ == "__main__":
    main()

# Time Spent: 20 minutes