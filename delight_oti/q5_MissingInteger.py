def MissingInteger(nums):

    '''
    Binary search variation
    Time Complexity: O(log n)
    Space Complexity: O(1)
    '''

    left=0
    right=len(nums)-1

    while left<=right:
        
        mid = (left+right)//2

        if nums[mid] == mid+1:
            # good
            left= mid+1
        else:
            # what is missing is here or to the left of this
            right= mid-1

    return left+1

# Time taken: 22mins

# arr = [1,2,3,4,6,7]
# n=7
# output = 5

# arr= [1]
# n=2
# output = 9
# print(MissingInteger(arr,n))