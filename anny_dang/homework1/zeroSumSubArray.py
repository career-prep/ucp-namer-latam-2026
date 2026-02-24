def countZeroSumSubArray(arr):
    """
    # Technique used: brute-force + pair checking

    # Idea:
    build prefix sums where prefix[i] = sum(arr[0...i])

    for each r
     - if prefix[r] == 0, then subarray sums to 0 
     - for each l < r, if prefix[r] == prefix[l], then subarray (l+1...r) sums to 0

    # Complexity 
    Time: O(n^2)
    Space: O(n)

    # Time spent: 20mins
    """
    count = 0

    for r in range(1, len(arr)):
        arr[r] += arr[r-1]
    
    for r in range(len(arr)):
        if arr[r] == 0:
            count += 1
        l = 0
        while l < r:
            if arr[r] - arr[l] == 0:
                count += 1
            l += 1
        
    return count

arr1 = [4, 5, 2, -1, -3, -3, 4, 6, -7]
print(countZeroSumSubArray(arr1))

arr2 = [1, 8, 7, 3, 11, 9]
print(countZeroSumSubArray(arr2))

arr3 = [8, -5, 0, -2, 3, -4]
print(countZeroSumSubArray(arr3))


