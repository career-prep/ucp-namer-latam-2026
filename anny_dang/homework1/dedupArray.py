def dedupArray(arr):
    """
    # Technique used: Reset/catch-up two pointer 

    # Idea:
    use r to scan the array and l to track the next position to write a unique value
    when arr[r] differs from the previous value, write it at arr[l] and increment l 

    # Complexity:
    time: O(n)
    space: O(1)

    # time spent: 30mins
    """
    if not arr:
        return arr

    l = 1
    for r in range(1, len(arr)):
        if arr[r] != arr[r-1]:
            arr[l] = arr[r]
            l += 1

    return arr[:l]
             
            

arr1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(dedupArray(arr1))

arr2 = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
print(dedupArray(arr2))

arr3 = [1, 3, 4, 8, 10, 12]
print(dedupArray(arr3))
