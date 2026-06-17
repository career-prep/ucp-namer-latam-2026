# Technique: Hashmap
# Runtime: O(n)
# Space complexity: O(n)

def MissingInteger(nums, n):
    hm = dict.fromkeys(nums)
    for x in range(nums[0], n+1):
        if x not in hm:
            return x

# Technique: Binary search variation
# Runtime: O(logn)
# Space complexity: O(1)
def MissingInteger(nums, n):
    #[1,2,3,4,5,6,7]
    #[1,2,3,4,6,7]
    #[1,3,4,5,6,7]
    left, right = 0, n - 2

    while left <= right:
        mid = (left + right) // 2
        expected = nums[0] + mid
        if nums[mid] == expected:
            left = mid + 1
        else:
            right = mid - 1
    return nums[0] + left


print(MissingInteger([1,2,3,4,6,7], 7) == 5)
print(MissingInteger([1], 2) == 2)
print(MissingInteger([1,2,3,4,5,6,7,8,10,11,12], 12) == 9)



# Time spent: 24:50
