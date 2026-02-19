#include <iostream>
#include <string>
using namespace std;

//processes a string by applying backspaces (#) and returns the result
string processBackspaces(const string& s) {
    string result;
    for (char c : s) {
        if (c == '#') {
            if (!result.empty()) {
                result.pop_back();
            }
            continue;
        }
        result += c;
    }
    return result;
}

//compares two strings after applying backspaces in O(n + m)
bool backspaceStringCompare(const string& s1, const string& s2) {
    return processBackspaces(s1) == processBackspaces(s2);
}

int main() {
    cout << boolalpha;
    cout << backspaceStringCompare("abcde", "abcde") << endl; // true
    cout << backspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep") << endl; // true
    cout << backspaceStringCompare("abcdef###xyz", "abcw#xyz") << endl; // true
    cout << backspaceStringCompare("abcdef###xyz", "abcdefxyz###") << endl; // false

    return 0;
}

//time spent: 12 minutes
