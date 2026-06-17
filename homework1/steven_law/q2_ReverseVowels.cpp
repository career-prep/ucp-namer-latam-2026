/*Time Complexity:O(n)
Space Complexity:O(1)
Technique used:Two Pointer
Time Taken: 36min 58 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

string reverseVowels(string s){
    int l = 0;
    int r = s.length() - 1;
    string vowels = "aeiouAEIOU";

    while(l<r){
        while(l<r && vowels.find(s[l]) == string::npos){ //search through vowels if foound breaks loop else not found the find method returns -1, string::npos or no position is -1 so it becomes true and continue the loop
            l++;
        }
        while(l<r && vowels.find(s[r]) == string::npos){
            r--;
        }

        if(l<r){
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;

            l++;
            r--;
        }
    }
    
    return s;
}

int main(){
string input = "Uber Career Prep"; 
string result = reverseVowels(input);

cout << result; //"eber Ceraer PrUp"


}

/* psudocode/thoughts/logic
goal: Reverse only the vowels in a string
restraints: Optimize time and space complex
strategy: 
Traverse through string, push each vowel to stack in order,
Traverse through string again swap each vowel with stack.top()
Pop the top after swapping and continue till loop termination
Not optimal O(n) space....


"Uber Career Prep"
u e a e e e 
e e e a e u 

eber ceraer prUp
if its a vowel stack it 
loop through array again remove the vowel and replace 


I need to solve in a way that does not require the use of 
data structures that'll take up O(n) space.

Hardcoded size when using string/array is O(1) we can use two pointer
method with a hardcoded string named "vowels".
We have a pointer on the left side index 0 and on the right index 
length - 1.
We can swap when they are both vowels , using a temp to prevent data loss.
Our loop condition is l<r. Once the loop terminates we should have reversed 
the vowels successfullly.

"Uber Career Prep"
u e a e e e 

1. e e a e e u
2. e e a e e u
3. e e e a e u
termination 
"eber Ceraer PrUp"


*/
