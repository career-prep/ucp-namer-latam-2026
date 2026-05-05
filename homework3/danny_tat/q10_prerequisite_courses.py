from collections import deque

# Data Structure: Graph, Hashmap, Queue
# Algorithm: Kahn's topological sort
# Time Complexity: O(V + E) — V
# Space Complexity: O(V + E)
# Given a list of courses and a prerequisite map, return a valid order to take all courses assuming
# only one course is taken at a time.


def prerequisiteCourses(courses, prereqMap):
    graph = {c: [] for c in courses}
    in_degree = {c: 0 for c in courses}

    for course, prereqs in prereqMap.items():
        for prereq in prereqs:
            graph[prereq].append(course)
            in_degree[course] += 1

    queue = deque([c for c in courses if in_degree[c] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == len(courses) else []


# Testing:
courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms",
            "Operating Systems", "Databases"]
prereqs1 = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"]
}
print(prerequisiteCourses(courses1, prereqs1))
# ['Intro to Programming', 'Data Structures', 'Advanced Algorithms', 'Operating Systems', 'Databases']

courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature",
            "Comparative Literature", "Plays & Screenplays"]
prereqs2 = {
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature": ["Intro to Writing"],
    "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
    "Plays & Screenplays": ["Intro to Writing"]
}
print(prerequisiteCourses(courses2, prereqs2))
