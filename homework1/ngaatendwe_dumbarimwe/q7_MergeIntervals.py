#Time: O(n log n)
#Space: O(n), where n is the length of intervals 

from typing import List
import unittest

def merge_intervals(intervals: List[tuple[int,int]]) -> List[tuple[int,int]]:
    intervals.sort(key=lambda x: x[0])
    res = []

    for start, end in intervals:
        if not res:
            res.append((start,end))
        elif start <= res[-1][1]:
            temp = res.pop()
            res.append((temp[0],max(temp[1] ,end)))
        else:
            res.append((start,end))
    return res



class TestMergeIntervals(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_intervals([]), [])

    def test_single_interval(self):
        self.assertEqual(merge_intervals([(1, 3)]), [(1, 3)])

    def test_no_overlaps(self):
        self.assertEqual(merge_intervals([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_overlapping_intervals(self):
        self.assertEqual(merge_intervals([(1, 3), (2, 6), (8, 10)]), [(1, 6), (8, 10)])

    def test_touching_intervals(self):
        self.assertEqual(merge_intervals([(1, 2), (2, 4)]), [(1, 4)])

    def test_unsorted_input(self):
        self.assertEqual(merge_intervals([(5, 7), (1, 3), (2, 4)]), [(1, 4), (5, 7)])


if __name__ == "__main__":
    unittest.main()

#Time-taken: 15 min