# Hashing Technique: One directional running computation
# O(n) Time Complexity where n is the number of elements in the input array
# O(n) Space Complexity where n is the number of unique running sums of the input array

arr1 = [4, 5, 2, -1, -3, -3, 4, 6, -7]

arr2 = [1, 8, 7, 3, 11, 9]

arr3 = [8, -5, 0, -2, 3, -4]


def ZeroSumSubArrays(nums):

    seenSum = {}

    # A runningSum of zero indicates a valid subarray.
    seenSum[0] = 1
    # This ^ makes sure that if we encounter a runningSum of zero, my logic will handle it properly

    runningSum = 0

    count = 0

    # While calculating the running sum, if we ever see a duplicate of an earlier running sum, we know that we have a subarray that sums to zero

    for i in range(len(nums)):

        runningSum += nums[i]

        if runningSum in seenSum:
            count += seenSum[runningSum]

        seenSum[runningSum] = 1 + seenSum.get(runningSum, 0)


    return count


print(ZeroSumSubArrays(arr1))
print(ZeroSumSubArrays(arr2))
print(ZeroSumSubArrays(arr3))

# 31 minutes