"""
time = n^2
space = n

40 minutes
"""
"""
[(A, B, "blue"), (A, C, "red"), (B, D, "blue"), (B, E, "blue"),
(C, B, "red"), (D, C, "blue"), (A, D, "red"), (D, E, "red"), (E, C, "red")]

Input: origin = A, destination = E
Output: 4 (path: A→D (red), D→C (blue), C→B (red), B→E (blue))

Input: origin = E, destination = D
Output: -1 (only path is: E→C (red), C→B (red), B→D (blue))

A = B, C, D
B = D, E
C = B
D = C, E
E = C

"""
from collections import defaultdict
from collections import deque

def graph(path, scr, des):
    dic = defaultdict(list)
    for key, spa, cl in path:
        dic[key].append(spa)

    if scr not in dic:
        return -1

    visited = set()
    search = deque([scr])

    while search:
        val = search.popleft()
        if val == des:
            return
        for each in dic[val]:
            if each not in visited:
                visited.add(val)
                search.append(each)

        visited.add(val)
        print(val)


    return dic
path = [("A", "B", "blue"),
        ("A", "C", "red"),
        ("B", "D", "blue"),
        ("B", "E", "blue"),
        ("C", "B", "red"),
        ("D", "C", "blue"),
        ("A", "D", "red"),
        ("D", "E", "red"),
        ("E", "C", "red")]
print(graph(path, 'A', 'E'))
