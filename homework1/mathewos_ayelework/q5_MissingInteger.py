# Technique used: Binary Search
# finds the missing integer in a list that goes from 1 to n-1
def missingInteger(nums: list[int], n: int) -> int:
    # exception handling when last or first index is the missing number
    if nums[0] != 1:
        return 1
    elif nums[-1] != n:
        return n
    elif len(nums) == 2:
        return nums[0] + 1
    
    l = 0
    r = n - 2

    while l < r - 1:
        m = (l + r) // 2
        lCount = m - l
        rCount = r - m
        if lCount < (nums[m] - nums[l]):
            r = m
        elif rCount < (nums[r] - nums[m]):
            l = m

    return nums[l] + 1


print("missingInteger Results:")
test_cases = [
                [[1,2,3,4,6,7],7],
                [[1],2],
                [[1,2,3,4,5,6,7,8,10,11,12],12],
                [[2,3,4,5,6,7],7],
                [[2,3],3],
                [[1,2],3],
              ]
for test_case in test_cases:
    print(missingInteger(test_case[0], test_case[1])) #Expected Output: 5,2,9,1,1,3

# Time Complexity: O(logn)
# Space Complexity: O(1)
# Time Taken: 38mins