"""
brute force
20 minutes
"""

def get_name(lst):
    count = 0
    Total = 0
    for i in range(len(lst)):
        Total += lst[i]
        check = Total
        for j in range(i):
            check -= lst[j]
            if check == 0:
                count += 1
                


    return count

lst = [4,5,2,-1,-3,-3,4,6,-7]

print(get_name(lst))
