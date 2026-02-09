def MaxMeanSubArray(nums, k):

    '''
    Growing Sliding Window

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    maximum= float("-inf")
    left,right= 0,0
    window_sum= 0

    if k<=0 or k>len(nums):
        return 0
    
    while right<len(nums):

        window_sum += nums[right]

        if right-left+1 == k:
            mean= window_sum/k

            maximum = max(mean, maximum)

            window_sum-=nums[left]
            left += 1

        right+=1
    return maximum


# nums=[4,5,-3,2,6,1]
# k=0
# Output= 0

# nums= [4,5,-3,2,6,1]
# k=2
# Output= 4.5

# print(MaxMeanSubArray(nums,k))

# Time taken: 30mins