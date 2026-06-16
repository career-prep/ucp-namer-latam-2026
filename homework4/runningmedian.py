# Technique: Maintain two heaps
# Time: O(n log n)
# Space: O(n)

import heapq


def runningMedian(stream):
    low = []   # max-heap (negated), smaller half
    high = []  # min-heap, larger half
    result = []

    for num in stream:
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)

        # rebalance
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2
        else:
            median = -low[0]
        result.append(int(median) if median == int(median) else median)
    return result


print(runningMedian([1, 11, 4, 15, 12]))  # [1, 6, 4, 7.5, 11]
print(runningMedian([5]))                 # [5]
print(runningMedian([5, 4, 3, 2, 1]))     # [5, 4.5, 4, 3.5, 3]

# Time spent: ~30 minutes