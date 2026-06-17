# Time Taken: 40 minutes
# Time Complexity: O(N)
# Space Complexity: O(N)
# Algorithm: BFS
# I am skeptic, since I dont have visited or a set to check cycles, I doubt there might be endless cycles, 
# I tried using the cycle detetor like in q4 but it doesnt work as intended, 
# My implementation was adding e in the cycle detetor (visited )set at the end of the loop and checking 
# if the node was already visited right after the condition on line 33

from collections import defaultdict, deque

def alternating_path(edges, origin, destination):
    """
    Given a directed graph with red and blue edges, return the length of the
    shortest path from origin to destination where edge colors alternate.
    """
    adj_list = defaultdict(list)
    for v, e, c in edges:
        adj_list[v].append((e,c))
    
    prev = ""
    q = deque()
    for e, c in adj_list[origin]:
        q.append((e,c))
    count = 0
    while q:
        count += 1
        N = len(q)
        for i in range(N):
            e, c = q.popleft()
            if e == destination:
                return count 
            for new_e, new_c in adj_list[e]:
                if new_c != c:
                    q.append((new_e, new_c))

    return -1



if __name__ == "__main__":
    edges = [
        ("A", "B", "blue"),
        ("A", "C", "red"),
        ("B", "D", "blue"),
        ("B", "E", "blue"),
        ("C", "B", "red"),
        ("D", "C", "blue"),
        ("A", "D", "red"),
        ("D", "E", "red"),
        ("E", "C", "red"),
    ]

    print(alternating_path(edges, "A", "E"))  # Expected: 4
    print(alternating_path(edges, "E", "D"))  # Expected: -1
