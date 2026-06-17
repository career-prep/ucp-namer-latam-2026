# Runtime: O(V + E)
# Space complexity: O(V + E)
# Data Structure: Graph
# Algorithm: Topological Sort

# Assuming valid order exists
import collections
def prerequisiteCourses(courses, preqs):
    if not courses or not preqs:
        return []
    graph = collections.defaultdict(list)
    for nextCourse, previousCourses in preqs.items():
        for course in previousCourses:
            graph[course].append(nextCourse)

    indegrees = {}
    for course in courses:
        indegrees[course] = len(preqs[course]) if course in preqs else 0

    q = collections.deque()
    res = []
    for key, val in indegrees.items():
        if val == 0:
            q.append(key)

    while q:
        currCourse = q.popleft()
        res.append(currCourse)
        for nei in graph[currCourse]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                q.append(nei)
    return res
print(prerequisiteCourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }))
print(prerequisiteCourses( ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }))
print(prerequisiteCourses(None, None))

# Time Spent: 20:00
