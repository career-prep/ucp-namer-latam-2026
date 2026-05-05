//Time Complexity: O(N).
//Space Complexity: O(N).
//Technique: Stack.

//N is the number of characters in the string.

#include "bits/stdc++.h"
using namespace std;

void solveReversedWords(string &s){

    s.push_back(' ');

    string word = "";

    //Pushing the words into the stack allows us to recover them later in reversed order.
    stack<string> words;

    for(char c : s){

        if(c == ' '){
            words.push(word);
            word = "";
        }
        else word.push_back(c);
    }

    while(!words.empty()){
        cout << words.top() << " ";
        words.pop();
    }
}

int main() {

    //string s = "Uber Career Prep";
    string s = "Emma lives in Brooklyn, New York.";

    solveReversedWords(s);

    return 0;
}

//Time Spent: 10 minutes