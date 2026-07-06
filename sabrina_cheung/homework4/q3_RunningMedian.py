# Method: Two Heaps
# Space Complexity: O(N)
# Time Complexity: O(NLogN)
# Total Time Taken: 30 mins
# Use a max heap for the bottom half of numbers so that the root is the maximum number of the bottom half.
# Use a min heap for the top half of numbers so that the root is the minimum number of the top half.
# Find the median of both roots to get the running median without having to recalculate the median every time.

import heapq
def RunningMedian(arr):
    maxHeap = []
    minHeap = []
    res = []

    for num in arr:
        if not maxHeap or num <= -maxHeap[0]: # If maxheap is empty or num is smaller than the largest number in bottom half
            heapq.heappush(maxHeap, -num)
        else:
            heapq.heappush(minHeap, num)
        
        if len(maxHeap) > len(minHeap) + 1: # If maxheap has more than one extra element, move the root node to min heap
            temp = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, temp)
        elif len(maxHeap) < len(minHeap): # If minheap has more than one extra element, move the root node to min heap
            temp = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -temp)

        if len(maxHeap) > len(minHeap): # Odd num of elements --> root of max heap is median
            res.append(-maxHeap[0])
        else: # Even num of elements --> average the two roots
            res.append((-maxHeap[0] + minHeap[0]) / 2.0)
    return res
    
print(RunningMedian([1, 11, 4, 15, 12]))
print(RunningMedian([0, 0, 0, 3, 5]))
print(RunningMedian([-5, -10, -2, -1]))
print(RunningMedian([10, -20, 0, 30, -5]))
print(RunningMedian([12]))
print(RunningMedian([5, 5, 5, 5]))