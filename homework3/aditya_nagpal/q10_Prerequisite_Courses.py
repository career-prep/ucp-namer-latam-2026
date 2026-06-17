"""
Given a list of courses that a student needs to take to complete their major and a map of courses
to their prerequisites, return avalid order for them to take their courses assuming
they only take one course for their major at once.
"""

#eg 

#input is 
"""
Input: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], 
{ "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], 
"Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
"""
#understand the realation:
#this is the resulting realtionship we need to understand
"""
Intro to Programming" ------> "Data Structures" ---------> "Advanced Algorithms" -------> "Operating Systems" 
                                                                    |
                                                                    |
                                                                    |
                                                                    |
                                                                    #
                                                               "Databases"

#this is what is given to us in terms of directed graph
"Operating Systems"-----> "Advanced Algorithms" ----> "Data Structures"----> "Intro to Programming"
                            /|
                             |
                             |
                             |
                        "database"

"""


def dfs(course, courseRelation, seen, res):
    seen.add(course)
    for nei in courseRelation.get(course, []):
        if nei not in seen:
            dfs(nei, courseRelation, seen, res)

    res.append(course)

def prereq_courses(courseArr, courseRelation):
    seen = set()
    res = []

    for course in courseArr:
        if course not in seen:
            dfs(course, courseRelation, seen, res)

    return res



print(prereq_courses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], 
                      { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], 
                        "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
                     ))


