/*
    Technique:
    - Dynamic Programming (Bottom-Up)

    - Let dp[i] = True if s[0...i-1] can be segmented.
      Otherwise, dp[i] = False.

    - Base case: dp[0] = true

    - For each position i:
        - Try every possible split point j, where j < i.
        - If:
            - s[0...j-1] can be segmented (dp[j] == true)
            - s[j...i-1] is a word
            => dp[i] = true.

    Recurrence:
        dp[i] = true
        if there exists a j < i such that
            dp[j] == true && s.substr(j, i-j) is in dict.

    - Ans = dp[n]

    Time Complexity: O(n²): n = length of the string
    Space Complexity: O(n)

    Time spent: 40 minutes
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

bool wordBreak(string s, unordered_set<string> &dict)
{
    int n = s.length();

    vector<bool> dp(n + 1, false);
    dp[0] = true;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (dp[j] &&
                dict.count(s.substr(j, i - j)))
            {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
}

int main()
{
    unordered_set<string> dict = {
        "elf",
        "go",
        "golf",
        "man",
        "manatee",
        "not",
        "note",
        "pig",
        "quip",
        "tee",
        "teen"};

    string s1 = "mangolf";
    string s2 = "manateenotelf";
    string s3 = "quipig";

    cout << s1 << ": "
         << (wordBreak(s1, dict) ? "True" : "False")
         << endl;

    cout << s2 << ": "
         << (wordBreak(s2, dict) ? "True" : "False")
         << endl;

    cout << s3 << ": "
         << (wordBreak(s3, dict) ? "True" : "False")
         << endl;

    return 0;
}