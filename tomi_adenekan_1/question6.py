"""
10 minutes
time complexity = O(n)
space complexity = O(1)
Linear search Technique 
"""

def mising(lst):
    n = len(lst)

    for i in range(n):
        if i+1 != lst[i]:
            return i+1


    return n+1

lst = [1]

print(mising(lst))
