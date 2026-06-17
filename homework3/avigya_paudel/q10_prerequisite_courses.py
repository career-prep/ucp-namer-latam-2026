# Time taken: 25 minutes
# Time complexity: O(V+E)
# Space complexity: O(V+E), where V = number of courses, and E = number of prerequisites
# Algorithm: Topological Sort (Kahn's Algorithm)

from collections import deque, defaultdict

def prerequisite_courses(courses, prerequisites):
    indegree = {}
    adj_list = defaultdict(list)

    for c in courses:
        indegree[c] = 0

    for course, prereqs in prerequisites.items():
        for prereq in prereqs:
            adj_list[prereq].append(course)
            indegree[course] += 1

    q = deque()

    for course, ind in indegree.items():
        if ind == 0:
            q.append(course)

    res = []

    while q:
        c = q.popleft()
        res.append(c)

        for next_course in adj_list[c]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                q.append(next_course)

    return [] if len(res) != len(courses) else res



if __name__ == "__main__":
    courses_1 = [
        "Intro to Programming",
        "Data Structures",
        "Advanced Algorithms",
        "Operating Systems",
        "Databases",
    ]
    prerequisites_1 = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"],
    }

    courses_2 = [
        "Intro to Writing",
        "Contemporary Literature",
        "Ancient Literature",
        "Comparative Literature",
        "Plays & Screenplays",
    ]
    prerequisites_2 = {
        "Contemporary Literature": ["Intro to Writing"],
        "Ancient Literature": ["Intro to Writing"],
        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
        "Plays & Screenplays": ["Intro to Writing"],
    }

    print(prerequisite_courses(courses_1, prerequisites_1))
    # Expected example: ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]

    print(prerequisite_courses(courses_2, prerequisites_2))
    # Expected: any order where each course comes after its prerequisites
