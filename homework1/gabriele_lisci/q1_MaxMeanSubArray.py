# Technique: Fixed-sized sliding widow
# Runtime: O(n)
# Space complexity: O(1)


def MaxMeanSubArray(nums, k):
    left = 0
    right = k - 1
    n = len(nums)

    if k > n:
        return

    sum = 0
    for i in range(k):
        sum += nums[i]
    maxMean = sum/k
    while right < n-1:
        sum -= nums[left]
        left +=1
        right += 1
        sum += nums[right]
        maxMean = max(maxMean, sum/k)
    return maxMean

print(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 2) == 4.5)
print(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 3) == 3)
print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3) == 1)
print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5) == 1)
print(MaxMeanSubArray([4, 5, 1], 3) == 10/3)
print(MaxMeanSubArray([4, 5], 3) == None)



# Time spent: 12:30
