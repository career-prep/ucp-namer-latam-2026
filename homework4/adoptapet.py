# Technique: Maintain a queue (regular / FIFO)
# One queue per species, longest-waiting at the front; fall back to other species
# Time: O(p log p + e)
# Space: O(p + e)

from collections import deque


def adoptAPet(initialPets, events):
    # person:  (name, "person", desiredSpecies)
    # animal:  (name, species)
    dogs, cats = deque(), deque()

    for name, species, days in sorted(initialPets, key=lambda p: p[2], reverse=True):
        (dogs if species == "dog" else cats).append(name)

    output = []
    for event in events:
        if len(event) == 3:
            desired = event[2]
            primary = dogs if desired == "dog" else cats
            other = cats if desired == "dog" else dogs
            if primary:
                output.append((primary.popleft(), desired))
            elif other:
                output.append((other.popleft(), "cat" if desired == "dog" else "dog"))
            else:
                output.append(None)
        else:
            name, species = event
            (dogs if species == "dog" else cats).append(name)
            output.append(None)
    return output


initialPets = [("Sadie", "dog", 4), ("Woof", "cat", 7),
               ("Chirpy", "dog", 2), ("Lola", "dog", 1)]
events = [("Bob", "person", "dog"), ("Floofy", "cat"),
          ("Sally", "person", "cat"), ("Ji", "person", "cat"),
          ("Ali", "person", "cat")]

for entry in adoptAPet(initialPets, events):
    print("Output:" if entry is None else f"Output: {entry[0]}, {entry[1]}")
# Sadie, dog / (empty) / Woof, cat / Floofy, cat / Chirpy, dog

# Time spent: ~40 minutes