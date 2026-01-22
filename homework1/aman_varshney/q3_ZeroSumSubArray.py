# variable size sliding window
# Time Complexity - O(n^2)
# Space Complexity - O(1)
# couldve used hashmap


def zeroSumCount(arr):
    count = 0
    for left in range(len(arr)-1):
        sum = arr[left]
        
        if sum == 0: # balanced
            count += 1
            
        for right in range(left+1, len(arr)):
            sum += arr[right]
            
            if sum == 0:
                count += 1
                
    return count



if __name__ == "__main__":
    arr1 = [4,5,2,-1,-3,-3,4,6,-7]
    out1 = zeroSumCount(arr1)
    print("test 1 -- ", out1)
    
    print() 
    
    arr2 = [1,8,7,3,11,9]
    out2 = zeroSumCount(arr2)
    print("test 2 -- ", out2) 
    
    print() 
    
    arr3 = [8,-5,0,-2,3,-4]
    out3 = zeroSumCount(arr3)
    print("test 3 -- ", out3)
    

   
# spent 40 minutes 
    

'''
def zeroSum(arr): 
    list_arrays = [] # will store balanced subarrays
    
    for start in range(len(arr)): 
        subarray = [arr[start]] # tracks numbers
        sum = arr[start] # tracks sum of subarray
        
        if sum == 0: # balanced --> add number as a subarray
            list_arrays.append(subarray)
            
            
        for end in range(start+1, len(arr)): # check rest of array for balanced subarray
            subarray.append(arr[end])
            sum += arr[end]
            
            if (sum == 0): # balanced --> add subarray 
                l = []
                for item in subarray: # had to do this for some reason instead of appending subarray
                    l.append(item)
                list_arrays.append(l)
                
        
    return list_arrays
'''
