from collections import deque

class Shelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order_counter = 0

    def add_pet(self, name: str, species: str) -> None:
        pet = {"name": name, "species": species, "order": self.order_counter}
        self.order_counter += 1
        if species == "dog":
            self.dogs.append(pet)
        else:
            self.cats.append(pet)

    def adopt(self, preferred_species: str) -> str:
        if preferred_species == "dog":
            if self.dogs:
                pet = self.dogs.popleft()
                return f"{pet['name']}, dog"
            elif self.cats:
                pet = self.cats.popleft()
                return f"{pet['name']}, cat"
        else:
            if self.cats:
                pet = self.cats.popleft()
                return f"{pet['name']}, cat"
            elif self.dogs:
                pet = self.dogs.popleft()
                return f"{pet['name']}, dog"
        return "No pets available"


if __name__ == "__main__":
    shelter = Shelter()
    
    shelter.add_pet("Woof", "cat")
    shelter.add_pet("Sadie", "dog")
    shelter.add_pet("Chirpy", "dog")
    shelter.add_pet("Lola", "dog")

    assert shelter.adopt("dog") == "Sadie, dog"
    
    shelter.add_pet("Floofy", "cat")
    
    assert shelter.adopt("cat") == "Woof, cat"
    assert shelter.adopt("cat") == "Floofy, cat"
    assert shelter.adopt("cat") == "Chirpy, dog"
    assert shelter.adopt("cat") == "Lola, dog"
    assert shelter.adopt("cat") == "No pets available"

    empty_shelter = Shelter()
    assert empty_shelter.adopt("dog") == "No pets available"
    assert empty_shelter.adopt("cat") == "No pets available"

    cat_only = Shelter()
    cat_only.add_pet("Whiskers", "cat")
    cat_only.add_pet("Mittens", "cat")
    assert cat_only.adopt("dog") == "Whiskers, cat"
    assert cat_only.adopt("dog") == "Mittens, cat"
    assert cat_only.adopt("dog") == "No pets available"

    dog_only = Shelter()
    dog_only.add_pet("Rex", "dog")
    assert dog_only.adopt("cat") == "Rex, dog"

    print("All AdoptAPet tests passed!")
