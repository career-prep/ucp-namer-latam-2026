# spent 15 min
# one directional ?
# Time Complexity - O(n)
# Space Complexity - O(n) 


def dedupArray(arr):
    if not arr: # empty case
        return []
    elif len(arr) == 1: # one element
        return arr
    
    recent = arr[0]
    i = 1 # counter
    while i < len(arr):
        if arr[i] == recent: # delete duplicate
            del arr[i]
        else: # update recent and increment
            recent = arr[i]
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