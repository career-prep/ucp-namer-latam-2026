# Technique: One directional running total
# Runtime: O(n)
# Space complexity: O(n)

def ZeroSumSubArrays(nums):
    prefixSum = {0: 1}
    count = 0
    sum = 0
    for num in nums:
        sum += num
        if sum in prefixSum:
            count += prefixSum[sum]
            prefixSum[sum] += 1
        else:
            prefixSum[sum] = 1

    return count



print(ZeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7]) == 2)
print(ZeroSumSubArrays([1, 8, 7, 3, 11, 9]) == 0)
print(ZeroSumSubArrays([8, -5, 0, -2, 3, -4]) == 2)



# Time spent: 32:46
