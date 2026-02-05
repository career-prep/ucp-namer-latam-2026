#Samaksh Arora
#ZeroSum
#Time Complexity: O(n)
#Space Complexity: O(n)


def ZeroSum(nums):
    pairs = {}
    result = 0

    for num in nums:
        if -num in pairs:
            result += 1
        else:
            pairs[num] = 1
    
    return result

test = [1,10,8,3,2,5,7,2,-2,-1]
print(ZeroSum(test)) #output: 2

test = [1,10,8,-2,2,5,7,2,-2,-1]
print(ZeroSum(test)) #output: 3

test = [4,3,3,5,7,0,2,3,8,6]
print(ZeroSum(test)) #output: 0
        
test = [4,3,3,5,7,0,2,3,8,0]
print(ZeroSum(test)) #output: 1

#Time Spent: 30 minutes
    

#Zero Sum Follow up
#Time Complexity: O(n)
#Space Complexity: O(n)
#Time Spent: 35 minutes

def ZeroSum_FollowUp(nums):
    pairs = {}
    result = 0

    for num in nums:
        if num in pairs:
            pairs[num] += 1
        else:
            pairs[num] = 1
    
    for val in pairs:
        if -val in pairs:
            if val > -val:
                result += pairs[val] * pairs[-val]
            elif val == 0:
                result += pairs[val] * (pairs[val] - 1) // 2
     
    return result

  

test = [1,10,8,3,2,5,7,2,-2,-1]
print(ZeroSum_FollowUp(test)) #output: 3

test = [1,10,8,-2,2,5,7,2,-2,-1]
print(ZeroSum_FollowUp(test)) #output: 5

test = [4,3,3,5,7,0,2,3,8,6]
print(ZeroSum_FollowUp(test)) #output: 0
        
test = [4,3,3,5,7,0,2,3,8,0]
print(ZeroSum_FollowUp(test)) #output: 1