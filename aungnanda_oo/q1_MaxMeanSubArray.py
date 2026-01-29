# Question 1: MaxMeanSubArray

# Given an array of integers and an integer, k, find the maximum mean of a subarray of size k.

# Examples:

# Input Array: [4, 5, -3, 2, 6, 1] # (6-2) + 1 = 4+1 = 5
# Input k = 2
# Output: 4.5

# Input Array: [4, 5, -3, 2, 6, 1]
# Input k = 3
# Output: 3

# Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1]
# Input k = 3
# Output: 1

# Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
# Input k = 5
# Output: 1

# Brute Force Solu
def MaxMeanSubArray_1(array,k) -> float:
    maximum_mean = float("-inf")
    for i in range(len(array)-k+1):
        sub_mean = sum(array[i:i+k]) / k
        maximum_mean = max(maximum_mean, sub_mean)
    return maximum_mean


# Optimal Solu
def MaxMeanSubArray_2(array,k) -> float:
    l = 0
    window_sum = 0
    maximum_mean = float("-inf")

    for r in range(len(array)):
        window_sum += array[r]

        if (r-l+1) == k:
            maximum_mean = max(maximum_mean, window_sum / k)

            window_sum -= array[l]
            l+=1
    return maximum_mean

test_cases = [([4, 5, -3, 2, 6, 1], 2), ([4, 5, -3, 2, 6, 1], 3), ([1, 1, 1, 1, -1, -1, 2, -1, -1], 3), ([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5)]

print("Brute Force Solu Output")
for test_case in test_cases:
    array, k = test_case
    print(MaxMeanSubArray_1(array, k))

# Time Complexity = O(n * k)
# Space Complexity = O(1)


print("Optimal Solu Output")
for test_case in test_cases:
    array, k = test_case
    print(MaxMeanSubArray_2(array, k))


# Time Complexity = O(n)
# Space Complexity = O(1)

# Spent a total of 20 mins on this question