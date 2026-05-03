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

struct TestCase
{
    string name;
    vector<string> towns;
    vector<pair<string, string>> roads;
    int expected;
};

int main()
{
    vector<TestCase> testCases = {
        {"Example 1: Mixed Networks with Isolated Towns",
         {"Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"},
         {{"Anchorage", "Homer"}, {"Glacier Bay", "Gustavus"}, {"Copper Center", "McCarthy"}, {"Anchorage", "Copper Center"}, {"Copper Center", "Fairbanks"}, {"Healy", "Fairbanks"}, {"Healy", "Anchorage"}},
         2},
        {"Example 2: All Towns Connected in 3 Networks",
         {"Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"},
         {{"Kona", "Volcano"}, {"Volcano", "Hilo"}, {"Lahaina", "Hana"}, {"Kahului", "Haiku"}, {"Hana", "Haiku"}, {"Kahului", "Lahaina"}, {"Princeville", "Lihue"}, {"Lihue", "Waimea"}},
         3},
        {"Edge Case: 0 Networks (No Roads)",
         {"TownA", "TownB", "TownC"},
         {},
         0},
        {"Edge Case: 1 Giant Network",
         {"A", "B", "C", "D"},
         {{"A", "B"}, {"B", "C"}, {"C", "D"}},
         1},
        {"Edge Case: Empty Input",
         {},
         {},
         0}};

    Solution sol;
    int passed = 0;

    cout << "=== ROAD NETWORKS TEST EXECUTION ===\n\n";

    for (const auto &tc : testCases)
    {
        // Pass by copy for safety in a test runner, though this algo doesn't mutate inputs
        vector<string> townsCopy = tc.towns;
        vector<pair<string, string>> roadsCopy = tc.roads;

        int result = sol.RoadNetworks(townsCopy, roadsCopy);

        if (result == tc.expected)
        {
            passed++;
            cout << "✅ Passed: " << tc.name << "\n";
        }
        else
        {
            cout << "❌ Failed: " << tc.name << " | Expected " << tc.expected << ", got " << result << "\n";
        }
    }

    cout << "\n--- Final Results: " << passed << "/" << testCases.size() << " Tests Passed ---\n";

    return 0;
}