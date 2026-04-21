from collections import deque, defaultdict
def prerequisiteCourses(courses, courseMap):
    """
    idea:
    use topological sort logic to solve this problem
    find indegree of all courses and put courses with indegree = 0 into queue 
    keep pop element out of queue and append that into output
        visit its neighbors and decresee indegree by 1
        if indegree = 0 -> append that neighbor into queue
    
    Time complexity: O(C + P) (C: number of courses; P: number of prerequisites)
    Space complexity: O(C + P)
    """
    indegree = {course: 0 for course in courses}
    graph = defaultdict(list)
    for course, pres in courseMap.items():
        indegree[course] = len(pres)
        for pre in pres:
            graph[pre].append(course)
    
    queue = deque([course for course in indegree if indegree[course] == 0])
    order = []
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for nei in graph[cur]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    if len(order) != len(courses):
        return []

    return order


if __name__ == "__main__":
    example1_courses = [
        "Intro to Programming",
        "Data Structures",
        "Advanced Algorithms",
        "Operating Systems",
        "Databases",
    ]
    example1_map = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"],
    }

    example2_courses = [
        "Intro to Writing",
        "Contemporary Literature",
        "Ancient Literature",
        "Comparative Literature",
        "Plays & Screenplays",
    ]
    example2_map = {
        "Contemporary Literature": ["Intro to Writing"],
        "Ancient Literature": ["Intro to Writing"],
        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
        "Plays & Screenplays": ["Intro to Writing"],
    }

    print(prerequisiteCourses(example1_courses, example1_map))
    # Expected: ["Intro to Programming", "Data Structures", "Advanced Algorithms",
    #            "Operating Systems", "Databases"]
    # or        ["Intro to Programming", "Data Structures", "Advanced Algorithms",
    #            "Databases", "Operating Systems"]

    print(prerequisiteCourses(example2_courses, example2_map))
    # Expected: any valid order where "Intro to Writing" comes before
    # "Contemporary Literature", "Ancient Literature", and "Plays & Screenplays",
    # and both "Contemporary Literature" and "Ancient Literature" come before
    # "Comparative Literature".
