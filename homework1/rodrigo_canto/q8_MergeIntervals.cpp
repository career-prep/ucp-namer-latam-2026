// Technique: Sorting

// Time Complexity: O(N log n)
// Space Complexity: O(N)

#include <bits/stdc++.h>
using namespace std;

void solve(vector<pair<int,int>> &intervals){

    //Sort the intervals by starting points.
    sort(intervals.begin(), intervals.end());

    //Keep track of the current interval we are considering.
    int first = intervals[0].first, last = intervals[0].second;

    vector<pair<int,int>> merged_intervals;

    for(auto interval : intervals){

        int l = interval.first, r = interval.second;

        /*
            If the starting point of the interval we are currently considering is less than or equal to the last element of the interval
            we already have, we can merge the intervals.
            The ending point will be the maximum between the ending point of the current interval and the ending point we already have.
        */

        if(l <= last){
            last = max(last, r);
        }
        else{

            //Otherwise, the intervals are disjoint, we add the interval we had to our answer and we have a new interval.

            merged_intervals.emplace_back(first, last);
            first = l, last = r;
        }
    }


    //We add the last interval.
    merged_intervals.emplace_back(first, last);
    
    for(auto interval : merged_intervals){
        int l = interval.first, r = interval.second;
        
        cout << "[" << l << "," << r << "]  ";
    }
    
    cout << "\n";
}

int main() {

    vector<vector<pair<int,int>>> cases;

    vector<pair<int,int>> case1 = {{2, 3}, {4, 8}, {1, 2}, {5, 7}, {9, 12}};
    vector<pair<int,int>> case2 = {{5, 8}, {6, 10}, {2, 4}, {3, 6}};
    vector<pair<int,int>> case3 = {{10, 12}, {5, 6}, {7, 9}, {1, 3}};

    cases.emplace_back(case1);
    cases.emplace_back(case2);
    cases.emplace_back(case3);


    for(auto &test_case: cases){

        solve(test_case);
    }

    return 0;
}

// Time: 14 minutes

