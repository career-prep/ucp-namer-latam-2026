# Method: BFS
# Space Complexity: O(V + E)
# Time Complexity: O(V + E)
# Total Time Taken: 30 mins

from collections import deque

def PrerequistieCourses(courses, prereqmap):
    numPrereqs = {course: 0 for course in courses} # Map number of pre reqs for each course
    graph = {course: [] for course in courses} # Map prereq to course

    for course, prereq in prereqmap.items():
        for i in prereq:
            graph[i].append(course)
            numPrereqs[course] += 1

    queue = deque([c for c in courses if numPrereqs[c] == 0]) # Add all courses with 0 prereqs to queue
    result = []
# Pop left element of queue and add to result. Decrease left elements neighbor prereq count by 1 and if it is 0 add to queue
    while queue:
        cur = queue.popleft()
        result.append(cur)

        for neighbor in graph[cur]:
            numPrereqs[neighbor] -= 1
            if numPrereqs[neighbor] == 0:
                queue.append(neighbor)
    return result

courses = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereqmap = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
print(PrerequistieCourses(courses, prereqmap))

courses = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
prereqmap = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
print(PrerequistieCourses(courses, prereqmap)) 