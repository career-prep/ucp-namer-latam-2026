def uniqueSum(nums):
    usedSet = set()
    result = 0 #made assumption of returning zero if nums is an empty list, could have been None
    for num in nums:
        if num not in usedSet:
            result += num
            usedSet.add(num)
    return result

nums = [4,3,3,5,7,0,2,3,8,6]
print(uniqueSum(nums))

# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 3 minutes