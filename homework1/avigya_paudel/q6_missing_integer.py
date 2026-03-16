# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~3 minutes
# TECHNIQUE:  One directional running computation/total

def find_missing_integer(arr, n):
    """
    returns the missing integer
    """
    return (n*(n+1))//2 - sum(arr)

if __name__ == "__main__":
    print(find_missing_integer([1,2,3,4,6,7], 7))
    print(find_missing_integer([1], 2))
    print(find_missing_integer([1,2,3,4,5,6,7,8,10,11,12], 12))
