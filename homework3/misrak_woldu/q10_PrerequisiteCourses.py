from collections import deque

# Data Structure: Graph (Adjacency List)
# Algorithm: Topological Sort (Kahn’s Algorithm - BFS)
# Time Complexity: O(courses + prerequisites)
# Space Complexity: O(courses + prerequisites)


def find_course_order(
    courses: list[str],
    prerequisites: dict[str, list[str]],
) -> list[str]:
    if not courses:
        return []

    graph = {course: [] for course in courses}
    in_degree = {course: 0 for course in courses}

    for course, prereq_list in prerequisites.items():
        for prereq in prereq_list:
            graph[prereq].append(course)
            in_degree[course] += 1

    queue = deque()

    for course in in_degree:
        if in_degree[course] == 0:
            queue.append(course)

    order = []

    while queue:
        current_course = queue.popleft()
        order.append(current_course)

        for neighbor in graph[current_course]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(courses):
        return []

    return order


def is_valid_order(order: list[str], prerequisites: dict[str, list[str]]) -> bool:
    position = {course: index for index, course in enumerate(order)}

    for course, prereq_list in prerequisites.items():
        for prereq in prereq_list:
            if position[prereq] > position[course]:
                return False

    return True


def run_tests() -> None:
    courses = [
        "Intro to Programming",
        "Data Structures",
        "Advanced Algorithms",
        "Operating Systems",
        "Databases",
    ]

    prerequisites = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"],
    }

    result = find_course_order(courses, prerequisites)
    assert is_valid_order(result, prerequisites)

    courses2 = ["A", "B", "C"]
    prerequisites2 = {
        "B": ["A"],
        "C": ["B"],
    }

    result2 = find_course_order(courses2, prerequisites2)
    assert is_valid_order(result2, prerequisites2)

    # cycle case
    courses3 = ["A", "B", "C"]
    prerequisites3 = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
    }

    assert find_course_order(courses3, prerequisites3) == []

    # no prerequisites
    courses4 = ["A", "B", "C"]
    prerequisites4 = {}

    result4 = find_course_order(courses4, prerequisites4)
    assert set(result4) == set(courses4)

    # empty input
    assert find_course_order([], {}) == []

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
