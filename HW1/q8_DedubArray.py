"""
Technique: Reset/catch up 2 pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""


"""
Problem:
sorted array of non-negative num: nums
modify array (not make a new one) by removing all duplicate, make each elem appear once, the rest of it could be replaced by -1

[1,2,2,3,3,3,4,4,4,4]

USING: RESET/CATCH UP 2 PTR

since the first character is always unique, we gonna set the left ptr at the second char to track idx of next unique elem:
l= 1

run the right ptr from 1-> len(nums)-1
if we see that the right ptr is diff from left ltr =>
we swap change left ptr to the value that right ptr points to
update the left ptr by 1 to track the position of next unique number


"""

def dedup_array(nums):
    if len(nums)==0:
        return nums
    
    l=1 

    for r in range(1,len(nums)):
        if nums[r]!=nums[r-1]:
            nums[l]= nums[r]
            l+=1
    
    
    return nums[0:l]

print(dedup_array([1,2,2,3,3,3,4,4,4,4]))
print(dedup_array([0,0,1,4,5,5,5,8,9,9,10,11,15,15]))
print(dedup_array([1,3,4,8,10,12]))

    
