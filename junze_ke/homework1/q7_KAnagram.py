# Time: 20 minutes
# Technique: Decrement Hash Count
def KAnagram(a,b,number):
    a1 = {}
    b1 = {}
    similar = 0

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        a1[a[i]] = a1.get(a[i],0) + 1
        b1[b[i]] = b1.get(b[i],0) + 1

    for j in range(len(a)):
        if a[j] in b1.keys() and b1[a[j]] > 0:
            b1[a[j]] -= 1
            a1[a[j]] -= 1
            similar += 1
    
    return (len(a) - similar) == number

print(KAnagram("apple","peach",1))
print(KAnagram("apple","peach",2))
print(KAnagram("cat","dog",3))
print(KAnagram("debit curd","bad credit",1))
print(KAnagram("baseball", "basketball", 2))
