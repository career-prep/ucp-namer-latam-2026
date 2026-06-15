# Runtime: O(nlogn)
# Space complexity: O(n)
# Technique: Maintain two heaps
import heapq
def runningMedian(nums):
    if not nums:
        return []
    minheap = []
    maxheap = [-nums[0]]
    res = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > res[-1]:
            heapq.heappush(minheap, nums[i])
        else:
            heapq.heappush(maxheap, -nums[i])
        if len(maxheap) > len(minheap) + 1:
            heapq.heappush(minheap, -heapq.heappop(maxheap))

        if len(minheap) > len(maxheap) + 1:
            heapq.heappush(maxheap, -heapq.heappop(minheap))

        if len(minheap) == len(maxheap):
            res.append((minheap[0]-maxheap[0])/2)
        elif len(minheap) > len(maxheap):
            res.append(minheap[0])
        else:
            res.append(-maxheap[0])
    return res

print(runningMedian([1,11,4,15,12]))
print(runningMedian([]))
print(runningMedian([32]))
print(runningMedian([1,2,3,4,5,6]))

# Time Spent: 40:00
