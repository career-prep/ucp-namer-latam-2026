# Two Pointer
# O(n) Time Complexity
# O(1) Space Complexity


arr1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
arr2 = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
arr3 = [1, 3, 4, 8, 10, 12]

def DedupArray(nums):

    if len(nums) == 1:
        return nums

    l = 0 # Keeps track of last unique element
          # New place to swap into is always gonna be l + 1

    r = 1 # Scanner

    while r < len(nums):

        # Find new element
        while r < len(nums) and nums[r] == nums[l]:
            r += 1

        # In case r gets out of bounds (no more unseen elements)
        if r >= len(nums):
            break


        # Now r is at a new unique element
        # Only swap if r is more than 1 index away
        if r != l+1:
            temp = nums[l+1]
            nums[l+1] = nums[r]
            nums[r] = temp

        # Continue Scanning
        l += 1
        r += 1 

    # l is on the last unique element
    return nums[:l+1]
    

print(DedupArray(arr1))
print(DedupArray(arr2))
print(DedupArray(arr3))

# 38 minutes
