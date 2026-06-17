/*Data Structure: Stack
Time Complexity: O(n)
Space Complexity: O(n)
Time Taken: 11 mins 53 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>
#include <stack>
#include <sstream>

using namespace std;

string reverseWords(string s){
    stack<string> st;
    stringstream ss(s);
    string word;

    while(ss >> word){
        st.push(word);
    }

    string result;
    while(!st.empty()){
        result += st.top();
        st.pop();
        if(!st.empty()) result += " ";
    }

    return result;
}

int main(){
    string s1 = "Uber Career Prep";
    cout << reverseWords(s1) << endl;

    string s2 = "i love food, its the best.";
    cout << reverseWords(s2) << endl;
}

/* psudocode/thoughts/logic
goal: reverse the order of space separated words in a string
restraints: keep the punctuation attached to its word (so "best." stays as "best.")

strategy: stack = reversing things. push every word in order onto
a stack, then pop off and concatenate to build the result

i used stringstream to split on spaces because thats the way to ik how to tokenize in c++.
could also do this with two pointers from the end without a stack but the question wants us
to identify the data structure so stack it is.
*/
