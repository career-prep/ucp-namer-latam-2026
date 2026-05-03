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

struct TestCase
{
    string name;
    int k;
    vector<string> expected;
};

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

int main()
{
    vector<TestCase> testCases = {
        {"Zero Element (Edge Case)", 0, {}},
        {"Negative Element (Edge Case)", -5, {}},
        {"First Element Only", 1, {"0"}},
        {"Example 1 (k=5)", 5, {"0", "1", "10", "11", "100"}},
        {"Example 2 (k=10)", 10, {"0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"}}};

    Solution sol;
    int passed = 0;

    cout << "=== FIRST K BINARY NUMBERS TEST EXECUTION ===\n\n";

    for (const auto &tc : testCases)
    {
        vector<string> result = sol.firstKBinaryNumbers(tc.k);

        if (result == tc.expected)
        {
            passed++;
            cout << "✅ Passed: " << tc.name << "\n";
        }
        else
        {
            cout << "❌ Failed: " << tc.name << "\n   Expected: ";
            printVector(tc.expected);
            cout << "\n   Got:      ";
            printVector(result);
            cout << "\n";
        }
    }

    cout << "\n--- Final Results: " << passed << "/" << testCases.size() << " Tests Passed ---\n";

    return 0;
}