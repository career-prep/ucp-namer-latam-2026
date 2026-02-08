#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

//uses two pointers to reverse the order of vowels in a string in O(n)
string reverseVowels(string s) {
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    int left = 0;
    int right = s.size() - 1;
    while (left < right) { //move pointers to vowels index
        if (!vowels.contains(s[left])) {
            ++left;
            continue;
        }
        if (!vowels.contains(s[right])) {
            --right;
            continue;
        }
        swap(s[left], s[right]);
        ++left;
        --right;
    }
    return s;
}

int main() {
    cout << reverseVowels("Uber Career Prep") << endl; // eber Ceraer PrUp
    cout << reverseVowels("xyz") << endl; // xyz
    cout << reverseVowels("flamingo") << endl; // flominga

    return 0;
}

//time spent: 5 minutes
