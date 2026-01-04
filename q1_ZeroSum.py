# Given an array of integers, return the number of pairs of integers in the array that sum to 0, assuming you can use the element at each index at most once.

# Examples:

# Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
# Output: 2
# (Pairs: (1, -1), (2, -2))

# Input Array: [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
# Output: 3
# (Pairs: (1, -1), (2, -2), (2, -2))

def sum_to_zero(arr):
    seen={}
    count=0
    for i,num in enumerate(arr):
        dif=0-num
        if dif in seen:
            count+=1
        else:
            seen[num]=i
    return count
print(sum_to_zero([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))
print(sum_to_zero([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))

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

def sum_to_zero(arr):
    count = 0
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num in freq:
        complement = -num
        if complement in freq:
            if num < complement:
                count += freq[num] * freq[complement]
            elif num == complement:
                count += freq[num] // 2
    
    return count

print(sum_to_zero([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))
print(sum_to_zero([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))

#Time Complexity= O(n)
#Space Complexity= O(n)
#Spent 20 minutes