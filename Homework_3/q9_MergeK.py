# Question 9: MergeKSortedArrays
#
# Given an array of k sorted arrays, merge the k arrays into a single sorted array.
#
# Examples:
# Input:  2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
# Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]
#
# Input:  3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
# Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]

import heapq

def merge_k_sorted_arrays(k, arrays):
    res=[]
    heap=[]
    for i,arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap,(arr[0],i,0))
    while heap:
        val,i,j=heapq.heappop(heap)
        res.append(val)
        if j+1<len(arrays[i]):
            heapq.heappush(heap,(arrays[i][j+1],i,j+1))
    return res


print(merge_k_sorted_arrays(2,[[1,2,3,4,5],[1,3,5,7,9]]))
print(merge_k_sorted_arrays(3,[[1,4,7,9],[2,6,7,10,11,13,15],[3,8,12,13,16]]))
print(merge_k_sorted_arrays(1,[[1,2,3]]))
print(merge_k_sorted_arrays(3,[[1],[2,3,4],[5,6]]))
print(merge_k_sorted_arrays(3,[[1,1],[1,1],[1,1]]))
print(merge_k_sorted_arrays(3,[[],[1,2],[3,4]]))
print(merge_k_sorted_arrays(2,[[-5,-3,-1],[-4,-2,0]]))



#Time Complexity: O(nlogk) k=number of arrays
#Space Complexity: O(k)

#Spent 30 mins