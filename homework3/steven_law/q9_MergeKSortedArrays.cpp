/*Data Structure: Priority Queue (min heap)
Time Complexity: O(N log k) where N is total elements and k is number of arrays
Space Complexity: O(k)
Time Taken: 33 mins 27 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>
#include <queue>

using namespace std;

struct Node {
    int val;
    int arrIdx;
    int elemIdx;
};

struct Compare {
    bool operator()(const Node& a, const Node& b){
        return a.val > b.val; // min heap
    }
};

vector<int> mergeKSortedArrays(int k, vector<vector<int>>& arrays){
    vector<int> result;
    priority_queue<Node, vector<Node>, Compare> pq;

    for(int i = 0; i < k; i++){
        if(!arrays[i].empty()){
            pq.push({arrays[i][0], i, 0});
        }
    }

    while(!pq.empty()){
        Node curr = pq.top();
        pq.pop();
        result.push_back(curr.val);

        if(curr.elemIdx + 1 < arrays[curr.arrIdx].size()){
            int nextIdx = curr.elemIdx + 1;
            pq.push({arrays[curr.arrIdx][nextIdx], curr.arrIdx, nextIdx});
        }
    }

    return result;
}

int main(){
    vector<vector<int>> arr1 = {{1, 2, 3, 4, 5}, {1, 3, 5, 7, 9}};
    vector<int> r1 = mergeKSortedArrays(2, arr1);
    for(int n : r1) cout << n << " ";
    cout << endl;

    vector<vector<int>> arr2 = {{1, 4, 7, 9}, {2, 6, 7, 10, 11, 13, 15}, {3, 8, 12, 13, 16}};
    vector<int> r2 = mergeKSortedArrays(3, arr2);
    for(int n : r2) cout << n << " ";
    cout << endl;
}

/* psudocode/thoughts/logic
goal: merge k sorted arrays into one sorted array
restraints: each input array is already sorted

strategy:  k way merge. slow way is dumping everything into one array and sorting,
O(N log N), we can do better with a heap.

push the first element of each array into a min heap, tracking which array it came from
and its index in that array. pop the smallest, add to result, push the next element from
that same array.

got [9, 7, 5, 5, 4, 3, 3, 2, 1, 1] which is REVERSE of what i need
priority_queue in c++ is a max heap by def
flipped to a.val > b.val for min heap and got the right output

took me a sec to remember the rule, priority_queue puts the "largest"  at top, so to 
make a min heap you have to reverse the comparison

O(N log k) since heap is bounded by k

made the Node struct since you cant just stick tuples in a pq with a custom
comparator without boilerplate
*/
