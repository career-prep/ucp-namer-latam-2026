# Question 1: Zero Sum
# given an array of integers, return whether there are two numbers that sum to zero
# element at each index may be used only once

# Approach:
# use a hashmap to store the occurrences of each number
# iterate through the array and check if diff=0-num exists in the hashmap
# if it exists, count+=1 and hashmap[diff]-=1 and hashmap[num]-=1
# if num is 0, count += hashmap[num]//2

# => Spend: 40 mins

# Implementation:

def zero_sum(arr):
    count=0
    hash_map={}

    for num in arr:
        if num in hash_map:
            hash_map[num]+=1
        else:
            hash_map[num]=1
    
    for elem in arr:
        diff= 0-elem

        if diff in hash_map and hash_map[diff]>0 and hash_map[elem]>0 and diff != elem:
            count+=1
            hash_map[diff]-=1
            hash_map[elem]-=1

        if elem==0 and hash_map[elem]>1:
            count+=hash_map[elem]//2
            hash_map[elem]=0

    return count 

# test cases
print(zero_sum([1,10,8,3,2,5,7,2,-2,-1])) 
print(zero_sum([1,10,8,-2,2,5,7,2,-2,-1]))
print(zero_sum([4,3,3,5,7,0,2,3,8,6]))
print(zero_sum([4,3,3,5,7,0,2,3,8,0]))

# Follow-up:
# Assume we can reuse elements in different pairs

# Approach:
# iterate through every num in arr
# if diff=0-num in array => count+=hash_map[diff]
# if not, track the number of occurrences of num

# => Spend: 30 mins

# Implementation:

def zero_sum_element_reused(arr):
    count=0
    hash_map={}

    for num in arr:
        diff= 0-num
        if diff in hash_map:
            count+=hash_map[diff]
        if num in hash_map:
            hash_map[num]+=1
        else:
            hash_map[num]=1
    return count


# test cases
print(zero_sum_element_reused([1,10,8,3,2,5,7,2,-2,-1]))
print(zero_sum_element_reused([1,10,8,-2,2,5,7,2,-2,-1]))
print(zero_sum_element_reused([4,3,3,5,7,0,2,3,8,6]))
print(zero_sum_element_reused([4,3,3,5,7,0,2,3,8,0]))





