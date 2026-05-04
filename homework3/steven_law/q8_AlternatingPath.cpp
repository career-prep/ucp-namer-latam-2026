/*Data Structure: Graph
Algorithm: BFS
Time Complexity: O(V+E) i think
Space Complexity: O(V+E)
Time Taken: 40 min, could not solve
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>
#include <queue>
#include <tuple>

using namespace std;

struct Edge {
    char to;
    string color;
};

int alternatingPath(vector<tuple<char, char, string>> edges, char origin, char destination){
    unordered_map<char, vector<Edge>> graph;
    for(auto& e : edges){
        char from = get<0>(e);
        char to = get<1>(e);
        string color = get<2>(e);
        graph[from].push_back({to, color});
    }

    if(origin == destination) return 0;

    queue<pair<char, int>> q; // node, dist
    unordered_set<char> visited;

    q.push({origin, 0});
    visited.insert(origin);

    // string lastColor = "";
    // ^ tried to put this here but it doesnt work because lastColor is per path
    // not per bfs, each branch in the bfs tree has its own lastColor and i cant
    // figure out how to track that with this queue setup.

    while(!q.empty()){
        auto [curr, dist] = q.front();
        q.pop();

        for(auto& edge : graph[curr]){
            // check edge.color != lastColorOnThisPath. dont know how to track that
            // without making the queue state bigger and reworking visited

            if(edge.to == destination) return dist + 1;

            if(!visited.count(edge.to)){
                visited.insert(edge.to);
                q.push({edge.to, dist + 1});
            }
        }
    }

    return -1;
}

int main(){
    vector<tuple<char, char, string>> edges = {
        {'A', 'B', "blue"}, {'A', 'C', "red"}, {'B', 'D', "blue"}, {'B', 'E', "blue"},
        {'C', 'B', "red"}, {'D', 'C', "blue"}, {'A', 'D', "red"}, {'D', 'E', "red"},
        {'E', 'C', "red"}
    };

    cout << "Test 1 Result: " << alternatingPath(edges, 'A', 'E') << " (expected: 4)" << endl;
    cout << "Test 2 Result: " << alternatingPath(edges, 'E', 'D') << " (expected: -1)" << endl;

    return 0;
}

/* psudocode/thoughts/logic
goal: shortest path origin -> destination where edge colors alternate, return -1 if impossible
restraints: directed graph, edges colored blue or red

strategy: ok so my first thought was just bfs since shortest path with no weights = bfs. so
thats what i did. built the graph, started bfs from origin, return when you hit destination.

then i remembered the alternating constraint. the issue is that you cant just mark a node
visited - you might need to revisit the same node from a different path that arrived using
a different color edge. like in test 1, you go A->D(red) then D->C(blue) then C->B(red) then
B->E(blue), so you need to remember the last color on each path.

i tried adding a lastColor variable but that only works for one path at a time, not bfs which
explores many paths in parallel. i think the right thing is to make the visited set track
(node, lastColor) instead of just node, AND have the queue store the lastColor too. but i ran
out of time refactoring it. the version below ignores the alternating thing entirely.

so test 1 is going to be wrong because itll find the shortest unconstrained path which is
A->B->E (length 2) or A->D->E (length 2) instead of the actual length 4 alternating path.

test 2 might come out right or wrong depending on bfs order, since theres a non alternating
path E->C->B->D (length 3) but the alternating answer is -1.


*/
