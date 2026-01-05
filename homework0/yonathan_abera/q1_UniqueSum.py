#Return sum of unqiue items
#O(n) time and O(n) space complexity
def uniqueSum(nums):
    unique = set()
    sums = 0
    for numbers in nums:
        unique.add(numbers)
    for uniques in unique:
        sums += uniques

    return sums

print(uniqueSum([1,10,8,3,2,5,7,2,-2,-1]))

#3 minutes