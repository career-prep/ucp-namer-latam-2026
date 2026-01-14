#Time Complexity: O(n)
#Space Complexity: O(n)

def UniqueSum(numbers):
    s = set(numbers)
    sum = 0
    for num in s:
        sum+=num
    return sum

#Test Case 1
print(UniqueSum([1,10,8,3,2,5,7,2,-2,-1]) == 33)
#Test Case 2
print(UniqueSum([4,3,3,5,7,0,2,3,8,6]) == 35)

#Spent 4 minutes