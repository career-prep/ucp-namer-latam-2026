# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~3 minutes
# TECHNIQUE: Note sure

def dedup_arr(arr):
    """
    returns a array with no duplicates from a sorted array
    """
    return list(set(arr))

if __name__ == "__main__":
    print(dedup_arr([1,2,2,3,3,4,4,4,4]))
    print(dedup_arr([0,0,1,2,3,3,4,4,4,4,6,5,5,5,5]))
    print(dedup_arr([1,2,3,4,8,10,12]))
