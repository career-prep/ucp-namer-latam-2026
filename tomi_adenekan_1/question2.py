"""
Two Pointers
30 minutes
time complexity = O(log N)
space complexity = O(N)
"""

def get_name(str):
    rig = len(str) - 1
    res = list(str)
    left = 0
    vowels = set("AEIOUaeiou")
    while left <= rig:
        if(res[left] in vowels ) and (res[rig] in vowels):
            res[left], res[rig] = res[rig], res[left]
            left += 1
            rig -= 1
        elif(res[left] in vowels) and (res[rig] not in vowels):
            rig -= 1
        elif (res[left] not in vowels) and (res[rig] in vowels):
            left += 1
        else:
            left += 1
            rig -= 1
    return "".join(res)



lis = "Uber Career Prep"
nxt = "Xyz"
txt = "Flamingo"


print(get_name(lis))
print(get_name(nxt))
print(get_name(txt))
