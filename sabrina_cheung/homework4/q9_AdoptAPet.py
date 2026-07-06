# Method: Two Queues (FIFO)
# Time Complexity: O(1)
# Space Complexity: O(N) 
# Total Time Taken: 30 mins
# Add species into a queue where the oldest animal is added first
# When adopting, pop the first animal out from that speciies. If the speciies is not available, pop the first item of the other speicies.

from collections import deque

class AnimalShelter:
    def __init__(self, initial_pets):
        self.dog_queue = deque()
        self.cat_queue = deque()
        
        initial_pets.sort(key=lambda x: x[2], reverse=True)
        
        for name, species, days in initial_pets:
            self.add_pet(name, species)

    def add_pet(self, name, species):
        if species == "dog":
            self.dog_queue.append((name, "dog"))
        elif species == "cat":
            self.cat_queue.append((name, "cat"))

    def adopt(self, preferred_species):
        if preferred_species == "dog":
            if self.dog_queue:
                return self.dog_queue.popleft()
            elif self.cat_queue:
                return self.cat_queue.popleft()
        elif preferred_species == "cat":
            if self.cat_queue:
                return self.cat_queue.popleft()
            elif self.dog_queue:
                return self.dog_queue.popleft()
        return None


initial_input = [
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1)
]
shelter = AnimalShelter(initial_input)

print(shelter.adopt("dog"))    # Output: ('Sadie', 'dog')
shelter.add_pet("Floofy", "cat") 
print(shelter.adopt("cat"))    # Output: ('Woof', 'cat')
print(shelter.adopt("cat"))    # Output: ('Floofy', 'cat')
print(shelter.adopt("cat"))    # Output: ('Chirpy', 'dog')