# Data structure: Directed graph (adjacency + indegree)
# Algorithm: Topological sort (Kahn)

from collections import deque


def find_order(courses, prereqs):
    g = {c: [] for c in courses}
    indeg = {c: 0 for c in courses}
    for c in courses:
        for p in prereqs.get(c, []):
            g[p].append(c)
            indeg[c] += 1
    q = deque([c for c in courses if indeg[c] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order


def respects(order, prereqs):
    pos = {c: i for i, c in enumerate(order)}
    for c, ps in prereqs.items():
        for p in ps:
            if pos[p] >= pos[c]:
                return False
    return True


if __name__ == "__main__":
    cs = [
        "Intro to Programming",
        "Data Structures",
        "Advanced Algorithms",
        "Operating Systems",
        "Databases",
    ]
    prereq_cs = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"],
    }
    o1 = find_order(cs, prereq_cs)
    print("=== CS major ===")
    print(" ", o1)
    print("  valid:", respects(o1, prereq_cs))

    lit = [
        "Intro to Writing",
        "Contemporary Literature",
        "Ancient Literature",
        "Comparative Literature",
        "Plays & Screenplays",
    ]
    prereq_lit = {
        "Contemporary Literature": ["Intro to Writing"],
        "Ancient Literature": ["Intro to Writing"],
        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
        "Plays & Screenplays": ["Intro to Writing"],
    }
    o2 = find_order(lit, prereq_lit)
    print("=== Literature ===")
    print(" ", o2)
    print("  valid:", respects(o2, prereq_lit))

    print("=== Single course ===")
    print(" ", find_order(["Only"], {}))

    print("=== Cycle A -> B -> A (partial order impossible) ===")
    o_cyc = find_order(["A", "B"], {"A": ["B"], "B": ["A"]})
    print(" ", len(o_cyc), o_cyc)


# Time complexity: O(V + E)
# Space complexity: O(V + E)
# Time spent: 40 minutes
