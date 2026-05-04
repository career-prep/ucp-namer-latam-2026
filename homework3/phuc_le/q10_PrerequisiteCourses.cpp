/*
    Data Structure: Graph (Adjacency List), Queue, Hash Map
    Algorithm: Topological Sort (Kahn's Algorithm / BFS)

    Calculate the in-degree (number of prerequisites) for every course and build an adjacency list representing dependencies.
    Initialize a queue with all courses that have an in-degree of 0 (no prerequisites).
    While the queue is not empty, pop a course and add it to the result list.
    For the popped course, decrement the in-degree of all courses that depend on it (its neighbors).
    If a dependent course's in-degree drops to 0, push it into the queue.
    Finally, if the number of courses in the result matches the total number of courses, a valid path exists; otherwise, a circular dependency (cycle) was detected.

    Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisite pairs. Each node and edge is processed exactly once.
    Space Complexity: O(V + E) to store the adjacency list, in-degree map, and the processing queue.

    Time: 40 mins
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
#include <unordered_set>

using namespace std;

vector<string> findPrerequisitePath(const vector<string> &courses, const unordered_map<string, vector<string>> &prereqs)
{
    unordered_map<string, int> inDegree;
    unordered_map<string, vector<string>> adjList;

    // Initialize in-degrees for all courses to 0
    for (const string &course : courses)
    {
        inDegree[course] = 0;
    }

    // Build the adjacency list and compute in-degrees
    for (auto const &pair : prereqs)
    {
        const string &course = pair.first;
        const vector<string> &prereqList = pair.second;

        for (const string &prereq : prereqList)
        {
            adjList[prereq].push_back(course);
            inDegree[course]++;
        }
    }

    queue<string> q;

    // Push all courses with 0 prerequisites to the queue
    for (const string &course : courses)
    {
        if (inDegree[course] == 0)
        {
            q.push(course);
        }
    }

    vector<string> result;

    // Process the graph
    while (!q.empty())
    {
        string current = q.front();
        q.pop();
        result.push_back(current);

        // Decrease the in-degree of neighboring courses
        for (const string &neighbor : adjList[current])
        {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0)
            {
                q.push(neighbor);
            }
        }
    }

    // If result size doesn't match total courses, a cycle exists.
    if (result.size() != courses.size())
    {
        return {};
    }

    return result;
}

// Helper function to print string vectors cleanly
void printVector(const vector<string> &vec)
{
    cout << "[";
    for (size_t i = 0; i < vec.size(); ++i)
    {
        cout << "\"" << vec[i] << "\"" << (i < vec.size() - 1 ? ", " : "");
    }
    cout << "]";
}

// Helper to mathematically verify if the returned order respects all prerequisites
bool isValidOrder(const vector<string> &result, const vector<string> &courses, const unordered_map<string, vector<string>> &prereqs)
{
    if (result.size() != courses.size())
        return false;

    unordered_set<string> taken;
    for (const string &course : result)
    {
        // Check if all prerequisites for the current 'course' have already been taken
        if (prereqs.count(course))
        {
            for (const string &p : prereqs.at(course))
            {
                if (taken.find(p) == taken.end())
                {
                    return false; // Prerequisite violated
                }
            }
        }
        taken.insert(course);
    }
    return taken.size() == courses.size();
}

// Helper function to run tests and format output
void runTest(int testNum, const string &description, const vector<string> &courses, const unordered_map<string, vector<string>> &prereqs)
{
    vector<string> result = findPrerequisitePath(courses, prereqs);

    cout << "Test " << testNum << " (" << description << "): ";
    if (isValidOrder(result, courses, prereqs))
    {
        cout << "PASS\n";
    }
    else
    {
        cout << "FAIL\n";
    }
    cout << "  Actual:   ";
    printVector(result);
    cout << "\n\n";
}

int main()
{
    cout << "--- Running PrerequisiteCourses Test Suite ---\n\n";

    // 1. Example 1
    runTest(1, "Prompt Example 1",
            {"Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"},
            {{"Data Structures", {"Intro to Programming"}},
             {"Advanced Algorithms", {"Data Structures"}},
             {"Operating Systems", {"Advanced Algorithms"}},
             {"Databases", {"Advanced Algorithms"}}});

    // 2. Example 2 (Complex dependencies yielding multiple valid paths)
    runTest(2, "Prompt Example 2",
            {"Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"},
            {{"Contemporary Literature", {"Intro to Writing"}},
             {"Ancient Literature", {"Intro to Writing"}},
             {"Comparative Literature", {"Ancient Literature", "Contemporary Literature"}},
             {"Plays & Screenplays", {"Intro to Writing"}}});

    // 3. Edge Case: No prerequisites required
    runTest(3, "No Prerequisites Required",
            {"Math 101", "Physics 101", "Chemistry 101"},
            {});

    // 4. Edge Case: Graph contains a cycle (Invalid curriculum map)
    vector<string> cycleResult = findPrerequisitePath(
        {"Course A", "Course B"},
        {{"Course A", {"Course B"}}, {"Course B", {"Course A"}}});
    cout << "Test 4 (Circular Dependency): ";
    if (cycleResult.empty())
    {
        cout << "PASS\n  Actual:   [] (Cycle properly handled)\n\n";
    }
    else
    {
        cout << "FAIL\n\n";
    }

    return 0;
}