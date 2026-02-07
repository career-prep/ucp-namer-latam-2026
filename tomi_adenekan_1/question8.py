"""
40 minutes
time complexity = O(n)
space complexity = O(n)
linear search
"""
def merge(lst):
    new = [list(x) for x in sorted(lst)]
    res = []
    res.append(new[0])

    for i in range(1, len(new)):
        if new[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], new[i][1])

        else:
            res.append(new[i])

    res = [tuple(each) for each in res]

    return res



lst = [(2,3),(4,8),(1,2),(5,7),(9,12)]
print(merge(lst))
    
