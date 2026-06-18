from collections import deque

def AdoptAPet(initial, events):
    dogs = deque()
    cats = deque()
    
    # Step 1: sort initial animals and add to queues
    initial.sort(key=lambda x: x[2], reverse=True)
    for name, species, days in initial:
        if species == "dog":
            dogs.append(name)
        elif species == "cat":
            cats.append(name)
    
    # Step 2: process events
    for event in events:
        if len(event) == 3:  # person adopting
            name, kind, wants = event
            if wants == "dog":
                if dogs:
                    print(dogs.popleft(), "dog")
                else:
                    print(cats.popleft(), "cat")
            elif wants == "cat":
                if cats:
                    print(cats.popleft(), "cat")
                else:
                    print(dogs.popleft(), "dog")
        else:  # new animal arriving
            name, species = event
            if species == "dog":
                dogs.append(name)
            elif species == "cat":
                cats.append(name)

initial = [
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1)
]

events = [
    ("Bob", "person", "dog"),
    ("Floofy", "cat"),
    ("Sally", "person", "cat"),
    ("Ji", "person", "cat"),
    ("Ali", "person", "cat")
]

print(AdoptAPet(initial, events))