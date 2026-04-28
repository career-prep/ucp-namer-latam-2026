# Question 10: PrerequisiteCourses

# Data Structure: Graph (directed acyclic graph)
# Algorithm: Topological Sort (Kahn's algorithm / BFS)
#   — prerequisites form directed edges; valid course order = topological order
# Time Complexity: O(V + E) where V = courses, E = prerequisite relationships
# Space Complexity: O(V + E)

from collections import deque


def prerequisiteCourses(courses, prerequisites):
    graph = {course: [] for course in courses}
    in_degree = {course: 0 for course in courses}

    for course, prereqs in prerequisites.items():
        for prereq in prereqs:
            graph[prereq].append(course)
            in_degree[course] += 1

    queue = deque([c for c in courses if in_degree[c] == 0])
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)
        for dependent in graph[course]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    return result


# --- Tests ---

# Test 1
courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms",
            "Operating Systems", "Databases"]
prereqs1 = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"],
}
result1 = prerequisiteCourses(courses1, prereqs1)
print("Test 1:", result1)
# Valid: ["Intro to Programming", "Data Structures", "Advanced Algorithms", ...]

# Test 2
courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature",
            "Comparative Literature", "Plays & Screenplays"]
prereqs2 = {
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature": ["Intro to Writing"],
    "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
    "Plays & Screenplays": ["Intro to Writing"],
}
result2 = prerequisiteCourses(courses2, prereqs2)
print("Test 2:", result2)
# Must start with "Intro to Writing", "Comparative Literature" must be last

# Validate ordering is correct
def is_valid_order(result, prereqs):
    pos = {course: i for i, course in enumerate(result)}
    for course, plist in prereqs.items():
        for p in plist:
            if pos[p] >= pos[course]:
                return False
    return True

print("Test 1 valid:", is_valid_order(result1, prereqs1))  # True
print("Test 2 valid:", is_valid_order(result2, prereqs2))  # True

# Test 3: no prerequisites
courses3 = ["A", "B", "C"]
print("Test 3 (no prereqs):", prerequisiteCourses(courses3, {}))  # ["A", "B", "C"] (any order)

# Spent a total of 30 mins on this question
