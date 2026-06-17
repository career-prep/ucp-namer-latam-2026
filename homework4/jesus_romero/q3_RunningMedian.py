# Runtime:
# Time: O(n logn)
# Space: O(n)
# Implementation time: 20 min

import heapq


def running_median(numbers):
    #1. Declare variables
    lower_half = []
    upper_half = []
    medians = []

    #2. Process each number
    for num in numbers:

        #3. Add number to heap
        if not lower_half or num <= -lower_half[0]:
            heapq.heappush(lower_half, -num)
        else:
            heapq.heappush(upper_half, num)

        #4. Rebalance heaps
        if len(lower_half) > len(upper_half) + 1:
            value = -heapq.heappop(lower_half)
            heapq.heappush(upper_half, value)

        elif len(upper_half) > len(lower_half):
            value = heapq.heappop(upper_half)
            heapq.heappush(lower_half, -value)

        #5. Calculate median
        if len(lower_half) == len(upper_half):
            median = (-lower_half[0] + upper_half[0]) / 2
        else:
            median = -lower_half[0]

        medians.append(median)

    #6. Return result
    return medians


def Test_RunningMedian():
    #1. Declare input
    numbers = [1, 11, 4, 15, 12]

    #2. Compute medians
    result = running_median(numbers)

    #3. Print results
    print("Input:", numbers)
    print("Output:", result)


if __name__ == "__main__":
    Test_RunningMedian()