#time complexity: O(logn)
#algorithm = BFS

from collections import deque, defaultdict
def AlternatingPath(paths, start, end):
    graph = defaultdict(list)

    for a, b, c in paths:
        graph[a].append((b, c))

    q = deque([(start, None, 0)])
    visited = set([(start, None)])

    while q:
        node, c, dist = q.popleft()

        if node == end:
            return dist

        for i, color in graph[node]:
            if color != c:
                state = (i, color)

                if state not in visited:
                    visited.add(state)
                    q.append((i, color, dist+1))

    return -1

#testcases
paths = [('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")]
start = 'A'
end = 'E' 
print(f'test1: {AlternatingPath(paths, start, end)}')
start = 'E'
end = 'D'
print(f'test2: {AlternatingPath(paths, start, end)}')

#time spent = 35 min