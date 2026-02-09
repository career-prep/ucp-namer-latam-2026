def DedupArray(nums):

    '''
    reset two pointer

    Space Complexity: O(1)
    Time Complexity: O(n) 
    '''

    left=1

    for right in range(1,len(nums)):
        if nums[right]!=nums[right-1]:
            nums[left] = nums[right]
            left+=1
        
    for i in range(left,len(nums)):
        nums[i]=-1
    
    return nums

# Time taken: 20mins

# nums=[1,2,2,3,3,3,4,4,4,4]
# output: 1, 2, 3, 4, -1, -1, -1, -1, -1, -1]

# nums=[5,5,5,5]
# output=[5,-1,-1,-1]
# print(DedupArray(nums))