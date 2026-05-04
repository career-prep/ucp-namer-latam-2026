# Data Structure: Graph + Topological Sort (Kahn's algorithm)
# Technique: Kahn's BFS on in-degrees, prereqs are edges pointing to dependents
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import deque

def prerequisiteCourses(courses, prereqMap):
    # build graph: prereq -> [courses that need it]
    graph    = {c: [] for c in courses}
    inDegree = {c: 0  for c in courses}

    for course, prereqs in prereqMap.items():
        for prereq in prereqs:
            graph[prereq].append(course)
            inDegree[course] += 1

    # start with courses that have no prerequisites
    queue  = deque([c for c in courses if inDegree[c] == 0])
    result = []

    while queue:
        course = queue.popleft()
        result.append(course)
        for next_course in graph[course]:
            inDegree[next_course] -= 1
            if inDegree[next_course] == 0:
                queue.append(next_course)

    return result


# Test 1
courses1   = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereqMap1 = {
    "Data Structures":     ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems":   ["Advanced Algorithms"],
    "Databases":           ["Advanced Algorithms"]
}
print(prerequisiteCourses(courses1, prereqMap1))
# ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"] or similar valid order

# Test 2
courses2   = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
prereqMap2 = {
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature":      ["Intro to Writing"],
    "Comparative Literature":  ["Ancient Literature", "Contemporary Literature"],
    "Plays & Screenplays":     ["Intro to Writing"]
}
print(prerequisiteCourses(courses2, prereqMap2))
# any valid order starting with "Intro to Writing", ending with "Comparative Literature"

# Test 3: no prerequisites at all
courses3   = ["Math", "English", "History"]
prereqMap3 = {}
print(prerequisiteCourses(courses3, prereqMap3))   # any order of all 3

# Test 4: single course no prereqs
courses4   = ["Solo"]
prereqMap4 = {}
print(prerequisiteCourses(courses4, prereqMap4))   # ["Solo"]

# Time spent: ~40 minutes