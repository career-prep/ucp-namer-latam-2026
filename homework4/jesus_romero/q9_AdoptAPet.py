# Runtime:
# Time: O(1) each adoption
# Space: O(n)
# Implementation time: 35 minutes

from collections import deque


class AnimalShelter:
    def __init__(self):
        #1. Declare variables
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def intake(self, name, species):
        #1. Add animal
        animal = [self.order, name, species]

        if species == "dog":
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

        self.order += 1

    def adopt(self, person_name, preferred_species):
        #1. Check preferred species
        if preferred_species == "dog" and self.dogs:
            animal = self.dogs.popleft()
            return animal[1], animal[2]

        if preferred_species == "cat" and self.cats:
            animal = self.cats.popleft()
            return animal[1], animal[2]

        #2. Take other species
        if self.dogs and self.cats:
            if self.dogs[0][0] < self.cats[0][0]:
                animal = self.dogs.popleft()
            else:
                animal = self.cats.popleft()

            return animal[1], animal[2]

        #3. Check remaining animal
        if self.dogs:
            animal = self.dogs.popleft()
            return animal[1], animal[2]

        if self.cats:
            animal = self.cats.popleft()
            return animal[1], animal[2]

        #4. Return no animal
        return None


def Test_AnimalShelter():
    #1. Declare shelter
    shelter = AnimalShelter()

    #2. Add initial animals
    shelter.intake("Sadie", "dog")
    shelter.intake("Woof", "cat")
    shelter.intake("Chirpy", "dog")
    shelter.intake("Lola", "dog")

    #3. Run sample inputs
    print("Input: Bob, person, dog")
    print("Output:", shelter.adopt("Bob", "dog"))
    print()

    print("Input: Floofy, cat")
    shelter.intake("Floofy", "cat")
    print("Output:")
    print()

    print("Input: Sally, person, cat")
    print("Output:", shelter.adopt("Sally", "cat"))
    print()

    print("Input: Ji, person, cat")
    print("Output:", shelter.adopt("Ji", "cat"))
    print()

    print("Input: Ali, person, cat")
    print("Output:", shelter.adopt("Ali", "cat"))


if __name__ == "__main__":
    Test_AnimalShelter()