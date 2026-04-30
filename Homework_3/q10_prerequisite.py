# Question 10: PrerequisiteCourses
#
# Given a list of courses that a student needs to take to complete their major
# and a map of courses to their prerequisites, return a valid order for them
# to take their courses assuming they only take one course for their major at once.
#
# Examples:
#
# Input: ["Intro to Programming", "Data Structures", "Advanced Algorithms",
#          "Operating Systems", "Databases"],
#        {"Data Structures": ["Intro to Programming"],
#         "Advanced Algorithms": ["Data Structures"],
#         "Operating Systems": ["Advanced Algorithms"],
#         "Databases": ["Advanced Algorithms"]}
#
# Output: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"]
#         or
#         ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
#
# Input: ["Intro to Writing", "Contemporary Literature", "Ancient Literature",
#          "Comparative Literature", "Plays & Screenplays"],
#        {"Contemporary Literature": ["Intro to Writing"],
#         "Ancient Literature": ["Intro to Writing"],
#         "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
#         "Plays & Screenplays": ["Intro to Writing"]}
#
# Output: ["Intro to Writing", "Plays & Screenplays", "Contemporary Literature",
#           "Ancient Literature", "Comparative Literature"] or many other valid orders

from collections import deque
def prereq(courses,req):
    #Finding degree of connection
    connections={node:0 for node in courses}
    #Fixing inverted prereq 
    graph={node:[] for node in courses}
    for c in courses:
        if c in req:        
            for k in req[c]:
                graph[k].append(c)         
                connections[c] += 1

    def bfs():
    #Starting from nodes with connections of 0
        queue=deque([node for node in connections if connections[node]==0])
        result=[]
        while queue:
            curr=queue.popleft()
            result.append(curr)
            for nei in graph[curr]:
                connections[nei]-=1
                if connections[nei]==0:
                    queue.append(nei)

        return result

    return bfs()


courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
req1 = {"Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"]}
print(prereq(courses1, req1))

courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
req2 = {"Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"]}
print(prereq(courses2, req2))

courses3 = ["Math", "Physics", "Chemistry"]
req3 = {}
print(prereq(courses3, req3))

courses4 = ["A", "B", "C", "D"]
req4 = {"B": ["A"], "C": ["B"], "D": ["C"]}
print(prereq(courses4, req4))


#Time Complexity: O(V+E)
#Space Complexity: O(V+E)

#Spent 40 mins