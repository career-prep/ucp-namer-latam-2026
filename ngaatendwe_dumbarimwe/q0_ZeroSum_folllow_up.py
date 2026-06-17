#Time: O(n)
#Space: O(n), where n is the number of items in array

from typing import List 
import unittest

def zero_sum(nums: List[int]) -> int:

    count_dict = {}
    pair_count = 0

    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1
    
    for num in count_dict:
        val = -num 
        if num == 0:
            zeroes = count_dict[num]
            pair_count += zeroes * (zeroes - 1) // 2
        elif num > 0 and val in count_dict:
            pair_count += count_dict[num] * count_dict[val] 

    return pair_count

#Tests
class TestZeroSum(unittest.TestCase):

    def test_basic_pairs(self):
        self.assertEqual(zero_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]), 3)

    def test_multiple_duplicates(self):
        self.assertEqual(zero_sum([3, 3, 3, -3, -3, -3]), 9)

    def test_zero_duplicates(self):
        self.assertEqual(zero_sum([0, 0, 0, 0]), 6)

    def test_no_pairs(self):
        self.assertEqual(zero_sum([4, 3, 5, 7, 2, 8, 6]), 0)

    def test_empty_array(self):
        self.assertEqual(zero_sum([]), 0)

    def test_mixed_with_zero(self):
        self.assertEqual(zero_sum([0, 0, 0, 1, 1, -1]), 5)


if __name__ == "__main__":
    unittest.main()

