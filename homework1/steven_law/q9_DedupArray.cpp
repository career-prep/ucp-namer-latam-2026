/*Time Complexity: O(n)
Space Complexity: O(1)
Technique used: two pointers
Time Taken: 6min 47sec
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

vector<int> dedupArray(vector<int>& nums){
    int j = 0;

    for(int i = 1; i<nums.size(); i++){
        if(nums[i] != nums[j]){
            j++;
            nums[j] = nums[i];

        }
    }
    fill(nums.begin() + j + 1, nums.end(), -1);

    

    return nums;
}

int main(){
    vector<int> arr1 = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4};
    vector<int> result1 = dedupArray(arr1);
    
    cout << "Expected: [1, 2, 3, 4, -1, -1, -1, -1, -1, -1]" << endl;
    cout << "Output:   [";
    for(int i = 0; i < result1.size(); i++){
        cout << result1[i];
        if(i < result1.size() - 1) cout << ", ";
    }
    cout << "]" << endl << endl;

    vector<int> arr2 = {0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15};
    vector<int> result2 = dedupArray(arr2);
    
    cout << "Expected: [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1]" << endl;
    cout << "Output:   [";
    for(int i = 0; i < result2.size(); i++){
        cout << result2[i];
        if(i < result2.size() - 1) cout << ", ";
    }
    cout << "]" << endl << endl;

    vector<int> arr3 = {1, 3, 4, 8, 10, 12};
    vector<int> result3 = dedupArray(arr3);
    
    cout << "Expected: [1, 3, 4, 8, 10, 12]" << endl;
    cout << "Output:   [";
    for(int i = 0; i < result3.size(); i++){
        cout << result3[i];
        if(i < result3.size() - 1) cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}

/* psudocode/thoughts/logic
goal: Remove duplicates from an array
restraints: N/A
strategy:
so we want {1, 2, 2, 3, 3, 3, 4, 4, 4, 4} to look like
{1, 2, 3, 4, -1, -1, -1, -1, -1, -1}
and we need to do this optimally. I think we can traverse the given array
and keep two pointers, i and j. i will discover unique values, and j will
copy the values in order. so for instance if we use the example above
we can set i = 1 and j = 0. so nums[j] = 1 , nums[i] = 2. Whenever 
i envounters a new value like right now we can increment j and copy.
so now j = 1 after j++. now since we are using a for loop i increments
on every loop so now i = 2 and nums[i] = 2 which is the same as nums[j]
so we can ingore it. now i = 3 and nums[i] = 3. 3 != 2 so we increment j
and copy so now the array looks like this so far {1,2,3,3,....} and as we
continue we should have all the unique values at the front. 
we encounter one issue though we have a bunch of 4s stuck at the end and
since we are using cpp we are dealing with static arrays so we must 
substiute the rest of the dupes for -1. 

to do this we simply take j since its the last unique values index and
we go from j+1 to the end of the array and replace it with -1, idk if 
i have to create another loop or if theres an inline function/method 
that does this for me. after that we should be able to return our 
nmodified array

*/