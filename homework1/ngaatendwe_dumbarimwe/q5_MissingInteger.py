#Time: O(n)
# Space: O(n), where n is the size of the input array   

from typing import List
import unittest

def missing_integer(nums: List, n: int) -> int:
    nums_set = set(nums)
    num = 1
    
    for _ in range(n):
        if num not in nums_set:
            return num
        num += 1
    return "No missing number"



class TestMissingInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(missing_integer([], 3), 1)

    def test_missing_in_middle(self):
        self.assertEqual(missing_integer([1, 2, 4, 5], 5), 3)

    def test_missing_first(self):
        self.assertEqual(missing_integer([2, 3, 4], 4), 1)

    def test_no_missing_number(self):
        self.assertEqual(missing_integer([1, 2, 3], 3), "No missing number")

    def test_with_duplicates_and_negatives(self):
        self.assertEqual(missing_integer([1, 1, 2, -3, 0], 3), 3)


if __name__ == "__main__":
    unittest.main()

#Time-taken: 10 min

    
