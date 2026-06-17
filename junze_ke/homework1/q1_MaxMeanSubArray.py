# Time: 24 minutes
# Technique: Fixed Size Sliding Window

def MaxMeanSubArray(n,k):
    window_sum = sum(n[:k])
    max_sum = window_sum

    for i in range(k,len(n)):
        window_sum += n[i]
        window_sum -= n[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum/2

print(MaxMeanSubArray([4,5,-3,2,6,1],2))
