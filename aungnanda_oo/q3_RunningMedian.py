# Question 3: RunningMedian

# Technique: Maintain two heaps
# Keep a max-heap (lo) for the lower half and a min-heap (hi) for the upper
# half. After each insertion, rebalance so their sizes differ by at most 1.
# The median is either the top of lo (odd total) or the average of both tops.

# Python's heapq is a min-heap, so negate values to simulate a max-heap for lo.

# Time Complexity:  O(n log n) — each of n insertions costs O(log n)
# Space Complexity: O(n)

import heapq


def runningMedian(nums):
    lo = []  # max-heap (negate to use heapq)
    hi = []  # min-heap
    result = []

    for num in nums:
        # Push to lo first
        heapq.heappush(lo, -num)

        # Balance: lo's max must not exceed hi's min
        if hi and -lo[0] > hi[0]:
            heapq.heappush(hi, -heapq.heappop(lo))

        # Keep sizes balanced (lo can be at most 1 larger)
        if len(lo) > len(hi) + 1:
            heapq.heappush(hi, -heapq.heappop(lo))
        elif len(hi) > len(lo):
            heapq.heappush(lo, -heapq.heappop(hi))

        if len(lo) == len(hi):
            median = (-lo[0] + hi[0]) / 2
        else:
            median = float(-lo[0])

        result.append(median)

    return result
# Time Complexity = O(n log n), Space Complexity = O(n)


# --- Tests ---

print("Input [1,11,4,15,12]:", runningMedian([1, 11, 4, 15, 12]))
# Expected: [1, 6.0, 4, 7.5, 11]

print("Input [5]:", runningMedian([5]))
# Expected: [5.0]

print("Input [3,1]:", runningMedian([3, 1]))
# Expected: [3.0, 2.0]

print("Input [2,4,6,8]:", runningMedian([2, 4, 6, 8]))
# Expected: [2.0, 3.0, 4.0, 5.0]

print("Input []:", runningMedian([]))
# Expected: []

# Spent a total of 25 mins on this question
