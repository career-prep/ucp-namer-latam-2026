def UniqueSum(nums):
    '''
    Understanding: Given the array, return a sum of unique elements

    Plan:
    create a variable sum
    create a set to track seen numbers

    iterate over the array
        if the number is not in set:
            add it to set
            sum+=number
    return sum
    '''

    sum=0
    seen=set()

    for num in nums:
        if num not in seen:
            seen.add(num)
            sum+=num
    return sum

# Testcase1
# arr=[1,5,3,2,5,7,9]
# # Output= 27

# Testcase2
# arr=[1,5,-1,3,6,7]
# # Output= 21
