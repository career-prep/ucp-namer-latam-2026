/*Time Complexity: O(n^2)
Space Complexity: O(n)
Technique used: Hashing
Time Taken: 40min, could not solve
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

vector<vector<int>> zeroSumSubArrays(vector<int>& nums){
    vector<vector<int>> result;
    unordered_map<int, vector<int>> map;
    int runningSum = 0;

    map[0].push_back(-1);

    for(int i = 0; i<nums.size(); i++){
        runningSum += nums[i];

        if(map.find(runningSum) != map.end()){
            for(int index : map[runningSum]){
               // vector<int> sum(nums.begin() +)
                /*
                so what i want to do here is push the values from 
                nums starting at the matching index and ending at the current
                index but idk the syntax for it
                */
               //result.push_back(sum);
            }
        }
        map[runningSum].push_back(i);
    }

    return result;
}

int main(){
    vector<int> ex1 = {4, 5, 2, -1, -3, -3, 4, 6, -7};
    vector<vector<int>> result = zeroSumSubArrays(ex1);

    for(auto& output: result){
        cout << "[ ";
        for(int i = 0; i < output.size(); i++){
            cout << output[i] << " ";
        }
        cout << "], ";
    }

}

/* psudocode/thoughts/logic
goal: Find the number of subarrays that sum to zero
restraints: Must be a contigous array from the input when creating a sub
array

strategy:
So i'm thinking my solution would involve keeping a count or tally 
for each value going left to right and when we reach a point where 
the sum is 0 we can turn that into a subarray spanning from the beginning
of when i started keeping tally so for example if we have 

Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]

Sum at index 0: 4

Sum at index 1: 4 + 5 = 9

Sum at index 2: 9 + 2 = 11

Sum at index 3: 11 - 1 = 10

Sum at index 4: 10 - 3 = 7

Sum at index 5: 7 - 3 = 4 , we have seen 4 at index 0

We have a valid sub array at index 0 + 1 through index 5

We insert that into our result array and continue on


Examples:

Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
Output: 2 (Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])
Input Array: [1, 8, 7, 3, 11, 9] 
Output: 0
Input Array: [8, -5, 0, -2, 3, -4]
 Output: 2 (Subarrays: [0], [8, -5, 0, -2, 3, -4])
*/
