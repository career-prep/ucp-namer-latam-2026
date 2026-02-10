# Tecnique used: Variable size Sliding Window
# counts all subarrays whose elements sum to 0 and returns the amount of subarrays which satisfy that property
def zeroSumSubArray(nums: list[int]) -> int:
    # iterate through the list
    result = 0
    for i in range(len(nums)):
        currVal = 0
        for j in range(i, len(nums)):
            currVal += nums[j]
            if currVal == 0:
                result += 1
    return result   

print("zeroSumSubArray Results:")
test_cases = [
            [4,5,2,-1,-3,-3,4,6,-7],
            [1,8,7,3,11,9],
            [8,-5,0,-2,3,-4],
            [],
            [0],
            [0,0]
              ]
for test_case in test_cases:
    print(zeroSumSubArray(test_case)) #Expected Output: 2,0,2,0,1,3 

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Time Taken: 17 mins
# Couldn't find optimal solution