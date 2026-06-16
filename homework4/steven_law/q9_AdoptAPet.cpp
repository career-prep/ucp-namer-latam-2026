/*Data Structure: two queues (one per species)
Algorithm: FIFO per species, longest-waiting at the front, fall back to other species if empty
Technique: maintain a queue (regular)
Time Complexity: O(E) for E events (each enqueue/dequeue O(1))
Space Complexity: O(N) animals held at once
Time Taken: 25 mins 4 seconds
*/

#include<iostream>
#include<vector>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

/*
1. two queues, dogs + cats, front = longest waiting.
2. load initial pets sorted longest-waiting first.
3. new animal event -> push to the back of its species queue (it just got here).
4. person event -> pop the requested species front. if that queue is empty, pop the other species.
5. print whoever got adopted (animal-add events print nothing).
*/

struct Pet { string name; string species; int days; };

struct Event {
    bool isPerson;   //true = adopter, false = new animal
    string name;
    string species;  //requested species (person) or the animals species
};

vector<Pet> AdoptAPet(vector<Pet> initial, vector<Event> events){
    //longest-waiting first
    sort(initial.begin(), initial.end(), [](const Pet& a, const Pet& b){ return a.days > b.days; });

    deque<string> dogs, cats; //store names, front = longest waiting
    for(auto& p : initial){
        if(p.species == "dog") dogs.push_back(p.name);
        else cats.push_back(p.name);
    }

    vector<Pet> adopted;
    for(auto& e : events){
        if(!e.isPerson){ //new animal arrives, goes to the back
            if(e.species == "dog") dogs.push_back(e.name);
            else cats.push_back(e.name);
            continue;
        }

        deque<string>* primary = (e.species == "dog") ? &dogs : &cats;
        deque<string>* other   = (e.species == "dog") ? &cats : &dogs;
        string primarySpecies  = e.species;
        string otherSpecies    = (e.species == "dog") ? "cat" : "dog";

        if(!primary->empty()){
            adopted.push_back({primary->front(), primarySpecies, 0});
            primary->pop_front();
        } else if(!other->empty()){
            adopted.push_back({other->front(), otherSpecies, 0});
            other->pop_front();
        }
        //both empty -> nobody adopted, print nothing
    }
    return adopted;
}

int main(){
    vector<Pet> initial = {
        {"Sadie","dog",4},
        {"Woof","cat",7},
        {"Chirpy","dog",2},
        {"Lola","dog",1}
    };
    vector<Event> events = {
        {true,  "Bob",    "dog"},   //Sadie, dog
        {false, "Floofy", "cat"},   //(no output)
        {true,  "Sally",  "cat"},   //Woof, cat
        {true,  "Ji",     "cat"},   //Floofy, cat
        {true,  "Ali",    "cat"}    //Chirpy, dog (no cats left)
    };

    vector<Pet> output = AdoptAPet(initial, events);

    cout << "Actual result:" << endl;
    for(auto& p : output) cout << "  " << p.name << ", " << p.species << endl;
    cout << "Expected result: Sadie/dog, Woof/cat, Floofy/cat, Chirpy/dog" << endl;
}

/* psudocode/thoughts/logic
goal: process adopters + new animals one at a time, print each pet as its adopted out
restraints: adopter picks a SPECIES not an animal, gets the longest-waiting of that species; if
none of that species, takes the other species' longest-waiting

assumption: animals added during the week have waited less than the ones already there, so a new
arrival goes to the back of its queue. initial pets get sorted by days so longest-waiting starts
at the front.

strategy: one regular FIFO queue per species does it for free — "longest waiting" is just the
front, new arrivals go to the back. adopter pops the requested species, or falls back to the
other queue if its empty. animal-add events just enqueue and print nothing. all O(1) per event.

walkthrough: dogs=[Sadie,Chirpy,Lola] cats=[Woof].
Bob/dog -> Sadie. Floofy added -> cats=[Woof,Floofy]. Sally/cat -> Woof. Ji/cat -> Floofy.
Ali/cat -> cats empty -> dogs.front = Chirpy. matches expected.
*/
