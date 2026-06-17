// Technique: Hash-Map, frequencies.

// Time Complexity: O(N) on average.
// Space Complexity: O(N)

#include <bits/stdc++.h>
using namespace std;

bool solve(const string &a, const string &b, const int k){

    //If the sizes are different, then it is not possible to convert one into the other.
    if(a.size() != b.size()) return false;

    //Use an unordered_map to keep track of the frequencies for both strings.
    unordered_map<char, int> frequency_a, frequency_b;

    for(char character : a){
        frequency_a[character]++;
    }

    for(char character : b){
        frequency_b[character]++;
    }

    int moves_a_to_b = 0, moves_b_to_a = 0;

    //Try to convert b into a.
    for(auto element: frequency_a){
        int key = element.first;
        int value = element.second;

        moves_b_to_a = moves_b_to_a + max(0, value - frequency_b[key]);
    }

    //Try to convert a into b.
    for(auto element: frequency_b){
        int key = element.first;
        int value = element.second;

        moves_a_to_b = moves_a_to_b + max(0, value - frequency_a[key]);
    }

    //Take the minimum and check if that minimum is less than or equal to k.
    return min(moves_a_to_b, moves_b_to_a) <= k;

}

int main() {

    vector<pair<pair<string, string>, int>> cases;

    pair<pair<string, string>, int> case1 = make_pair(make_pair("apple", "peach"), 1);
    pair<pair<string, string>, int> case2 = make_pair(make_pair("apple", "peach"), 2);
    pair<pair<string, string>, int> case3 = make_pair(make_pair("cat", "dog"), 3);
    pair<pair<string, string>, int> case4 = make_pair(make_pair("debit curd", "bad credit"), 1);
    pair<pair<string, string>, int> case5 = make_pair(make_pair("baseball", "basketball"), 2);


    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);
    cases.emplace_back(case4);
    cases.emplace_back(case5);


    for(auto &test_case: cases){

        string a = test_case.first.first;
        string b = test_case.first.second;
        int k = test_case.second;

        if(solve(a, b, k)) cout << "True" << "\n";
        else cout << "False" << "\n";
    }

    return 0;
}

// Time: 15 minutes

