# Question 6: MissingInteger
# Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.
# Examples:
# Input Array: [1, 2, 3, 4, 6, 7]
# Input n: 7
# Output: 5
# Input Array: [1]
# Input n: 2
# Output: 2
# Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
# Input n: 12
# Output: 9


# o(n) compexity- time 10 min - just comparing the total count of number and finding the missing one
# def missinginteger(arr, n):
#     for i in range(len(arr)):
#         if arr[i] != i+1:
#             return i+1
#     return n
# print(missinginteger([1, 2, 3, 4, 6, 7],7))


# time complexity- o(N), time taken- 30 mins, 
def missinginteger(arr, n):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1

    return left + 1
print(missinginteger([1, 2, 3, 4, 6, 7],7))


