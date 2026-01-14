# Time complexity: O(n)
# Space complexity: O(n)
# 39 minutes

array1 = [1,10,8,3,2,5,7,2,-2,-1]
array2 = [1,10,8,-2,2,5,7,2,-2,-1]
array3 = [4,3,3,5,7,0,2,3,8,6]
array4 = [4,3,3,5,7,0,2,3,8,0]
array5 = [0,0,0,0]
array6 = [1,-1,1,-1]

def zero_sum(arr):
    occurences = dict() #space O(n)
    count = 0
    for i in range(len(arr)): #loop time O(n)
        occurences[arr[i]] = occurences.get(arr[i], 0) + 1 #get time O(1)
        if occurences.get(-arr[i], 0) > 0 and arr[i] != 0:
            count += 1
            occurences[-arr[i]] = occurences.get(-arr[i], 0) - 1
            occurences[arr[i]] = occurences.get(arr[i], 0) - 1
        elif arr[i] == 0 and occurences.get(0, 0) > 1:
            count += 1
            occurences[0] = occurences.get(0, 0) - 2
    return count

print(zero_sum(array1))
print(zero_sum(array2))
print(zero_sum(array3))
print(zero_sum(array4))
print(zero_sum(array5))
print(zero_sum(array6))

def zero_sum_updated(arr):
    occurences = dict()
    count = 0
    for i in range(len(arr)):
        occurences[arr[i]] = occurences.get(arr[i], 0) + 1
        if occurences.get(-arr[i], 0) > 0 and arr[i] != 0:
            count += 1*occurences.get(-arr[i], 0)
        elif arr[i] == 0 and occurences.get(0, 0) > 1:
            count += 1*(occurences.get(-arr[i], 0)-1)
    return count

print(zero_sum_updated(array1))
print(zero_sum_updated(array2))
print(zero_sum_updated(array3))
print(zero_sum_updated(array4))
print(zero_sum_updated(array5))
print(zero_sum_updated(array6))
