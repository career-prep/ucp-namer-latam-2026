# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Fixed-size sliding window

def MaxMeanSubArray(arr, k):
    if len(arr) < k or k <= 0:
        return None

    maxSum = 0
    for i in range(k):
        maxSum += arr[i]

    currSum = maxSum
    for i in range(k, len(arr)):
        currSum += arr[i] - arr[i-k] # add new element and subtract old element
        maxSum = max(currSum, maxSum)
    
    return maxSum/k


if __name__ == '__main__':
    # inputArr = [4, 5, -3, 2, 6, 1]
    # k = 2
    # inputArr = [4, 5, -3, 2, 6, 1]
    # k = 3
    # inputArr = [1, 1, 1, 1, -1, -1, 2, -1, -1]
    # k = 3
    # inputArr = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
    # k = 5
    inputArr = []
    k = 5
    print("Input Array:", inputArr)
    print("Output:", MaxMeanSubArray(inputArr, k))

# ~ time spent: 15 minutes