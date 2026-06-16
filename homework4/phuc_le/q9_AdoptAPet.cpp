/*
    Technique:
    - Queue  First-In-First-Out (FIFO)

    - One queue for dogs and one for cats.
    - The animal that has waited the longest is always
      at the front of its species queue.

    Enqueue:
    - Add the animal to the appropriate queue.

    Dequeue:
    - If the preferred species is available,
      remove the animal from that queue.
    - Otherwise, remove the oldest animal from the
      other species queue.
    - If both queues are empty, return an invalid animal.

    Time Complexity: O(1) (enqueue and dequeue)
    Space Complexity: O(n): n is the number of animals in the shelter.

    Time spent: 35 minutes
*/

#include <iostream>
#include <queue>
#include <string>

using namespace std;

struct Animal
{
    string name;
    string species;
    int days; // higher = waited longer
};

class Shelter
{
private:
    queue<Animal> dogs;
    queue<Animal> cats;

public:
    void enqueue(Animal a)
    {
        if (a.species == "dog")
            dogs.push(a);
        else
            cats.push(a);
    }

    // Dequeue preferred species;
    // if empty, give the other species
    Animal dequeue(string preference)
    {
        if (preference == "dog")
        {
            if (!dogs.empty())
            {
                Animal a = dogs.front();
                dogs.pop();
                return a;
            }
            else if (!cats.empty())
            {
                Animal a = cats.front();
                cats.pop();
                return a;
            }
        }
        else
        { // preference == "cat"
            if (!cats.empty())
            {
                Animal a = cats.front();
                cats.pop();
                return a;
            }
            else if (!dogs.empty())
            {
                Animal a = dogs.front();
                dogs.pop();
                return a;
            }
        }
        return {"", "", -1}; // shelter empty
    }
};

int main()
{
    Shelter shelter;

    // Initial animals — sorted by days descending
    shelter.enqueue({"Woof", "cat", 7});
    shelter.enqueue({"Sadie", "dog", 4});
    shelter.enqueue({"Chirpy", "dog", 2});
    shelter.enqueue({"Lola", "dog", 1});

    // Process sequence of events
    struct Event
    {
        string name;
        string type;
        string preference;
    };

    auto process = [&](string name, string type,
                       string preference = "")
    {
        if (type == "person")
        {
            Animal a = shelter.dequeue(preference);
            if (a.days == -1)
                cout << "Output: (shelter empty)\n\n";
            else
                cout << "Output: " << a.name
                     << ", " << a.species << "\n\n";
        }
        else
        {
            shelter.enqueue({name, type, 0});
            cout << "Output:\n\n";
        }
    };

    cout << "Input: Bob, person, dog\n";
    process("Bob", "person", "dog");

    cout << "Input: Floofy, cat\n";
    process("Floofy", "cat");

    cout << "Input: Sally, person, cat\n";
    process("Sally", "person", "cat");

    cout << "Input: Ji, person, cat\n";
    process("Ji", "person", "cat");

    cout << "Input: Ali, person, cat\n";
    process("Ali", "person", "cat");

    return 0;
}