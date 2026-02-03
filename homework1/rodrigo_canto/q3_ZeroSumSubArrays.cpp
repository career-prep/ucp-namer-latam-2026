// Technique: One-directional running computation.

// Time Complexity: O(N) on average.
// Space Complexity: O(1).

#include <bits/stdc++.h>
using namespace std;

long long solve(const vector<int> &array){

    //We keep track of the frequencies for the sums of prefixes.
    unordered_map<long long, int> prefix_sum_frequency;

    //The empty array has sum zero.
    prefix_sum_frequency[0] = 1;

    long long current_sum = 0;
    long long answer = 0;

    for(long long value : array){
        
        current_sum = current_sum + value;

        /*
            Lets suppose that you have a prefix that ends at the index "r" with sum x.
            If you found earlier another prefix that ends at index "l" with sum x, then
            you have that the subarray [l + 1, r] has sum 0.

        */

        answer = answer + prefix_sum_frequency[current_sum];

        prefix_sum_frequency[current_sum]++;

    }

    return answer;
}

int main() {

    vector<vector<int>> cases;

    vector<int> case1 = {4, 5, 2, -1, -3, -3, 4, 6, -7};
    vector<int> case2 = {1, 8, 7, 3, 11, 9};
    vector<int> case3 = {8, -5, 0, -2, 3, -4};

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);

    for(auto &test_case: cases){
        cout << solve(test_case) << "\n";
    }

    return 0;
}

// Time: 10 minutes

