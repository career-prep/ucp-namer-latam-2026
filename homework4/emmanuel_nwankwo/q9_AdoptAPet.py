# Technique: Maintain a queue (Deque)
# Time Complexity: O(p + e)
# Space Complexity: O(p)

from collections import deque

def adopt_pet(initial_pets, events):
    dogs = deque()
    cats = deque()

    for name, species, days in sorted(initial_pets, key=lambda x: x[2], reverse=True):
        if species == "dog":
            dogs.append(name)
        else:
            cats.append(name)

    outputs = []
    for event in events:
        if event[1] == "person":
            desired = event[2]

            if desired == "dog":
                if dogs:
                    outputs.append((dogs.popleft(), "dog"))
                elif cats:
                    outputs.append((cats.popleft(), "cat"))
            else:
                if cats:
                    outputs.append((cats.popleft(), "cat"))
                elif dogs:
                    outputs.append((dogs.popleft(), "dog"))
        else:
            name = event[0]
            species = event[1]

            if species == "dog":
                dogs.append(name)
            else:
                cats.append(name)
    return outputs

# Time Taken: 14mins 21secs

# Testcases:
initial_pets_1 = [
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1)
]

events_1 = [
    ("Bob", "person", "dog"),
    ("Floofy", "cat"),
    ("Sally", "person", "cat"),
    ("Ji", "person", "cat"),
    ("Ali", "person", "cat")
]
print(adopt_pet(initial_pets_1, events_1))

# Edge cases:
# Desired species unavailable
initial_pets_2 = [
    ("Milo", "dog", 3)
]
events_2 = [
    ("Ana", "person", "cat")
]
print(adopt_pet(initial_pets_2, events_2))

initial_pets_3 = [] # No pets
events_3 = [
    ("Ben", "person", "dog")
]
print(adopt_pet(initial_pets_3, events_3))