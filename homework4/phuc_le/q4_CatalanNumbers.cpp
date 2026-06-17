/*
    Technique:
    - Dynamic Programming (Bottom-Up)

    The problem statement gives the closed-form formula:
        - Cn = (2n)! / ((n+1)! n!)

    For implementation, we use the equivalent recurrence:
    - The nth Catalan number is defined by:
        C0 = 1
        Cn = sum(Ci * Cn-1-i), for i = 0 to n-1

    - Build the Catalan numbers from smaller to larger values.
    - Store all computed Catalan numbers in a DP array.
    - Each Catalan number depends on previously computed Catalan numbers (DP).
    - For each i:
        - Consider every possible split j.
        - The left subtree contributes Catalan[j].
        - The right subtree contributes Catalan[i-1-j].
        - Multiply the two values and add them to Catalan[i].

    Time Complexity: O(n²): n = input number
        - Outer loop runs n times.
        - Inner loop runs up to i times.

    Space Complexity: O(n)
        - Store Catalan numbers from C0 to Cn.

    Time spent: 40 minutes
*/

#include <iostream>
#include <vector>

using namespace std;

vector<long long> catalanNumbers(int n)
{
    vector<long long> catalan(n + 1);

    catalan[0] = 1;

    for (int i = 1; i <= n; i++)
    {
        catalan[i] = 0;

        for (int j = 0; j < i; j++)
        {
            catalan[i] += catalan[j] * catalan[i - 1 - j];
        }
    }

    return catalan;
}

int main()
{
    int n = 5;

    vector<long long> ans = catalanNumbers(n);

    cout << "Input: " << n << endl;
    cout << "Output: ";

    for (long long x : ans)
        cout << x << " ";

    cout << endl;

    return 0;
}