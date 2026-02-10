#Time Taken: 10mins
#concept used: two distinct stacks
#Time complexity: O(n2) and space complexity: O(n)

#given: 
    ##SORTED ARRAY of non negative INTEGERS
   
#todo:
##  remove duplicates
##  and for each removed duplicate add -1 to the array

# implementation:

# algo:
 ## initially I thought we can just convert it into set 
 ## but we need -1 for removed duplicate so cant do that

# another approach:
# using stacks, the array is already sorted 

def DedupArray(arr):
    stack_num = []
    stack_dup = []
    for num in arr:
      if num not in stack_num:
        stack_num.append(num)
      else:
        stack_dup.append(-1)
    
    return stack_num + stack_dup

print(DedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4 ,4]))
print(DedupArray([1, 3, 4, 8, 10, 12]))