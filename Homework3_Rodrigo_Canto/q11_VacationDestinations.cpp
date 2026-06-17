//Time Complexity: O((V + E) log(V)).
//Space Complexity: O(V + E).
//Technique: Min-Heap

//V is the number of cities.
//E is the number of edges.

#include "bits/stdc++.h"
using namespace std;

const int inf = 1e9;

class PriorityQueue {
private:
    
    vector<pair<string, double>> arr;

    void relocate_Up(int index) {

        //For min-heap

        //If the index is not the root and my father is greater than me,
        //we swap values to mantain the structure of the tree.

        //In this case, we compare the second value because that gives us the priority for the elements.
        while (index > 0 && arr[(index - 1) / 2].second < arr[index].second) {
            swap(arr[index], arr[(index - 1) / 2]);
            index = (index - 1) / 2;
        }
    }

    //To handle removals in the tree.
    void relocate_Down(int index) {
        int maxIndex = index;
        int left = 2 * index + 1;
        int right = 2 * index + 2;

        //Compare left child.
        if (left < arr.size() && arr[left].second > arr[maxIndex].second) {
            maxIndex = left;
        }

        //Compare right child.
        if (right < arr.size() && arr[right].second > arr[maxIndex].second) {
            maxIndex = right;
        }

        //If there is a change, we keep going down into the tree.
        if (index != maxIndex) {
            swap(arr[index], arr[maxIndex]);
            relocate_Down(maxIndex);
        }
    }

public:

    //This function must not be called if the heap is empty.
    pair<string, int> top() {
        return arr[0];
    }   

    //Put the element at the end of the heap, and relocate it if necessary.
    void insert(string x, int weight) {
        arr.push_back({x, weight});
        relocate_Up(arr.size() - 1);
    }

    void remove() {
        if (arr.empty()) return;

        //We move the last element to the root and relocate its value if necessary.
        arr[0] = arr.back();
        arr.pop_back();

        if (!arr.empty()) {
            relocate_Down(0);
        }
    }

    bool empty() {
        return arr.empty();
    }
};

/*
    We can use Dijkstra´s algorithm to calculate all shortest paths starting from the city origin.
    Then we can check all the cities within range k.
*/

int solveVacationDestinations(string origin, double k, vector<pair<pair<string, string>, double>> &edges){

    map<string, double> dist;
    map<string, vector<pair<string, double>>> adj_list;

    //Build adjacency list.
    for(auto edge : edges){
        string u = edge.first.first;
        string v = edge.first.second;

        dist[u] = inf;
        dist[v] = inf;

        double duration = edge.second;

        //Add one in the duration for the stopover.
        duration = duration + 1.0;

        adj_list[u].push_back({v, duration});
        adj_list[v].push_back({u, duration});
    }

    dist[origin] = 0;

    PriorityQueue pq;

    pq.insert(origin, dist[origin]);

    //Execute Dijkstra's algorithm.
    while(!pq.empty()){

        auto curr = pq.top();
        pq.remove();

        string city = curr.first;
        double curr_dist = curr.second;

        if(curr_dist > dist[city]) continue;

        for(auto edge : adj_list[city]){

            string to_city = edge.first;
            double duration = edge.second;

            if(curr_dist + duration < dist[to_city]){
                dist[to_city] = curr_dist + duration;
                pq.insert(to_city, dist[to_city]);
            }
        }
    }

    int reachable_cities = 0;

    //Check all the cities with distance no greater than k to compute the answer.
    for(auto element : dist){

        double distance = element.second;

        //We decrease the distance calculated by 1 because the last city is not a stopover.
        if(distance != 0 && distance - 1.0 <= k){
            reachable_cities++;
        }
    }

    return reachable_cities;
}


int main() {
    
    vector<pair<pair<string, string>, double>> edges = {
        {{"Boston", "New York"}, 4.0},
        {{"New York", "Philadelphia"}, 2.0},
        {{"Boston", "Newport"}, 1.5},
        {{"Washington, D.C.", "Harper's Ferry"}, 1.0},
        {{"Boston", "Portland"}, 2.5},
        {{"Philadelphia", "Washington, D.C."}, 2.5}
    };

    string origin = "New York";
    double k = 8.0;

    int result = solveVacationDestinations(origin, k, edges);

    cout << result << "\n";

    return 0;
}

//Time Spent: 23 minutes