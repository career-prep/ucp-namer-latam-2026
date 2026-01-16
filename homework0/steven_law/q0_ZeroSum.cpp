/*Time Complexity:O(n)
Space Complexity:????? maybe O(n)...
Time Taken: 14mins 36sec left after solving initial problem
            9mins 27secs left to solve follow up
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

/* psudocode/thoughts/logic
goal = return total number of pairs that sum to zero example (1,-1)(2,-2)
restraints = we can only use a value at its respected index once. 

strategy = i realize that for a pair to sum to zero the x and y must be inverse pairs along their axises
otherwise this is impossible. let me make sure this is correct... yeah i belelive this checks out

possible solutions include: (x,-x) or (-x,x) everything else should not work

so i believe using a hashmap here is most optimal since accessing is O(1) time

we can create a hashmap and map the values to their index on the first pass
using the example we shuold get somehting like this
vector<int> test1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1}; 
unordered_map<int, int> pairs = {(0,1), (1,10), (2,8), (3,3) (4,2), (5,5), (6,7), (7,2), (8,-2), (9,-1)}
now the next step i think is to grab a value at each index starting from the begin and seeing if there exists a matching pair.
using our logic from before we know if we have x we need -x so we can check if we have it in O(1) time, and if we do, we can remove
both pairs from the map and continue down the line. i believe this should work. if its empty ill return 0 as an edge case.

okay this did not work i need to back track my logic. so the issue is that im getting errors because i cannot
modify a hashmap during a loop, its causing a segmentation fault. i need to do it all in one pass.
i can check if the elemnt exists(-x) in the first loop on the first pass and determine if that works.
a slighlty altered approach, i can keep a count for x and -x appearnces if x = 1, we check if -1 exists
if so decrement the count of -1 and increment our total count and dont even bother incrementing at pairs[x]
if it does not exist we then increment it like this pairs[x]++.

okay i completed the first version of the problem with 14mins 36sec left time complex is O(n). since we go through
the array once and the input can be n size. idk space complexity but im assuming its O(n) since thats all the space
we are using, the hashmap is storing n distinct nums.
now we can reuse elements. im assuming i can now remove the pairs[x]-- and leave it be. if we find an -x value
we can just increment the count based on how many pairs[-x] we have. 

this worked with 9mins 27secs left. still dont know space complexity, im assuming since its one pass and hashing
that time complexity is O(n) because we go through an array of n size. 

*/

int zeroSum(vector<int>& nums){
    unordered_map<int,int> pairs;
    int count = 0;

    for (int x : nums) {
        if (pairs[-x] > 0) {   
            pairs[-x]--;
            count++;              
        } else {
            pairs[x]++;          
        }
    }
    return count;
 }

 //////// flawed logic, had to review my approach...
 //at this point we should have
 //unordered_map<int, int> pairs = {(0,1), (1,10), (2,8), (3,3) (4,2), (5,5), (6,7), (7,2), (8,-2), (9,-1)}
/*int count = 0;
i = 0;
for(auto& pair: pairs){
    int x = pair.second;
    if(pairs.count(-x)){
        int j = pairs[-x];

        count++;
        pairs.erase(i);
        pairs.erase(j);
    }
}
*/


int followUp(vector<int>& nums){
 if(nums.empty()) return 0;
unordered_map<int,int> pairs; 
    int count = 0;

    for (int x : nums) {
        count += pairs[-x]; 
        pairs[x]++;    
    }   
    return count;
}

int main() {
    //example 1 from document
    vector<int> test1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    cout << "Test 1 Result: " << zeroSum(test1) << " (Expected: 2)" << endl;

    //example 2 from document
    vector<int> test2 = {1, 10, 8, -2, 2, 5, 7, 2, -2, -1};
    cout << "Test 2 Result: " << zeroSum(test2) << " (Expected: 3)" << endl<< endl;

    vector<int> followUp1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    cout << "Test 1 Result: " << followUp(followUp1) << " (Expected: 3)" << endl;

  
    vector<int> followUp2 = {1, 10, 8, -2, 2, 5, 7, 2, -2, -1};
    cout << "Test 2 Result: " << followUp(followUp2) << " (Expected: 5)" << endl;

    return 0;
}

/* Total time spent: 26 minutes for first then 5 minutes for second */