//Time Complexity: O(n) average-case
//Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

int solve(vector<int> &array){

    //Use an unordered map to keep track of the frequency of the elements.
    unordered_map<int,int> frequency_positives;
    unordered_map<int,int> frequency_negatives;
    
    //Consider the number zero as a special case that will be covered later.
    int count_zero = 0;

    //Update the data structure according to the value that is found.
    for(int i = 0; i < array.size(); ++i){
        if(array[i] == 0){
            count_zero++;
            continue;
        }
        if(array[i] > 0) frequency_positives[array[i]]++;
        else frequency_negatives[array[i]]++;
    }

    int answer = 0;

    /*
        Iterate through the frequency of the positive elements and calculate its negative value.
        If the negative value does not exist in the data structure C++ automatically inserts this value
        with a frequency of zero, so the answer will not be affected.

        The number of pairs for that particular value will be the minimum between both frequencies.
    */

    for(auto element: frequency_positives){
        int number = element.first;
        int curr_frequency = element.second;
        int opposite_number = number * (-1);
        
        int pairs = min(curr_frequency, frequency_negatives[opposite_number]);
        answer = answer + pairs;
    }

    //The number of pairs for zero will be its frequency divided by two. (The floor of that division is taken).
    return answer + (count_zero >> 1);
}

int solve_follow_up(vector<int> &array){

    //Use an unordered map to keep track of the frequency of the elements.
    unordered_map<int,int> frequency_positives;
    unordered_map<int,int> frequency_negatives;
    
    //Consider the number zero as a special case that will be covered later.
    int count_zero = 0;

    //Update the data structure according to the value that is found.
    for(int i = 0; i < array.size(); ++i){
        if(array[i] == 0){
            count_zero++;
            continue;
        }
        if(array[i] > 0) frequency_positives[array[i]]++;
        else frequency_negatives[array[i]]++;
    }

    int answer = 0;

    /*
        Iterate through the frequency of the positive elements and calculate its negative value.
        If the negative value does not exist in the data structure C++ automatically inserts this value
        with a frequency of zero, so the answer will not be affected.

        The number of pairs for that particular value will be product of the frequencies.
    */

    for(auto element: frequency_positives){
        int number = element.first;
        int curr_frequency = element.second;
        int opposite_number = number * (-1);
        
        int pairs = curr_frequency * frequency_negatives[opposite_number];
        answer = answer + pairs;
    }

    /*
        The number of pairs for zero will be the number of combinations of 2 elements out of n elements, 
        where n is the frequency of the number zero in the array.
    */

    int zero_combinations = (count_zero) * (count_zero - 1) / 2;

    return answer + zero_combinations;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    vector<vector<int>> cases;

    vector<int> case1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    vector<int> case2 = {1, 10, 8, -2, 2, 5, 7, 2, -2, -1};
    vector<int> case3 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 6};
    vector<int> case4 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 0};

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);
    cases.emplace_back(case4);

    for(auto &test_case: cases){
        cout << solve(test_case) << "\n";
        //cout << solve_follow_up(test_case) << "\n";
    }

    return 0;
}

//Time Spent
//First Part: 18 minutes
//Second Part: 7 minutes
