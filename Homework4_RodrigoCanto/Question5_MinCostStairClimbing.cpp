//Time Complexity: O(n), where n is the number of stairs.
//Space Complexity: O(1).

//Technique: DP (Tabulation).

#include "bits/stdc++.h"
using namespace std;

int solve_minCostStairClimbing(vector<int> &array){

    int n = array.size();

    //There is no need to step a stair.
    if(n == 1) return 0;

    //When calculating the minimum value for a specific stair we only care about the two previous stairs.
    int one_before_last_value = array[0];
    int last_value = array[1];

    for(int i = 2; i < n; ++i){

        //Transition
        int curr_value = min(one_before_last_value, last_value) + array[i];

        //Update the values to calculate correctly the next stair
        swap(one_before_last_value, last_value);
        swap(curr_value, last_value);
    }

    //We can stop at stair "n - 1" or stair "n - 2" so we take the minimum.
    return min(one_before_last_value, last_value);
}

int main(){

    vector<int> array = {4, 1, 6, 3, 5, 8};
    //vector<int> array = {11, 8, 3, 4, 9, 13, 10};

    cout << solve_minCostStairClimbing(array) << "\n";
    return 0;
}

//Time Spent: 10 minutes.