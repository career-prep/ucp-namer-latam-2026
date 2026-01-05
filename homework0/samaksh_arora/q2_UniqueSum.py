#Samaksh Arora
#UniqueSum
#Time Complexity: O(n)
#Space Complexity: O(n)


def uniqueSum(nums):
    nums = set(nums)
    sum = 0
    for num in nums:
        sum+= num
    return sum

testNums = [1,10,8,3,2,5,7,2,-2,-1]
print(uniqueSum(testNums)) #output = 33

testNums2 = [4,3,3,5,7,0,2,3,8,6]
print(uniqueSum(testNums2)) #output = 35


#Time Spent: 5 minutes