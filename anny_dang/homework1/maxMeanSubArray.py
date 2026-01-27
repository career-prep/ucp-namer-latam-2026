def findMaxMean(arr, k):
    """
    # Technique used: Fixed-size sliding window 

    # Idea:
    edge cases: length of array < k or k = 0 -> return 0 

    loop through the array -> add new value to total 
    if current window size = k -> update maxTotal, subtract arr[left], then increase left by 1

    # Complexity:
    Time: O(n)
    Space: O(1)

    # Time spent: 20mins
    """
    if len(arr) < k or k == 0:
        return 0
    l = 0
    maxTotal = float("-inf")
    total = 0
    for r in range(len(arr)):
        total += arr[r]
        if r - l + 1 == k:
            maxTotal = max(total, maxTotal)
            total -= arr[l]
            l += 1
    
    return maxTotal/k if maxTotal != 0 else 0

arr1 = [4, 5, -3, 2, 6, 1]
k1 = 2
print(findMaxMean(arr1, 2))

arr2 = [4, 5, -3, 2, 6, 1]
k2 = 3
print(findMaxMean(arr2, k2))

arr3 = [1, 1, 1, 1, -1, -1, 2, -1, -1]
k3 = 3
print(findMaxMean(arr3, k3))

arr4 = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
k4 = 5
print(findMaxMean(arr4, k4))
