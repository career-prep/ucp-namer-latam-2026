#Time Complexity: O(n)
#Space Complexity: O(n)

def zero_sum(arr) -> int:
    count = 0
    my_map = {}

    for num in arr:
        complement = -num
        if complement in my_map:
            count += 1
        else:
            my_map[num] = my_map.get(num, 0) + 1
    
    return count


test_case1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
#Output: 2

test_case2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
#Output: 3

test_case3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
#Output: 0

test_case4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
#Output: 1

#print(zero_sum(test_case1))
#print(zero_sum(test_case2))
#print(zero_sum(test_case3))
#print(zero_sum(test_case4))

def zero_sum_follow_up(arr) -> int:
    count = 0
    my_map = {}

    for num in arr:
        complement = -num

        if complement in my_map:
            count += my_map.get(complement, 0)
        
        my_map[num] = my_map.get(num, 0) + 1
    
    return count


test_case5 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
#Output: 3

test_case6 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
#Output: 5

test_case7 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
#Output: 0

test_case8 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
#Output: 1

print(zero_sum_follow_up(test_case5))
print(zero_sum_follow_up(test_case6))
print(zero_sum_follow_up(test_case7))
print(zero_sum_follow_up(test_case8))

#Time spent on zero_sum: 20 minutes
#Time spent on zero_sum_follow_up: 16 minutes
#Total time spent: 36 minutes