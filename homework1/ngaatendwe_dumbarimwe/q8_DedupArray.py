# Time: O(n)
# Space: O(n), where n is the length of the array

from typing import List
import unittest

def dedup_array(nums: List[int]) -> List[int]:
    res = []

    for num in nums:
        if not res:
            res.append(num)
        elif num != res[-1]:
            res.append(num)
        else:
            continue
    
    return res



class TestDedupArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(dedup_array([]), [])

    def test_single_element(self):
        self.assertEqual(dedup_array([5]), [5])

    def test_all_duplicates(self):
        self.assertEqual(dedup_array([2, 2, 2, 2]), [2])

    def test_consecutive_duplicates(self):
        self.assertEqual(dedup_array([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_non_consecutive_duplicates(self):
        self.assertEqual(dedup_array([1, 2, 1, 2, 2, 3]), [1, 2, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()

#Time-taken: 30 min