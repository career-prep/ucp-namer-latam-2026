def findMissingInteger(n, arr):
    """
    # Technique used: set (i used it because it takes O(1) when searching)

    # Idea:
    Put all values in a set, then scan 0..n-1 and return the first value not present.

    # Complexity:
    Time: O(n)
    Space: O(n)

    # Time spent: 7mins
    """
    arr = set(arr)
    for i in range(n):
        if i + 1 not in arr:
            return i + 1
    
n1, arr1 = 7, [1, 2, 3, 4, 6, 7]
print(findMissingInteger(n1, arr1))

n2, arr2 = 2, [1]
print(findMissingInteger(n2, arr2))

n3, arr3 = 12, [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
print(findMissingInteger(n3, arr3))
