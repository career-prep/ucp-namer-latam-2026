#Technique: Binary Search Variation

#Time Complexity: O(log(n))
#Space Complexity: O(1)

def missingInteger(arr, n):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == mid + 1:
            l = mid + 1

        else:
            r = mid - 1

    return l + 1
        
print(missingInteger([1, 2, 3, 4, 6, 7], 7))
print(missingInteger([1], 2))
print(missingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12))
print(missingInteger([1, 2, 3], 4))

#Time taken: 19 min