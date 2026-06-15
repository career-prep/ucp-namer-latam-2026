#Samaksh Arora
#Question 9 - Adopt a Pet
#Maintain a queue
#Time Complexity:
#Space Complexity:
#Time Spent:



class AnimalShelter:
    def __init__(self):
        from collections import deque
        self.species_queues = {}  # {species: queue of animals}
        self.overall_queue = deque()  # track global entry order

    def enqueueAnimal(self, name, species, days_in_shelter):
        from collections import deque
        animal = (name, species, days_in_shelter)

        if species not in self.species_queues:
            self.species_queues[species] = deque()

        self.species_queues[species].append(animal)
        self.overall_queue.append(animal)

    def adoptAnimal(self, preferred_species):
        # If preferred species exists, adopt the oldest of that species
        if preferred_species in self.species_queues and len(self.species_queues[preferred_species]) > 0:
            animal = self.species_queues[preferred_species].popleft()
            self.overall_queue.remove(animal)
            return (animal[0], animal[1])

        # Otherwise, find the oldest animal overall
        while len(self.overall_queue) > 0:
            animal = self.overall_queue.popleft()
            species = animal[1]
            # Check if this animal is still available (not already adopted)
            if animal in self.species_queues[species]:
                self.species_queues[species].remove(animal)
                return (animal[0], animal[1])

        return None    

#Test Cases
# shelter = AnimalShelter()
# shelter.enqueueAnimal("Sadie", "dog", 4)
# shelter.enqueueAnimal("Woof", "cat", 7)
# shelter.enqueueAnimal("Chirpy", "dog", 2)
# shelter.enqueueAnimal("Lola", "dog", 1)
# assert shelter.adoptAnimal("Bob", "dog") == ("Sadie", "dog")
# shelter.enqueueAnimal("Floofy", "cat", 0)
# assert shelter.adoptAnimal("Sally", "cat") == ("Woof", "cat")
# assert shelter.adoptAnimal("Ji", "cat") == ("Floofy", "cat")
# assert shelter.adoptAnimal("Ali", "cat") == ("Chirpy", "dog")

# Extra: shelter2 = AnimalShelter()
# shelter2.enqueueAnimal("Rex", "dog", 3)
# shelter2.enqueueAnimal("Mittens", "cat", 5)
# assert shelter2.adoptAnimal("Mary", "dog") == ("Rex", "dog")
# shelter2.enqueueAnimal("Oscar", "dog", 1)
# assert shelter2.adoptAnimal("Nina", "cat") == ("Mittens", "cat")
# assert shelter2.adoptAnimal("Paul", "dog") == ("Oscar", "dog")
