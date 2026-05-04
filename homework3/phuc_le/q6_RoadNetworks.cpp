/*
    Data Structure: Graph (Adjacency List), Hash Set
    Algorithm: Depth-first search (DFS)

    Build an adjacency list to represent the bidirectional roads between towns.
    Iterate through every town that has at least one road connection.
    Whenever an unvisited town is encountered, it indicates the start of a new road network.
    Increment the network counter and immediately initiate a DFS from that town.

    The DFS explores all connected towns.
    As the DFS visits each town, it adds it to a "visited" hash set.
    This ensures subsequent iterations do not recount the same connected component.

    Time Complexity: O(V + E), where V is the number of towns and E is the number of roads.
    Space Complexity: O(V + E), to maintain the adjacency list and the visited hash set.

    Time: 40 mins
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>

using namespace std;

class Solution
{
private:
    void dfs(const string &currentTown, unordered_map<string, vector<string>> &adj, unordered_set<string> &visited)
    {
        // Mark the current town as visited
        visited.insert(currentTown);

        // Traverse all neighboring towns (connected by roads)
        for (const string &neighbor : adj[currentTown])
        {
            if (visited.find(neighbor) == visited.end())
            {
                dfs(neighbor, adj, visited); // Recursively visit the neighbor
            }
        }
    }

public:
    int RoadNetworks(vector<string> &towns, vector<pair<string, string>> &roads)
    {
        // Build the adjacency list for the graph
        unordered_map<string, vector<string>> adj;
        for (const auto &road : roads)
        {
            adj[road.first].push_back(road.second);
            adj[road.second].push_back(road.first); // Since roads are bidirectional
        }

        unordered_set<string> visited;
        int networkCount = 0;

        // Find towns that has atleast 1 connection
        for (const auto &pair : adj)
        {
            const string &town = pair.first;

            // If the town has not been visited, it means we have found a new network
            if (visited.find(town) == visited.end())
            {
                networkCount++;          // Increment the count of networks
                dfs(town, adj, visited); // Perform DFS to mark all towns in this network
            }
        }
        return networkCount;
    }
};

// Helper function to run tests and format output
void runTest(int testNum, const string &description, const vector<string> &towns, const vector<pair<string, string>> &roads, int expected)
{
    Solution sol;

    // Copy the vectors to match the function signature (which expects non-const references)
    vector<string> townsCopy = towns;
    vector<pair<string, string>> roadsCopy = roads;

    int result = sol.RoadNetworks(townsCopy, roadsCopy);

    cout << "Test " << testNum << " (" << description << "): ";
    if (result == expected)
    {
        cout << "PASS\n";
    }
    else
    {
        cout << "FAIL\n";
    }
    cout << "  Expected: " << expected << "\n";
    cout << "  Actual:   " << result << "\n";
    cout << "\n";
}

int main()
{
    cout << "--- Running Road Networks Test Suite ---\n\n";

    runTest(1, "Example 1: Mixed Networks with Isolated Towns",
            {"Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"},
            {{"Anchorage", "Homer"}, {"Glacier Bay", "Gustavus"}, {"Copper Center", "McCarthy"}, {"Anchorage", "Copper Center"}, {"Copper Center", "Fairbanks"}, {"Healy", "Fairbanks"}, {"Healy", "Anchorage"}},
            2);

    runTest(2, "Example 2: All Towns Connected in 3 Networks",
            {"Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"},
            {{"Kona", "Volcano"}, {"Volcano", "Hilo"}, {"Lahaina", "Hana"}, {"Kahului", "Haiku"}, {"Hana", "Haiku"}, {"Kahului", "Lahaina"}, {"Princeville", "Lihue"}, {"Lihue", "Waimea"}},
            3);

    runTest(3, "Edge Case: 0 Networks (No Roads)",
            {"TownA", "TownB", "TownC"},
            {},
            0);

    runTest(4, "Edge Case: 1 Giant Network",
            {"A", "B", "C", "D"},
            {{"A", "B"}, {"B", "C"}, {"C", "D"}},
            1);

    runTest(5, "Edge Case: Empty Input",
            {},
            {},
            0);

    return 0;
}