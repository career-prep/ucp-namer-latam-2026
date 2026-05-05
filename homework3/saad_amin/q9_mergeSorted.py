#Time: O(N log k)
#Space: O(N)
#Technique: Heap

import heapq

def mergeKSortedArrays(arrays):
    heap = []
    result = []
    
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(heap, (arrays[i][0], i, 0))
    
    while heap:
        val, arr_idx, ele_idx = heapq.heappop(heap)
        result.append(val)
        
        if ele_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][ele_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, ele_idx + 1))
    
    return result

print(mergeKSortedArrays([[1,2,3,4,5], [1,3,5,7,9]]))
print(mergeKSortedArrays([[1,4,7,9], [2,6,7,10,11,13,15], [3,8,12,13,16]]))

#Time: 30 min 
