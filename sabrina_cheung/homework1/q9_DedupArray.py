"""
Technique Used: Two Pointer
Time Complexity: O(n)
Space Complexity: O(1)

"""

def DedupArray(arr):
    unique_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[unique_index] = arr[i]
            unique_index += 1

    return arr[:unique_index]

test = [[1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
        [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15],
        [1, 3, 4, 8, 10, 12],
        []]

for i in test:
    print(DedupArray(i))


# Time Spent: 15 mins