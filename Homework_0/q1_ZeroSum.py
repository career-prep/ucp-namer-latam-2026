# Given an array of integers, return the number of pairs of integers in the array that sum to 0, assuming you can use the element at each index at most once.

# Examples:

# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 2
# (Pairs: (1, -1), (2, -2))

# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
# Output: 3
# (Pairs: (1, -1), (2, -2), (2, -2))

def zero_sum(arr):
    seen={}
    count=0
    for num in arr:
        dif = 0 - num 
        
    
        if dif in seen and seen[dif] > 0:
            count += 1
            seen[dif] -= 1
        else:
            seen[num] = seen.get(num, 0) + 1
    
    return count
print(zero_sum([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))
print(zero_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))

#Time Complexity= O(n)
#Space Complexity= O(n)
#Spent 7 minutes




#Follow-Up Question: ZeroSum (Reuse Allowed)

#Now assume you can re-use elements in different pairs (i.e., the elements in a pair must be from different indices, but different pairs may use an element from the same index).

#Examples:

#Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
#Output: 3
#(Pairs: (1, -1), (2, -2), (2, -2))

#Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
#Output: 5
#(Pairs: (1, -1), (2, -2), (2, -2), (2, -2), (2, -2))

from collections import Counter

def zero_sum_reuse(arr):
    count = 0
    freq = Counter(arr)
    
    for num in freq:
        complement = -num
        
        if complement in freq:
            if num < complement:
                count += freq[num] * freq[complement]
            elif num == complement:
                n = freq[num]
                count += (n * (n - 1)) // 2
    
    return count

print(zero_sum_reuse([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))
print(zero_sum_reuse([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))

#Time Complexity= O(n)
#Space Complexity= O(n)
#Spent 20 minutes