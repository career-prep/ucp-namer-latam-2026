# Given a number, k, return an array of the first k binary numbers, represented as strings.
# Examples:
# Input: 5  --> Output: ["0", "1", "10", "11", "100"]
# Input: 10 --> Output: ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"]
from collections import deque

def kbinary(num):
    if num==0:
        return []
    result=["0"]
    queue=deque(["1"])
    count=num
    while len(result)<num:
        val=queue.popleft()
        result.append(val)
        queue.append(val+'0')
        queue.append(val+'1')
    return result

print(kbinary(1))
print(kbinary(2))
print(kbinary(5))
print(kbinary(10))
print(kbinary(0))

#Time Complexity: O(n)
#Space Complexity: O(n)

#Spent 20 mins


#Notice from each values is the addition of i-1 + 0/1 
#This forms a dp problem
#DP honestly came into mind before using queues

def dp_kbinary(num):
    if num==0:
        return []
    if num==1:
        return ["0"]
    
    dp=["0"]*num
    dp[0],dp[1]="0","1"
    
    for i in range(2,num):
        if i%2==0:
            dp[i]=dp[i//2]+"0" 
        else:
            dp[i]=dp[i//2]+"1"
    
    return dp

print(dp_kbinary(1))
print(dp_kbinary(2))
print(dp_kbinary(5))
print(dp_kbinary(10))
print(dp_kbinary(0))


#Time Complexity: O(n)
#Space Complexity: O(n)