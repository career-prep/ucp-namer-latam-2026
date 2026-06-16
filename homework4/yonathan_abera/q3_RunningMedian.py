# Technique: Maintain two heaps
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

import heapq

def running_median(stream):
    lower = []
    upper = []
    medians = []
    for num in stream:
        if not lower or num <= -lower[0]:
            heapq.heappush(lower, -num)
        else:
            heapq.heappush(upper, num)
        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))
        if len(lower) == len(upper):
            med = (-lower[0] + upper[0]) / 2
        else:
            med = -lower[0]
        medians.append(int(med) if med == int(med) else med)
    return medians

print(running_median([1, 11, 4, 15, 12]))
print(running_median([]))
print(running_median([5]))
print(running_median([2, 4]))
print(running_median([5, 4, 3, 2, 1]))

# Time spent:
