#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//sorts intervals by start then merges overlapping ones in O(n log n)
vector<pair<int, int>> mergeIntervals(vector<pair<int, int>> intervals) {
    sort(intervals.begin(), intervals.end());
    vector<pair<int, int>> merged;
    for (const auto& interval : intervals) {
        if (!merged.empty() && interval.first <= merged.back().second) {
            merged.back().second = max(merged.back().second, interval.second);
            continue;
        }
        merged.push_back(interval);
    }
    return merged;
}

void print(const vector<pair<int, int>>& intervals) {
    cout << "[";
    for (int i = 0; i < (int)intervals.size(); ++i) {
        if (i > 0) cout << ", ";
        cout << "(" << intervals[i].first << ", " << intervals[i].second << ")";
    }
    cout << "]" << endl;
}

int main() {
    print(mergeIntervals({{2, 3}, {4, 8}, {1, 2}, {5, 7}, {9, 12}})); // [(1, 3), (4, 8), (9, 12)]
    print(mergeIntervals({{5, 8}, {6, 10}, {2, 4}, {3, 6}})); // [(2, 10)]
    print(mergeIntervals({{10, 12}, {5, 6}, {7, 9}, {1, 3}})); // [(1, 3), (5, 6), (7, 9), (10, 12)]

    return 0;
}

//time spent: 23 minutes
