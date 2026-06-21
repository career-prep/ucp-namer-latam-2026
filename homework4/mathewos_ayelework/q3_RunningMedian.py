# technique: maintain two heaps (max-heap for lower half, min-heap for upper half)
# time complexity: O(n log n)
# space complexity: O(n)
# time taken: 30 mins

import heapq

def runningMedian(nums):
    lower = []  # max-heap (negate values)
    upper = []  # min-heap
    result = []

    for num in nums:
        heapq.heappush(lower, -num)

        # balance: largest of lower must be <= smallest of upper
        if upper and -lower[0] > upper[0]:
            heapq.heappush(upper, -heapq.heappop(lower))

        # keep sizes balanced (lower can be at most 1 larger)
        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))

        if len(lower) == len(upper):
            result.append((-lower[0] + upper[0]) / 2)
        else:
            result.append(-lower[0])

    return result


print(runningMedian([1, 11, 4, 15, 12]))    # [1, 6.0, 4, 7.5, 11]
print(runningMedian([5]))                   # [5]
print(runningMedian([3, 1, 2]))             # [3, 2.0, 2]
