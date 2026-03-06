# Time complexity - O(n)
# Space complexity - O(n)

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



def zero_sum_followup(arr):
    visited = set()
    count = 0
    
    for num in arr:
        visited.add(num)
        if -num in visited: # no need to remove
            count += 1
            
    return count

    
    
if __name__ == "__main__":
    input_arr = [1, 2, 3, 4, 5, -1, -2, -2]
    out = zero_sum(input_arr)
    out2 = zero_sum_followup(input_arr)
    print(out)
    print(out2)
    
    
# spent 15 minutes