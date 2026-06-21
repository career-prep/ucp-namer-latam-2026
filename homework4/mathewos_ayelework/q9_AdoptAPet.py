# technique: maintain a queue (regular queue per species, ordered by time in shelter)
# time complexity: O(1) per operation (enqueue/dequeue)
# space complexity: O(n) where n = total number of animals
# time taken: 28 mins

from collections import deque

def adoptAPet(initial_pets, events):
    dogs = deque()
    cats = deque()

    # sort initial pets by time in shelter descending so front = longest wait
    initial_pets.sort(key=lambda x: -x[2])
    for name, species, days in initial_pets:
        if species == "dog":
            dogs.append(name)
        else:
            cats.append(name)

    for event in events:
        if event[1] == "person":
            desired = event[2]
            if desired == "dog":
                if dogs:
                    adopted = dogs.popleft()
                    print(f"{adopted}, dog")
                elif cats:
                    adopted = cats.popleft()
                    print(f"{adopted}, cat")
            else:
                if cats:
                    adopted = cats.popleft()
                    print(f"{adopted}, cat")
                elif dogs:
                    adopted = dogs.popleft()
                    print(f"{adopted}, dog")
        else:
            # new animal arriving
            name, species = event[0], event[1]
            if species == "dog":
                dogs.append(name)
            else:
                cats.append(name)


initial_pets = [
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
    ("Ali", "person", "cat"),
]

adoptAPet(initial_pets, events)
# Sadie, dog
# Woof, cat
# Floofy, cat
# Chirpy, dog
