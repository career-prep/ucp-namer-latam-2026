# Technique: Maintain a queue — two regular queues

from collections import deque


def adopt_a_pet(initial_pets, incoming):
    initial_pets.sort(key=lambda pet: pet[2], reverse=True)

    cats = deque()
    dogs = deque()

    for name, species, days in initial_pets:
        if species == "cat":
            cats.append((name, species))
        else:
            dogs.append((name, species))

    adopted = []

    for event in incoming:
        if event[1] == "person":
            wanted_species = event[2]

            if wanted_species == "cat":
                if cats:
                    pet = cats.popleft()
                elif dogs:
                    pet = dogs.popleft()
                else:
                    continue
            else:
                if dogs:
                    pet = dogs.popleft()
                elif cats:
                    pet = cats.popleft()
                else:
                    continue

            adopted.append(pet)

        else:
            name = event[0]
            species = event[1]

            if species == "cat":
                cats.append((name, species))
            else:
                dogs.append((name, species))

    return adopted

# pets = [
#     ("Sadie", "dog", 4),
#     ("Woof", "cat", 7),
#     ("Chirpy", "dog", 2),
#     ("Lola", "dog", 1)
# ]

# incoming = [
#     ("Bob", "person", "dog"),
#     ("Floofy", "cat"),
#     ("Sally", "person", "cat"),
#     ("Ji", "person", "cat"),
#     ("Ali", "person", "cat")
# ]

# for name, species in adopt_a_pet(pets, incoming):
#     print(name + ", " + species)

# Output:
# Sadie, dog
# Woof, cat
# Floofy, cat
# Chirpy, dog