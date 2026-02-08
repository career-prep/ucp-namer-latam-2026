#include <iostream>
#include <string>
#include <unordered_map>
#include <climits>
using namespace std;

//uses a sliding window to find the shortest substring containing all required chars in O(n)
int shortestSubstring(const string& s, const string& req) {
    unordered_map<char, int> need;
    for (char c : req) {
        ++need[c];
    }
    unordered_map<char, int> window;
    int have = 0; //number of unique chars in req that are satisfied in the window
    int total = need.size(); //number of unique chars to satisfy
    int minLen = INT_MAX;
    int left = 0;
    for (int right = 0; right < (int)s.size(); ++right) {
        ++window[s[right]];
        if (need.contains(s[right]) && window[s[right]] == need[s[right]]) {
            ++have;
        }
        while (have == total) { //shrink window from left
            minLen = min(minLen, right - left + 1);
            --window[s[left]];
            if (need.contains(s[left]) && window[s[left]] < need[s[left]]) {
                --have;
            }
            ++left;
        }
    }
    return (minLen == INT_MAX) ? -1 : minLen;
}

int main() {
    cout << shortestSubstring("abracadabra", "abc") << endl; // 4
    cout << shortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx") << endl; // 10
    cout << shortestSubstring("dog", "god") << endl; // 3

    return 0;
}

//time spent: 20 minutes
