"""
Technique: Binary Search 
Time Complexity: O(log(n))
Space Complexity: O(1)
"""

#OPTIMIZED:
# since the array is sorted and we need to find a missed int => binary search
# we gonna use 2 ptr => l=0, r=len(arr)-1

# we gonna loop until 2 ptr meet each other:
#mid = (r+l)//2
# if mid = idx+1 => it means that mid and the rest on the left of mid is in the correct order => l=mid+1
# if mid != idx+1 => we need to move to the left to find the closest element that have the correct order  => r=mid-1

# that element +1 will be the missing int

def missing_integer_optimized(nums,n):
    l=0
    r=n-2

    while l<=r:
        mid = (l+r)//2
        if nums[mid] == mid+1:
            l=mid+1
        else:
            r=mid-1
    
    missing_int=l+1

    return missing_int


print(missing_integer_optimized([1,2,3,4,6,7],7))
print(missing_integer_optimized([1],2))
print(missing_integer_optimized([1,2,3,4,5,6,7,8,10,11,12],12))



    


    

