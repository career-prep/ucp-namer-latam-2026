'''
    Two pointer & Sorting technique:

    Sort the array based on start time
    Maintains 2 pointers, if the start time of the next one <= the current one, merge it
    The end time will be the max between the two
    If start > previous endtime, start new time interval

    Time: O(nlogn)
    Space: O(n)
    n: numbers of elements in the array

    Time spent: 35 mins
'''


from typing import List, Tuple

def MergeIntervals(nums: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(nums) == 0:
        return []
    # Sorted based on starting time
    nums.sort(key=lambda x: x[0])
    ans = []
    prevStart, prevEnd = nums[0]
    for start, end in nums[1:]:
        # Append and start a new time interval, update prevStart, prevEnd
        if start > prevEnd:
            ans.append((prevStart, prevEnd))
            prevStart, prevEnd = start, end
        else:
            # Extend the current time interval
            prevEnd = max(prevEnd, end)
    # Append the last interval
    ans.append((prevStart, prevEnd))
    return ans

nums = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
print(MergeIntervals(nums))
nums = [(5, 8), (6, 10), (2, 4), (3, 6)]
print(MergeIntervals(nums))
nums = [(10, 12), (5, 6), (7, 9), (1, 3)]
print(MergeIntervals(nums))