# Question 9 (Dedup Array)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time spent: 18 mins 23s

def DedupArray(arr):
    left = 0
    for right in range(1, len(arr)):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]

    for i in range(left + 1, len(arr)):
        arr[i] = -1

    return arr




#Tests
print(DedupArray([1,1,2,2,3,3,4,4]))
# [1, 2, 3, 4, -1, -1, -1, -1]

print(DedupArray([1,1,1,1]))
# [1, -1, -1, -1]

print(DedupArray([1,2,3]))
# [1, 2, 3]

print(DedupArray([]))
# []

