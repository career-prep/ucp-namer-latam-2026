# O(V + E) time and space
# Data structure is a graph. This is topological sort using DFS.

def PrerequisiteCourses(classes, prereqs):

    visited = set()
    output = []

    def dfs(course):
        if course not in visited:
            visited.add(course)
            for prereq in prereqs.get(course, []):
                dfs(prereq)

            output.append(course)


    for p in classes:
        dfs(p)

    return output 

classes1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereqs1 = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
test1 = PrerequisiteCourses(classes1, prereqs1)
print(test1)

classes2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
prereqs2 = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
test2 = PrerequisiteCourses(classes2, prereqs2)
print(test2)

# 20 minutes
