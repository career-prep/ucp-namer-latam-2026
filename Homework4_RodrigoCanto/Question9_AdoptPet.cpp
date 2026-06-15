//Time Complexity: O(q + n * log n)
//Where q is the number of queries and n is the number of pets.

//Space Complexity: O(n + q)

//Technique: Queue

#include "bits/stdc++.h"
using namespace std;


string getName(string &s){

    string name = "";

    int idx = 0;

    while(s[idx] != ','){
        name.push_back(s[idx]);
        idx++;
    }

    return name;
}

bool is_digit(char c){
    if(c >= '0' && c <= '9') return true;
    return false;
}

int getDays(string &s){

    int idx = 0;

    while(is_digit(s[idx]) == false) idx++;

    string number = "";

    while(is_digit(s[idx])){
        number.push_back(s[idx]);
        idx++;
    }

    return stoi(number) * -1;
}

void deliver_dog(queue<string> &dog){

    cout << dog.front() << ", dog" << "\n";
    dog.pop();
}

void deliver_cat(queue<string> &cat){

    cout << cat.front() << ", cat" << "\n";
    cat.pop();
}


void solve_adoptAPet(vector<string> &input, vector<string> &queries){

    //We process the input, get the name of the pets and the time they have been in the shelter
    //to process all of them in the correct order.

    vector<pair<int,string>> array_cat, array_dog;

    for(auto s : input){

        if(s.find("cat") != string::npos){
            array_cat.emplace_back(getDays(s), getName(s));
        }
        else{
            array_dog.emplace_back(getDays(s), getName(s));
        }
    }

    sort(array_cat.begin(), array_cat.end());
    sort(array_dog.begin(), array_dog.end());

    //Based on the description about how we choose the pets, we can use a queue to simulate that behaviour.
    queue<string> cat, dog;

    for(auto element : array_cat){
        string cat_name = element.second;
        cat.push(cat_name);
    }

    for(auto element : array_dog){
        string dog_name = element.second;
        dog.push(dog_name);
    }

    for(string s : queries){

        //If the query is a person, we deliver the corresponding animal.
        if(s.find("person") != string::npos){

            if(s.find("cat") != string::npos){

                if(cat.size() > 0){
                    deliver_cat(cat);
                    continue;
                }

                if(dog.size() > 0){
                    deliver_dog(dog);
                    continue;
                }
            }
            else{

                if(dog.size() > 0){
                    deliver_dog(dog);
                    continue;
                }

                if(cat.size() > 0){
                    deliver_cat(cat);
                    continue;
                }
            }
        }
        else{

            //Otherwise, based on the specie we push the name of the pet into the corresponding queue.
            if(s.find("cat") != string::npos){
                cat.push(getName(s));
            }
            else{
                dog.push(getName(s));
            }
        }
    }
}

int main(){

    vector<string> input = {
        "Sadie, dog, 4 days",
        "Woof, cat, 7 days",
        "Chirpy, dog, 2 days",
        "Lola, dog, 1 day"
    };

    vector<string> queries = {
        "Bob, person, dog",
        "Floofy, cat",
        "Sally, person, cat",
        "Ji, person, cat",
        "Ali, person, cat"
    };

    solve_adoptAPet(input, queries);
    
    return 0;
}

//Time Spent: 15 minutes.