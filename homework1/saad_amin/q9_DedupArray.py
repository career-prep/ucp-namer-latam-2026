#Technique: Reset/catch-up two pointer

#Time Complexity: O(n)
#Space Complexity: O(1)

def DedupArray(arr):
    j = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[j + 1] = arr[i]
            j += 1

    del arr[j + 1:]

    return arr

print(DedupArray([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4,]))
print(DedupArray([0, 0, 0, 0, 0, 1, 2, 3]))

#Time taken: 15 min