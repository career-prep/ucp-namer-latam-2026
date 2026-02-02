"""
brute force
20 minutes
"""

def get_name(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i):
            if sum(lst[j:i+1]) == 0:
                count += 1
                


    return count


lst = [4,5,2,-1,-3,-3,4,6,-7]

print(get_name(lst))
