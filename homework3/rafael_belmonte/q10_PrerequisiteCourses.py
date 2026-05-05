# Data Structure: Graph (DAG of courses)
# Algorithm: Topological sort (Kahn's algorithm)
#
# Build a directed graph where each prerequisite -> course edge represents
# "prereq must come before course". Kahn's algorithm produces a valid order.
#
# If a cycle exists (a course depends, transitively, on itself) we raise.
# Prereqs that are not in the courses list are ignored — assumption: a course
# whose prereqs are missing from the major list is treated as having no
# enforced ordering against them (alternative interpretation: raise; documented
# here in code).
#
# Time complexity:  O(V + E), V = number of courses, E = number of prereq edges.
# Space complexity: O(V + E)

from collections import defaultdict, deque


def course_order(courses, prerequisites):
    course_set = set(courses)
    graph = defaultdict(list)        # prereq -> [course]
    in_degree = {c: 0 for c in courses}

    for course, prereqs in prerequisites.items():
        if course not in course_set:
            continue
        for prereq in prereqs:
            if prereq not in course_set:
                # prereq lives outside the major list; skip per assumption above
                continue
            graph[prereq].append(course)
            in_degree[course] += 1

    queue = deque([c for c in courses if in_degree[c] == 0])
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for nxt in graph[course]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(order) != len(courses):
        raise ValueError("Cycle detected in prerequisites; no valid order.")
    return order


def is_valid_order(order, courses, prerequisites):
    if sorted(order) != sorted(courses):
        return False
    pos = {c: i for i, c in enumerate(order)}
    for course, prereqs in prerequisites.items():
        if course not in pos:
            continue
        for p in prereqs:
            if p in pos and pos[p] >= pos[course]:
                return False
    return True


# test cases
if __name__ == "__main__":
    courses1 = ["Intro to Programming", "Data Structures",
                "Advanced Algorithms", "Operating Systems", "Databases"]
    prereqs1 = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"],
    }
    order1 = course_order(courses1, prereqs1)
    assert is_valid_order(order1, courses1, prereqs1), order1

    courses2 = ["Intro to Writing", "Contemporary Literature",
                "Ancient Literature", "Comparative Literature",
                "Plays & Screenplays"]
    prereqs2 = {
        "Contemporary Literature": ["Intro to Writing"],
        "Ancient Literature": ["Intro to Writing"],
        "Comparative Literature": ["Ancient Literature",
                                   "Contemporary Literature"],
        "Plays & Screenplays": ["Intro to Writing"],
    }
    order2 = course_order(courses2, prereqs2)
    assert is_valid_order(order2, courses2, prereqs2), order2

    print("Order 1:", order1)
    print("Order 2:", order2)

    # cycle detection
    cyclic = {"A": ["B"], "B": ["A"]}
    try:
        course_order(["A", "B"], cyclic)
        assert False
    except ValueError:
        pass

    print("yay!!")

# Time spent: ~25 minutes
