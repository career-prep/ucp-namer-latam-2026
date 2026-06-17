def uniqueSum(nums):
    """
    convert to a set to remove duplicates
    sum the elements of the set 
    
    """
    return sum(set(nums))

ex1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
expected_ans1 = 33
print(uniqueSum(ex1) == expected_ans1)

ex2 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
expected_ans2 = 35
print(uniqueSum(ex2) == expected_ans2)

