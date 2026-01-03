def zero_sum(arr):
    visited = set() # tracks which numbers have been visited
    count = 0 # number of pairs
    
    for num in arr: # iterate through each number
        if -num in visited: # if negative is unpaired, remove and increment count
            visited.remove(-num) 
            count += 1
        else: # add number to visited set
            visited.add(num)
            
    return count




    
    
if __name__ == "__main__":
    input_arr = [1, 2, 3, 4, 5, -1, -2, -2]
    out = zero_sum(input_arr)
    print(out)