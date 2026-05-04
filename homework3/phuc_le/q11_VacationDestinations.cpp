/*
    Data Structure: Graph (Adjacency List), Priority Queue (Min-Heap), Hash Map
    Algorithm: Dijkstra's Algorithm (Modified Shortest Path)

    Build an undirected graph using an adjacency list to represent the routes.
    Initialize a priority queue (min-heap) to always explore the destination with the shortest accumulated travel time next.
    Maintain a hash map to track the minimum time required to reach each city, preventing redundant processing and cycles.
    For each explored city, iterate through its neighbors. Calculate the total time to reach the neighbor, adding a 1-hour stopover penalty if the current city is not the origin.
    If the neighbor is reachable within the time limit 'k' and the new time is strictly faster than any previously recorded time, update the map and push the new state into the queue.
    Finally, count all cities in the min-time map (excluding the origin) that were reached within 'k' hours.

    Time Complexity: O((V + E) log V), where V is the number of cities and E is the number of routes. Each extraction and insertion operation on the min-heap takes logarithmic time.
    Space Complexity: O(V + E) to store the adjacency list representation of the graph, the priority queue, and the minimum time tracker map.

    Time: 40 mins
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>

using namespace std;

struct Route
{
    string u;
    string v;
    double time;
};

int findReachableDestinations(const string &origin, double k, const vector<Route> &routes)
{
    // Build the adjacency list (undirected graph)
    unordered_map<string, vector<pair<string, double>>> graph;
    for (const auto &route : routes)
    {
        graph[route.u].push_back({route.v, route.time});
        graph[route.v].push_back({route.u, route.time});
    }

    // Min-heap priority queue to store {current_time, city_name}
    priority_queue<pair<double, string>, vector<pair<double, string>>, greater<pair<double, string>>> pq;

    // Map to track the shortest time to reach each city
    unordered_map<string, double> min_time;

    // Initialize origin
    pq.push({0.0, origin});
    min_time[origin] = 0.0;

    int reachable_count = 0;

    while (!pq.empty())
    {
        auto current = pq.top();
        double curr_time = current.first;
        string u = current.second;
        pq.pop();

        // If we found a shorter path to this node already, skip it
        if (min_time.count(u) && min_time[u] < curr_time)
        {
            continue;
        }

        // Explore neighbors
        for (const auto &edge : graph[u])
        {
            string v = edge.first;
            double travel_time = edge.second;

            // Calculate the total time to reach neighbor 'v'
            // Add a 1-hour stopover penalty if 'u' is NOT the origin
            double stopover_penalty = (u == origin) ? 0.0 : 1.0;
            double next_time = curr_time + travel_time + stopover_penalty;

            // If it's reachable within k hours and is a strictly faster path
            if (next_time <= k)
            {
                if (!min_time.count(v) || next_time < min_time[v])
                {
                    min_time[v] = next_time;
                    pq.push({next_time, v});
                }
            }
        }
    }

    // Count all valid destinations (excluding the origin itself)
    for (const auto &pair : min_time)
    {
        if (pair.first != origin && pair.second <= k)
        {
            reachable_count++;
        }
    }

    return reachable_count;
}

// Helper function to run tests and format output cleanly
void runTest(int testNum, const string &description, const string &origin, double k, const vector<Route> &routes, int expected)
{
    int result = findReachableDestinations(origin, k, routes);

    cout << "Test " << testNum << " (" << description << "): ";
    if (result == expected)
    {
        cout << "PASS\n";
    }
    else
    {
        cout << "FAIL\n";
    }
    cout << "  Expected Count: " << expected << "\n";
    cout << "  Actual Count:   " << result << "\n\n";
}

int main()
{
    cout << "--- Running VacationDestinations Test Suite ---\n\n";

    vector<Route> Routes = {
        {"Boston", "New York", 4.0},
        {"New York", "Philadelphia", 2.0},
        {"Boston", "Newport", 1.5},
        {"Washington, D.C.", "Harper's Ferry", 1.0},
        {"Boston", "Portland", 2.5},
        {"Philadelphia", "Washington, D.C.", 2.5}};

    // 1. Example 1 (k=5)
    runTest(1, "Example 1 (k=5)", "New York", 5.0, Routes, 2);

    // 2. Example 2 (k=7)
    // Fix: Image text says "Output: 2" but lists 4 destinations. Expected count is 4.
    runTest(2, "Example 2 (k=7)", "New York", 7.0, Routes, 4);

    // 3. Example 3 (k=8)
    // Fix: Image text says "Output: 2" but lists 6 destinations. Expected count is 6.
    runTest(3, "Example 3 (k=8)", "New York", 8.0, Routes, 6);

    // 4. Edge Case: Zero time allowed
    runTest(4, "Zero travel time (k=0)", "New York", 0.0, Routes, 0);

    // 5. Edge Case: Origin has no routes
    runTest(5, "Isolated Origin", "Los Angeles", 10.0, Routes, 0);

    // 6. Edge Case: Reaching a destination requires multiple stopovers
    vector<Route> linearRoutes = {
        {"A", "B", 1.0},
        {"B", "C", 1.0},
        {"C", "D", 1.0}};
    // Path A->D takes 1(A->B) + 1(stop) + 1(B->C) + 1(stop) + 1(C->D) = 5 hours total
    runTest(6, "Multiple Stopovers", "A", 5.0, linearRoutes, 3);

    return 0;
}