/*Time Complexity:O(n)
Space Complexity:O(1) 26 letters in alpha 
Technique used: Hashing
Time Taken: 10mins 46 secs
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

bool kAnagrams(string s1, string s2, int k){
    if (s1.length() != s2.length()) return false;

    int changesNeeded = 0;
    unordered_map<char, int> count;
    for(char letter: s1){
        count[letter]++;
    }
    for(char letter: s2){
        count[letter]--;
    }
    for(auto const& [letter, counts] : count){
        if(counts>0){
        changesNeeded+= counts;
        }
    }
    if(changesNeeded <= k) return true;
    return false;
}

/* psudocode/thoughts/logic
goal: Determine if two strings are k-anagrams
restraints: Must be same length strings.
strategy: My strategy going into this is just to sort each string and 
compare in line with one another, rack up a count for the different 
characters or unique characters then compare that to k, if less or = to 
then it works, if not then it does not. this is slow though. O(n log n)
to sort. we can try hashing. we can use a similar approach instead of 
sorting we can keep a count of the frequency of each character in the first
string and comapre it to the second string and calculate the difference
and compare that to k.

*/

int main(){
    string s1 = "apple", s2 = "peach";
    int k = 1;
    cout << "Expected: False" << endl;
    cout << "Output:   " << (kAnagrams(s1, s2, k) ? "True" : "False") << endl << endl;

    s1 = "apple"; s2 = "peach"; k = 2;
    cout << "Expected: True" << endl;
    cout << "Output:   " << (kAnagrams(s1, s2, k) ? "True" : "False") << endl << endl;

    s1 = "cat"; s2 = "dog"; k = 3;
    cout << "Expected: True" << endl;
    cout << "Output:   " << (kAnagrams(s1, s2, k) ? "True" : "False") << endl << endl;

    s1 = "debit curd"; s2 = "bad credit"; k = 1;
    cout << "Expected: True" << endl;
    cout << "Output:   " << (kAnagrams(s1, s2, k) ? "True" : "False") << endl << endl;

    s1 = "baseball"; s2 = "basketball"; k = 2;
    cout << "Expected: False" << endl;
    cout << "Output:   " << (kAnagrams(s1, s2, k) ? "True" : "False") << endl;

    return 0;
}
