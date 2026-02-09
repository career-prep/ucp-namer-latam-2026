# Technique: Hashmap counts

def MissingInteger(a,b):
    have = {}

    for j in range(len(a)):
        have[a[j]] = have.get(a[j],0) + 1

    for l in range(1,b+1):
        if l not in have:
            return l

print(MissingInteger([1],2))
print(MissingInteger([1,2,3,4,6,7],7))
print(MissingInteger([1,2,3,4,5,6,7,8,10,11,12],12))