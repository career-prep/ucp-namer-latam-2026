# Question 1 (MaxMean Subarray)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time spent: 21 mins


def MaxMean(arr, k):
    window_sum = sum(arr[:k])
    max_mean = window_sum/k

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]

        current_mean = window_sum/k

        max_mean = max(max_mean,current_mean)

    return max_mean

# Q1 Tests
print(MaxMean([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))  # expected: 0.8
print(MaxMean([5, 5, 5, 5], 2))                      # expected: 5.0
print(MaxMean([-1, -2, -3, -4], 2))                  # expected: -1.5
print(MaxMean([1, 2, 3, 4, 5], 1))                   # expected: 5.0
