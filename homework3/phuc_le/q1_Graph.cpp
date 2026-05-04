#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

// 1. Build Graph Representation
map<int, set<int>> adjacencySet(vector<pair<int, int>> edges)
{
    // Create an adjacency list representation of the graph using a map of sets
    map<int, set<int>> graph;

    for (const auto &edge : edges)
    {
        // Extract the vertices from the edge
        int u = edge.first;
        int v = edge.second;
        // Add the edge to the graph
        graph[u].insert(v);
        // Ensure that all vertices are present in the graph, even if they have no outgoing edges
        if (graph.find(v) == graph.end())
        {
            // If vertex v is not already in the graph, add it with an empty set of adjacent vertices
            graph[v] = set<int>();
        }
    }
    return graph;
}

// 2. Breadth-First Search (BFS)
bool bfs(int target, map<int, set<int>> &graph)
{
    set<int> visited;

    // Iterate through all nodes in the graph to ensure we cover disconnected components
    for (const auto &pair : graph)
    {
        int startNode = pair.first;
        // If the start node has not been visited, perform BFS from that node
        if (visited.find(startNode) == visited.end())
        {
            queue<int> q;
            q.push(startNode);
            visited.insert(startNode);

            while (!q.empty())
            {
                int currNode = q.front();
                q.pop();
                // Check if the current node is the target
                if (currNode == target)
                {
                    return true; // Target found
                }
                // Explore the neighbors of the current node
                for (int neighbor : graph[currNode])
                {
                    // If the neighbor has not been visited, add it to the queue and mark it as visited
                    if (visited.find(neighbor) == visited.end())
                    {
                        visited.insert(neighbor);
                        q.push(neighbor);
                    }
                }
            }
        }
    }
    return false; // Target not found
}

// 3. Depth-First Search (DFS)
bool dfsHelper(int current, int target, map<int, set<int>> &graph, set<int> &visited)
{
    if (current == target)
    {
        return true; // Target found
    }
    // Mark the current node as visited
    visited.insert(current);
    // Explore the neighbors of the current node
    for (int neighbor : graph[current])
    {
        // If the neighbor has not been visited, recursively call dfsHelper on it
        if (visited.find(neighbor) == visited.end())
        {
            if (dfsHelper(neighbor, target, graph, visited))
            {
                return true; // Target found in the recursive call
            }
        }
    }
    return false; // Target not found in this path
}

bool dfs(int target, map<int, set<int>> &graph)
{
    set<int> visited;
    // Iterate through all nodes in the graph to ensure we cover disconnected components
    for (const auto &pair : graph)
    {
        int startNode = pair.first;
        // If the start node has not been visited, perform DFS from that node
        if (visited.find(startNode) == visited.end())
        {
            if (dfsHelper(startNode, target, graph, visited))
            {
                return true; // Target found
            }
        }
    }
    return false; // Target not found
}

// 4. Topological Sort using BFS (Kahn's Algorithm)
vector<int> topologicalSortBfs(map<int, set<int>> &graph)
{
    // Numbers of dependencies for each node
    map<int, int> inDegree;

    // Initialize in-degree for all nodes to 0
    for (const auto &pair : graph)
    {
        inDegree[pair.first] = 0;
    }

    // Calculate in-degrees by counting incoming edges
    for (const auto &pair : graph)
    {
        for (int neighbor : pair.second)
        {
            inDegree[neighbor]++;
        }
    }

    queue<int> q;
    // Enqueue nodes with in-degree of 0 (no dependencies)
    for (const auto &pair : inDegree)
    {
        if (pair.second == 0)
        {
            q.push(pair.first);
        }
    }

    vector<int> result;
    while (!q.empty())
    {
        int currNode = q.front();
        q.pop();
        result.push_back(currNode); // Add the current node to the topological order

        // Decrease the in-degree of neighboring nodes
        for (int neighbor : graph[currNode])
        {
            inDegree[neighbor]--;
            // If in-degree becomes 0, add the neighbor to the queue
            if (inDegree[neighbor] == 0)
            {
                q.push(neighbor);
            }
        }
    }

    if (result.size() != graph.size())
    {
        return {}; // Cycle detected, return an empty vector
    }
    return result; // Return the topological order
}

// 5. Topological Sort using DFS
bool topoDfsHelper(int current, map<int, set<int>> &graph, map<int, int> &state, vector<int> &result)
{
    state[current] = 1; // Mark the current node as being visited (gray)
    for (int neighbor : graph[current])
    {
        if (state[neighbor] == 1) // A cycle is detected
        {
            return false; // Cycle detected, topological sort not possible
        }
        if (state[neighbor] == 0)
        {
            if (!topoDfsHelper(neighbor, graph, state, result))
            {
                return false; // Cycle detected in the recursive call
            }
        }
    }
    state[current] = 2;        // Mark the current node as fully visited (black)
    result.push_back(current); // Add the current node to the result
    return true;               // No cycle detected
}

vector<int> topologicalSortDfs(map<int, set<int>> &graph)
{
    // states: 0 = unvisited, 1 = visiting, 2 = fully visited
    map<int, int> state;
    vector<int> result;

    for (const auto &pair : graph)
    {
        state[pair.first] = 0; // Initialize all nodes as unvisited
    }

    for (const auto &pair : graph)
    {
        int startNode = pair.first;
        // If the start node has not been visited, perform DFS from that node
        if (state[startNode] == 0)
        {
            if (!topoDfsHelper(startNode, graph, state, result))
            {
                return {}; // Return an empty vector if a cycle is detected
            }
        }
    }
    reverse(result.begin(), result.end()); // Reverse the result to get the correct topological order
    return result;
}

// Helper function to print a vector inline
void printVector(const vector<int> &v)
{
    if (v.empty())
    {
        cout << "[]";
        return;
    }
    cout << "[";
    for (size_t i = 0; i < v.size(); ++i)
    {
        cout << v[i] << (i < v.size() - 1 ? ", " : "");
    }
    cout << "]";
}

// Helper function to run a single test suite and format the output
void runTest(int testNum, const string &description, const vector<pair<int, int>> &edges, int target,
             bool expBfs, bool expDfs, const vector<int> &expKahn, const vector<int> &expDfsTopo)
{
    map<int, set<int>> graph = adjacencySet(edges);

    bool actBfs = bfs(target, graph);
    bool actDfs = dfs(target, graph);
    vector<int> actKahn = topologicalSortBfs(graph);
    vector<int> actDfsTopo = topologicalSortDfs(graph);

    bool passed = (actBfs == expBfs) && (actDfs == expDfs) && (actKahn == expKahn) && (actDfsTopo == expDfsTopo);

    cout << "Test " << testNum << " (" << description << "): ";
    if (passed)
    {
        cout << "PASS\n";
        cout << "  BFS/DFS Target " << target << ": " << (actBfs ? "Found" : "Not Found") << "\n";
        cout << "  Kahn's Sort:   ";
        printVector(actKahn);
        cout << "\n";
        cout << "  DFS Sort:      ";
        printVector(actDfsTopo);
        cout << "\n\n";
    }
    else
    {
        cout << "FAIL\n";
        if (actBfs != expBfs)
            cout << "  BFS - Expected: " << (expBfs ? "True" : "False") << ", Actual: " << (actBfs ? "True" : "False") << "\n";
        if (actDfs != expDfs)
            cout << "  DFS - Expected: " << (expDfs ? "True" : "False") << ", Actual: " << (actDfs ? "True" : "False") << "\n";
        if (actKahn != expKahn)
        {
            cout << "  Kahn - Expected: ";
            printVector(expKahn);
            cout << "\n         Actual:   ";
            printVector(actKahn);
            cout << "\n";
        }
        if (actDfsTopo != expDfsTopo)
        {
            cout << "  DFS Topo - Expected: ";
            printVector(expDfsTopo);
            cout << "\n             Actual:   ";
            printVector(actDfsTopo);
            cout << "\n";
        }
        cout << "\n";
    }
}

int main()
{
    cout << "--- Running Graph Traversals & Topological Sort Test Suite ---\n\n";

    runTest(1, "Standard DAG",
            {{1, 2}, {2, 3}, {1, 3}, {3, 4}, {2, 0}}, 3,
            true, true, {1, 2, 0, 3, 4}, {1, 2, 3, 4, 0});

    runTest(2, "Disconnected DAG",
            {{1, 2}, {3, 4}}, 4,
            true, true, {1, 3, 2, 4}, {3, 4, 1, 2});

    runTest(3, "Cyclic Graph",
            {{1, 2}, {2, 3}, {3, 1}}, 1,
            true, true, {}, {});

    runTest(4, "Self-Loop (Immediate Cycle)",
            {{1, 2}, {2, 2}}, 2,
            true, true, {}, {});

    runTest(5, "Empty Graph",
            {}, 99,
            false, false, {}, {});

    runTest(6, "Target Missing",
            {{1, 2}, {2, 3}}, 999,
            false, false, {1, 2, 3}, {1, 2, 3});

    runTest(7, "Linear Chain",
            {{1, 2}, {2, 3}, {3, 4}, {4, 5}}, 5,
            true, true, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5});

    return 0;
}