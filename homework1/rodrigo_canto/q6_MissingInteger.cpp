// Technique: Math

// Time Complexity: O(N)
// Space Complexity: O(1)

#include <bits/stdc++.h>
using namespace std;

long long solve(const vector<long long> &array, long long n){

    //Use gauss formula to calculate the sum of the numbers from 1 to n.
    long long gauss_sum = n * (n + 1) / 2ll;
    long long sum = 0;

    //Calculate the sum of the array.
    for(long long value : array){
        sum = sum + value;
    }

    //The difference between the sums is the number that is missing.
    long long missing_element = gauss_sum - sum;

    return missing_element;

}

int main() {

    vector<pair<vector<long long>, long long>> cases;

    vector<long long> array_case1 = {1, 2, 3, 4, 6, 7};
    pair<vector<long long>, long long> case1 = make_pair(array_case1, 7ll);

    vector<long long> array_case2 = {1};
    pair<vector<long long>, long long> case2 = make_pair(array_case2, 2ll);

    vector<long long> array_case3 = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12};
    pair<vector<long long>, long long> case3 = make_pair(array_case3, 12ll);

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);


    for(auto &test_case: cases){

        vector<long long> array = test_case.first;
        long long n = test_case.second;

        cout << solve(array, n) << "\n";
    }

    return 0;
}

//There is another way to solve this problem with the same complexity using the bitwise operation XOR.

// Time: 8 minutes

