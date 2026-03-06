# Fixed Size Sliding Window
# O(n) Time Complexity where n is the number of elements in the nums array
# O(1) Space Complexity because we do not create any new data structures to help us

arr1 = [4, 5, -3, 2, 6, 1]
k1 = 2

arr2 = [4, 5, -3, 2, 6, 1]
k2 = 3

arr3 = [1, 1, 1, 1, -1, -1, 2, -1, -1]
k3 = 3

arr4 = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
k4 = 5


def MaxMeanSubArray(nums, k):

    maxMean = 0

    # Calculate the initial subarray sum
    for i in range(k):
        maxMean += nums[i]

    l = 0
    currMaxMean = maxMean

    for r in range(k, len(nums)):

        currMaxMean -= nums[l]
        l += 1

        currMaxMean += nums[r]

        maxMean = max(maxMean, currMaxMean)

    # After finding the biggest sum within a window of k, return the mean of the sum
    return maxMean / k


print(MaxMeanSubArray(arr1, k1))
print(MaxMeanSubArray(arr2, k2))
print(MaxMeanSubArray(arr3, k3))
print(MaxMeanSubArray(arr4, k4))



# 13 minutes
