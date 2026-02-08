/*Time Complexity: O(N+M)
Space Complexity:O(1)
Technique used: Two Pointers
Time Taken: 31mins 56seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

bool backspaceCompare(string s, string t){
    int i = s.length() - 1;
    int j = t.length() - 1;

    int skipS = 0;
    int skipT = 0;

    while (i >= 0 || j >= 0) {

        while (i >= 0) {
            if (s[i] == '#') {
                skipS++;
                i--;
            } else if (skipS > 0) {
                skipS--;
                i--;
            } else {
                break; 
            }
        }

        while (j >= 0) {
            if (t[j] == '#') {
                skipT++;
                j--;
            } else if (skipT > 0) {
                skipT--;
                j--;
            } else {
                break; 
            }
        }

        if (i >= 0 && j >= 0) {
            if (tolower(s[i]) != tolower(t[j])) {
                return false;
            }
        } 
        else if ((i >= 0) != (j >= 0)) {
            return false;
        }
        i--;
        j--;
    }

    return true;
}

int main(){

    string s1 =  "abcde";
    string t1 =  "abcde";


    string s2 = "Uber Career Prep";
    string t2 = "u#Uber Careee#r Prep";

    string s3 = "abcdef###xyz";
    string t3 = "abcdefxyz###";

    cout << backspaceCompare(s1, t1) <<  endl;
    cout << backspaceCompare(s2, t2) <<  endl;
    cout << backspaceCompare(s3, t3) <<  endl;

    cout << "expected results: " << endl << "1 " << endl << "1 "<< endl << "0";
}
/* psudocode/thoughts/logic
goal: Compare two strings where '#' represents backspace
restraints: # deletes the character before it 
strategy:
i think if we just go through the string backwards from end to begining and skip the
characters following the # we should be able to get our result. we will need to create 
two new strings for this approach though. i think if we delete the character after the # and
the # we shouldnt have to create a new string. if we modify the string in the middle of 
a loop there will be errors though.. we have to compare s and t in one loop and doge the chars
after the #'s so we can traverse this string backwards and compare s and t at every char,
if s or t = # we simply compare the following char after the delted one and continue until
termination.?

"Uber Career Prep", "u#Uber Careee#r Prep"
s: perp reerac rebu , done
t: perp r skip e, eerac rebu skip u , done = perp eerac rebu

examples:

Input Strings: "abcde", "abcde"
Output: True

Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
Output: True

Input Strings: "abcdef###xyz", "abcw#xyz"
Output: True

Input Strings: "abcdef###xyz", "abcdefxyz###"
Output: False
*/
