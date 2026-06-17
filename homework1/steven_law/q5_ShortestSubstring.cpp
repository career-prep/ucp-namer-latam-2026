/*Time Complexity: O(n)
Space Complexity: O(1)
Technique used: Hashing/Slidinf Window
Time Taken: 23mins 29 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

int shortestSubstring(string s, string t){

    unordered_map<char, int> charCount;
    for (char ch : t){
        charCount[ch]++;
    } 

    int targetCharsRemaining = t.length();
    int minLen = INT_MAX;
    int startIndex = 0;
    int left = 0;

    for (int right = 0; right < s.length(); right++) {
        char ch = s[right];
        
        if (charCount.find(ch) != charCount.end() && charCount[ch] > 0) {
            targetCharsRemaining--;
        }
        charCount[ch]--;

        if (targetCharsRemaining == 0) {
            while (true) {
                char charAtStart = s[left];

                if (charCount.find(charAtStart) != charCount.end() && charCount[charAtStart] == 0) {
                    break;
                }
                charCount[charAtStart]++;
                left++;
            }

            minLen = min(minLen, right - left + 1);

            charCount[s[left]]++;
            targetCharsRemaining++;
            left++;
        }
    }
    if(minLen == INT_MAX) return 0;
    return minLen;

}



int main() {
    // Test case 1
    string s1 = "abracadabra";
    string t1 = "abc";
    cout << "Result: " << shortestSubstring(s1, t1) << endl;
    cout << "Expected: brac (length 4)" << endl << endl;
    
    // Test case 2
    string s2 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx";
    string t2 = "zzyzx";
    cout << "Result: " << shortestSubstring(s2, t2) << endl;
    cout << "Expected: zzxwdcbxyz (length 10)" << endl << endl;
    
    // Test case 3
    string s3 = "dog";
    string t3 = "god";
    cout << "Result: " << shortestSubstring(s3, t3) << endl;
    cout << "Expected: dog (length 3)" << endl;
    
    return 0;
}

/* psudocode/thoughts/logic
goal: Find the shortest substring containing all unique characters
restraints: N/A
strategy: Use a sliding window approach with two pointers. 
Expand the right pointer until all characters in t are included in
the current window. Once all characters are included, shrink the
window from the left while maintaining inclusion of all characters 
in t. Track the minimum length of such valid windows.

*/