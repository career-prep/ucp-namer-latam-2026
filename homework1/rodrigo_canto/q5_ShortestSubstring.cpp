// Technique: Variable size sliding window.

// Time Complexity: O(N + M)
// Space Complexity: O(26)

/*
    I assume that the string only contains lowercase letters 
    and all the letters in the second string are contained in the first one.
*/

#include <bits/stdc++.h>
using namespace std;

void add_character(char character, vector<int> &frequency, int &covered_characters){

    int idx = character - 'a';

    //If the frequency is greater than zero that means the character is not covered so we update the number of characters covered.
    if(frequency[idx] > 0){
        covered_characters++;
    }

    frequency[idx]--;
}

void remove_character(char character, vector<int> &frequency, int &covered_characters){
    
    int idx = character - 'a';
    frequency[idx]++;
    
    //If the frequency is greater than zero that means we remove a character that was being covered.
    if(frequency[idx] > 0) covered_characters--;
}

double solve(const string &a, const string &b){

    vector<int> frequency(26);

    int n = a.size();
    int m = b.size();

    //Calculate the frequency of the characters for string b.

    for(auto character : b){

        //Mapping the letter to its corresponding index.
        int idx = character - 'a';
        frequency[idx]++;
    }

    int l = 0, r = -1;
    int covered_characters = 0;
    int answer = 1e9;
    
    while(r < n){

        //Keep considering more elements until we find them all.
        while(r + 1 < n && covered_characters < m){
            add_character(a[r + 1], frequency, covered_characters);
            r++;
        }

        //If all the characters are covered we update our answer.
        if(covered_characters == m) answer = min(answer, r - l + 1);
        else break;

        //Reduce the size of the window to find a better answer.
        remove_character(a[l], frequency, covered_characters);
        l++;
    }

    return answer;
}

int main() {

    vector<pair<string, string>> cases;

    pair<string, string> case1 = make_pair("abracadabra", "abc");
    pair<string, string> case2 = make_pair("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx");
    pair<string, string> case3 = make_pair("dog", "god");

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);


    for(auto &test_case: cases){
        
        string a = test_case.first;
        string b = test_case.second;

        cout << solve(a, b) << "\n";
    }

    return 0;
}

// Time: 14  minutes

