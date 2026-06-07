# Min-Heap
# O(nlog(n)) Time Complexity where 'n' is the total number of elements across all arrays.
# O(n) Space Compleixty where 'n' is the total number of elements across all arrays.
# Given an array of k sorted arrays, merge the k arrays into a single sorted array.

from q2_Heap import Heap


def mergeKSortedArrays(k, sortedArrays):

    # My intuition is to build a min-heap from all values, then pop from the min-heap repeatedly until it is empty to create one sorted array
    # This is basically heap sort

    # If there are no arrays, return an empty array (Or I could return None. This is something I would ask in an interview when discussing edge cases)
    if k == 0:
        return []

    # If we only have one sorted subarray, we can just return it immediately
    if k == 1:
        return sortedArrays[0]

    minHeap = Heap()

    length = 0 # Will hold length of fully merged arrays

    for i in range(k):
        length += len(sortedArrays[i])
        for j in range(len(sortedArrays[i])):
            minHeap.insert(sortedArrays[i][j]) # Each insert is O(log(n))


    res = []

    for _ in range(length):

        res.append(minHeap.top())

        minHeap.remove() # Each remove is O(log(n))


    return res


# 23 minutes


# Test Cases
k1 = 2
arrs1 = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]

k2 = 3
arrs2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]

k3 = 0
arrs3 = [[]]

k4 = 1
arrs4 = [[1, 2, 3, 4, 5, 6]]


print(mergeKSortedArrays(k1, arrs1))
print(mergeKSortedArrays(k2, arrs2))

# My Added Test Cases
print(mergeKSortedArrays(k3, arrs3))
print(mergeKSortedArrays(k4, arrs4))

