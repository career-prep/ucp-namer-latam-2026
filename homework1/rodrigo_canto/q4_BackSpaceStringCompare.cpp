// Technique: Stack

// Time Complexity: O(N)
// Space Complexity: O(N)

#include <bits/stdc++.h>
using namespace std;

//We can simulate the backspace effect using a stack.

stack<char> process(const string &s){

    stack<char> result;

    for(char character : s){
        
        //if we find a backspace we erase the last character written, otherwise we insert the character at the top of the stack.
        if(character == '#'){
            if(!result.empty()){
                result.pop();
            }
        }
        else{
            result.push(character);
        }
    }

    return result;

}

double solve(const string &a, const string &b){

    stack<char> first_string = process(a);
    stack<char> second_string = process(b);

    //If the content for both stacks is the same, the result is the same.

    if(first_string.size() != second_string.size()) return false;

    while(!first_string.empty()){

        char first_char = first_string.top();
        char second_char = second_string.top();

        if(first_char != second_char) return false;
        
        first_string.pop();
        second_string.pop();
    }

    return true;
}

int main() {

    vector<pair<string, string>> cases;

    pair<string, string> case1 = make_pair("abcde", "abcde");
    pair<string, string> case2 = make_pair("Uber Career Prep", "u#Uber Careee#r Prep");
    pair<string, string> case3 = make_pair("abcdef###xyz", "abcw#xyz");
    pair<string, string> case4 = make_pair("abcdef###xyz", "abcdefxyz###");


    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);
    cases.emplace_back(case4);


    for(auto &test_case: cases){
        
        string a = test_case.first;
        string b = test_case.second;

        if(solve(a, b)) cout << "True" << "\n";
        else cout << "False" << "\n";
    }

    return 0;
}

// Time: 10 minutes

