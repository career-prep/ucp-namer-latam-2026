# Time complexity - O(n)
# Space complexity - O(n)

def unique_sum(arr):
    seen = set() # visited set
    sum = 0 # unique sum
    
    for num in arr:
        if num not in seen: # unique so far
            seen.add(num)
            sum += num
        else: # not unique anymore so need to remove from sum
            sum -= num
    
    return sum



if __name__ == "__main__":
    input_arr = [1,2,3,4,1,2,3,4]
    out = unique_sum(input_arr)
    print(out)
    
    
# spent 15 minutes