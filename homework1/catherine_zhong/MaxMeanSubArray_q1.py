#time complexity: O(n)
#space complexity: O(1)

def MaxMeanSubArray(nums, k):
    maxSum = 0

    #checks for empty list
    if not nums:
        return 0
    
    #computes the sum of first k elements
    for i in range(k):
        maxSum += nums[i]
    
    #checks all sums of subarrays length k
    start = 0
    end = k
    currentSum = maxSum
    while end < len(nums):
        maxSum = max(maxSum, currentSum - nums[start] + nums[end])
        currentSum = currentSum - nums[start] + nums[end]
        start += 1
        end += 1
    
    return maxSum/k

#test cases
test1 = []
test2 = [4,5,-3,2,6,1]
test3 = [1,1,1,1,1,-1,2,-1,-1]
test4 = [-1,1,-1,1]
test5 = [0,0,0]
test6 = [-1,-2,-3,-1,-1]

print("test1: ", MaxMeanSubArray(test1, 0))
print("test2: ", MaxMeanSubArray(test2, 2))
print("test3: ", MaxMeanSubArray(test3, 3))
print("test4: ", MaxMeanSubArray(test4, 4))
print("test5: ", MaxMeanSubArray(test5, 1))
print("test6: ", MaxMeanSubArray(test6, 2))

#time spent: 15 min