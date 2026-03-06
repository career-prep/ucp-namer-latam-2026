def MaxMeanSubArray(nums, k):

    '''
    Growing Sliding Window

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''
    maximum = float("-inf")
    l, r = 0,0
    window_sum = 0

    if k <= 0 or k > len(nums):
        return 0
    
    N = len(nums)

    while r < N:

        window_sum += nums[r]

        if r - l + 1 == k:
            mean = window_sum/k

            maximum = max(mean, maximum)

            window_sum -= nums[l]
            l += 1

        r += 1
    return maximum


# nums=[4,5,-3,2,6,1]
# k=0
# Output= 0

# nums= [4,5,-3,2,6,1]
# k=2
# Output= 4.5

# print(MaxMeanSubArray(nums,k))

# Time taken: 30mins