#approach:
#first: i want to store each num with the number of its occurance because we only want to use each elem once
#there is gonna be 2 case:
#first case: diff= 0- num = num => the num must be 0 =>  count = hashmap[number_of_0]//2
#second case: diff = 0-num => count +=1, decrease the num of occurance in diff and num to avoid duplicate

def zero_sum(arr):
    hashmap={}
    #track the occurance
    for num in arr:
        if num in hashmap:
            hashmap[num]+=1
        else:
            hashmap[num]=1

    #loop through elem and find the pair
    count=0
    for elem in arr:
        diff = 0-elem
        if diff in hashmap and diff!= elem and hashmap[diff]>0 and hashmap[elem]>0:
            count+=1
            hashmap[diff]-=1
            hashmap[elem]-=1

        if diff==elem and hashmap[diff]>1:
            count+=hashmap[elem]//2
            hashmap[elem]=0

    return count

print(zero_sum([1,10,8,3,2,5,7,2,-2,-1])) 
print(zero_sum([1,10,8,-2,2,5,7,2,-2,-1]))
print(zero_sum([4,3,3,5,7,0,2,3,8,6]))
print(zero_sum([4,3,3,5,7,0,2,3,8,0]))


#approach:
#use a hashmap to track the occurance of each element
# loop through every elem and check if diff=0-num in the hashmap(seen) or not
#if it is in, then count+=hashmap[diff]
#if num not in hashmap, add it into hashmap
#if it is already in hashmap, increase the value by one

def zero_sum_follow_up(arr):
    hashmap={} #seen
    count=0
    
    for num in arr:
        diff=0-num
        if diff in hashmap:
            count+=hashmap[diff]
        if num in hashmap:
            hashmap[num]+=1
        else:
            hashmap[num]=1
    
    return count

# test cases
print(zero_sum_follow_up([1,10,8,3,2,5,7,2,-2,-1]))
print(zero_sum_follow_up([1,10,8,-2,2,5,7,2,-2,-1]))
print(zero_sum_follow_up([4,3,3,5,7,0,2,3,8,6]))
print(zero_sum_follow_up([4,3,3,5,7,0,2,3,8,0]))



def zero_sum_better(arr):
    seen={} #store the number that has been seen but does not have any pair yet
    counter=0

    for num in arr:
        diff = 0 - num
        if diff in seen and seen[diff]>0:
            counter+=1
            seen[diff]-=1
        else:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
    
    return counter








            
