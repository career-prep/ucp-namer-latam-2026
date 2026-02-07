# Technique: sort array then solve
# Runtime: O(nlogn)
# Space complexity: O(n)

def MergeIntervals(nums):
    if not nums:
        return
    nums.sort()
    result = [nums[0]]
    n = len(nums)
    x = 1
    while x < n:
        if len(result) > 0  and result[-1][1] >= nums[x][0] and result[-1][0] <= nums[x][0]:
            interval = [result[-1][0], max(nums[x][1], result[-1][1])]
            result[-1] = interval
        elif nums[x-1][1] >= nums[x][0] and nums[x-1][0] <= nums[x][0]:
            interval = [nums[x-1][0], max(nums[x][1], nums[x-1][1])]
            result.append(interval)
        else:
            result.append(nums[x])
        x+=1
    return result
print(MergeIntervals([[2,3],[4,8],[1,2],[5,7],[9,12]])) #== [[4,8], [1,3], [9,12]])
print(MergeIntervals([[5,8],[6,10],[2,4],[3,6]])) #== [[2,10]])
print(MergeIntervals([[10,12], [5,6], [7,9], [1,3]])) #== [[10,12], [5,6], [7,9], [1,3]])

# Time spent: 36:00
