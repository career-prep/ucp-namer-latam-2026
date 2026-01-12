#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

string firstOccurrence(string str) {
    unordered_set<char> seen;
    string result = "";
    for (char c : str) {
        if (!seen.count(c)) {
            result += c;
            seen.insert(c);
        }
    }
    return result;
}

int main() {
    cout << firstOccurrence("abracadabra") << endl;
    cout << firstOccurrence("Uber Career Prep") << endl;
    cout << firstOccurrence("zzyzx") << endl;
    return 0;
}

// Time spent: 9 minutes
