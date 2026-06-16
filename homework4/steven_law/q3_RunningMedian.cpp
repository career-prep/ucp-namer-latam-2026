/*Data Structure: two heaps (max-heap + min-heap)
Algorithm: maintain a balanced low/high split, median reads off the top(s)
Technique: maintain two heaps
Time Complexity: O(n log n) — each insert is O(log n)
Space Complexity: O(n)
Time Taken: 26 mins 9 seconds
*/

#include<iostream>
#include<vector>
#include <queue>

using namespace std;

/*
1. lo = max-heap holding the smaller half, hi = min-heap holding the larger half.
2. push new x into lo if its <= lo.top(), else hi.
3. rebalance so lo is equal size or exactly one bigger than hi.
4. odd count -> median = lo.top(). even -> median = avg of the two tops.
*/

vector<double> RunningMedian(vector<int> stream){
    priority_queue<int> lo;                              //max-heap, lower half
    priority_queue<int, vector<int>, greater<int>> hi;   //min-heap, upper half
    vector<double> medians;

    for(int x : stream){
        if(lo.empty() || x <= lo.top()) lo.push(x);
        else hi.push(x);

        //rebalance
        if(lo.size() > hi.size() + 1){ hi.push(lo.top()); lo.pop(); }
        else if(hi.size() > lo.size()){ lo.push(hi.top()); hi.pop(); }

        if(lo.size() == hi.size()) medians.push_back((lo.top() + hi.top()) / 2.0);
        else medians.push_back(lo.top());
    }
    return medians;
}

int main(){
    vector<int> stream = {1, 11, 4, 15, 12};
    vector<double> output = RunningMedian(stream);

    cout << "Actual result:   ";
    for(size_t i = 0; i < output.size(); i++) cout << output[i] << (i+1 < output.size() ? ", " : "");
    cout << endl;
    cout << "Expected result: 1, 6, 4, 7.5, 11" << endl;
}

/* psudocode/thoughts/logic
goal: after each incoming number, report the running median
restraints: stream comes one at a time, cant sort the whole thing each step (too slow)

strategy: two heaps. lo is a max-heap for the smaller half so its biggest element (the middle-ish
one) sits on top. hi is a min-heap for the bigger half. keep them balanced (equal, or lo one
bigger). then the median is either lo.top() (odd total) or the average of both tops (even total).
each insert is a couple O(log n) heap ops, way better than re-sorting.

walkthrough on 1,11,4,15,12:
- 1     -> lo[1]               median 1
- 11    -> hi[11], balance     median (1+11)/2 = 6
- 4     -> lo[1,4]             median 4
- 15    -> hi[11,15]           median (4+11)/2 = 7.5
- 12    -> hi then rebalance   median 11
*/
