//Time Complexity: O(N + M).
//Space Complexity: O(N + M).
//Technique: Dfs.

//N is the number of states
//M is the number of roads.

#include "bits/stdc++.h"
using namespace std;

int dfs(int state, vector<vector<int>> &adj_list, vector<bool> &visited){

    visited[state] = true;
    int visited_states = 1;

    for(auto neighbor_state : adj_list[state]){
        if(visited[neighbor_state] == false){
            visited_states += dfs(neighbor_state, adj_list, visited);
        }
    }

    return visited_states;
}

int solveRoadNetworks(vector<string> &states, vector<pair<string, string>> &connections){

    //The map allows us to recover the index for an specific state.
    //We can construct the adjacency list with numbers using this.
    unordered_map<string, int> state_to_idx;

    for(int idx = 0; idx < states.size(); ++idx){
        state_to_idx[states[idx]] = idx;
    }

    vector<vector<int>> adj_list(states.size());
    vector<bool> visited(states.size());

    //Build the adjacency list.
    for(int i = 0; i < connections.size(); ++i){

        string a = connections[i].first;
        string b = connections[i].second;

        int idx_a = state_to_idx[a];
        int idx_b = state_to_idx[b];

        adj_list[idx_a].push_back(idx_b);
        adj_list[idx_b].push_back(idx_a);
    }

    int road_networks = 0;

    //Use a dfs to find all the road networks for states that have not been visited.
    for(int state = 0; state < states.size(); ++state){
        if(visited[state] == false){

            int visited_states = dfs(state, adj_list, visited);

            //The number of states in the network must be greater than 1.
            if(visited_states > 1) road_networks++;
        }
    }

    return road_networks;
}

int main() {

    /*
    vector<string> states = {
        "Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", 
        "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", 
        "Healy", "Anchorage"
    };
    
    vector<pair<string, string>> connections = {
        {"Anchorage", "Homer"}, 
        {"Glacier Bay", "Gustavus"}, 
        {"Copper Center", "McCarthy"}, 
        {"Anchorage", "Copper Center"}, 
        {"Copper Center", "Fairbanks"}, 
        {"Healy", "Fairbanks"}, 
        {"Healy", "Anchorage"}
    };
    */

    vector<string> states = {
        "Kona", "Hilo", "Volcano", "Lahaina", "Hana", 
        "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"
    };

    vector<pair<string, string>> connections = {
        {"Kona", "Volcano"}, 
        {"Volcano", "Hilo"}, 
        {"Lahaina", "Hana"}, 
        {"Kahului", "Haiku"}, 
        {"Hana", "Haiku"}, 
        {"Kahului", "Lahaina"}, 
        {"Princeville", "Lihue"}, 
        {"Lihue", "Waimea"}
    };

    int result = solveRoadNetworks(states, connections);

    cout << result << "\n";

    return 0;
}

//Time Spent: 25 minutes