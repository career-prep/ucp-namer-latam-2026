/*Data Structure: Graph
Algorithm: DFS (generic, bfs/dfs equivalent here)
Time Complexity: O(V+E)
Space Complexity: O(V+E)
Time Taken: 31 mins 49 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>

using namespace std;

void dfs(string node, unordered_map<string, vector<string>>& graph, unordered_set<string>& visited){
    if(visited.count(node)) return;
    visited.insert(node);
    for(string& neighbor : graph[node]){
        dfs(neighbor, graph, visited);
    }
}

int roadNetworks(vector<string> towns, vector<pair<string, string>> roads){
    unordered_map<string, vector<string>> graph;

    for(string& t : towns){
        graph[t];
    }

    // undirected so add both ways
    for(auto& r : roads){
        graph[r.first].push_back(r.second);
        graph[r.second].push_back(r.first);
    }

    unordered_set<string> visited;
    int count = 0;

    for(string& t : towns){
        if(!visited.count(t)){
            // skip isolated towns, they dont count as a network
            if(graph[t].empty()){
                visited.insert(t);
                continue;
            }
            count++;
            dfs(t, graph, visited);
        }
    }

    return count;
}

int main(){
    vector<string> towns1 = {"Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"};
    vector<pair<string, string>> roads1 = {
        {"Anchorage", "Homer"}, {"Glacier Bay", "Gustavus"}, {"Copper Center", "McCarthy"},
        {"Anchorage", "Copper Center"}, {"Copper Center", "Fairbanks"}, {"Healy", "Fairbanks"},
        {"Healy", "Anchorage"}
    };
    cout << "Test 1 Result: " << roadNetworks(towns1, roads1) << " (Expected: 2)" << endl;

    vector<string> towns2 = {"Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"};
    vector<pair<string, string>> roads2 = {
        {"Kona", "Volcano"}, {"Volcano", "Hilo"}, {"Lahaina", "Hana"}, {"Kahului", "Haiku"},
        {"Hana", "Haiku"}, {"Kahului", "Lahaina"}, {"Princeville", "Lihue"}, {"Lihue", "Waimea"}
    };
    cout << "Test 2 Result: " << roadNetworks(towns2, roads2) << " (Expected: 3)" << endl;

    return 0;
}

/* psudocode/thoughts/logic
goal: count number of road networks (connected components in undirected graph)
restraints: a town with no roads doesnt count as its own network

strategy: build adjacency list (undirected so add both directions). dfs from every unvisited
town and bump a counter each time we start a fresh dfs. skip isolated towns since they dont
count.

*/
