# Time complexity - O(n)
# Space complexity - O(n)

def unique_sum(arr):
    freq = {} # frequency map
    sum = 0 # unique sum
    
    for num in arr:
        if num not in freq: # unique so far
            freq[num] = 1
            sum += num
        elif freq[num] == 1: # not unique anymore so need to remove from sum
            freq[num] += 1
            sum -= num
        
    return sum
    


if __name__ == "__main__":
    input_arr = [1,2,3,4,1,4,1]
    out = unique_sum(input_arr)
    print(out)
    
    
# spent 20 minutes