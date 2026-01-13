//Time Complexity: O(n) average-case
//Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

int solve(vector<int> &array){

    //Use an unorered set to keep track of distinct elements.
    unordered_set<int> distinct_elements;

    for(int i = 0; i < array.size(); ++i){
        distinct_elements.insert(array[i]);
    }

    int answer = 0;
    
    //Iterate through the set and add the value of the current element to the answer.
    for(auto element: distinct_elements){
        answer = answer + element;
    }

    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

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