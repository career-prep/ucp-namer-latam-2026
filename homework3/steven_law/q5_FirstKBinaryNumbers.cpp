/*Data Structure: Queue
Algorithm: BFS-style generation
Time Complexity: O(k)
Space Complexity: O(k)
Time Taken: 22 mins 16 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>
#include <queue>

using namespace std;

vector<string> firstKBinaryNumbers(int k){
    vector<string> result;
    if(k <= 0) return result;

    result.push_back("0");
    if(k == 1) return result;

    queue<string> q;
    q.push("1");

    while(result.size() < k){
        string curr = q.front();
        q.pop();
        result.push_back(curr);

        q.push(curr + "0");
        q.push(curr + "1");
    }

    return result;
}

int main(){
    // k=5
    vector<string> r1 = firstKBinaryNumbers(5);
    for(auto& s : r1) cout << s << " ";
    cout << endl;

    // k=10
    vector<string> r2 = firstKBinaryNumbers(10);
    for(auto& s : r2) cout << s << " ";
    cout << endl;
}

/* psudocode/thoughts/logic
goal: generate the first k binary numbers as strings
restraints: must be in increasing order (0, 1, 10, 11, 100...)

strategy: at first i was thinking convert integers to binary one by one but that felt like
cheating, the question seems to want me to actually BUILD the numbers up

so the pattern... if you have "1", the next two are "10" and "11". if you have "10" the next
two are "100" and "101". this is bfs level expansion which means q 

seed the queue with "1", manually push "0" as the first result then loop: pop front, add to
result, push curr+"0" and curr+"1". stop when result hits size k.
*/
