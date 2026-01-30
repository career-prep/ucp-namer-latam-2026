/*Time Complexity:O(n)
Space Complexity:O(1)
Technique used:Sliding Window
Time Taken: 6 min 40 secs
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>
#include<algorithm>

using namespace std;


double maxMeanSubArray(vector<int>& nums, int k){

    double total = 0;
   
    for(int i = 0; i<k; i++){
        total+= nums[i];
    }

    double maxTotal = total;

    for(int i = k; i<nums.size(); i++){
        total += nums[i] - nums[i-k];

        maxTotal = max(maxTotal, total);
    }

    return maxTotal / k;

}

int main() {
    vector<int> ex1 = {4, 5, -3, 2, 6, 1};
    int k = 2;

    double result = maxMeanSubArray(ex1, k);

    cout << result << endl;

    return 0;

}

/* psudocode/thoughts/logic
goal: Find the subarray with the maximum mean (average)
restraints: Subarray means it has to be contiguous.
strategy: We need to find the total for all the 
subarrays, then take the max total and divide it by k to 
get the mean. We can start by taking the total of the
first subarray and use that value to initialize our 
"max total". We theen use a sliding window approach 
and use i-k as like the left end of our window and i
as the right end. On every pass through the loop we 
update the current total and compare it to our max.
Once we reach loop termination we should be left with our
true max total and then we just divide by k and return it.

*/