# Algorithm: Topological sort - Kahn's Algorithm
# Time: O(V + E)
# Space: O(V + E)

from collections import deque


def prerequisite_course_order(courses, prerequisites):
    course_set = set(courses)
    in_degree = {c: 0 for c in courses}
    graph = {c: [] for c in courses}

    for course in courses:
        for prereq in prerequisites.get(course, []):
            if prereq not in course_set:
                continue
            graph[prereq].append(course)
            in_degree[course] += 1

    queue = deque(c for c in courses if in_degree[c] == 0)
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != len(courses):
        return []
    return order


courses_example = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereqs_example = {"Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"]}
print("Correct:", ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"])
print("Output: ", prerequisite_course_order(courses_example, prereqs_example))
print()

print("Correct:", ["A", "B"])
print("Output: ", prerequisite_course_order(["A", "B"], {"B": ["A"]}))
print()

print("Correct:", [])
print("Output: ", prerequisite_course_order(["A", "B"], {"A": ["B"], "B": ["A"]}))
print()

# time taken: 28 min