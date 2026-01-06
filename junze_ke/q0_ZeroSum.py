#Time Taken: 40 minutes
def ZeroSum(n):
    map1 = {}
    total_pairs = 0
    for i in range(len(n)):
        if -n[i] in map1:
            total_pairs += 1
            map1[-n[i]] -= 1
        else:
            map1[n[i]] = map1.get(n[i],0) + 1
    return total_pairs

#print(ZeroSum([1,10,8,3,2,5,7,2,-2,-1]))
#print(ZeroSum([1,10,8,-2,2,5,7,2,-2,-1]))
#print(ZeroSum([4,3,3,5,7,0,2,3,8,6]))
#print(ZeroSum([4,3,3,5,7,0,2,3,8,0])) 

#Follow up Question:
def ZeroSum2(n):
    map1 = {}
    total_pairs = 0
    for i in range(len(n)):
        if -n[i] in map1:
            total_pairs += map1[-n[i]]
        map1[n[i]] = map1.get(n[i],0) + 1
    return total_pairs

print(ZeroSum2([1,10,8,3,2,5,7,2,-2,-1]))
print(ZeroSum2([1,10,8,-2,2,5,7,2,-2,-1]))
print(ZeroSum2([4,3,3,5,7,0,2,3,8,6]))
print(ZeroSum2([4,3,3,5,7,0,2,3,8,0])) 