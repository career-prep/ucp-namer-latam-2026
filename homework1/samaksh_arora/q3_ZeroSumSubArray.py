#Samaksh Arora
#ZeroSumSubArray
#Time Complexity: O(n)
#Space Complexity: O(n)
#Hash Maps
def ZeroSumSubArray(nums):
    
    sum_frequency = {0 : 1}
    sum = 0
    count = 0
    for num in nums:
        sum += num
        sum_frequency[sum] = sum_frequency.get(sum,0) + 1

    for sum, freq in sum_frequency.items():
        if freq>1:
            count += (freq*(freq-1))//2
    
    return count

test = [4,5,2,-1,-3,-3,4,6,-7]
print (ZeroSumSubArray(test)) #output= 2

test = [1,8,7,3,11,9]
print (ZeroSumSubArray(test)) #output = 0

#Time spent: >40 minutes

    
        

