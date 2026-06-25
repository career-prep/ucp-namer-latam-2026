#two heaps
#time complexity: O(n)
#space complexity: O(n)

import heapq 

def RunningMedian(nums):
    small = []
    large = []

    result = []

    for num in nums:
        heapq.heappush(small, -num)
        heapq.heappush(large, -heapq.heappop(small))

        if len(small) < len(large):
            heapq.heappush(small, -heapq.heappop(large))

        if len(small) > len(large):
            result.append(-small[0])
        else:
            result.append((-small[0]+large[0])/2)

    return result
        
#test cases
input = [1, 11, 4, 15, 12]
print(RunningMedian(input))