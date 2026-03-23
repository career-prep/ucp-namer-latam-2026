# spent 15 min
# one directional ?
# Time Complexity - O(n)
# Space Complexity - O(1) 


def dedupArray(arr):
    if not arr: 
        return []
    
    i = 1 # counter
    for j in range(1, len(arr)):
        if arr[j] != arr[j-1]: # if not duplicate, move to i and increment, otherwise skip
            arr[i] = arr[j]
            i += 1
    return arr
    
    


if __name__ == "__main__":
    arrs = [
        [1,2,2,3,3,3,4,4,4,4],
        [0,0,1,4,5,5,5,8,9,9,10,11,15,15],
        [1,3,4,8,10,12]
    ]
    
    for a in arrs:
        print(dedupArray(a))
        print()