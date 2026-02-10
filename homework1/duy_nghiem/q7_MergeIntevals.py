"""
Technique: Sorting algorithm
Time Complexity: O(nlog(n))
Space Complexity: O(n)
"""



"""
thinking of sorting the array first
[(2,3),(4,8),(1,2),(5,7),(9,12)]
=> [(1,2),(2,3),(4,8),(5,7),(9,12)];   (1,12),(4,13)

res= []
start_track= elem[0][0] 
end_track=elem[0][1]

we gonna loop through every single pair after the first pair:
we gonna check if the next pair can merge with the prev pair and next pair or not:
=> if match with the first pair: 

#REMEBER THEY ARE SORTED, DONT NEED TO CARE THE START

"""

            



"""
thinking of sorting the array first
[(2,3),(4,8),(1,2),(5,7),(9,12)]
=> [(1,2),(2,3),(4,8),(5,7),(9,12)]

take a simple example: (1,10),(2,11),(12,13)

we create a an array to store the valid interval

we gonna track the current interval, which will start with the first interval in the list which is (1,10)
    current_start=nums[0][0]
    current_end= nums[0][1]
    current_interval= nums[0]

we gonna loop through every interval until reaching the final one:

loop through all the interval:

there is gonna be 2 case:
1: 2 interval can be merge => nums[i][0] <= current_end.
after that, update the current interval to the merged interval

2: they cannot be merge => append the current interval and update the new current interval

=> after that, at the end, append the last interval to the arr (as when we loop through the last elem, we just update the current interval but never append to the arr)
"""

def merge_intervals(nums):
    if len(nums)==0:
        return []
    
    nums.sort()
    curr_start=nums[0][0]
    curr_end=nums[0][1]
    curr_interval= nums[0]
    merged_arr=[]

    for i in range(1,len(nums)):
        if nums[i][0] <= curr_end:
            curr_end = max(curr_end,nums[i][1])
            curr_interval=(curr_start,curr_end)
        else:
            merged_arr.append(curr_interval)
            curr_start=nums[i][0]
            curr_end=nums[i][1]
            curr_interval=nums[i]
    
    merged_arr.append(curr_interval)
    
    return merged_arr


print(merge_intervals([(2,3),(4,8),(1,2),(5,7),(9,12)]))
print(merge_intervals([(5,8),(6,10),(2,4),(3,6)]))
print(merge_intervals([(10,12),(5,6),(7,9),(1,3)]))







"""
[(2,3),(4,8),(1,2),(5,7),(9,12)]
=> [(1,2),(2,3),(4,8),(5,7),(9,12)]

def merge(nums):
    nums.sort()
    
    curr=nums[0]
    arr=[]

    for i in range(1,len(nums)):
        if nums[i][0] <= curr[1]:
            new_end=max(nums[i][1],curr[1])
            curr=(curr[0],new_end)
        else:
            arr.append(curr)
            curr=nums[i]
    
    arr.append(curr)
    return arr



"""



