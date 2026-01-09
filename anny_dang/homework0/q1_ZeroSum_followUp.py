from collections import Counter
def zero_sum2(nums):
    """
    use Counter to count how many times each number appears 
    for zeros -> use combination formula to calculate it 
    iterate through each element 
    if number > 0 -> increase ans by multiplying the counts
    
    """
    count = Counter(nums)
    ans = 0
    ans += count[0] * (count[0] - 1) // 2
    for num in count:
        if num > 0:
            ans += count[num]*count[-num]
    
    return ans 

ex1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
expected_ans1 = 3
print(zero_sum2(ex1) == expected_ans1)

ex2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
expected_ans2 = 5
print(zero_sum2(ex2) == expected_ans2)

ex3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
expected_ans3 = 0
print(zero_sum2(ex3) == expected_ans3)

ex4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
expected_ans4 = 1
print(zero_sum2(ex4) == expected_ans4)