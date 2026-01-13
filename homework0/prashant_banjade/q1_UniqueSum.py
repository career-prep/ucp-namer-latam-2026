# Question 2: UniqueSum
# Given an array of integers, return the sum of unique elements in the array.
# Examples:
# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, - 2, -1]
# Output: 33 (1+10+8+3+2+5+7+-2+-1)
# Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# Output: 35 (4+3+5+7+0+2+8+6)

def unique_sum(arr):
    sum = 0
    seen=set()
    for num in arr:
        if num not in seen:
            seen.add(num)
            sum += num 
    return sum 

print(unique_sum([1, 10, 8, 3, 2, 5, 7, 2, - 2, -1]))
print(unique_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))


# solved in 6 min