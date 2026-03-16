// Technique: Fixed-size sliding window

// Time Complexity: O(N)
// Space Complexity: O(1)

#include <bits/stdc++.h>
using namespace std;

double solve(const vector<int> &array, const int k){
    double current_sum = 0;

    //Get the first window of size k.
    //If n is the lenght of the array, we assume that n >= k.
    for(int i = 0; i < k; ++i){
        current_sum = current_sum + array[i];
    }

    //Get the mean for the first window.
    double mean = current_sum / (double)k;

    //Use two pointers to iterate through all the windows of size k.
    int l = 0, r = k - 1;

    while(r + 1 < (int)array.size()){
        

        //Update the location of the pointers to mantain the size.
        r++;
        current_sum = current_sum + array[r];
        current_sum = current_sum - array[l];
        l++;

        //Update the answer.
        //We use double type because the mean is not always an integer.
        double current_mean = current_sum / (double)k;

        mean = max(mean, current_mean);

    }

    return mean;
}

int main() {

    vector<pair<vector<int>, int>> cases;

    vector<int> array_case1 = {4, 5, -3, 2, 6, 1};
    int k_case1 = 2;

    vector<int> array_case2 = {4, 5, -3, 2, 6, 1};
    int k_case2 = 3;

    vector<int> array_case3 = {1, 1, 1, 1, -1, 2, -1, -1};
    int k_case3 = 3;

    vector<int> array_case4 = {1, 1, 1, 1, -1, -1, 2, -1, -1, 6};
    int k_case4 = 5;

    cases.emplace_back(make_pair(array_case1, k_case1));
    cases.emplace_back(make_pair(array_case2, k_case2));
    cases.emplace_back(make_pair(array_case3, k_case3));
    cases.emplace_back(make_pair(array_case4, k_case4));


    for(auto &test_case: cases){
        vector<int> array = test_case.first;
        int k = test_case.second;

        cout << fixed << setprecision(2) << solve(array, k) << "\n";
    }

    return 0;
}

// Time: 16 minutes

