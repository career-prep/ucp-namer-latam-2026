# Technique: Maintain two heaps
# Time Complexity: O(n log n)
# Space Complexity: O(n)

import heapq

def running_median(nums):
    max_heap = []
    min_heap = []
    medians = []

    for num in nums:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(max_heap) > len(min_heap):
            medians.append(-max_heap[0])
        else:
            medians.append((-max_heap[0] + min_heap[0]) / 2)
    return medians

# Time Taken: 12mins 43secs

# Testcases:
nums_1 = [1, 11, 4, 15, 12]
print(running_median(nums_1))

# Edge cases:
nums_2 = [5] #Single element
print(running_median(nums_2))

nums_3 = [7, 7, 7, 7] #Same values
print(running_median(nums_3))