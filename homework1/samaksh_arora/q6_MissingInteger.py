#Samaksh Arora
#MissingInteger
#Time Complexity: O(log(n))
#Space Complexity: O(1)
#Binary search variation

def MissingInteger(nums, n):
    low = 0
    high = n-2
    mid = (low + high) // 2
   
    while low < high:
        if nums[mid] == mid+1:
            low = mid + 1
            mid = (low + high) // 2
        else:
            high = mid 
            mid = (low + high) // 2
    
    if nums[mid] == mid+1:
        return nums[mid] + 1
        
    return low + 1

test = [1,2,3,4,6,7]
print(MissingInteger(test, 7)) #output = 5

test = [1,2,3,4,5,6,7,8,10,12]
print(MissingInteger(test, 12)) #output = 9

#Time Spent: 25 minutes