"""
time = n^2
space = n
40 minutes
"""

from collections import defaultdict
from collections import deque

def pcr(input, path):
    ind = {}
    for each in input:
        ind[each] = 0
    for key, val in path.items():
        for each in val:
            ind[each] += 1

    res = []
    queue = deque()
    for key, val in ind.items():
        if val == 0:
            queue.append(key)

    while queue:
        val = queue.popleft()
        if val in path:
            for each in path[val]:
                ind[each] -= 1
                if ind[each] == 0:
                    queue.append(each)
        res.append(val)

    return res[::-1]
