#Time complexity: O(n)
#Space complexity: O(n)
#9 minutes

array1 = [1,10,8,3,2,5,7,2,-2,-1]
array2 = [4,3,3,5,7,0,2,3,8,6]

def unique_sum(arr):
    ocurrences = set() #space O(n)
    total_sum = 0
    for num in arr: #loop time O(n)
        if num not in ocurrences:
            ocurrences.add(num) #add time O(1)
            total_sum += num
        else:
            continue
    return total_sum

print(unique_sum(array1))
print(unique_sum(array2))
