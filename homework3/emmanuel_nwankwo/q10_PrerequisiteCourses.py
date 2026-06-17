# Data Structure: Graph
# Algorithm: Topological sort
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import deque

def prerequisite_courses(courses, prereqs):
    graph = {c: [] for c in courses}
    indegree = {c: 0 for c in courses}

    for course in prereqs:
        for pre in prereqs[course]:
            graph[pre].append(course)
            indegree[course] += 1

    q = deque([c for c in courses if indegree[c] == 0])
    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return result

# Time Taken: 18 mins 05 secs

# Test Cases
courses1 = ["Intro to Programming","Data Structures","Advanced Algorithms","Operating Systems","Databases"]
pr1 = {
    "Data Structures":["Intro to Programming"],
    "Advanced Algorithms":["Data Structures"],
    "Operating Systems":["Advanced Algorithms"],
    "Databases":["Advanced Algorithms"]
}
print(prerequisite_courses(courses1, pr1))

courses2 = ["Intro to Writing","Contemporary Literature","Ancient Literature","Comparative Literature","Plays & Screenplays"]
pr2 = {
    "Contemporary Literature":["Intro to Writing"],
    "Ancient Literature":["Intro to Writing"],
    "Comparative Literature":["Ancient Literature","Contemporary Literature"],
    "Plays & Screenplays":["Intro to Writing"]
}
print(prerequisite_courses(courses2, pr2))

# Edge Cases
print(prerequisite_courses([], {}))
print(prerequisite_courses(["Calculus"], {}))
print(prerequisite_courses(["English 1101","English 1102"], {"English 1102":["English 1101"]}))