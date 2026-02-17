/*Time Complexity:  O(n log n)
Space Complexity: O(n)
Technique used: Sort the array then solve
Time Taken: 19mins 32 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals){

   sort(intervals.begin(), intervals.end());
    //{{2, 3}, {4, 8}, {1, 2}, {5, 7}, {9, 12}}
    //{{1,2},  {2,3},  {4,8},  {5,7},  {9,12}}
    vector<vector<int>> result;
    result.push_back(intervals[0]);

    int k = 0;

    for(int i = 1; i < intervals.size(); i++){
        if(result[k][1] >= intervals[i][0]){
            result[k][1] = max(result[k][1], intervals[i][1]);
        } else{
            result.push_back(intervals[i]);
            k++;
        }
    }
    return result;
  
}


void printIntervals(vector<vector<int>>& intervals) {
    cout << "[";
    for (int i = 0; i < intervals.size(); i++) {
        cout << "[" << intervals[i][0] << "," << intervals[i][1] << "]";
        if (i < intervals.size() - 1) cout << ",";
    }
    cout << "]" << endl;
}

int main() {
    // Test case 1
    vector<vector<int>> intervals1 = {{2, 3}, {4, 8}, {1, 2}, {5, 7}, {9, 12}};
    printIntervals(intervals1);
    vector<vector<int>> result1 = mergeIntervals(intervals1);
    cout << "Result: ";
    printIntervals(result1);
    cout << "Expected: [[4,8],[1,3],[9,12]]" << endl << endl;
    
    // Test case 2
    vector<vector<int>> intervals2 = {{5, 8}, {6, 10}, {2, 4}, {3, 6}};
    printIntervals(intervals2);
    vector<vector<int>> result2 = mergeIntervals(intervals2);
    cout << "Result: ";
    printIntervals(result2);
    cout << "Expected: [[2,10]]" << endl << endl;
    
    // Test case 3
    vector<vector<int>> intervals3 = {{10, 12}, {5, 6}, {7, 9}, {1, 3}};
    printIntervals(intervals3);
    vector<vector<int>> result3 = mergeIntervals(intervals3);
    cout << "Result: ";
    printIntervals(result3);
    cout << "Expected: [[10,12],[5,6],[7,9],[1,3]]" << endl;
    
    return 0;
}

/* psudocode/thoughts/logic
goal: Merge overlapping intervals
restraints: No real restraint
strategy: Looking at this problem from first glance i'm not sure
we can solve it without sorting even though sorting is O(n log n).

My idea is that we sort it right so for example we go from
{2, 3}, {4, 8}, {1, 2}, {5, 7}, {9, 12}}
To
{{1,2},  {2,3},  {4,8},  {5,7},  {9,12}}

Now from here can see a clear pattern. In each vector we see at max 2
values. We can think of these as X and Y pairs. The question is 
essentially asking if Y from the previous vector is greater than X
in the current vector we should merge them.

To do this I can create a for loop where I compare the prev Y to 
current X and if its less than or = to then we merge them.


my output does not match the output from the homework document but
idk if the order matters...

*/
    
