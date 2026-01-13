# given array of int
#find num of pairs in array theat sum to 0
#we want to pair up the pos and negative nums using a hash map
#return the pairs that add to 0

def zero_sum_pairs(arr):
    num_map = {} #hash map to store the nums we have seen
    count = 0 #count of pairs

    for num in arr:
        target = -num #the num we need to find to make the sum 0

        if target in num_map and num_map[target] > 0: #if we have seen the target num before and it is available to pair
            count += 1 #increment the count of pairs
            num_map[target] -= 1   # consume the target
        else:
            if num in num_map: 
                num_map[num] += 1  #increment the count of the current num seen so far
            else:
                num_map[num] = 1 #initialize the count of the current num seen so far to 1

    return count


#Follow up: reuse allowed
def reuse_zero_sum_pairs(arr):
    num_map = {} #hash map to store the nums we have seen
    count = 0 #count of pairs

    for num in arr:
        target = -num #the num we need to find to make the sum 0

        if target in num_map:
            count += num_map[target] #add the count of target nums seen so far to the count

        if num in num_map:
            num_map[num] += 1   #increment the count of the current num seen so far
        else:
            num_map[num] = 1 #initialize the count of the current num seen so far to 1

    return count

#example usage
arr = [1, 10,8,3,2,5,7,2,-2,-1,-3,-5]
print(zero_sum_pairs(arr)) #prints 4

arr= [1, -1, 2, -2, 3, -3, 1, -1]
print(reuse_zero_sum_pairs(arr)) #prints 8

#time spent 45 min
