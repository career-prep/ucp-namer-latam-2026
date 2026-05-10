# Time: 40 minutes
# Topological Sort 
def PrereqCourses(courses, prereqs):
    graph = {}
    in_degree = {}

    for course in courses:
        graph[course] = set()

    for course, requirements in prereqs.items():
        for req in requirements:
            graph[req].add(course)
    
    for u in graph:
        in_degree[u] = 0

    for u, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1
        
    q = [node for node in graph if in_degree[node] == 0]    
    result = []

    while q:
        node = q.pop()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0: 
                q.append(neighbor)

    return result

print(PrereqCourses(
    ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"],
    {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"]
    }
))