from collections import defaultdict, deque

def prerequisiteCourses(courses, prereqs):
    graph = defaultdict(set)
    in_degree = {course: 0 for course in courses}

    for course, prerequisites in prereqs.items():
        for pre in prerequisites:
            graph[pre].add(course)
            in_degree[course] += 1

    queue = deque()
    result = []

    for course in courses:
        if in_degree[course] == 0:
            queue.append(course)

    while queue:
        course = queue.popleft()
        result.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


if __name__ == "__main__":

    courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms",
                "Operating Systems", "Databases"]
    prereqs1 = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"]
    }
    print("Test 1:")
    print("Got:     ", prerequisiteCourses(courses1, prereqs1))
    print("Expected: Intro to Programming -> Data Structures -> Advanced Algorithms -> OS/Databases")

    courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature",
                "Comparative Literature", "Plays & Screenplays"]
    prereqs2 = {
        "Contemporary Literature": ["Intro to Writing"],
        "Ancient Literature": ["Intro to Writing"],
        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
        "Plays & Screenplays": ["Intro to Writing"]
    }
    print("\nTest 2:")
    print("Got:     ", prerequisiteCourses(courses2, prereqs2))
    print("Expected: Intro to Writing first, Comparative Literature last")