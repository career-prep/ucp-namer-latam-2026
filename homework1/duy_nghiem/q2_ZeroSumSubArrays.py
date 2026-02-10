"""
Technique: Hashing 1 directional running computation/total
Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
Problem:
array of int: nums
return the number of su barray that sum=0

ideas: i was thinking of using a prefix sum, we gonna store the prefix sum and its count inside the a hashmap:
we gonna track the prefix sum of the sub array running from 0->len(nums)-1 and store it inside a hashmap
if we see the prefix sum appear again while looping, it means that there must be a sub array with sum=0 between the process => count+=1

for example:
we got: nums= [4,5,2,-1,-3,-3,4,6,-7]
=> prefix sum = 4,9,11,10,7,4,8,14,7
"""
def zero_sum_sub_arrays(nums):
    total=0
    count=0
    hashmap={0:1} #before the loop start, the prefix_sum is already=0
    
    for i in range(len(nums)):
        total+= nums[i]

        prefix_sum=total - 0
        if prefix_sum in hashmap:
            count+=hashmap[prefix_sum]

        if total in hashmap:
            hashmap[total]+=1
        else:
            hashmap[total]=1
    return count

        

print(zero_sum_sub_arrays([4,5,2,-1,-3,-3,4,6,-7]))
print(zero_sum_sub_arrays([1,8,7,3,11,9]))
print(zero_sum_sub_arrays([8,-5,0,-2,3,-4]))
print(zero_sum_sub_arrays([8,-8,0,2]))





            

            
        


