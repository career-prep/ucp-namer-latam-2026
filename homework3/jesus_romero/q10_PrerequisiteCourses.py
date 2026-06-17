# Technique: Topological Sort (Kahn's Algorithm) for Dependency Resolution

from collections import deque

def prerequisiteCourses(courses, prerequisites): # Time, Space Complexities: O(V + E), O(V + E)
    # 1. Build adjacency list and in-degree counter
    # prerequisites map: {course: [list of courses that depend on it]}
    adj = {course: [] for course in courses}
    in_degree = {course: 0 for course in courses}
    
    for course, prereqs in prerequisites.items():
        for p in prereqs:
            # Check if p is in our course list (handling potential external refs)
            if p in adj:
                adj[p].append(course)
                in_degree[course] += 1
            else:
                # If a prerequisite isn't in our course list, we can't complete the major
                return []

    # 2. Queue all courses with 0 in-degree (no prerequisites)
    queue = deque([c for c in courses if in_degree[c] == 0])
    result = []
    
    # 3. Process the queue (BFS approach)
    while queue:
        curr = queue.popleft()
        result.append(curr)
        
        # 4. For each course that depends on curr, decrement its in-degree
        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, all prerequisites are met
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    # 5. If result contains all courses, return the order; else, there's a cycle
    return result if len(result) == len(courses) else []

class Test:
    def run_tests(self):
        # 1. Test Case: Computer Science curriculum
        courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
        prereqs1 = {
            "Data Structures": ["Intro to Programming"],
            "Advanced Algorithms": ["Data Structures"],
            "Operating Systems": ["Advanced Algorithms"],
            "Databases": ["Advanced Algorithms"]
        }
        order1 = prerequisiteCourses(courses1, prereqs1)
        # Verify order (e.g., Intro must come before Data Structures)
        assert order1.index("Intro to Programming") < order1.index("Data Structures")
        assert order1.index("Advanced Algorithms") < order1.index("Operating Systems")
        
        # 2. Test Case: Literature curriculum (Multiple valid orders)
        courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
        prereqs2 = {
            "Contemporary Literature": ["Intro to Writing"],
            "Ancient Literature": ["Intro to Writing"],
            "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
            "Plays & Screenplays": ["Intro to Writing"]
        }
        order2 = prerequisiteCourses(courses2, prereqs2)
        assert "Intro to Writing" == order2[0]
        assert order2.index("Ancient Literature") < order2.index("Comparative Literature")

        print("PrerequisiteCourses tests passed")

if __name__ == "__main__":
    tester = Test()
    tester.run_tests()

# Time complexity: O(V + E) where V is number of courses and E is total number of prerequisite links.
# Space complexity: O(V + E) for the adjacency list and tracking structures.
