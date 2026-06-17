# Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once. If arrays are static (aka, not 
# dynamic/resizable) in your language of choice, the remaining elements should appear in the left-hand side of the array and the extra space in the right-hand 
# side should be padded with -1s.

# Examples:

# Input Array: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# Modified Array: [1, 2, 3, 4]
# or [1, 2, 3, 4, -1, -1, -1, -1, -1, -1] (depending on language)

# Input Array: [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
# Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15]
# or [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

# Input Array: [1, 3, 4, 8, 10, 12]
# Modified Array: [1, 3, 4, 8, 10, 12]

def dedup_array(arr):
    seen=[]
    for nums in arr:
        if nums in seen:
            continue
        else:
            seen.append(nums)
    return seen
print(dedup_array([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))
print(dedup_array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
print(dedup_array([1, 3, 4, 8, 10, 12]))
print(dedup_array([5, 5, 5, 5, 5]))
print(dedup_array([1]))
print(dedup_array([]))
print(dedup_array([0, 0, 0, 1, 1, 1, 2, 2, 2]))
print(dedup_array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))

#Can use return set(arr) but the questions return a list hence this solution 


#Time Complexity: O(n)
#Space Complexity: O(n^2)
#Spent 4 mins