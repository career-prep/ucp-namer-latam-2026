def PrerequisiteCourses(courses, prereqs):

    res = []
    visited = set()

    def dfs(course):

        if course in visited:
            return
        
        if course in prereqs:
            for prereq in prereqs[course]:
                dfs(prereq)

        visited.add(course)
        res.append(course)

    for course in courses:
        dfs(course)

    return res

# courses = [
#     "Intro to Programming",
#     "Data Structures",
#     "Advanced Algorithms",
#     "Operating Systems",
#     "Databases"
# ]

# prereqs = {
#     "Data Structures": ["Intro to Programming"],
#     "Advanced Algorithms": ["Data Structures"],
#     "Operating Systems": ["Advanced Algorithms"],
#     "Databases": ["Advanced Algorithms"]
# }

# courses = [
#     "Intro to Writing",
#     "Contemporary Literature",
#     "Ancient Literature",
#     "Comparative Literature",
#     "Plays & Screenplays"
# ]

# prereqs = {
#     "Contemporary Literature": ["Intro to Writing"],
#     "Ancient Literature": ["Intro to Writing"],
#     "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
#     "Plays & Screenplays": ["Intro to Writing"]
# }

# print(PrerequisiteCourses(courses, prereqs))

# 40