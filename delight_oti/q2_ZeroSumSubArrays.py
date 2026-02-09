def ZeroSumSubArrays(nums):
    '''
    one directional computation

    Time Complexity: O(n)
    Space Complexity: O(1)
    '''

    sum=0
    freq={0:1}
    count=0

    for num in nums:

        sum += num

        if num in freq:
            count+= freq[num]
        else:
            freq[num] = 1
    return count

# nums=[4,5,2,-1,-3,-3,4,6,-7]
# Output= 2

# nums=[1,8,7,3,11,9]
# Output=0

# print(ZeroSumSubArrays(nums))

# Time taken: 40mins
