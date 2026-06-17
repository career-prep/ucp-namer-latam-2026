from collections import Counter
def zero_sum(numbers):
    """
    - use Counter to track how many unused values remain
    - special case: zeros can only pair with zeros -> floor(count[0]/2)
    - for nonzero num, form a pair (num, -num) whenever both still have unused 
    values -> each time pairing, we decrement both counts so no element is reused
    """
    count = Counter(numbers) 
    ans = 0
    ans += count[0] // 2

    for num in numbers: 
        if num != 0 and count[num] > 0 and count[-num] > 0:
            ans += 1
            count[num] -= 1
            count[-num] -= 1
    
    return ans 

ex1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
expected_ans1 = 2
print(zero_sum(ex1) == expected_ans1)

ex2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
expected_ans2 = 3
print(zero_sum(ex2) == expected_ans2)

ex3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
expected_ans3 = 0
print(zero_sum(ex3) == expected_ans3)

ex4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
expected_ans4 = 1
print(zero_sum(ex4) == expected_ans4)