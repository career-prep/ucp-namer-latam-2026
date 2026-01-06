def UniqueSum(n): 
    sett = set()
    total = 0
    for i in range(len(n)):
        if n[i] not in sett:
            sett.add(n[i])
            total += n[i]
    print(sett)
    return total

print(UniqueSum([1,10,8,3,2,5,7,2,-2,-1]))
print(UniqueSum([4,3,3,5,7,0,2,3,8,6]))

#Time taken: 10 minutes and 34 seconds. 