"""
time = n^2
space = n
55 minutes

Input: [("Boston", "New York", 4), ("New York", "Philadelphia.", 2), ("Boston", "Newport", 1.5),
("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

Origin = "New York", k=5
Output: 2 (["Boston", "Philadelphia"])

Origin = "New York", k=7
Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport"])

Origin = "New York", k=8
Output: 2 (["Boston", "Philadelphia", "Washington, D.C", "Newport", "Harper's Ferry", "Portland"])

Boston -> New york, New port, Portland
Portland -> Boston
New york -> Boston, Philadelphia
Philadelphia -> New york,  Washington, D.C.
New port -> Boston
Washington, D.C. -> Harper's Ferry, Philadelphia 
Harper's Ferry -> Washington, D.C.

"""
from collections import defaultdict
from collections import deque
def inner(path, src, val):
    dic = defaultdict(list)
    

    for a, b, idx in path:
        dic[a].append([b, idx])
        dic[b].append([a, idx])
    queue = deque([(src, 0)])
    res = []

    dis = {src: 0}

    while queue:
        node, cost = queue.popleft()

        for var, new_c in dic[node]:
            cur = cost + new_c
            if cur <= val and ( var not in dis or cur < dis[var]):
                dis[var] = cur
                queue.append([var, cur])
                res.append(var)


    
    return  res
