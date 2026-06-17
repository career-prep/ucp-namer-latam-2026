# Algorithm: Kahn's algorithm (BFS-based topological sort)
# Edge prereq -> course; nodes with in-degree 0 can be taken first.
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import deque


def prerequisiteCourses(courses, prereqs):
    graph = {c: [] for c in courses}
    in_degree = {c: 0 for c in courses}

    for course, plist in prereqs.items():
        for p in plist:
            graph[p].append(course)
            in_degree[course] += 1

    queue = deque()
    for c in courses:
        if in_degree[c] == 0:
            queue.append(c)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(courses):
        return []  # cycle in prerequisites, no valid order
    return result


print("PrerequisiteCourses Results:")

courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms",
            "Operating Systems", "Databases"]
prereqs1 = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"],
}
print(prerequisiteCourses(courses1, prereqs1))

courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature",
            "Comparative Literature", "Plays & Screenplays"]
prereqs2 = {
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature": ["Intro to Writing"],
    "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
    "Plays & Screenplays": ["Intro to Writing"],
}
print(prerequisiteCourses(courses2, prereqs2))

# Cycle case (A requires B, B requires A) -> []
print(prerequisiteCourses(["A", "B"], {"A": ["B"], "B": ["A"]}))

# No prereqs at all
print(prerequisiteCourses(["X", "Y", "Z"], {}))
