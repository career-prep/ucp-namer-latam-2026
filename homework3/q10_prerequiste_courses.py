# Time complexity: O(V + E), v = # of courses, e = # of edges/prerequisite relationship mappings
# Space complexity: O(V + E)

# Technique: Topological sort
from collections import deque

def PrerequisiteCourses(courses, requirements):
    res = []
    q = deque()

    adjacencyList = {}
    indegrees = {}
    for course in courses:
        adjacencyList[course] = list()
        indegrees[course] = 0

    for course, prerequisites in requirements.items():
        for p in prerequisites:
            adjacencyList[p].append(course)
            indegrees[course] += 1
        
    for node, indegree in indegrees.items():
        if indegree == 0:
            q.append(node)
    
    while q:
        curr = q.popleft()
        res.append(curr)

        for neighbor in adjacencyList.get(curr, []):
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                q.append(neighbor)

    if len(res) != len(courses):
        print("\tCycle detected!")
        return None

    return res

if __name__ == "__main__":
  
    inputs = (
         (["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }),
         ( ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
)
    )

    for courses, requirements in inputs:
        print(PrerequisiteCourses(courses, requirements))
