from collections import deque


def build_graph(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        if v not in graph[u]:
            graph[u].append(v)
    for node in graph:
        graph[node] = sorted(graph[node])
    return graph


def bfs(target, graph):
    if target not in graph:
        return False
    visited = set()
    for node in sorted(graph.keys()):
        if node in visited:
            continue
        q = deque()
        visited.add(node)
        q.append(node)
        while q:
            u = q.popleft()
            if u == target:
                return True
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
    return False


def dfs(target, graph):
    if target not in graph:
        return False
    visited = set()

    for node in sorted(graph.keys()):
        if node in visited:
            continue
        stack = []
        visited.add(node)
        stack.append(node)
        while stack:
            u = stack.pop()
            if u == target:
                return True
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
    return False


def topological_sort(graph):
    in_degree = {}
    for u in graph:
        if u not in in_degree:
            in_degree[u] = 0
        for v in graph[u]:
            if v not in in_degree:
                in_degree[v] = 0
            in_degree[v] += 1

    q = deque()
    for u in sorted(in_degree):
        if in_degree[u] == 0:
            q.append(u)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(graph[u]):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(order) != len(in_degree):
        raise ValueError("graph contains a cycle")
    return order


def topological_sort_dfs(graph):
    NOT_VISITED = 0
    VISITING = 1
    FINISHED = 2

    state = {}
    for u in graph:
        state[u] = NOT_VISITED
        for v in graph[u]:
            if v not in state:
                state[v] = NOT_VISITED

    finished_postorder = []

    for node in sorted(state.keys()):
        if state[node] != NOT_VISITED:
            continue
        stack = [(node, False)]
        while stack:
            u, exiting = stack.pop()
            if exiting:
                state[u] = FINISHED
                finished_postorder.append(u)
                continue
            if state[u] == FINISHED:
                continue
            state[u] = VISITING
            for v in sorted(graph[u]):
                if state[v] == VISITING:
                    raise ValueError("graph contains a cycle")
            stack.append((u, True))
            for v in reversed(sorted(graph[u])):
                if state[v] == NOT_VISITED:
                    stack.append((v, False))

    finished_postorder.reverse()
    return finished_postorder


edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
g = build_graph(edges)
print("build_graph:", g)
print("bfs(0):", bfs(0, g))
print("bfs(-1):", bfs(-1, g))
print("dfs(3):", dfs(3, g))
print("dfs(-1):", dfs(-1, g))

dag = build_graph([(0, 1), (1, 2), (2, 3)])
print("topological_sort:", topological_sort(dag))
print("topological_sort_dfs:", topological_sort_dfs(dag))
