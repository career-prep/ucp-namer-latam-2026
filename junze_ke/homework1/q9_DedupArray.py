# Time: 5 minutes
# Technique: Hashmap incremention 
def DedupArray(a):
    modified = []
    seen = {}

    for i in range(len(a)):
        if a[i] not in seen:
            modified.append(a[i])
        seen[a[i]] = seen.get(a[i], 0) + 1

    return modified

print(DedupArray([1,2,2,3,3,3,4,4,4,4]))
print(DedupArray([0,0,1,4,5,5,5,8,9,9,10,11,15,15]))
print(DedupArray([1,3,4,8,10,12]))

