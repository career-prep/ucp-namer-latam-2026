#given an array of INT
# return the number of pairs whos sum is 0.

def zerSum(arr, target):
    empty_set = set()
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                empty_set.add(arr[i])
                
    return len(empty_set)

print(zerSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 0))
print(zerSum([1, 10, 8, -2, 2, 5, 7, 2, -2, -1], 0))  
print(zerSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 0))

#assume you can re-use the elemnets

def zeroSum(arr, target):
    count =0
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                count+=1
                
    return count

print(zeroSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 0))
print(zeroSum([1, 10, 8, -2, 2, 5, 7, 2, -2, -1], 0))  
print(zeroSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 0))