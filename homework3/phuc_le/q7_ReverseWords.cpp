// Assume no multiple white space or trailing zeros at beginning and ending
/*
    Data Structure: String / Array
    Algorithm: In-place Reversal (Two-pointer technique)

    First, reverse the entire string. This puts the words in the correct reversed order,
    but the characters within each word are also backwards.
    Iterate through the string to find the start and end boundaries of each word (separated by spaces).
    Whenever a word boundary or the end of the string is reached, reverse just that specific word
    to restore its original internal character order.

    Time Complexity: O(N), where N is the length of the string.
    Space Complexity: O(1) auxiliary space, as the string modifications are done in-place

    Time: 40 mins
*/

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string reverseWords(string s)
{
    // Reverse the whole string, words in correct places but the inside are reversed
    reverse(s.begin(), s.end());

    int n = s.length();
    int start = 0; // Start index of a word

    // Reverse each word in the reversed string to correct their positions
    for (int end = 0; end <= n; end++)
    {
        // Reverse the last word also when end reaches the end of the string
        if (end == n || s[end] == ' ')
        {
            // Reverse the current word
            reverse(s.begin() + start, s.begin() + end);
            start = end + 1; // Move to the start of the next word
        }
    }
    return s;
}

void runTest(int testNum, const string &description, const string &input, const string &expected)
{
    string result = reverseWords(input);

    cout << "Test " << testNum << " (" << description << "): ";

    if (result == expected)
    {
        cout << "PASS\n";
    }
    else
    {
        cout << "FAIL\n";
    }
    cout << "  Input:    \"" << input << "\"\n";
    cout << "  Expected: \"" << expected << "\"\n";
    cout << "  Actual:   \"" << result << "\"\n";
    cout << "\n";
}

int main()
{
    cout << "--- Running ReverseWords Test Suite ---\n\n";

    // 1. Standard base cases
    runTest(1, "Standard Case 1",
            "Uber Career Prep",
            "Prep Career Uber");

    runTest(2, "Standard Case 2 (Punctuation)",
            "Emma lives in Brooklyn, New York.",
            "York. New Brooklyn, in lives Emma");

    // 3. Edge Case: Empty String
    runTest(3, "Empty String",
            "",
            "");

    // 4. Edge Case: Single Word
    runTest(4, "Single Word",
            "Algorithm",
            "Algorithm");

    // 5. Edge Case: Mixed Numbers and Symbols
    runTest(5, "Numbers and Symbols",
            "C++ 17 is 100% great!",
            "great! 100% is 17 C++");

    return 0;
}