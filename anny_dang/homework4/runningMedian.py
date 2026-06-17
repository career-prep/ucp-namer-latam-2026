import heapq
def runningMedian(stream):
    """
    idea:
    - create empty max and min heap 
    - max heap keeps negative values (smaller half)
    - min heap keeps positive values (higher half)
    - for loop to walk through each value in stream
        - if no elements in max_heap or current value <= -max_heap[0] -> push it into max_heap
        - otherwise -> push it into min_heap 

        - if len(max_heap) > len(min_heap) + 1 -> push largest value in max_heap to min_heap
        - otherwise -> push smallest value in min_heap to max_heap 

        - if len(max_heap) == len(min_heap) -> median = sum of two first values in both heaps / 2
        - else if len(max_heap) > len(min_heap) -> median = - first value in max_heap 
        - else -> median = first value in min_heap 

        - then add median into ans list
    
    time: O(nlogn)
    space: O(n)
    """
    ans = []
    min_heap, max_heap = [], []
    for x in stream:
        if not max_heap or x <= max_heap[0]:
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(min_heap, x)
        
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        if len(min_heap) == len(max_heap):
            median = (min_heap[0] - max_heap[0])/2
        elif len(min_heap) > len(max_heap):
            median = min_heap[0]
        else:
            median = -max_heap[0]
        
        ans.append(median)
    
    return ans 


ex1 = [1, 11, 4, 15, 12]
print(runningMedian(ex1))