# Runtime: O(nlogn)
# Space complexity: O(n)
# Technique: Maintain two heaps
import heapq
class Shelter:
    def __init__(self, animals):
        self.catHeap = []
        self.dogHeap = []
        self.time = 0
        for name, specie, time in animals:
            if specie == "cat":
                heapq.heappush(self.catHeap, (-time, name))
            else:
                heapq.heappush(self.dogHeap, (-time, name))

    def adoptAPet(self, input):
        if len(input) == 3:
            return self.adoptPet(input)
        else:
            return self.addPet(input)
    def adoptPet(self, input):
        preferred = input[2]
        if preferred == "dog":
            if self.dogHeap:
                animal = heapq.heappop(self.dogHeap)
                return animal[1] + ", dog"
            elif self.catHeap:
                animal = heapq.heappop(self.catHeap)
                return animal[1] + ", cat"
        else:
            if self.catHeap:
                animal = heapq.heappop(self.catHeap)
                return animal[1] + ", cat"
            elif self.dogHeap:
                animal = heapq.heappop(self.dogHeap)
                return animal[1] + ", dog"

        return None
    def addPet(self, input):
        self.time += 1
        if input[1] == "dog":
            heapq.heappush(self.dogHeap, (-self.time, input[0]))
        else:
            heapq.heappush(self.catHeap, (-self.time, input[0]))

animals = [
    ["Sadie", "dog", 4],
    ["Woof", "cat", 7],
    ["Chirpy", "dog", 2],
    ["Lola", "dog", 1]
]

shelter = Shelter(animals)
print(shelter.adoptAPet(["Bob", "person", "dog"]))
print(shelter.adoptAPet(["Floofy", "cat"]))
print(shelter.adoptAPet(["Sally", "person", "cat"]))
print(shelter.adoptAPet(["Ji", "person", "cat"]))
print(shelter.adoptAPet(["Ali", "person", "cat"]))

# Time Spent: 40:00
