# Data Structure: Graph
# Algorithm: Topological Sort (Kahn's algorithm)
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import defaultdict, deque

def prerequisiteCourses(courses, prereq_map):
    graph = defaultdict(list)
    in_degree = {course: 0 for course in courses}

    for course, prereqs in prereq_map.items():
        for prereq in prereqs:
            graph[prereq].append(course)
            in_degree[course] += 1

    queue = deque([c for c in courses if in_degree[c] == 0])
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)

    if len(result) != len(courses):
        return []
    return result


courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms",
            "Operating Systems", "Databases"]
prereqs1 = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"]
}
print(prerequisiteCourses(courses1, prereqs1))

courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature",
            "Comparative Literature", "Plays & Screenplays"]
prereqs2 = {
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature": ["Intro to Writing"],
    "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
    "Plays & Screenplays": ["Intro to Writing"]
}
print(prerequisiteCourses(courses2, prereqs2))

# Time spent: ~60 minutes
