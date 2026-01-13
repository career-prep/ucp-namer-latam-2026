//Time Complexity: O(n) average-case
//Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

string solve(string &input){

    //Use an unorered set to keep track of distinct elements.
    unordered_set<char> distinct_elements;

    string answer = "";

    for(int i = 0; i < input.size(); ++i){
        int previous_size = distinct_elements.size();
        distinct_elements.insert(input[i]);
        int new_size = distinct_elements.size();

        //If the sizes are different that means we have a found a new character.
        if(previous_size != new_size){
            answer.push_back(input[i]);
        }
    }

    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    vector<string> cases;

    string case1 = "abracadabra";
    string case2 = "Uber Career Prep";
    string case3 = "zzyzx";

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);

    for(auto &test_case: cases){
        cout << solve(test_case) << "\n";
    }

    return 0;
}

//Time Spent: 10 minutes

