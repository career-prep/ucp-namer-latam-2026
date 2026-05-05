# Data Structure: Graph
# Algorithm: Topological Sort
# Time Complexity: O(V + E) since each node is visited at most once
# Space Complexity: O(V + E) to store the graph and in-degree counts

from collections import deque, defaultdict

def prerequisite_courses(courses, prereq_map):
    adj_list = defaultdict(list)
    in_degree = {course: 0 for course in courses}

    for course, prereqs in prereq_map.items():
        for p in prereqs:
            adj_list[p].append(course)
            in_degree[course] += 1

    queue = deque([c for c in courses if in_degree[c] == 0])
    ordered_courses = []

    while queue:
        curr = queue.popleft()
        ordered_courses.append(curr)

        for neighbor in adj_list[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)


    if len(ordered_courses) == len(courses):
        return ordered_courses
    else:
        return []
    
course_list_1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereq_1 = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"]
    }

course_list_2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
prereq_2 = { 
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature": ["Intro to Writing"], 
    "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], 
    "Plays & Screenplays": ["Intro to Writing"]
    }

print(prerequisite_courses(course_list_1, prereq_1))
print(prerequisite_courses(course_list_2, prereq_2))

# Time Spent: 28 min