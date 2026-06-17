# spent 25 minutes
# minheap
# TC - O(n*logk) where n is total elements across lists
# SC - O(k) 

import heapq

def mergeKLists(num_lists: int, lists: list[list[int]]) -> list[int]:        
    # initialize heap with first element of each list
    heap = [] # (value, list index, element index)
    for i in range(num_lists):
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, 0))

    res = [] # sorted output list
    while heap:
        # pop and append to output
        val, list_idx, elem_idx = heapq.heappop(heap)
        res.append(val)        
        
        if elem_idx + 1 < len(lists[list_idx]): # checks that list is not empty yet
            next_val = lists[list_idx][elem_idx + 1] # gets next element in list
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return res
    
    
    
    
if __name__ == "__main__":
    num_lists1 = 2
    list1 = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
    print("Input: [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]")
    print("Expected: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]")
    print("Actual  :", mergeKLists(num_lists1, list1))
    
    print()
    
    num_lists2 = 3
    list2 = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
    print("Input: [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]")
    print("Expected: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]")
    print("Actual  :", mergeKLists(num_lists2, list2))