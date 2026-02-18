#Samaksh Arora
#DeDupArray
#Time Complexity: O(n)
#Space Complexity: O(n)
#Hash Sets

def DeDupArray(nums):
    
    nums = set(nums)
    nums = list(nums)
    return nums


test = [1,2,2,3,3,3,4,4,4,4]
print(DeDupArray(test)) #output: [1,2,3,4]

test = [1,3,4,8,10,12]
print(DeDupArray(test)) #output: [1,3,4,8,10,12]

#Time Spent: 1 minute