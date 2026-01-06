
def FirstOccurence(n):
    list1 = []
    sett = set()
    string = ""
    for i in range(len(n)):
        if n[i] not in sett:
            sett.add(n[i])
            list1 += n[i]
    return string.join(list1)

print(FirstOccurence("abracadabra"))
print(FirstOccurence("Uber Career Prep"))
print(FirstOccurence("zzyzx"))