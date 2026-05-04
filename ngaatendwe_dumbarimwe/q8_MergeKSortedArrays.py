#Time: O(N log N), where N is total number of elements
#Space: O(N)

import heapq
import unittest

def merge_ksorted_arrays(nums: list[list]) -> list:
    heap = []
    res = []

    for arr in nums:
        for val in arr:
            heapq.heappush(heap, val)

    while heap:
        res.append(heapq.heappop(heap))

    return res


#Tests
class TestMergeKSortedArrays(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(merge_ksorted_arrays([[1,3],[2,4]]), [1,2,3,4])

    def test_single_array(self):
        self.assertEqual(merge_ksorted_arrays([[5,6,7]]), [5,6,7])

    def test_empty(self):
        self.assertEqual(merge_ksorted_arrays([]), [])


if __name__ == "__main__":
    unittest.main()
            
#Time-taken: 15 minutes