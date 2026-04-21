#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

//uses hash maps to count character differences and check if at most k changes make anagrams in O(n)
bool kAnagrams(const string& s1, const string& s2, int k) {
    if (s1.size() != s2.size()) {
        return false;
    }
    unordered_map<char, int> count;
    for (char c : s1) {
        ++count[c];
    }
    for (char c : s2) {
        --count[c];
    }
    int changes = 0;
    for (const auto& p : count) { //summing pos and neg mirrors, so count one side is sufficient
        if (p.second > 0) {
            changes += p.second;
        }
    }
    return changes <= k;
}

int main() {
    cout << boolalpha;
    cout << kAnagrams("apple", "peach", 1) << endl; // false
    cout << kAnagrams("apple", "peach", 2) << endl; // true
    cout << kAnagrams("cat", "dog", 3) << endl; // true
    cout << kAnagrams("debit curd", "bad credit", 1) << endl; // true
    cout << kAnagrams("baseball", "basketball", 2) << endl; // false

    return 0;
}

//time spent: 10 mins
