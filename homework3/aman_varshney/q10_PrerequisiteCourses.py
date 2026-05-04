# spent 25 minutes
# Kahns algorithm
# TC - O(V+E)
# SC - O(V+E) 

from collections import deque


def prerequisiteCourses(requirements: list[str], prereqs: dict[str, list[str]]) -> list[str]:
    # calculate indegree for each requirement and build reversed graph
    indegree = {course : 0 for course in requirements} # course : # of prereqs
    graph = {course : [] for course in requirements} # prereq : courses
    for course in prereqs:
        for prereq in prereqs[course]:
            graph[prereq].append(course)
            indegree[course] += 1
            
    # initialize queue with courses that have no prereqs
    queue = deque()
    for course in requirements:
        if indegree[course] == 0:
            queue.append(course)
            
    # kahns
    result = []
    while queue:
        course = queue.popleft()
        result.append(course)
        
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(result) != len(graph): # cycle
        return []
    return result
    
    
    
    

if __name__ == "__main__":
    # test 1
    req1 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    prereq1 = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
    valid_outputs1 = [
        ["Intro to Writing", "Plays & Screenplays", "Contemporary Literature", "Ancient Literature", "Comparative Literature"],
        ["Intro to Writing", "Contemporary Literature", "Plays & Screenplays", "Ancient Literature", "Comparative Literature"] or
        ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Plays & Screenplays", "Comparative Literature"], 
        ["Intro to Writing", "Ancient Literature", "Contemporary Literature",  "Plays & Screenplays", "Comparative Literature"], 
        ["Intro to Writing", "Ancient Literature",  "Plays & Screenplays",  "Contemporary Literature", "Comparative Literature"],
        ["Intro to Writing", "Plays & Screenplays", "Ancient Literature",  "Contemporary Literature", "Comparative Literature"], 
        ["Intro to Writing", "Ancient Literature",  "Contemporary Literature", "Comparative Literature", "Plays & Screenplays"], 
        ["Intro to Writing", "Contemporary Literature",  "Ancient Literature", "Comparative Literature", "Plays & Screenplays"],
    ]
    
    output1 = prerequisiteCourses(req1, prereq1)
    length1 = len(valid_outputs1[0])
    print("Output:", output1)
    
    if length1 != len(output1):
        print("Test 1: Fail")
    else:   
        valid1 = False
        for example in valid_outputs1:
            for i in range(length1):
                if example[i] != output1[i]:
                    break
            valid1 = True
        print("Test 1: Success") if valid1 else print("Test 1: Fail")
    
    # test 2
    req2 =  ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    prereq2 =  { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
    valid_outputs2 = [
        ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"],
        ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"],
    ]
    
    output2 = prerequisiteCourses(req2, prereq2)
    length2 = len(valid_outputs2[0])
    print("Output:", output2)
    
    if length2 != len(output2):
        print("Test 2: Fail")
    else:   
        valid2 = False
        for example in valid_outputs2:
            for i in range(length2):
                if example[i] != output2[i]:
                    break
            valid2 = True
        print("Test 2: Success") if valid2 else print("Test 2: Fail")