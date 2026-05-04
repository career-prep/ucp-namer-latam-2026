/*Data Structure: Graph
Algorithm: Topological Sort (Kahn's algorithm)
Time Complexity: O(V+E)
Space Complexity: O(V+E)
Time Taken: 29 mins 58 seconds
*/

#include<iostream>
#include<vector>
#include<unordered_map>
#include <string>
#include <unordered_set>
#include <queue>

using namespace std;

vector<string> prerequisiteCourses(vector<string> courses, unordered_map<string, vector<string>> prereqs){
    unordered_map<string, vector<string>> graph;
    unordered_map<string, int> indegree;

    for(string& c : courses){
        indegree[c] = 0;
        graph[c];
    }

    for(auto& [course, list] : prereqs){
        for(const string& p : list){
            graph[p].push_back(course);
            indegree[course]++;
        }
    }

    queue<string> q;
    for(string& c : courses){
        if(indegree[c] == 0) q.push(c);
    }

    vector<string> result;
    while(!q.empty()){
        string curr = q.front();
        q.pop();
        result.push_back(curr);

        for(string& next : graph[curr]){
            indegree[next]--;
            if(indegree[next] == 0) q.push(next);
        }
    }

    return result;
}

int main(){
    vector<string> courses1 = {"Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"};
    unordered_map<string, vector<string>> prereqs1 = {
        {"Data Structures", {"Intro to Programming"}},
        {"Advanced Algorithms", {"Data Structures"}},
        {"Operating Systems", {"Advanced Algorithms"}},
        {"Databases", {"Advanced Algorithms"}}
    };
    vector<string> r1 = prerequisiteCourses(courses1, prereqs1);
    for(auto& c : r1) cout << c << " -> ";
    cout << endl;

    vector<string> courses2 = {"Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"};
    unordered_map<string, vector<string>> prereqs2 = {
        {"Contemporary Literature", {"Intro to Writing"}},
        {"Ancient Literature", {"Intro to Writing"}},
        {"Comparative Literature", {"Ancient Literature", "Contemporary Literature"}},
        {"Plays & Screenplays", {"Intro to Writing"}}
    };
    vector<string> r2 = prerequisiteCourses(courses2, prereqs2);
    for(auto& c : r2) cout << c << " -> ";
    cout << endl;
}

/* psudocode/thoughts/logic
goal: return a valid order to take courses respecting prereqs
restraints: only one course at a time, must finish prereqs first

strategy:  topo sort, going with kahns algorithm because its bfs based

build a graph where edges go prereq -> course, compute indegree of each course (= number
of prereqs)... push every course with indegree 0 onto a queue. pop one, add to result, for
each course depending on it decrement indegree, if it hits 0 push it.

thought about doing dfs based topo sort but kahns feels easier here

note: result might not exactly match the prompts first ordering since multiple valid orders
exist, the prompt mentions this
*/
