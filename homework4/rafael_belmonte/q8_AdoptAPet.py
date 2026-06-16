# Technique: Maintain a queue
# time complexity: O(n log n + e)
# space complexity: O(n)

from collections import deque


def adopt_a_pet(initial_pets, events):
    cats = deque()
    dogs = deque()
    adopted = []

    for name, species, days in sorted(initial_pets, key=lambda pet: -pet[2]):
        if species == "cat":
            cats.append(name)
        if species == "dog":
            dogs.append(name)

    for event in events:
        if len(event) == 2:
            name, species = event
            if species == "cat":
                cats.append(name)
            if species == "dog":
                dogs.append(name)
        else:
            name, kind, species = event
            if kind != "person":
                continue
            if species == "cat" and cats:
                adopted.append((cats.popleft(), "cat"))
            elif species == "dog" and dogs:
                adopted.append((dogs.popleft(), "dog"))
            elif cats:
                adopted.append((cats.popleft(), "cat"))
            elif dogs:
                adopted.append((dogs.popleft(), "dog"))
    return adopted

#test cases
initial_pets = [
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1),
]
events = [
    ("Bob", "person", "dog"),
    ("Floofy", "cat"),
    ("Sally", "person", "cat"),
    ("Ji", "person", "cat"),
    ("Ali", "person", "cat"),
]

assert adopt_a_pet(initial_pets, events) == [
    ("Sadie", "dog"),
    ("Woof", "cat"),
    ("Floofy", "cat"),
    ("Chirpy", "dog"),
]
assert adopt_a_pet([], [("Bob", "person", "cat")]) == []

# edge cases
assert adopt_a_pet([("Milo", "cat", 3)], [("Bob", "person", "dog")]) == [
    ("Milo", "cat")
]
assert adopt_a_pet([("Rex", "dog", 1)], [("Bob", "person", "cat")]) == [
    ("Rex", "dog")
]
assert adopt_a_pet([], [
    ("NewCat", "cat"),
    ("Ann", "person", "cat"),
    ("NewDog", "dog"),
    ("Sam", "person", "dog"),
]) == [("NewCat", "cat"), ("NewDog", "dog")]
assert adopt_a_pet([
    ("OldCat", "cat", 8),
    ("YoungCat", "cat", 2),
], [("Ann", "person", "cat"), ("Sam", "person", "cat")]) == [
    ("OldCat", "cat"),
    ("YoungCat", "cat"),
]

print("yay!!")

# Time spent: ~30 minutes
