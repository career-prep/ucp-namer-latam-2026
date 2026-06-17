#Time: O(n log n) - sorting animals by days; O(1) per adopt call
#Space: O(n) - storing animals in two deques


from collections import deque

class AnimalShelter:
    def __init__(self, animals):
        self.dogs = deque()
        self.cats = deque()

        animals.sort(key=lambda x: -x[2])

        for name, species, days in animals:
            if species == "dog":
                self.dogs.append((name, species))
            else:
                self.cats.append((name, species))

    def adopt(self, preferred_species):

        if preferred_species == "dog":
            if self.dogs:
                return self.dogs.popleft()
            elif self.cats:
                return self.cats.popleft()

        elif preferred_species == "cat":
            if self.cats:
                return self.cats.popleft()
            elif self.dogs:
                return self.dogs.popleft()

        return None

#Time-taken: 35 minutes


import unittest


class TestAnimalShelter(unittest.TestCase):

    def setUp(self):
        animals = [
            ("Buddy", "dog", 5),
            ("Whiskers", "cat", 10),
            ("Max", "dog", 3),
            ("Fluffy", "cat", 7),
            ("Rex", "dog", 1),
        ]
        self.shelter = AnimalShelter(animals)

    def test_adopt_dog_prefers_dog(self):
        self.assertEqual(self.shelter.adopt("dog"), ("Buddy", "dog"))

    def test_adopt_cat_prefers_cat(self):
        self.assertEqual(self.shelter.adopt("cat"), ("Whiskers", "cat"))

    def test_fallback_when_preferred_type_empty(self):
        self.shelter.dogs.clear()
        self.assertEqual(self.shelter.adopt("dog"), ("Whiskers", "cat"))


if __name__ == "__main__":
    unittest.main()