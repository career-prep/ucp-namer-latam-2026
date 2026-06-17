// Technique: Forward/backward two pointer

// Time Complexity: O(N)
// Space Complexity: O(N)

#include <bits/stdc++.h>
using namespace std;

//Function that return if a character is a vowel.
//We consider uppercase and lowercase letters.

bool isVowel(char c){

    if(c == 'a' || c == 'A') return true;
    if(c == 'e' || c == 'E') return true;
    if(c == 'i' || c == 'I') return true;
    if(c == 'o' || c == 'O') return true;
    if(c == 'u' || c == 'U') return true;
    
    //not a vowel
    return false;
}

void solve(string &input){

    //The main idea is to keep track of the positions of the vowels in an array.

    vector<int> vowel_positions;

    for(int i = 0; i < input.size(); ++i){
        
        char character = input[i];

        if(isVowel(character)){
            vowel_positions.emplace_back(i);
        }
    }

    //Reversing the vowels can be done using two pointers.
    //One pointer at the beginning and the other one at the end of the array.
    //We keep swapping values until the pointers meet.

    int l = 0, r = vowel_positions.size() - 1;

    while(l < r){
        
        int first_vowel_position = vowel_positions[l];
        int second_vowel_position = vowel_positions[r];

        swap(input[first_vowel_position], input[second_vowel_position]);

        l++; r--;
    }

    //No need to return the string because we update the original one.
    //We can see the result in the main function.
}

int main() {

    vector<string> cases;

    string case1 = "Uber Career Prep";
    string case2 = "xyz";
    string case3 = "flamingo";

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);

    for(auto &test_case: cases){
        solve(test_case);
        cout << test_case << "\n";
    }

    return 0;
}

// Time: 13 minutes

