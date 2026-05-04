# Prerequisite Courses
# Data Structure: Graph
# Algorithm: Topological Sort (Kahn's Algorithm)
# Time Complexity: O(C + P) where C is the number of courses and P is the number of prerequisite relationships
# Space Complexity: O(C + P) where C is the number of courses and P is the number of prerequisite relationships
# Assumption: There exists a valid order for course taking i.e. no cycles

from collections import deque

def prerequisiteCourses(listOfCourses, courseToPrerequistesMap):
    courseToDependentsMap = {}
    courseToDependencyCountMap = {}

    for course in listOfCourses:
        courseToDependentsMap[course] = set()
        courseToDependencyCountMap[course] = 0

    for course, listOfPrereqs in courseToPrerequistesMap.items():
        for prerequisiteCourse in listOfPrereqs:
            courseToDependentsMap[prerequisiteCourse].add(course)
            courseToDependencyCountMap[course] += 1

    zeroDependencyCourseQueue = deque()
    for course in listOfCourses:
        if courseToDependencyCountMap[course] == 0:
            zeroDependencyCourseQueue.append(course)

    validCourseOrder = []

    while zeroDependencyCourseQueue:
        currentCourse = zeroDependencyCourseQueue.popleft()
        validCourseOrder.append(currentCourse)

        for dependentCourse in courseToDependentsMap[currentCourse]:
            courseToDependencyCountMap[dependentCourse] -= 1
            if courseToDependencyCountMap[dependentCourse] == 0:
                zeroDependencyCourseQueue.append(dependentCourse)

    return validCourseOrder

#Test Cases
courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereqs1 = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"]
}
print(prerequisiteCourses(courses1, prereqs1))
# expected: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
# or:       ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"]

courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
prereqs2 = {
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature": ["Intro to Writing"],
    "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
    "Plays & Screenplays": ["Intro to Writing"]
}
print(prerequisiteCourses(courses2, prereqs2))
# expected: any valid ordering where Intro to Writing is first and Comparative Literature is last