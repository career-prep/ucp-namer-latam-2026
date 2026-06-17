#binary search variation
#time complexity: O(log n) --> binary search yooooo
#space complexity: O(1)
#8 minutes

def missing_integer(arr, n):
    left, right = 0, n-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > mid + 1:
            right = mid
        else:
            left = mid + 1
    return left + 1

#test cases

array1 = [1, 2, 3, 4, 6, 7]
assert missing_integer(array1, 7) == 5

array2 = [1]
assert missing_integer(array2, 2) == 2

array3 = [1,2,3,4,5,6,7,8,10,11,12]
assert missing_integer(array3, 12) == 9

print("ya!!")