#Time: O(n)
#Space: O(n)

from typing import List
import unittest

def unique_sum(nums: List[int]) -> int:
    if not nums:
        return 0
    return sum(set(nums))

#Tests
class TestUniqueSum(unittest.TestCase):

    def test_all_unique(self):
        self.assertEqual(unique_sum([1,2,3,4,5,6,7,8,9,10]), 55)

    def test_empty_array(self):
        self.assertEqual(unique_sum([]), 0)

    def test_all_duplicates(self):
        self.assertEqual(unique_sum([2,2,2,2,2,2,2,2,2,2]), 2)

    def test_mixed_duplicates(self):
        self.assertEqual(unique_sum([4,1,2,2,3,4,4,5,5,5,2]), 15)

if __name__ == "__main__":
    unittest.main()

#Time taken: 15 minutes