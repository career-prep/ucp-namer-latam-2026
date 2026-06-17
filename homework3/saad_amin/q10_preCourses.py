#Time Complexity: O(V + E)
#Space Complexity: O(V + E)
#Technique: Topological Sort


from collections import defaultdict, deque

def preCourses(courses, prereqs):
    graph = defaultdict(list)
    indegree = {course: 0 for course in courses}
    
    for course in prereqs:
        for pre in prereqs[course]:
            graph[pre].append(course)
            indegree[course] += 1
    
    queue = deque()
    for course in indegree:
        if indegree[course] == 0:
            queue.append(course)
    
    result = []
    
    while queue:
        curr = queue.popleft()
        result.append(curr)
        
        for nei in graph[curr]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    return result if len(result) == len(courses) else []


courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]

prereqs1 = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"]
}

print(preCourses(courses1, prereqs1))

#Time : 38 min