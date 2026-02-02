# Time complexity: O(n)
# Space complexity: O(n)

# Technique: One-directional running computation/total

def ZeroSumSubArray(arr):
    currentSum, count = 0, 0
    subArraySumFrequency = {}

    # If a zero sum sub array starts at zero
    subArraySumFrequency[0] = 1

    for i in arr:
        currentSum += i

        if currentSum in subArraySumFrequency:
            count += subArraySumFrequency[currentSum]
        
        subArraySumFrequency[currentSum] = subArraySumFrequency.get(currentSum, 0) + 1

    return count
        
if __name__ == '__main__':
    # inputArr = [4, 5, 2 -1, -3, -3, 4, 6, -7]
    # inputArr = [1, 8, 7, 3, 11, 9]
    # inputArr = [8, -5, 0, -2, 3, -4]
    inputArr = [0, 0, 0]
    print("Input Array:", inputArr)
    print("Output:", ZeroSumSubArray(inputArr))

# ~ time spent: 20 minutes