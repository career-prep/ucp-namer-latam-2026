# Topological Sort (Kahn's Algoritm)
# O(V + E) Time Complexity, where V is the number of courses, and E is the number of edges.
# O(V) Space Complexity, where V is the number of courses.
# Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, 
# return a valid order for them to take their courses assuming they only take one course for their major at once.

from collections import deque


def PrerequisiteCourses(courses, prerequisites):

    # prerequisites input is a bit misleading. prerequisites holds a course -> [all prerequisites], so if we treat prerequisites as our graph, then we get 
    # a reversed order of the topological sort. Instead, we need to make a graph such as: prereq -> course.
    # Although, I could have kept my original logic and just reversed my result array at the end and most likely gotten a valid result.

    # Each course either has no preqrequisites or has at least one prerequisite... so this graph is definitely a directed graph...
    # Which means we can use topological sort to return a valid order for this student to take all their courses

    if not courses:
        return None

    # If no courses have prerequisites, we can return the order of courses given to us
    if not prerequisites:
        return courses


    # I will use the BFS version of topological sort

    # Build the correct graph and inDegree
    graph = {} 
    inDegree = {} # {Course: Value} - Where value represents how many prerequisites this course still needs before it can be taken

    for course in courses:
        graph[course] = [] # Each course has a list of prerequisites, initially empty
        inDegree[course] = 0 # Initially zero for every course

    
    # Populate the graph and inDegree
    for course in prerequisites:
        for nei in prerequisites[course]:
            graph[nei].append(course)
            inDegree[course] += 1

    
    # Now initialize a queue with all nodes (courses) that have an inDegree of zero (which means this course has no prerequisites)
    q = deque()
    for course in courses:
        if inDegree[course] == 0:
            q.append(course)



    orderOfCourses = [] # Stores our topological sort



    # Next, do a BFS. Pop from the left of the queue, reduce inDegree of all neighbors of popped course, then add current course to result array
    while q:

        course = q.popleft()

        # Add current course to result array
        orderOfCourses.append(course)

        # Reduce inDegree of all neighbors, then add any course to the queue which now has an inDegree of zero
        if course in graph:
            for nei in graph[course]:
                inDegree[nei] -= 1

                if inDegree[nei] == 0:
                    q.append(nei)

        



    return orderOfCourses



# 33 minutes

# Test Cases

courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prereqs1 = {"Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], 
            "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"]}



courses2 =  ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
prereqs2 = {"Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], 
            "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"]}


courses3 = ["CS1", "OOP", "CS2", "CDA", "CIS"]
prereqs3 = {}

courses4 = []



print(PrerequisiteCourses(courses1, prereqs1)) # Gives the first expected output from the assignment doc
print(PrerequisiteCourses(courses2, prereqs2)) # Gives the 3rd expected output from the assignment doc

# My Added Test Cases
print(PrerequisiteCourses(courses3, prereqs3))
print(PrerequisiteCourses(courses4, prereqs2))
        


        

        





