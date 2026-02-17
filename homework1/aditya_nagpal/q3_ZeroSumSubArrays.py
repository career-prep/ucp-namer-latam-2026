#given: 
## an ARRAY of INTEGERS

#todo:
## count the number of subarray euqal to 0.

#Solution:
def ZeroSum(arr):
    i = 0
    count = 0

    for num in arr:
        if num == 0:
            count = count +1

    while(i < len(arr)):
        for j in range(i+1, len(arr)):
            if sum(arr[i:j+1]) == 0:
                count = count + 1
        i = i + 1

    return count

print(ZeroSum([4, 5, 2, -1, -3, -3, 4, 6, -7]))
print(ZeroSum([1, 8, 7, 3, 11, 9]))
print(ZeroSum([8, -5, 0, -2, 3, -4]))
