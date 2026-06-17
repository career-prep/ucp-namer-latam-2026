# Technique: Maintain a queue (one FIFO per species)
# Time Complexity: O(nlogn) setup, O(1) per event
# Space Complexity: O(total animals)

from collections import deque

class AnimalShelter:
    def __init__(self, initial_pets=None):
        self.queues = {"cat": deque(), "dog": deque()}
        if initial_pets:
            for name, species, _days in sorted(initial_pets, key=lambda p: p[2], reverse=True):
                self.queues[species].append(name)

    def add_animal(self, name, species):
        self.queues[species].append(name)

    def adopt(self, species):
        other = "dog" if species == "cat" else "cat"
        if self.queues[species]:
            return self.queues[species].popleft(), species
        if self.queues[other]:
            return self.queues[other].popleft(), other
        return None

shelter = AnimalShelter([
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1),
])
print(shelter.adopt("dog"))
shelter.add_animal("Floofy", "cat")
print(shelter.adopt("cat"))
print(shelter.adopt("cat"))
print(shelter.adopt("cat"))
print(AnimalShelter().adopt("dog"))

# Time spent: 120
