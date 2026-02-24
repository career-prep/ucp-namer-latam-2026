#time complexity: O(logn)
#space complexity: O(1)

def MissingInteger(n, nums):
    left = 0
    right = len(nums)-1

    #returns 1 if list is empty
    if not nums:
        return 1

    #binary search for missing element
    while left < right:
        mid = left + int((right-left)/2)

        #if element in middle is greater than expected, update right pointer
        if nums[0] + mid < nums[mid]:
            right = mid 
        else:
            left = mid + 1
    
    #assumes that if all elements are consecutive, the missing element is the next number
    if nums[left] == nums[0] + left:
        return nums[left] + 1
    return nums[0] + left

test1 = 6
array1 = [1,2,3,4,6]
test2 = 0
array2 = []
test3 = 7
array3 = [3,5,6,7,8,9]
test4 = 2
array4 = [1]
test5 = 5
array5 = [2,3,4,5]

print('test1: ', MissingInteger(test1, array1))
print('test2: ', MissingInteger(test2, array2))
print('test3: ', MissingInteger(test3, array3))
print('test4: ', MissingInteger(test4, array4))
print('test5: ', MissingInteger(test5, array5))

#time spent: 30 mins