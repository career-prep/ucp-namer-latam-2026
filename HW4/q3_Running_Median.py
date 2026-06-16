"""
problem:
    - given array of nums represent stream received 1 by 1
    - return array representing the median after each new number is receive


idea:
    - split into 2 smaller function:    
        + add number 
        + find the median 

    -  to find the median, we might need to store them in sorted order 
    - we can use 2 heap:
        + small heap: we use maxHeap
        + large heap: we use minHeap
        + every elem in largeHeap > elem in smallHeap
        + 2 heap must have apporximately the same number of elem in it
        => we use maxHeap small heap and minHeap for large heap because:

            CASE 1: when num of elem in small and large heap equals:
            +  EX:  smallHeap: 1,2    largeHeap: 3,4
            + to find the median, we gotta find the max of small heap (2) and the min of large heap (3)   
                * (the above happen when number of elem in small heap = number of elem in max heap) 
            
            CASE 2: when num of elem in small heap > large heap:
            + EX:  smallHeap: 1,2,3    largeHeap: 3,4
            + to find the median, we gotta find the max of small heap (3)

            CASE 3: when num of elem in small heap < large heap:
            + EX: smallHeap: 1,2    largeHeap: 2,3,4
            + to find the median, we gotta find the min of large heap (2)


"""
import heapq

def running_median(nums):
    
    #max Heap
    small_heap = []
    heapq.heapify(small_heap)

    #min Heap
    large_heap = []
    heapq.heapify (large_heap)

    res = []

    def add_num(num):
        # by default add number to small_heap
        heapq.heappush(small_heap, -1 * num)

        # push the largest val of small heap to large heap
        largest_val_in_small_heap  = -heapq.heappop(small_heap)
        heapq.heappush(large_heap, largest_val_in_small_heap)

        # re-arrange the elem to maintain the balance of 2 heap
        if len(large_heap) > len(small_heap):
            smallest_val_in_large_heap = heapq.heappop(large_heap)

            heapq.heappush(large_heap, -1 * smallest_val_in_large_heap)
            

    def find_median():
        if len(small_heap) > len(large_heap):
            return -1 * small_heap[0]
        
        largest_val_in_small_heap = -1 * small_heap[0]
        smallest_val_in_large_heap = large_heap[0]

        median = (largest_val_in_small_heap + smallest_val_in_large_heap) / 2
        return median
    
    for num in nums:
        add_num(num)
        res.append(find_median)
    
    return res