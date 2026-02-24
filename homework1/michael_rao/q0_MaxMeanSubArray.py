# method: fixed size sliding window
# time: O(n)
# space: O(1)

def maxMeanSubArray(arr, k):
    maxMean = 0

    currSum = 0
    for i in range(k):
        currSum += arr[i]
    maxMean = currSum / k

    for i in range(k, len(arr)):
        currSum += arr[i] - arr[i-k]
        maxMean = max(maxMean, currSum / k)
    
    return maxMean

def checkSolution(arr, k, correct):
    print("Input Array:", arr)
    print("Input k:", k)
    print("Correct:", correct)
    print("Output: ", maxMeanSubArray(arr,k))
    print()

checkSolution([4,5,-3,2,6,1], 2, 4.5)
checkSolution([4,5,-3,2,6,1], 3, 3)
checkSolution([1,1,1,1,-1,-1,2,-1,-1], 3, 1)
checkSolution([1,1,1,1,-1,-1,2,-1,-1,6], 5, 1)
checkSolution([2], 1, 2)

# time taken: 18 min