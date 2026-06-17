# method: one directional running computation
# time: O(n)
# space: O(n)

def zeroSumSubArrays(arr):
    prefixSum = {0: -1} # Sum: index

    count = 0
    subarrays = []
    currSum = 0
    for idx, num in enumerate(arr):
        currSum += num
        if currSum in prefixSum:
            count += 1
            subarrays.append(arr[prefixSum[currSum]+1:idx+1])
        prefixSum[currSum] = idx
    
    return count, subarrays

def checkSolution(arr, count, subarrays):
    print("Input Array:", arr)
    print("Correct:", count)
    print("Correct:", subarrays)
    output1, output2 = zeroSumSubArrays(arr)
    print("Output: ", output1)
    print("Output: ", output2)
    print()

checkSolution([4,5,2,-1,-3,-3,4,6,-7],2,[[5,2,-1,-3,-3],[-3,4,6,-7]])
checkSolution([1,8,7,3,11,9],0,[])
checkSolution([8,-5,0,-2,3,-4],2,[[0],[8,-5,0,-2,3,-4]])
    
# time taken: 30 min