# Data Structure: Graph (Adjacency List)
# Algorithm: Topological Sort (Kahn's Algorithm)
# Time Complexity: O(V + E) 
# Space Complexity: O(V + E)

from collections import deque, defaultdict

def prerequisiteCourses(courses, prerequisites):
    adj = defaultdict(list)
    in_degree = {course: 0 for course in courses}
    
    for course, prereqs in prerequisites.items():
        for prereq in prereqs:
            adj[prereq].append(course)
            in_degree[course] += 1
            
    queue = deque([course for course in courses if in_degree[course] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(result) != len(courses):
        return []
        
    return result

def main():
    courses1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    prereqs1 = {
        "Data Structures": ["Intro to Programming"],
        "Advanced Algorithms": ["Data Structures"],
        "Operating Systems": ["Advanced Algorithms"],
        "Databases": ["Advanced Algorithms"]
    }
    print(f"Test Case 1 - Result: {prerequisiteCourses(courses1, prereqs1)}")

    courses2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
    prereqs2 = {
        "Contemporary Literature": ["Intro to Writing"],
        "Ancient Literature": ["Intro to Writing"],
        "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
        "Plays & Screenplays": ["Intro to Writing"]
    }
    print(f"Test Case 2 - Result: {prerequisiteCourses(courses2, prereqs2)}")

if __name__ == "__main__":
    main()

# Time Spent: 30 minutes