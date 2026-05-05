"""
idea: min heap
    - create state such that: 
        + val: the elem 
        + array_idx: the idx of the array that val belongs to
        + val_idx: the idx of val in the array
    
    - push first elem of each array to heap
    - pop all elem from heap and add to merged_array
    - if an elem of a array was chosen, we then move the ptr to next elem in same array and do all the step again


"""
import heapq

class State:
    def __init__(self, val=None, arr_idx=None, val_idx=None):
        self.val=val
        self.arr_idx= arr_idx
        self.val_idx= val_idx

    #compare 2 state for when use heappop or heappush
    def __compare__(self, other_state):
            return self.val< other_state.val

def merge_k_sorted_arrays(k: int, sorted_arrays):
    min_heap=[]
    merged_arr=[]
    
    #add first elem of every array to min heap
    for i in range(k):
        arr= sorted_arrays[i]
        if len(arr)!=0:
            state= State(arr[0], i, 0)
            heapq.heappush(min_heap, state)
    

    while min_heap:
        removed_state= heapq.heappop(min_heap)
        merged_arr.append(removed_state.val)

        val_idx= removed_state.val_idx
        next_idx= val_idx + 1

        arr_idx= removed_state.arr_idx
        curr_arr= sorted_arrays[arr_idx]

        if next_idx < len(curr_arr):
            next_val= curr_arr[next_idx]
            next_state= State(next_val, arr_idx, next_idx)
            heapq.heappush(min_heap, next_state)
    
    return merged_arr
    



