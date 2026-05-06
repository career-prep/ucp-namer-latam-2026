from collections import deque, defaultdict


def adjacency_set(edges):
    g = defaultdict(set)
    nodes = set()
    for u, v in edges:
        g[u].add(v)
        nodes.add(u)
        nodes.add(v)
    for x in nodes:
        g.setdefault(x, set())
    return g


def bfs(target, graph, start):
    q = deque([start])
    seen = set()
    while q:
        u = q.popleft()
        if u == target:
            return True
        if u in seen:
            continue
        seen.add(u)
        q.extend(graph[u] - seen)
    return False


def dfs(target, graph, start):
    seen = set()

    def visit(u):
        if u == target:
            return True
        seen.add(u)
        for v in graph[u]:
            if v not in seen and visit(v):
                return True
        return False

    return visit(start)


def topological_sort(graph):
    indeg = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            indeg[v] += 1
    q = deque([u for u in indeg if indeg[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order


def topological_sort_dfs(graph):
    vis = set()
    stack = []

    def dfs2(u):
        vis.add(u)
        for v in graph[u]:
            if v not in vis:
                dfs2(v)
        stack.append(u)

    for u in graph:
        if u not in vis:
            dfs2(u)
    return stack[::-1]


def _valid_topo(order, graph):
    pos = {x: i for i, x in enumerate(order)}
    for u in graph:
        for v in graph[u]:
            if pos[u] >= pos[v]:
                return False
    return True


if __name__ == "__main__":
    print("=== Spec example edges ===")
    edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    graph = dict(adjacency_set(edges))
    expect = {0: [], 1: [2, 3], 2: [0, 3], 3: [2]}
    for k in sorted(expect):
        got = sorted(graph[k])
        print(f"  {k}: {got}  ok={got == sorted(expect[k])}")

    print("=== BFS / DFS ===")
    print("  target 0 from 1:", bfs(0, graph, 1), dfs(0, graph, 1))
    print("  missing node from 1:", bfs(999, graph, 1), dfs(999, graph, 1))
    empty_adj = dict(adjacency_set([]))
    empty_adj[5] = set()
    print("  start==target isolated:", bfs(5, empty_adj, 5), dfs(5, empty_adj, 5))
    line = dict(adjacency_set([(1, 2), (2, 3), (3, 4)]))
    print("  end of chain:", bfs(4, line, 1), dfs(4, line, 1))

    print("=== Topological sort ===")
    dag = {10: {20}, 20: {30}, 30: set()}
    kahn = topological_sort(dag)
    dfs_topo = topological_sort_dfs(dag)
    print("  linear DAG Kahn:", kahn, _valid_topo(kahn, dag))
    print("  linear DAG DFS-order:", dfs_topo, _valid_topo(dfs_topo, dag))
    fork = {1: {3}, 2: {3}, 3: set()}
    fk = topological_sort(fork)
    print("  diamond-ish fork:", fk, _valid_topo(fk, fork))
    cycle = {1: {2}, 2: {1}}
    print("  cycle Kahn length < 2:", len(topological_sort(cycle)) < 2)


# Time complexity: O(V + E)
# Space complexity: O(V + E)
# Time spent: 40 minutes
