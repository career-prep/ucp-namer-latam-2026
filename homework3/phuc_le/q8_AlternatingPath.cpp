#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <tuple>

using namespace std;

// Create an Edge struct to represent the graph edges
struct Edge
{
    string src;
    string dest;
    string color;
};

// Custom hash function so we can store std::pair<string, string> in an unordered_set
struct pair_hash
{
    inline size_t operator()(const pair<string, string> &p) const
    {
        return hash<string>()(p.first) ^ hash<string>()(p.second);
    }
};

int alternatingPath(const vector<Edge> &edges, const string &start, const string &end)
{
    if (start == end)
    {
        return 0; // No edges needed if start and end are the same
    }

    // Queue stores tuples of: (Current Node, Color of the edge used to get here, Current Distance)
    queue<tuple<string, string, int>> q;
    // Build the graph as an adjacency list: node -> list of (neighbor, color)
    unordered_map<string, vector<pair<string, string>>> graph;
    for (const auto &edge : edges)
    {
        graph[edge.src].push_back({edge.dest, edge.color});
    }

    // Visited set to track (node, lastColor) pairs to prevent cycles
    unordered_set<pair<string, string>, pair_hash> visited;

    // Starting color can be any color
    q.push({start, "", 0}); // (currentNode, lastColor, pathLength)
    visited.insert({start, ""});

    while (!q.empty())
    {
        auto [currentNode, lastColor, pathLength] = q.front();
        q.pop();

        if (currentNode == end)
        {
            return pathLength; // Found the end node, return the path length
        }

        // Check all neighbors
        for (const auto &neighbor : graph[currentNode])
        {
            string nextNode = neighbor.first;
            string edgeColor = neighbor.second;

            if (lastColor.empty() || edgeColor != lastColor)
            {
                pair<string, string> state = {nextNode, edgeColor};
                if (visited.find(state) == visited.end())
                {
                    visited.insert(state);
                    q.push({nextNode, edgeColor, pathLength + 1});
                }
            }
        }
    }
    return -1; // No alternating path found
}

// Helper function to run tests and format output cleanly
void runTest(int testNum, const vector<Edge> &edges, const string &origin, const string &dest, int expected)
{
    int result = alternatingPath(edges, origin, dest);
    cout << "Test " << testNum << " (Origin: " << origin << ", Dest: " << dest << "): ";
    if (result == expected)
    {
        cout << "PASS (Distance: " << result << ")\n";
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
    cout << "--- Running AlternatingPath Test Suite ---\n\n";

    vector<Edge> graphEdges = {
        {"A", "B", "blue"},
        {"A", "C", "red"},
        {"B", "D", "blue"},
        {"B", "E", "blue"},
        {"C", "B", "red"},
        {"D", "C", "blue"},
        {"A", "D", "red"},
        {"D", "E", "red"},
        {"E", "C", "red"}};

    // 1. Example 1
    runTest(1, graphEdges, "A", "E", 4);

    // 2. Example 2 (Unreachable via alternating colors)
    runTest(2, graphEdges, "E", "D", -1);

    // 3. Edge Case: Origin is Destination
    runTest(3, graphEdges, "A", "A", 0);

    // 4. Edge Case: Reachable but no alternating path (C -> E)
    // C to B is red. B to E is blue. Total distance 2.
    runTest(4, graphEdges, "C", "E", 2);

    return 0;
}