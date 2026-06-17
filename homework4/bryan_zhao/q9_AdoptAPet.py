# Technique: Regular Queue
# Time Complexity: O(1) since append and pop are constant time
# Space Complexity: O(P) where P is the # of pets

from collections import deque

class AnimalShelter:
    def __init__(self, initial_pets: list[dict]):
        self.dogs = deque()
        self.cats = deque()
        self.timestamp = 0

        initial_sorted = sorted(initial_pets, key=lambda x: x['days'], reverse=True)
        for pet in initial_sorted:
            pet_data = {"name": pet["name"], "species": pet["species"], "arrival_order": self.timestamp}
            self.timestamp += 1

            if pet["species"] == "dog":
                self.dogs.append(pet_data)
            elif pet["species"] == "cat":
                self.cats.append(pet_data)

        
    def enqueue_animal(self, name: str, species: str) -> None:
        pet_data = {"name": name, "species": species, "arrival_order": self.timestamp}
        self.timestamp += 1

        if species == "dog":
            self.dogs.append(pet_data)
        elif species == "cat":
            self.cats.append(pet_data)

    def adopt(self, preferred_species: str) -> str:
        if not self.dogs and not self.cats:
            return ""
        
        if preferred_species == "dog":
            if self.dogs:
                pet = self.dogs.popleft()
                return f"{pet['name']}, dog"
            else:
                pet = self.cats.popleft()
                return f"{pet['name']}, cat"
        elif preferred_species == "cat":
            if self.cats:
                pet = self.cats.popleft()
                return f"{pet['name']}, cat"
            else:
                pet = self.dogs.popleft()
                return f"{pet['name']}, dog"

initial_inventory = [
    {"name": "Sadie", "species": "dog", "days": 4},
    {"name": "Woof", "species": "cat", "days": 7},
    {"name": "Chirpy", "species": "dog", "days": 2},
    {"name": "Lola", "species": "dog", "days": 1}
]

shelter = AnimalShelter(initial_inventory)
print("Input: Bob, person, dog")
print("Output:", shelter.adopt("dog"))

print("Input: Floofy, cat")
shelter.enqueue_animal("Floofy", "cat")
print("Output: ")

print("Input: Sally, person, cat")
print("Output:", shelter.adopt("cat"))

print("Input: Ji, person, cat")
print("Output:", shelter.adopt("cat"))

print("Input: Ali, person, cat")
print("Output:", shelter.adopt("cat"))

# Time Spent: 38 minutes