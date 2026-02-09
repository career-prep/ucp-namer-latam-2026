#Technique: Fixed size sliding window
#Time Complexity: O(n)
#Space Complexity: O(1)

def maxmeanSubArray(arr, k):
    curr_sum = 0

    for i in range(k):
        curr_sum += arr[i]

    max_avg = curr_sum / k


    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i - k]
        avg = curr_sum / k
        max_avg = max(max_avg, avg)

    return max_avg

print(maxmeanSubArray([4, 5, -3, 2, 6, 1], 2))
print(maxmeanSubArray([5, 3, 4, 5, 6], 3))

#Time taken: 14 min 