# Question 9: AdoptAPet
# Given the starting pets in a shelter and a sequence of incoming adopters and
# new animals, print the name and species of each adopted pet. Adopters choose
# a species, receive the longest-waiting pet of that species, and receive the
# other species if their preferred species is unavailable.

from collections import deque
class Pet:
    def __init__(self, name, species, days_waiting, arrival_order):
        self.name = name
        self.species = species
        self.days_waiting = days_waiting
        self.arrival_order = arrival_order
class AnimalShelter:
    def __init__(self, initial_pets):
        self.cats = deque()
        self.dogs = deque()
        self.arrival_order = 0
        pets = []
        for name, species, days_waiting in initial_pets:
            pets.append(Pet(name, species, days_waiting, self.arrival_order))
            self.arrival_order += 1
        pets.sort(key=lambda pet: (-pet.days_waiting, pet.arrival_order))
        for pet in pets:
            self.add_existing_pet(pet)
    def add_existing_pet(self, pet):
        if pet.species == "cat":
            self.cats.append(pet)
        else:
            self.dogs.append(pet)
    def add_pet(self, name, species):
        pet = Pet(name, species, 0, self.arrival_order)
        self.arrival_order += 1
        if species == "cat":
            self.cats.append(pet)
        else:
            self.dogs.append(pet)
    def adopt(self, preferred_species):
        if preferred_species == "cat":
            if self.cats:
                return self.cats.popleft()
            if self.dogs:
                return self.dogs.popleft()
        else:
            if self.dogs:
                return self.dogs.popleft()
            if self.cats:
                return self.cats.popleft()
        return None
def adopt_a_pet(initial_pets, events):
    shelter = AnimalShelter(initial_pets)
    adopted = []
    for event in events:
        if len(event) == 3 and event[1] == "person":
            pet = shelter.adopt(event[2])
            if pet:
                adopted.append((pet.name, pet.species))
            else:
                adopted.append(None)
        else:
            name, species = event
            shelter.add_pet(name, species)
    return adopted
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



print(adopt_a_pet(initial_pets, events))
print(adopt_a_pet([], [("Nia", "person", "dog")]))
print(adopt_a_pet([("Mochi", "cat", 2)], [("Sam", "person", "dog")]))



# Spent 30 mins
# Time Complexity: O(n + e), where n is initial pets and e is events.
# Space Complexity: O(n + e)
