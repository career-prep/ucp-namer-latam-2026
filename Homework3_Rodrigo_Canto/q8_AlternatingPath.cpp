//Time Complexity: O(N + M)
//Space Complexity: O(N + M)
//Technique: Bfs.

//N is the number of cities.
//M is the number of connections.

#include "bits/stdc++.h"
using namespace std;

const int inf = 1e9;

int solveAlternatingPath(vector<pair<pair<string, string>, string>> &connections, string origin, string destination){

    //Get all the cities that are involved in the network.
    set<string> distinct_cities;

    for(int i = 0; i < connections.size(); ++i){

        string a = connections[i].first.first;
        string b = connections[i].first.second;

        distinct_cities.insert(a);
        distinct_cities.insert(b);
    }

    //Map the string to int so we can generate the adjacency list using this values.
    vector<string> cities;
    map<string, int> city_to_idx;

    int idx = 0;

    for(auto citie : distinct_cities){
        cities.push_back(citie);
        city_to_idx[cities.back()] = idx;
        idx++;
    }

    //Build the adjacency list.
    vector<vector<pair<int,int>>> adj_list(cities.size());

    for(int i = 0; i < connections.size(); ++i){

        string a = connections[i].first.first;
        string b = connections[i].first.second;

        int idx_a = city_to_idx[a];
        int idx_b = city_to_idx[b];

        int color = (connections[i].second == "red") ? 0 : 1;

        adj_list[idx_a].push_back({idx_b, color});
    }

    /*
        We define dist[i][{0, 1}] as the shortest path that ends at city i using a specific color
        0 is red, 1 is blue.
    */

    vector<vector<int>> dist(cities.size(), vector<int>(2, inf));

    int idx_origin = city_to_idx[origin];
    int idx_destination = city_to_idx[destination];

    //Initialize in 0 for the origin and get the shortest paths for the remaining cities.
    dist[idx_origin][0] = dist[idx_origin][1] = 0;

    queue<pair<int,int>> q;

    q.push(make_pair(idx_origin, 0));
    q.push(make_pair(idx_origin, 1));

    while(!q.empty()){

        auto curr = q.front(); q.pop();

        int city = curr.first;
        int curr_color = curr.second;

        //We need to alternate the color so we need to keep track of the color we just used.
        int next_color = (curr_color ^ 1);

        for(auto neighbor : adj_list[city]){

            if(neighbor.second != next_color) continue;

            int neighbor_city = neighbor.first;

            if(dist[neighbor_city][next_color] > dist[city][curr_color] + 1){
                dist[neighbor_city][next_color] = dist[city][curr_color] + 1;
                q.push(make_pair(neighbor_city, next_color));
            }
        }
    }

    int answer = min(dist[idx_destination][0], dist[idx_destination][1]);

    //If the answer is infinity, then the alternating path does not exist.
    if(answer == inf) answer = -1;

    return answer;
}

int main() {
    
    vector<pair<pair<string, string>, string>> connections = {
        {{"A", "B"}, "blue"},
        {{"A", "C"}, "red"},
        {{"B", "D"}, "blue"},
        {{"B", "E"}, "blue"},
        {{"C", "B"}, "red"},
        {{"D", "C"}, "blue"},
        {{"A", "D"}, "red"},
        {{"D", "E"}, "red"},
        {{"E", "C"}, "red"}
    };

    string origin = "E";
    string destination = "D";

    int result = solveAlternatingPath(connections, origin, destination);

    cout << result << "\n";

    return 0;
}

//Time Spent: 22 minutes