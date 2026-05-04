#time complexity: O(V+E)
#algorithm: dfs

def PrerequisiteCourses(courses, prereqs):
    graph = {course: [] for course in courses}

    for a,b in prereqs.items():
        for i in b:
            graph[i].append(a)

    state = {c: 0 for c in courses}
    result = []

    def dfs(node):
        if state[node] == 1:
            return False
        if state[node] == 2:
            return True

        state[node] = 1

        for i in graph[node]:
            if not dfs(i):
                return False

        state[node] = 2
        result.append(node)

        return True

    for c in courses:
        if state[c] == 0:
            if not dfs(c):
                return []
    
    return result[::-1]
    
#test cases
courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereqs = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
print(f'test1: {PrerequisiteCourses(courses, prereqs)}')

#time spent: 35 min