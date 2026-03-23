# one directional running computation
# Time Complexity - O(n)
# Space Complexity - O(n)


def zeroSumCount(arr):
    sum = 0 
    count = 0
    freq = {0: 1}
    
    for num in arr:
        sum += num
        if sum in freq:
            count += freq[sum] # add count of previous occurrences of this prefix sum
        freq[sum] = freq.get(sum, 0) + 1 # update frequency of current prefix sum
        
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
    
