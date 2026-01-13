//Time Complexity: O(n) average-case
//Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

string solve(const string &input){

    //Use an unordered set to keep track of distinct elements.
    unordered_set<char> distinct_elements;

    string answer = "";

    for(char character : input){
        int previous_size = distinct_elements.size();
        distinct_elements.insert(character);
        int new_size = distinct_elements.size();

        //If the sizes are different that means we have a found a new character.
        if(previous_size != new_size){
            answer.push_back(character);
        }
    }

    return answer;
}

int main() {

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

