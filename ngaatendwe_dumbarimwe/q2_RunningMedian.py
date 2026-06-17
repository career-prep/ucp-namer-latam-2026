#Time: O(n log n), where n is the total number of elements in the stream
#Space: O(n)

import heapq

def running_median(nums):
    lower = []   
    upper = []   

    medians = []

    for num in nums:
        if not lower or num <= -lower[0]:
            heapq.heappush(lower, -num)
        else:
            heapq.heappush(upper, num)

        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))

        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))

        if len(lower) == len(upper):
            median = (-lower[0] + upper[0]) / 2
        else:
            median = -lower[0]

        medians.append(median)

    return medians


#Time-taken: 30 minutes


import unittest


class TestRunningMedian(unittest.TestCase):

    def test_single_value(self):
        self.assertEqual(running_median([5]), [5])

    def test_even_and_odd_lengths(self):
        self.assertEqual(running_median([1, 2, 3, 4]), [1, 1.5, 2, 2.5])

    def test_unsorted_values(self):
        self.assertEqual(running_median([3, 1, 4, 1]), [3, 2.0, 3, 2.0])


if __name__ == "__main__":
    unittest.main()