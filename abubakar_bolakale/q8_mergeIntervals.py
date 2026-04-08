""" 
Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.
"""
# Start by sorting
#If the current start number is greater and the next one on the list, replace with the lesser number.
#if the current end number is greater and the next one on the list, replace with the lesser number.
#add the result to an empty list and return
#time complesity O(n log n)
#space complexity 0(n)
class Solution:
    def mergeintervals(self, intervals):
        if not intervals:
            return []

        intervals.sort()

        merged = []
        cur_start, cur_end = intervals[0]

        for left, right in intervals[1:]:
            if left <= cur_end:
                if right > cur_end:
                    cur_end = right
            else:
                merged.append([cur_start, cur_end])
                cur_start, cur_end = left, right

        merged.append([cur_start, cur_end])
        return merged
    
sol = Solution()
test_cases = [
    [[2, 3], [4, 8], [1, 2], [5, 7], [9, 12]],
    [[5, 8], [6, 10], [2, 4], [3, 6]],
    [[10, 12], [5, 6], [7, 9], [1, 3]],

    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
    [[1, 2], [3, 4], [5, 6]],
    [[1, 10], [2, 3], [4, 8]],
    [[5, 7], [1, 2], [3, 4]],

    [],
    [[1, 1]],
    [[2, 2], [2, 2]],
    [[1, 5], [2, 3]],
    [[0, 0], [1, 3]],
    [[1, 3], [0, 0]],

    [[-10, -1], [-5, 0], [1, 2]],
    [[-3, -1], [-2, 2], [3, 5]],

    [[1, 4], [5, 6]],
    [[1, 4], [4, 4]],
    [[1, 4], [5, 5]],

    [[1, 1000000], [2, 3], [999999, 1000000]],
]

for test in test_cases:
    print(sol.mergeintervals(test))
    
#40 mins spent