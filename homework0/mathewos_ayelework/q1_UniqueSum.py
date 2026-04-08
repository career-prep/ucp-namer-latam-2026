# uniqueSum returns the sum of unique elements in the list
def uniqueSum(nums: list[int]) -> int:
    usedSet = set()
    result = 0 #made assumption of returning zero if nums is an empty list, could have been None
    for num in nums:
        if num not in usedSet:
            result += num
            usedSet.add(num)
    return result

print("uniqueSum Results:")
test_cases = [[1,10,8,3,2,5,7,2,-2,-1], [1,10,8,-2,2,5,7,2,-2,-1],[1,1,1], [3],[],[1,-1,-1,-1]]
for test_case in test_cases:
    print(uniqueSum(test_case)) # Expected Output: 33,30,1,3,0,0
 
# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 3 minutes