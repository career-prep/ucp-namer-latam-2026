# Binary Search Variation
# O(log(n)) Time complexity
# O(1) Space Complexity

arr1 = [1, 2, 3, 4, 6, 7]
n1 = 7

arr2 = [1]
n2 = 2

arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
n3 = 12


def MissingInteger(nums, n):

    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] == mid + 1:
            l = mid + 1
        elif nums[mid] > mid + 1:
            r = mid - 1

    return l+1

print(MissingInteger(arr1, n1))
print(MissingInteger(arr2, n2))
print(MissingInteger(arr3, n3))


# 27 minutes