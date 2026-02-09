# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~10 minutes
# TECHNIQUE: Sort the array, then solve

def merge_intervals(arr):
    """
    returns an array with intervals are merged
    arr[i] = (start, end) where start <= end
    """
    if len(arr) <= 1: return arr

    sorted_arr = sorted(arr) 
    
    sorted_merged_arr = merge_sorted_arr(sorted_arr)
    
    start_keys = {}
    ans = []
    for s, e in sorted_merged_arr:
        start_keys[s] = (s,e)

    for s, e in arr:
        if s in start_keys:
            ans.append(start_keys[s])
            del start_keys[s]
    return ans

def merge_sorted_arr(sorted_arr):
    """
    returns the result for array by merging but the elements are in sorted order
    """
    res = [[sorted_arr[0][0], sorted_arr[0][1]]]
    for i in range(1,len(sorted_arr)):
        s, e = sorted_arr[i][0], sorted_arr[i][1]
        if res[-1][1] >= s:
            if res[-1][1] < e:
                res[-1][1] = e
        else:
            res.append([s,e])
    return res
        
if __name__ == "__main__":
    print(merge_intervals([(2,3),(4,8),(1,2),(5,7),(9,12)]))
    print(merge_intervals([(5,8),(6,10),(2,4),(3,6)]))
    print(merge_intervals([(10,12),(5,6),(7,9),(1,3)]))