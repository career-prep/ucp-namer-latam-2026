#Time: O(V + E)
#Space: O(V + E)

import unittest

def prerequisite_courses(courses, adj_dict) -> list:

    UNVISITED, VISITING, VISITED = 0, 1, 2
    state = [UNVISITED] * len(courses)

    course_index = {courses[i]: i for i in range(len(courses))}
    course_order = []

    def dfs(course):
        idx = course_index[course]

        if state[idx] == VISITING:
            return False
        if state[idx] == VISITED:
            return True

        state[idx] = VISITING

        for prereq in adj_dict.get(course, []):
            if not dfs(prereq):
                return False

        state[idx] = VISITED
        course_order.append(course)
        return True

    for course in courses:
        if state[course_index[course]] == UNVISITED:
            if not dfs(course):
                return []

    return course_order


#Tests
class TestPrerequisites(unittest.TestCase):

    def test_simple_chain(self):
        courses = ["A","B","C"]
        adj = {"C":["B"], "B":["A"]}
        self.assertEqual(prerequisite_courses(courses, adj), ["A","B","C"])

    def test_cycle(self):
        courses = ["A","B"]
        adj = {"A":["B"], "B":["A"]}
        self.assertEqual(prerequisite_courses(courses, adj), [])

    def test_no_prereqs(self):
        courses = ["A","B","C"]
        adj = {}
        self.assertEqual(len(prerequisite_courses(courses, adj)), 3)


if __name__ == "__main__":
    unittest.main()

#Time-taken: 30 minutes