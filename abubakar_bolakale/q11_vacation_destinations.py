# Data structure: Graph (weighted undirected)
# Algorithm: BFS with relaxation (shortest travel time with stopover rule)

from collections import defaultdict, deque


def vacation(edges, origin, k):
    g = defaultdict(list)
    for u, v, t in edges:
        g[u].append((v, t))
        g[v].append((u, t))
    dq = deque([(origin, 0.0)])
    best = {origin: 0.0}
    reach = set()
    while dq:
        u, tm = dq.popleft()
        for v, w in g[u]:
            stop = 0.0 if u == origin else 1.0
            nt = tm + w + stop
            if nt <= k and (v not in best or nt < best[v]):
                best[v] = nt
                reach.add(v)
                dq.append((v, nt))
    return len(reach)


if __name__ == "__main__":
    trips = [
        ("Boston", "New York", 4),
        ("New York", "Philadelphia", 2),
        ("Boston", "Newport", 1.5),
        ("Washington, D.C.", "Harper's Ferry", 1),
        ("Boston", "Portland", 2.5),
        ("Philadelphia", "Washington, D.C.", 2.5),
    ]
    o = "New York"
    print("=== Same graph k = 5, 7, 8 ===")
    print(" ", vacation(trips, o, 5))
    print(" ", vacation(trips, o, 7))
    print(" ", vacation(trips, o, 8))

    print("=== No trips ===")
    print(" ", vacation([], "Boston", 99))

    print("=== Budget zero ===")
    print(" ", vacation(trips, o, 0))

    print("=== Tiny graph ===")
    print(" ", vacation([("A", "B", 1.0)], "A", 1.0))

    print("=== Large budget full graph ===")
    print(" ", vacation(trips, o, 1000))


# Time complexity: O(V + E)
# Space complexity: O(V + E)
# Time spent: 38 minutes
