# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(1)
# TIME TAKEN: ~10 minutes
# TECHNIQUE: 1. Fixed-size sliding window

def max_min_subarr(arr, k):
    """
    return the maximum mean of the subarray of 
    return data type: integer 
    """
    prev_idx = 0
    prev = arr[prev_idx]
    cur_sum = find_sum(arr, k)
    max_mean = cur_sum/k
    N = len(arr)

    for i in range(k, N):
        cur_sum -= prev
        cur_sum += arr[i]
        prev_idx += 1
        prev = arr[prev_idx]
        max_mean = max(max_mean, cur_sum/k)

    return max_mean

def find_sum(arr,k):
    """
    returns the sum of array from i = 0 to i = k-1
    """
    sum = 0
    for i in range(k):
        sum += arr[i]
    return sum

if __name__== "__main__":
    print(max_min_subarr([4,5,-3,2,6,1], 2))            # Expected 4.5
    print(max_min_subarr([4,5,-3,2,6,1], 3))            # Expected 3
    print(max_min_subarr([1,1,1,1,-1,-1,2,-1,-1], 3))   # Expected 1
    print(max_min_subarr([1,1,1,1,-1,-1,2,-1,-1,6], 5)) # Expected 1


