/*Data Structure: hash set (dictionary) + dp array
Algorithm: tabulation over prefixes
Technique: dynamic programming (tabulation)
Time Complexity: O(n^2 * L) — n=string len, substring+lookup cost L
Space Complexity: O(total dict chars) + O(n)
Time Taken: 24 mins 12 seconds
*/

#include<iostream>
#include<vector>
#include <string>
#include <unordered_set>

using namespace std;

/*
1. dump dict into a set (lowercase), lowercase the input.
2. dp[i] = can s[0..i) be split into valid words. dp[0] = true (empty string).
3. dp[i] = true if there is some j<i where dp[j] is true AND s[j..i) is in the dict.
4. answer = dp[n].
*/

bool WordBreak(string s, vector<string> dictionary){
    unordered_set<string> dict;
    for(string w : dictionary){
        for(char& ch : w) ch = tolower(ch);
        dict.insert(w);
    }
    for(char& ch : s) ch = tolower(ch);

    int n = s.size();
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    for(int i = 1; i <= n; i++){
        for(int j = 0; j < i; j++){
            if(dp[j] && dict.count(s.substr(j, i - j))){
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}

int main(){
    vector<string> dictionary = {
        "elf","go","golf","man","manatee","not","note","pig","quip","tee","teen"
    };

    cout << boolalpha;
    cout << "mangolf        Actual: " << WordBreak("mangolf", dictionary)       << "  Expected: true"  << endl;
    cout << "manateenotelf  Actual: " << WordBreak("manateenotelf", dictionary) << "  Expected: true"  << endl;
    cout << "quipig         Actual: " << WordBreak("quipig", dictionary)        << "  Expected: false" << endl;
}

/* psudocode/thoughts/logic
goal: can the no-spaces string be cut into valid dict words
restraints: greedy doesnt work (a long word can swallow letters a later split needs), so its dp

strategy: dp over prefixes. dp[i] answers "is s[0..i) fully breakable". it is if some earlier cut
point j is breakable (dp[j]) and the chunk s[j..i) is a real word. dp[0]=true seeds it (empty
prefix). set gives O(1)-ish word lookups; a trie would work too if i wanted to walk chars instead
of slicing substrings.

quipig fails because no valid split exists — "quip"+"ig"? ig isnt a word. "qu..."? not a word.
every path dead-ends so dp[n] stays false.
*/
