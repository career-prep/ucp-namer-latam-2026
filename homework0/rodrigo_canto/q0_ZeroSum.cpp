//Time Complexity: O(n) average-case
//Space Complexity: O(n)

#include <bits/stdc++.h>
using namespace std;

//Use an unordered map to keep track of the frequency of the elements.
unordered_map<int, int> frequency_positives, frequency_negatives;

//Consider the number zero as a special case that will be covered later.
long long count_zero = 0;

//Reset variables and data structures for next iteration.
void reset(){
    frequency_positives.clear();
    frequency_negatives.clear();
    count_zero = 0;
}

//Update the data structure according to the value that is found.
void calculate_frequencies(const vector<int> &array){
    
    for(int value : array){
        if(value == 0){
            count_zero++;
            continue;
        }
        if(value > 0) frequency_positives[value]++;
        else frequency_negatives[value]++;
    }
}

/*
    Iterate through the frequency of the positive elements and calculate its negative value.
    If the negative value does not exist in the data structure C++ automatically inserts this value
    with a frequency of zero, so the answer will not be affected.

    The number of pairs for that particular value will be the minimum between both frequencies for the first part
    and the product of the frequencies for the second part of the problem
*/

void calculate_pairs(bool solving_follow_up, long long &answer){

    for(auto element: frequency_positives){

        long long number = element.first;
        long long curr_frequency = element.second;
        long long opposite_number = number * (-1);

        long long pairs = 0;

        if(solving_follow_up) pairs = curr_frequency * (long long) frequency_negatives[opposite_number];
        else pairs = min(curr_frequency, (long long)frequency_negatives[opposite_number]);
        
        answer = answer + pairs;
    }
}

long long solve(const vector<int> &array){

    calculate_frequencies(array);

    long long answer = 0;

    calculate_pairs(false, answer);

    //The number of pairs for zero will be its frequency divided by two. (The floor of that division is taken).
    return answer + (count_zero / 2);
}

long long solve_follow_up(const vector<int> &array){

    calculate_frequencies(array);

    long long answer = 0;

    calculate_pairs(true, answer);

    /*
        The number of pairs for zero will be the number of combinations of 2 elements out of n elements, 
        where n is the frequency of the number zero in the array.
    */

    long long zero_combinations = (count_zero) * (count_zero - 1) / 2;

    return answer + zero_combinations;
}

int main() {

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

        reset();
    }

    return 0;
}

//Time Spent
//First Part: 18 minutes
//Second Part: 7 minutes
