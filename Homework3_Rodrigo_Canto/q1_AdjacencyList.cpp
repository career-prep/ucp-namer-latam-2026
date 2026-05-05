#include "bits/stdc++.h"
using namespace std;

map<int, set<int>> adjacencySet(vector<pair<int,int>> &edges){

    map<int, set<int>> adj_list;

    set<int> empty_set;

    //Edges are directed
    for(auto edge : edges){
        int u = edge.first;
        int v = edge.second;

        adj_list[u].insert(v);

        //For nodes that do not have connections.
        if(adj_list.find(v) == adj_list.end()) adj_list[v] = empty_set;
    }

    return adj_list;
}

int main() {

    vector<pair<int,int>> edges = {
        {1, 2},
        {2, 3},
        {1, 3},
        {3, 2},
        {2, 0}
    };

    map<int, set<int>> adj_list = adjacencySet(edges);

    for(auto connections : adj_list){

        cout << connections.first << ": ";
        
        for(auto to : connections.second){
            cout << to << " ";
        }
        cout << "\n";
    }
}
