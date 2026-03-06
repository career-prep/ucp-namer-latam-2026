"""

inputArr = [4, 5, 3, 7, 4, 2, 3, 8, 7, 1, 5, 3], k= 2
Output = 0


inputArr = [4, 5, 3, 7, 4, 2, 3, 8, 7, 1, 5, 3], k= 5
Output = 2,

we are given an array, k is the size of the sub-array, return the number of subarray that have duplicate

i was thinking of using fixed slide sliding window
check the first window
then move it to the right, keep checking duplicate with the hashmap
if there is a dup => count +=1

the logic to check duplicate:
create a dummy var named "dup" to track if there is duplicate, if yes, then increase it by 1 for each pair of dup value
at the end of every window, if the dup>0 => then there exists duplicate in the window => count+=1

"""
def dup_in_sub(nums,k):
    count=0
    hashmap={}
    dup=0

    #check the duplicate in the initial window 
    for i in range(k):
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
            if hashmap[nums[i]]==2:
                dup+=1
        else:
            hashmap[nums[i]]=1
    
    # if there exists at least 1 pair of dup => the window contains dup var
    if dup>0:
        count+=1
    
    l=0
    
    for r in range(k,len(nums)):
        #check if the value that the left ptr used to point to still have dup or not
        hashmap[nums[l]]-=1
        if hashmap[nums[l]]==1:
            dup-=1
        l+=1
        
        #check if the value that the new right ptr point to have dup or not
        if nums[r] in hashmap:
            hashmap[nums[r]]+=1
            if hashmap[nums[r]]==2:
                dup+=1
        else:
            hashmap[nums[r]]=1
        
        if dup>0:
            count+=1
    
    return count
    

print(dup_in_sub([4, 5, 3, 7, 4, 2, 3, 8, 7, 1, 5, 3],2))
print(dup_in_sub([4, 5, 3, 7, 4, 2, 3, 8, 7, 1, 5, 3],5))
print(dup_in_sub([1,1,2,2],4))
print(dup_in_sub([1,0,2,2],4))
print(dup_in_sub([1,2,3,4,5],2))
print(dup_in_sub([4,5,3,7,4,2,3,8,7,1,5,3],5))



    

