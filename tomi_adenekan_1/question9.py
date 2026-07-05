"""
Two pointer
40 minutes
time complexity = O(n)
space complexity = O(1)
Linear search Technique 
"""

def array(nums):
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i += 1
            

    return nums[:i]



lst = [1,2,2,3,3,3,4,4,4,4]

print(array(lst))
