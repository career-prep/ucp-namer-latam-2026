/*Time Complexity:O(n)
Space Complexity:O(n)
Time taken: 37:10 left
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

/* psudocode/thoughts/logic
goal: return string with only unique characters from the given input string.
no restrictions going for optimization

strategy: same approach as the last problem we can do a hashset of characters,
check if the character exists in our result string. if not append it return the result.
finished with 37:10 left. same time and space complexity i believe. O(n) O(n)

*/

string firstOccurrence(string& word){
    string result = "";
    unordered_set<char> check;

    for(char c: word){
        if(!check.count(c)){

            check.insert(c);
            result+= c;
        }
    }

    return result;
 }

 




int main() {
    //example 1 from document
   string test1 = "abracadabra";
    cout << "Test 1 Result: " << firstOccurrence(test1) << " (Expected:  abrcd)" << endl;

    //example 2 from document
    string test2 = "Uber Career Prep";
    cout << "Test 2 Result: " << firstOccurrence(test2) << " (Expected: Uber CaPp)" << endl<< endl;


    return 0;
}

/* Total time spent: 3 minutes */