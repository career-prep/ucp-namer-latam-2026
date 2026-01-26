# fixed size sliding window
# Time Complexity - O(n)
# Space Complexity - O(1)

from math import inf # for -infinity

def maxMeanSubarray(arr, k):
    # ensure array size >= k 
    if len(arr) < k:
        return None
    # ensure k != 0
    if k == 0: 
        return None
    
    maxMean = -inf # stores greatest mean of subarray of size k
    valid_range = len(arr) - (k-1) # stores range for i
    for left in range(valid_range): # left pointer
        # get mean of subarray
        sum = 0
        for right in range(k): # right pointer
            sum += arr[left+right]
        mean = sum/k
        
        # update max
        maxMean = max(maxMean, mean)
        
    return maxMean



if __name__ == "__main__":
    arr1 = [4,5,-3,2,6,1]
    tgt1 = 2
    out = maxMeanSubarray(arr1, tgt1)
    print("test 1", out)
    
    print()
    
    arr2 = [4,5,-3,2,6,1]
    tgt2 = 3
    out = maxMeanSubarray(arr2, tgt2)
    print("test 2:", out)
    
    print()
    
    arr3 = [1,1,1,1,-1,-1,2,-1,-1]
    tgt3 = 3
    out = maxMeanSubarray(arr3, tgt3)
    print("test 3:", out)
    
    print()
    
    arr4 = [1,1,1,1,-1,-1,2,-1,-1,7]
    tgt4 = 5
    out = maxMeanSubarray(arr4, tgt4)
    print("test 4:", out)
    
    
    # spent 20 minutes