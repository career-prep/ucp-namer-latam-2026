#reset/catch-up two-pointer
#time complexity: O(n)
#space complexity: O(1)
#21 minutes

def dedup_array(arr):
    if not arr:
        return []
    write_index = 1
    for read_index in range(1, len(arr)): # start from second element
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    for i in range(write_index, len(arr)): #because popping is slow
        arr[i] = -1
    return arr

# test cases

array1 = [1,2,2,3,3,3,4,4,4,4]
assert dedup_array(array1) == [1,2,3,4,-1,-1,-1,-1,-1,-1]

array2 = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
assert dedup_array(array2) == [0,1,4,5,8,9,10,11,15,-1,-1,-1,-1,-1]

array3 = [1,3,4,8,10,12]
assert dedup_array(array3) == [1,3,4,8,10,12]

print("yeaaaaaaahhh!!!!")