# Technique: Maintain two heaps
# Time Complexity: O (N log N) since we are dealing with heaps
# Space Complexity: O(N) to maintain the elements inside the two heaps

import heapq

def running_median(stream: list[int]) -> list[float]:
    max_heap = []
    min_heap = []
    medians = []

    for num in stream:
        heapq.heappush(max_heap, -num)

        if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)

        if len(max_heap) > len(min_heap) + 1:
            val = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, val)
        elif len(min_heap) > len(max_heap):
            val = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -val)
        
        if len(max_heap) > len(min_heap):
            medians.append(float(-max_heap[0]))
        else:
            median = (-max_heap[0] + min_heap[0]) / 2.0
            medians.append(int(median) if median.is_integer() else median)
        
    return medians

stream = [1, 11, 4, 15, 12]
print(running_median(stream))

# Time Spent: 21 minutes