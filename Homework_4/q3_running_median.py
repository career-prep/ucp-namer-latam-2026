# Question 3: RunningMedian
# Given an array of numbers representing a stream received one by one, return
# an array representing the median after each new number is received.

import heapq
def running_median(nums):
    lowers = []
    uppers = []
    medians = []
    for num in nums:
        if not lowers or num <= -lowers[0]:
            heapq.heappush(lowers, -num)
        else:
            heapq.heappush(uppers, num)
        if len(lowers) > len(uppers) + 1:
            heapq.heappush(uppers, -heapq.heappop(lowers))
        elif len(uppers) > len(lowers):
            heapq.heappush(lowers, -heapq.heappop(uppers))
        if len(lowers) == len(uppers):
            medians.append((-lowers[0] + uppers[0]) / 2)
        else:
            medians.append(-lowers[0])
    return medians


print(running_median([1, 11, 4, 15, 12]))
print(running_median([5, 10, 100, 200]))
print(running_median([3]))
print(running_median([]))


# Spent 25 mins
# Time Complexity: O(n log n)
# Space Complexity: O(n)
