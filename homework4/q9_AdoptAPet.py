# Array/String Technique: Maintain a queue - Double-ended (deque)
# Time Complexity: O(1)
# Space Complexity: O(N)

from collections import deque

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.timestamp = 0

    def enqueue(self, name: str, species: str) -> None:
        if species == "dog":
            self.dogs.append((name, self.timestamp))
        elif species == "cat":
            self.cats.append((name, self.timestamp))
        self.timestamp += 1

    def dequeueAny(self) -> str:
        if not self.dogs and not self.cats:
            return None
        if not self.dogs:
            return self.cats.popleft()[0]
        if not self.cats:
            return self.dogs.popleft()[0]
        
        if self.dogs[0][1] < self.cats[0][1]:
            return self.dogs.popleft()[0]
        else:
            return self.cats.popleft()[0]

    def dequeueDog(self) -> str:
        return self.dogs.popleft()[0] if self.dogs else None

    def dequeueCat(self) -> str:
        return self.cats.popleft()[0] if self.cats else None

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("Bob", "dog")
    shelter.enqueue("Mia", "cat")
    shelter.enqueue("Rex", "dog")
    print("Dequeue Any:", shelter.dequeueAny())
    print("Dequeue Dog:", shelter.dequeueDog())
    print("Dequeue Cat:", shelter.dequeueCat())

# Time Spent: 20 minutes