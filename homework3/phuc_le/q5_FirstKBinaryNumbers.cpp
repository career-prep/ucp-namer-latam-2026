#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

class Solution
{
public:
    vector<string> firstKBinaryNumbers(int k)
    {
        if (k <= 0)
        {
            return {};
        }

        vector<string> result;
        // Base case: 0 is the first binary number, and cant add 0 or 1 to it
        result.push_back("0");
        if (k == 1)
        {
            return result;
        }

        // Use a queue to generate binary numbers in level order
        queue<string> q;
        q.push("1"); // Start with the first binary number
        for (int i = 0; i < k - 1; i++)
        {
            string current = q.front(); // Get the next binary number
            q.pop();
            result.push_back(current); // Add the current binary number to the result list
            q.push(current + "0");     // Generate left child
            q.push(current + "1");     // Generate right child
        }
        return result;
    }
};

// Helper function to print vectors cleanly
void printVector(const vector<string> &vec)
{
    cout << "[";
    for (size_t i = 0; i < vec.size(); ++i)
    {
        cout << "\"" << vec[i] << "\"";
        if (i < vec.size() - 1)
            cout << ", ";
    }
    cout << "]";
}

// Helper function to run tests and format output
void runTest(int testNum, const string &description, int k, const vector<string> &expected)
{
    Solution sol;
    vector<string> result = sol.firstKBinaryNumbers(k);

    cout << "Test " << testNum << " (" << description << "): ";
    if (result == expected)
    {
        cout << "PASS\n";
    }
    else
    {
        cout << "FAIL\n";
    }
    cout << "  Expected: ";
    printVector(expected);
    cout << "\n";
    cout << "  Actual:   ";
    printVector(result);
    cout << "\n\n";
}

int main()
{
    cout << "--- Running First K Binary Numbers Test Suite ---\n\n";

    runTest(1, "Zero Element (Edge Case)", 0, {});

    runTest(2, "Negative Element (Edge Case)", -5, {});

    runTest(3, "First Element Only", 1, {"0"});

    runTest(4, "Example 1 (k=5)", 5,
            {"0", "1", "10", "11", "100"});

    runTest(5, "Example 2 (k=10)", 10,
            {"0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"});

    return 0;
}