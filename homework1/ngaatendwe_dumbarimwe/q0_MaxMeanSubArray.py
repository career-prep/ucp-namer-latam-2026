#Time: O(n), where n is the length of nums
#Space: O(1)

from typing import List
import unittest

def max_subArray(nums: List[int], k:int ) -> int:

    max_total = float("-inf")
    temp = 0

    for i in range(k):
        temp += nums[i]
    max_total = max(max_total,temp)

    for i in range(k,len(nums)):
        temp -= nums[i - k]
        temp += nums[i]
        max_total = max(max_total,temp)
        
    
    return max_total/k



#Tests
class TestMaxSubArray(unittest.TestCase):

    def test_basic_case(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        self.assertEqual(max_subArray(nums, k), 12.75)

    def test_mixed_numbers(self):
        nums = [5, -1, 3, 2, -6, 4]
        k = 2
        self.assertEqual(max_subArray(nums, k), 2.5)

    def test_all_negative_numbers(self):
        nums = [-4, -2, -8, -1]
        k = 2
        self.assertEqual(max_subArray(nums, k), -3.0)

    def test_k_equals_length(self):
        nums = [2, 4, 6]
        k = 3
        self.assertEqual(max_subArray(nums, k), 4.0)

    def test_k_equals_one(self):
        nums = [7, -3, 5, 1]
        k = 1
        self.assertEqual(max_subArray(nums, k), 7)


if __name__ == "__main__":
    unittest.main()

#Time-taken: 15 minutes 