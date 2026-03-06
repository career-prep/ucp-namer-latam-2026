# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~20 minutes
# TECHNIQUE: One directional running computation
from collections import defaultdict 

def zero_sum_sub_arrays(arr):
    """
    returns (int) which is the number of subarrays which sum to zero
    """
    count = 0
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    cur_sum = 0
    for num in arr:
        cur_sum += num 
        if cur_sum in prefix_sum:
            count += prefix_sum[cur_sum]
        prefix_sum[cur_sum] += 1
    return count


if __name__ == "__main__":
    print(zero_sum_sub_arrays([4,5,2,-1,-3,-3,4,6,-7])) # Expected 2
    print(zero_sum_sub_arrays([1,8,7,3,11,9]))          # Expected 0
    print(zero_sum_sub_arrays([8,-5,0,-2,3,-4]))        # Expected 2
    print(zero_sum_sub_arrays([0,0,0]))                 # Expected 6

