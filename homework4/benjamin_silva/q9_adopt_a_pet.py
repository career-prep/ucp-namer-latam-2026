from collections import deque

def adopt_a_pet(initial_animals, events):
    dogs = deque()
    cats = deque()

    for name, species, _ in initial_animals:
        if species == "dog":
            dogs.append(name)
        else:
            cats.append(name)
    
    for event in events:
        if event[0] == 'animal':
            _, name, species = event
            if species == "dog":
                dogs.append(name)
            else:
                cats.append(name)
        elif event[0] == 'person':
            _, _, desired_species = event
            if desired_species == "dog":
                if dogs:
                    name = dogs.popleft()
                    print(name, "dog")
                else:
                    name = cats.popleft()
                    print(name, "cat")
            else:
                if cats:
                    name = cats.popleft()
                    print(name, "cat")
                else:
                    name = dogs.popleft()
                    print(name, "dog")


if __name__ == "__main__":
    initial_animals = [
        ("Sadie",  "dog", 4),
        ("Woof",   "cat", 7),
        ("Chirpy", "dog", 2),
        ("Lola",   "dog", 1),
    ]

    events = [
        ("person", "Bob",   "dog"),  
        ("animal", "Floofy", "cat"),
        ("person", "Sally", "cat"),  
        ("person", "Ji",    "cat"),  
        ("person", "Ali",   "cat"),  
    ]

    adopt_a_pet(initial_animals, events)


    # Time spent: 40 minutes