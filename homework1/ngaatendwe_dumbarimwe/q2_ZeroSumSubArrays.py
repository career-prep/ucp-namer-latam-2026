# Time: O(n * n), where n is the number of elements in nums
# Space: O(1)

from typing import List
import unittest

def zero_sum_subarrays(nums: List[int]) -> int:
    
    length  = len(nums)
    count = 0
    

    for i in range(length):
        total = 0
        for j in range(i, length):
            total += nums[j]
            if total == 0:
                count += 1
                break

    return count

class TestZeroSumSubarrays(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(zero_sum_subarrays([]), 0)

    def test_no_zero_sum(self):
        self.assertEqual(zero_sum_subarrays([1, 2, 3]), 0)

    def test_single_zero(self):
        self.assertEqual(zero_sum_subarrays([0]), 1)

    def test_zero_sum_later_in_subarray(self):
        self.assertEqual(zero_sum_subarrays([1, -1]), 1)

    def test_multiple_starting_points(self):
        self.assertEqual(zero_sum_subarrays([1, -1, 1]), 2)

    def test_all_zeros(self):
        self.assertEqual(zero_sum_subarrays([0, 0, 0]), 3)


if __name__ == "__main__":
    unittest.main()
            
#Time-taken: 20 minutes