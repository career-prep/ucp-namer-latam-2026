// Technique: Sorting

// Time Complexity: O(N log n)
// Space Complexity: O(1)

#include <bits/stdc++.h>
using namespace std;

void solve(vector<long long> &array){

    //If we sort the array, equal elements will be together.
    sort(array.begin(), array.end());

    //We keep track of the position where we are going to insert the new element.
    int curr_position = 0;

    for(int i = 0; i < array.size(); ++i){
        
        /*
            We find a new element if we are at the beginning of the array
            or the previous element is different from the current one.
        */

        if(i == 0 || array[i] != array[i - 1]){
            array[curr_position] = array[i];
            curr_position++;
        }
    }

    int distinct_elements = curr_position;

    //We erase the remaining elements of the array because they are not different.
    while(array.size() > distinct_elements){
        array.pop_back();
    }

    for(long long value : array){
        cout << value << " ";
    }

    cout << "\n";

}

int main() {

    vector<vector<long long>> cases;

    vector<long long> case1 = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4};
    vector<long long> case2 = {0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15};
    vector<long long> case3 = {1, 3, 4, 8, 10, 12};

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);

    for(auto &test_case: cases){

        solve(test_case);
    }

    return 0;
}

// Time: 10 minutes

