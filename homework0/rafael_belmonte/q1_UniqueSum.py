#Time complexity: O(n)
#Space complexity: O(n)

array1 = [1,10,8,3,2,5,7,2,-2,-1]
array2 = [4,3,3,5,7,0,2,3,8,6]

def unique_sum(arr):
    ocurrences = dict()
    total_sum = 0
    for i in range(len(arr)):
        ocurrences[arr[i]] = ocurrences.get(arr[i], 0) + 1
        if ocurrences.get(arr[i]) == 1:
            total_sum += arr[i]
        else:
            continue
    return total_sum

print(unique_sum(array1))
print(unique_sum(array2))

#9 minutes