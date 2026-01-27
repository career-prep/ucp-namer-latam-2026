#time complexity: O(n)
#space complexity: O(n)

def ZeroSumSubArrays (nums):
    #hash map for partial sums
    prefixCount = {0:1}
    prefixSum = 0

    zeroSum = 0

    #loops through and calculates partial sums
    #checks if partial sum has occured before
    for num in nums:
        prefixSum += num

        if prefixSum in prefixCount:
            zeroSum += 1
        
        prefixCount[prefixSum] = prefixCount.get(prefixSum, 0) + 1
    
    return zeroSum

test1 = []
test2 = [0,0,0]
test3 = [4,5,2,-1,-3,-3,4,6,-7]
test4 = [1,8,7,3,11,9]
test5 = [8,-5,0,-2,3,-4]
test6 = [1,-1,1,-1]

print("test1: ", ZeroSumSubArrays(test1))
print("test2: ", ZeroSumSubArrays(test2))
print("test3: ", ZeroSumSubArrays(test3))
print("test4: ", ZeroSumSubArrays(test4))
print("test5: ", ZeroSumSubArrays(test5))
print("test6: ", ZeroSumSubArrays(test6))

#time spent: 30 min