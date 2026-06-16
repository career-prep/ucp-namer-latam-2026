# Technique: Maintain two heaps
import heapq

def RunningMedian(nums):
    small = []
    large = []
    result = []

    for num in nums:
        heapq.heappush(small, -num)

        biggest_small = -heapq.heappop(small)
        heapq.heappush(large, biggest_small)

        if len(large) > len(small):
            smallest_large = heapq.heappop(large)
            heapq.heappush(small, -smallest_large)

        if len(small) > len(large):
            median = -small[0]
        else:
            median = (-small[0] + large[0]) / 2

        if median == int(median):
            median = int(median)

        result.append(median)

    return result


# print(RunningMedian([1, 11, 4, 15, 12]))
# Output: [1, 6, 4, 7.5, 11]

# print(RunningMedian([5]))
# Output: [5]

# print(RunningMedian([5, 10]))
# Output: [5, 7.5]

# print(RunningMedian([10, 5, 2, 8]))
# Output: [10, 7.5, 5, 6.5]