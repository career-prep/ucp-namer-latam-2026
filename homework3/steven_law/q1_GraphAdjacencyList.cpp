// Time spent: 1 hr 38 mins

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

map<int, set<int>> adjacencySet(vector<pair<int, int>> edges) {
    map<int, set<int>> result;

    for(auto& edge: edges){
        result[edge.first];
        result[edge.second];

        result[edge.first].insert(edge.second);
    }
    return result;
}

bool bfs(int target, map<int, set<int>> graph) {
    if(graph.empty()) return false;

    set<int> visited;

    // first version i was just doing graph.begin() as the start, but in a directed graph
    // some nodes arent reachable from any single origin (node 0 in our test has no outgoing
    // edges, so starting there finds nothing). iterate every node as a start instead.
    for(auto& kv : graph){
        int start = kv.first;
        if(visited.count(start)) continue;

        queue<int> q;
        q.push(start);
        visited.insert(start);

        while(!q.empty()){
            int curr = q.front();
            q.pop();

            if(curr == target) return true;

            for(int neighbor : graph[curr]){
                if(!visited.count(neighbor)){
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
    }
    return false;
}

bool dfs(int target, map<int, set<int>> graph){
    if(graph.empty()) return false;

    set<int> visited;

    for(auto& kv : graph){
        int start = kv.first;
        if(visited.count(start)) continue;

        vector<int> stack;
        stack.push_back(start);

        while(!stack.empty()){
            int curr = stack.back();
            stack.pop_back();

            if(visited.count(curr)) continue;
            visited.insert(curr);

            if(curr == target) return true;

            for(int neighbor : graph[curr]){
                if(!visited.count(neighbor)){
                    stack.push_back(neighbor);
                }
            }
        }
    }
    return false;
}

// kahn's
vector<int> topologicalSort(map<int, set<int>> graph){
    vector<int> result;
    map<int, int> indegree;

    for(auto& [node, neighbors] : graph){
        indegree[node];
    }
    for(auto& [node, neighbors] : graph){
        for(int n : neighbors){
            indegree[n]++;
        }
    }

    queue<int> q;
    for(auto& [node, deg] : indegree){
        if(deg == 0) q.push(node);
    }

    while(!q.empty()){
        int curr = q.front();
        q.pop();
        result.push_back(curr);

        for(int neighbor : graph[curr]){
            indegree[neighbor]--;
            if(indegree[neighbor] == 0) q.push(neighbor);
        }
    }

    return result;
}

void topoHelper(int node, map<int, set<int>>& graph, set<int>& visited, vector<int>& result){
    if(visited.count(node)) return;
    visited.insert(node);
    for(int neighbor : graph[node]){
        topoHelper(neighbor, graph, visited, result);
    }
    result.push_back(node);
}

// dfs based
vector<int> topologicalSortDfs(map<int, set<int>> graph){
    vector<int> result;
    set<int> visited;

    for(auto& [node, neighbors] : graph){
        if(!visited.count(node)){
            topoHelper(node, graph, visited, result);
        }
    }

    reverse(result.begin(), result.end());
    return result;
}

int main(){
    vector<pair<int,int>> edges = {{1,2}, {2,3}, {1,3}, {3,2}, {2,0}};

    auto g = adjacencySet(edges);
    cout << "Adjacency set:" << endl;
    for (auto& [node, neighbors] : g) {
        cout << node << ": {";
        for (int n : neighbors) cout << n << " ";
        cout << "}" << endl;
    }

    cout << endl;

    cout << "bfs 0: " << (bfs(0, g) ? "found" : "not found") << endl;
    cout << "bfs 99: " << (bfs(99, g) ? "found" : "not found") << endl;
    cout << "dfs 3: " << (dfs(3, g) ? "found" : "not found") << endl;
    cout << "dfs 50: " << (dfs(50, g) ? "found" : "not found") << endl;

    cout << endl;

    // topo sort needs a DAG
    vector<pair<int,int>> dagEdges = {{5,2}, {5,0}, {4,0}, {4,1}, {2,3}, {3,1}};
    auto dag = adjacencySet(dagEdges);

    cout << "Kahn's topo sort: ";
    vector<int> topo = topologicalSort(dag);
    for(int n : topo) cout << n << " ";
    cout << endl;

    cout << "DFS topo sort:    ";
    vector<int> topoDfs = topologicalSortDfs(dag);
    for(int n : topoDfs) cout << n << " ";
    cout << endl;

    return 0;
}
