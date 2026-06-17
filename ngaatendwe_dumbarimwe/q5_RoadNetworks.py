#Time: O(V + E), each node and edge visited once
#Space: O(V + E)

from collections import defaultdict
import unittest

def road_networks(towns, connections) -> int:

    def dfs(town):
        visited.add(town)
        for nei in adj_dict[town]:
            if nei not in visited:
                dfs(nei)

    visited = set()
    networks = 0

    adj_dict = defaultdict(list)

    for town1, town2 in connections:
        adj_dict[town1].append(town2)
        adj_dict[town2].append(town1)

    for town in adj_dict:
        if town not in visited:
            networks += 1
            dfs(town)

    return networks


#Tests
class TestRoadNetworks(unittest.TestCase):

    def test_two_networks(self):
        towns = ["A","B","C","D"]
        connections = [("A","B"),("C","D")]
        self.assertEqual(road_networks(towns, connections), 2)

    def test_one_network(self):
        towns = ["A","B","C"]
        connections = [("A","B"),("B","C")]
        self.assertEqual(road_networks(towns, connections), 1)

    def test_no_connections(self):
        towns = ["A","B","C"]
        connections = []
        self.assertEqual(road_networks(towns, connections), 0)


if __name__ == "__main__":
    unittest.main()

#Time-taken: 30 minutes