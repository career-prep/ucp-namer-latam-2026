/*Time Complexity:O(n)
Space Complexity:O(n)
Time taken: 33:45 left
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

/* psudocode/thoughts/logic
goal: return sum of unique elements in an array
no implicit restraints, trying to maximize effciency and stick to the 
theme of hash .... O(1)/O(n) approach.

strategy:
instantly my goes to a one pass range based for loop where i'll
pretty much just check if the value exists in the hashset, if it does 
continue, if not add it to our total and into the hashset. this should
ensure we only get unique values in our solution. i think the key here
is using the hash SET to identify unique integers as we pass through the loop.

yeah pretty straight forward not too bad completion time 33:45 left i belive this is 
O(n) time and space for the same reason the last problem was. we have to pass through the entire array
so n is the size of the input and we much visit each value at least once.

*/

int uniqueSum(vector<int>& nums){
    int sum = 0;
    unordered_set<int> check;

    for(int num: nums){
        if(!check.count(num)) {
            sum+= num;
            check.insert(num);

    }
}

    return sum;
 }

 




int main() {
    //example 1 from document
    vector<int> test1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    cout << "Test 1 Result: " << uniqueSum(test1) << " (Expected: 33)" << endl;

    //example 2 from document
    vector<int> test2 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 6};
    cout << "Test 2 Result: " << uniqueSum(test2) << " (Expected: 35)" << endl<< endl;


    return 0;
}

/* Total time spent: 7 minutes */

