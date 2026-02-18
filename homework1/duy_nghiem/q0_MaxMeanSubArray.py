"""
Technique: Fixed-size sliding window
Time Complexity: O(n)
Space Complexity: O(1)
"""


# Problems:
# array of int: nums
# int : k
# find the maximum mean of subarray of size k
"""
Example:
nums= [4,5,-3,2,6,1]
k = 2
=> output: res= 4.5 since (4+5)/2 = 4.5 is the largest

nums= [4,5,-3,2,6,1]
k= 3
=> output: res= 3 since (2+6+1)/3 = 3 is the largest
"""

#approach:
# Since we want to find the mean of a sub array with a fixed size of k => we could use fixed-size sliding window 
# l=0 => represent the left limit

# next, we gonna loop through the first window and track their sum 
# => since we have not loop through any other window, we consider it to be the max_sub_arr

# loop the right ptr from k -> len(nums)-1 to find the sum of other window 
# since the size is fixed => it have to subtract the value in left ptr and add the value in the right ptr to create a new window (imagine shifting a fixed window to the right)

#while looping and find the total of elem in the window, keep comapring it with the max_sub_arr to find the one with largest value
#after every loop, we gonna move left ptr by 1 so that it can maintain a fixed size window

#=> BASICALLY FINDING MAX_SUB_ARRAY BUT WITH FIXED SIZE AND WHEN RETURN, WE GONNA RETURN TOTAL/K
def max_mean_sub_array(nums,k):
    l=0
    sub_arr_total = 0

    for i in range(k):
        sub_arr_total+=nums[i]
    
    max_sub_array = sub_arr_total

    for r in range(k,len(nums)):
        sub_arr_total-=nums[l]
        sub_arr_total+=nums[r]
        max_sub_array=max(max_sub_array,sub_arr_total)
        l+=1
    
    return max_sub_array/k


print(max_mean_sub_array([4,5,-3,2,6,1],2))
print(max_mean_sub_array([4,5,-3,2,6,1],3))
print(max_mean_sub_array([1,1,1,1,-1,-1,2,-1,-1],3))
print(max_mean_sub_array([1,1,1,1,-1,-1,2,-1,-1,6],5))








