
# Technique used: Variable-size sliding Window

# finds the max mean from the subarray of length k 
def maxMeanSubArray(nums: list[int],k:int) -> float:
    # constraints:
    # len(num) >= k >= 1
    currMean, maxMean = 0, 0
    # create list containing elements from index 0 to k
    for i in range(k):
        currMean += nums[i]/k
        maxMean = currMean

    for i in range(k,len(nums)):
        currMean += nums[i]/k
        currMean -= nums[i-k]/k
        maxMean = max(currMean, maxMean)
    return round(maxMean, 2)

print("maxMeanSubArray Results:")
test_cases = [[[4,5,-3,2,6,1],2], 
              [[4,5,-3,2,6,1],3],
              [[1,1,1,1,-1,-1,2,-1,-1],3],
              [[1,1,1,1,-1,-1,2,-1,-1,6],5],
              [[2,3,4,5],4]
              ]
for test_case in test_cases:
    print(maxMeanSubArray(test_case[0], test_case[1])) #Expected Output: 4.5,3,1,1,3.5

# Time Complexity: O(n)
# Space Complexity: O(1)
# Time Taken: 26 minutes