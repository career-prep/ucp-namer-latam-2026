//Time Complexity: O(n) average-case
//Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

long long solve(const vector<int> &array){

    //Use an unordered set to keep track of distinct elements.
    unordered_set<long long> distinct_elements;

    for(long long value : array){
        distinct_elements.insert(value);
    }

    long long answer = 0;
    
    //Iterate through the set and add the value of the current element to the answer.
    for(auto element: distinct_elements){
        answer = answer + element;
    }

    return answer;
}

int main() {

    vector<vector<int>> cases;

    vector<int> case1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    vector<int> case2 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 6};

    cases.emplace_back(case1);
    cases.emplace_back(case2);

    for(auto &test_case: cases){
        cout << solve(test_case) << "\n";
    }

    return 0;
}

//Time Spent: 8 minutes