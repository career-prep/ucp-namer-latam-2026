# Technique: Maintain two heaps
# time complexity: O(n log n)
# space complexity: O(n)

import heapq


def running_median(nums):
    low = []   # max heap using negative values
    high = []  # min heap
    result = []

    for num in nums:
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)

        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        if len(low) == len(high):
            result.append((-low[0] + high[0]) / 2)
        else:
            result.append(-low[0])

    return result

#test cases
assert running_median([1, 11, 4, 15, 12]) == [1, 6, 4, 7.5, 11]
assert running_median([5]) == [5]
assert running_median([2, 1, 3]) == [2, 1.5, 2]
assert running_median([]) == []

# edge cases
assert running_median([5, 5, 5]) == [5, 5.0, 5]
assert running_median([-1, -5, -2, -10]) == [-1, -3.0, -2, -3.5]
assert running_median([10, 9, 8, 7]) == [10, 9.5, 9, 8.5]
assert running_median([1, 2, 100, 3]) == [1, 1.5, 2, 2.5]

print("yay!!")

# Time spent: ~25 minutes
