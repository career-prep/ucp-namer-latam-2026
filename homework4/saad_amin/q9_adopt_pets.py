# Technique: Maintain a queue: double-ended queue (deque)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque


def adopt_pets(initial_pets, events):
    cats = deque()
    dogs = deque()
    output = []

    for name, species, days in initial_pets:
        if species == "cat":
            cats.append((days, name, species))
        else:
            dogs.append((days, name, species))

    for event in events:
        name = event[0]
        kind = event[1]

        if kind == "cat":
            cats.append((0, name, "cat"))
            print("")

        elif kind == "dog":
            dogs.append((0, name, "dog"))
            print("")

        elif kind == "person":
            requested_species = event[2]
            adopted = None

            if requested_species == "cat":
                if cats:
                    adopted = cats.popleft()
                elif dogs:
                    adopted = dogs.popleft()

            elif requested_species == "dog":
                if dogs:
                    adopted = dogs.popleft()
                elif cats:
                    adopted = cats.popleft()

            if adopted:
                days, pet_name, species = adopted
                output.append((pet_name, species))
                print(pet_name + ", " + species)
            else:
                print("")

    return output


def main():
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
        ("Ali", "person", "cat")
    ]

    adopt_pets(initial_pets, events)


if __name__ == "__main__":
    main()

# Time: 40 min