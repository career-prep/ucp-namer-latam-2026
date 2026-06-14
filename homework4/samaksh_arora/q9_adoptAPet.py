#Samaksh Arora
#Question 9 - Adopt a Pet
#Maintain a queue
#Time Complexity:
#Space Complexity:
#Time Spent:



class AnimalShelter:
    def __init__(self):
        pass

    def enqueueAnimal(self, name, species, days_in_shelter):
        pass

    def adoptAnimal(self, person_name, preferred_species):
        pass

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
