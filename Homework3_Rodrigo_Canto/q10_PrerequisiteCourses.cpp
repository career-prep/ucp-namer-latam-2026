//Time Complexity: O(N + M).
//Space Complexity: O(N + M).
//Technique: Topological Ordering.

//N is the number of courses.
//M is the number of prerequisites.

#include "bits/stdc++.h"
using namespace std;

/*
    The problem asks us to output the topological ordering based on the prerequisites for the courses.
    We can use Kahn´s algorithm to compute that.
*/

void solvePrerequisiteCourses(vector<string> courses, map<string, vector<string>> course_prerequisites){

    //Kahn's algorithm works using the in-degree value for the courses.
    map<string, int> in_degree;
    map<string, vector<string>> adj_list;

    //We need to build the adjacency list in the reversed order of connections.
    for(auto element : course_prerequisites){

        string course = element.first;

        for(auto requisite : element.second){
            adj_list[requisite].push_back(course);
            in_degree[course]++;
        }
    }
 
    queue<string> q;

    //Start with the courses that do not have dependencies.
    for(int i = 0; i < courses.size(); ++i){
        if(in_degree[courses[i]] == 0){
            q.push(courses[i]);
        }
    }

    vector<string> ordering;

    //Apply Kahn´s algorithm to handle the remaining courses.
    while(!q.empty()){

        auto course = q.front(); q.pop();

        ordering.push_back(course);

        for(auto next_course : adj_list[course]){

            in_degree[next_course]--;

            if(in_degree[next_course] == 0){
                q.push(next_course);
            }
        }
    }

    for(auto course : ordering) cout << course << "\n";
}

int main() {

    /*
    vector<string> courses = {
        "Intro to Programming", 
        "Data Structures", 
        "Advanced Algorithms", 
        "Operating Systems", 
        "Databases"
    };

    map<string, vector<string>> course_prerequisites = {
        {"Data Structures",      {"Intro to Programming"}},
        {"Advanced Algorithms",  {"Data Structures"}},
        {"Operating Systems",   {"Advanced Algorithms"}},
        {"Databases",            {"Advanced Algorithms"}}
    };
    */

    vector<string> courses = {
        "Intro to Writing", 
        "Contemporary Literature", 
        "Ancient Literature", 
        "Comparative Literature", 
        "Plays & Screenplays"
    };

    map<string, vector<string>> course_prerequisites = {
        {"Contemporary Literature", {"Intro to Writing"}},
        {"Ancient Literature",      {"Intro to Writing"}},
        {"Comparative Literature",  {"Ancient Literature", "Contemporary Literature"}},
        {"Plays & Screenplays",     {"Intro to Writing"}}
    };

    solvePrerequisiteCourses(courses, course_prerequisites);

    return 0;
}

//Time Spent: 20 minutes