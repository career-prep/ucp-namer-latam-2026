#Time: O(n)
#Space: O(n), where n is the number of items in arr 

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
    
    for num in nums:
        val = -num
        if val == num and count_dict[val] > 1:
            pair_count += 1
            count_dict[val] -= 2
        elif val in count_dict and count_dict[val] > 0 and count_dict[num] > 0 and val != num :
            pair_count += 1
            count_dict[val] -= 1
            count_dict[num] -= 1
    return pair_count

#Tests
class TestZeroSum(unittest.TestCase):

    def test_no_pairs(self):
        self.assertEqual(zero_sum([0,1,2,3,4,5,6,7,8]), 0)

    def test_empty(self):
        self.assertEqual(zero_sum([]), 0)

    def test_multiple_pairs(self):
        self.assertEqual(zero_sum([0,2,3,7,-2,5,0,-7,-3]), 4)

    def test_duplicates(self):
        self.assertEqual(zero_sum([3,-3,3,-3,5,-5]), 3)


if __name__ == "__main__":
    unittest.main()

#Time_taken: 40 minutes 



