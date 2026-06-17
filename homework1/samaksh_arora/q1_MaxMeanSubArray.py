#Samaksh Arora
#MaxMeanSubArray
#Time Complexity: O(n)
#Space Complexity: O(1)
#Two Pointers

def MaxMeanSubArray(nums, k):
    leftPtr = 0
    rightPtr = k-1

    currSum = sum(nums[leftPtr:k])
    maxMean = currSum/k
    while rightPtr < len(nums):
        currSum -= nums[leftPtr]
        if rightPtr+1 != len(nums):
            currSum += nums[rightPtr+1]
        currMean = currSum/k
        maxMean = max(currMean,maxMean)
        leftPtr += 1
        rightPtr +=1 
    return maxMean

test = [4,5,-3,2,6,1]
k = 2
print(MaxMeanSubArray(test, k)) #output = 4.5
k = 3
print(MaxMeanSubArray(test, k)) #output = 3

# Time Spent: 20 minutes


