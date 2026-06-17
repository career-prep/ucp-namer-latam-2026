#Time: O(V + E), BFS over (node, color) states
#Space: O(V + E)

from collections import defaultdict, deque
import unittest

def shortest_alternating_path(edges, origin, destination):
    graph = defaultdict(list)

    for u, v, color in edges:
        graph[u].append((v, color))

    queue = deque([(origin, None, 0)])
    visited = set([(origin, None)])

    while queue:
        node, last_color, dist = queue.popleft()

        if node == destination:
            return dist

        for nei, color in graph[node]:
            if color != last_color:
                state = (nei, color)
                if state not in visited:
                    visited.add(state)
                    queue.append((nei, color, dist + 1))

    return -1


#Tests
class TestAlternatingPath(unittest.TestCase):

    def test_basic_path(self):
        edges = [("A","B","red"),("B","C","blue")]
        self.assertEqual(shortest_alternating_path(edges,"A","C"), 2)

    def test_no_path(self):
        edges = [("A","B","red"),("B","C","red")]
        self.assertEqual(shortest_alternating_path(edges,"A","C"), -1)

    def test_same_start_end(self):
        edges = [("A","B","red")]
        self.assertEqual(shortest_alternating_path(edges,"A","A"), 0)


if __name__ == "__main__":
    unittest.main()

#Time-taken: 30 minutes