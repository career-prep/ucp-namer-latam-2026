# Technique: Maintain two heaps
# Time Complexity: O(n log n)
# Space Complexity: O(n)

import heapq

def running_median(nums):
    small = []  
    large = [] 
    medians = []

    for num in nums:
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
        else:
            heapq.heappush(large, num)

        if len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        elif len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))

        if len(small) == len(large):
            median = (-small[0] + large[0]) / 2
        else:
            median = -small[0]

        medians.append(median)

    return medians


def main():
    nums = [1, 11, 4, 15, 12]
    print("Running medians:", running_median(nums))


if __name__ == "__main__":
    main()
    
#Time: 27 min