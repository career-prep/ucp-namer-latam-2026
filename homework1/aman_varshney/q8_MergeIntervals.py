# spent > 40 min
# sort then solve
# Time Complexity - O(nlogn)
# Space Complexity - O(n) 


def mergeIntervals(arr):
    merged = [] # output
    if not arr: # empty case
        return merged
    
    sorted_arr = sorted(arr) # sort
    
    for interval in sorted_arr:
        low, high = interval # untuple
        
        if not merged: # first case
            merged.append((low, high))
        elif low > merged[-1][1]: # low > highest -> create new interval
            merged.append((low, high))
        else: # merge
            merged[-1] = (merged[-1][0], max(merged[-1][1], high))
            
    return merged
        
            
      
if __name__ == "__main__":
    arr0 = []
    print("expected: []")
    print("actual: ", mergeIntervals(arr0))
    print()

    arr1 = [(2,3), (4,8), (1,2), (5,7), (9,12)]
    print("expected: [(4,8), (1,3), (9,12)]")
    print("actual: ", mergeIntervals(arr1))
    print() 
    
    arr2 = [(5,8), (6,10), (2,4), (3,6)]
    print("expected: [(2,10)]")
    print("actual: ", mergeIntervals(arr2))
        
    # (2,3) (4,8) (1,2) (5,7) (9,12)
    # (1,2) (2,3) (4,8) (5,7) (9,12)
    # (1,2) l = 1 h = 2
    # (2,3) l = 1 h = 3
    # (4,8) 
    