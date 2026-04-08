# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(1)
# TIME TAKEN: ~3 minutes
# TECHNIQUE: Reset/catch-up two pointer

def dedup_arr(arr):
    """
    returns a array with no duplicates from a sorted array
    """
    if not arr:
        return []
    
    slow = 0
    for fast in range(1, len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
    return arr[:slow+1]

if __name__ == "__main__":
    print(dedup_arr([1,2,2,3,3,4,4,4,4]))
    print(dedup_arr([0,0,1,2,3,3,4,4,4,4,6,5,5,5,5]))
    print(dedup_arr([1,2,3,4,8,10,12]))
