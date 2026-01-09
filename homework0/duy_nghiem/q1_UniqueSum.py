# Question 2: Unique Sum
# Given an int array => return the sum of unique elements in the array

# Approach:
# loop through every num in arr and put them in a set to make sure they are unique
# loop through every element in the set and add them up to find the total

# => Spend: 5 mins

# Implementation:

def unique_sum(arr):
    unique_set=set()
    total=0
    for num in arr:
        unique_set.add(num)

    for elem in unique_set:
        total+=elem
    
    return total

#test case:
print(unique_sum([1,10,8,3,2,5,7,2,-2,-1]))
print(unique_sum([4,3,3,5,7,0,2,3,8,6]))

