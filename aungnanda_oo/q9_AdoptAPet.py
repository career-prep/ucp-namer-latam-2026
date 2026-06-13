# Question 9: AdoptAPet

# Technique: Maintain a queue (two queues — one per species)
# One deque for dogs, one for cats, each ordered by time in shelter
# (longest-waiting at the front).
# When a person arrives wanting species X: dequeue from X's queue.
# If X's queue is empty, dequeue from the other species' queue.
# When a new animal arrives: enqueue to the appropriate species queue.

# Assumption: "time in shelter" for initial animals is used to pre-sort
# them so the longest-waiting is at the front. New arrivals are appended
# to the back (they just arrived, so they wait the longest from now).

# Time Complexity:  O(n log n) for initial sort + O(1) per event (enqueue/dequeue)
# Space Complexity: O(n) for the queues

from collections import deque


class Shelter:
    def __init__(self, initial_pets):
        # initial_pets: list of (name, species, days_in_shelter)
        # Sort by days descending so longest-waiting is at front after sorting
        dogs = sorted(
            [(name, days) for name, species, days in initial_pets if species == "dog"],
            key=lambda x: -x[1]
        )
        cats = sorted(
            [(name, days) for name, species, days in initial_pets if species == "cat"],
            key=lambda x: -x[1]
        )
        self.dogs = deque(name for name, _ in dogs)
        self.cats = deque(name for name, _ in cats)

    def add_animal(self, name, species):
        if species == "dog":
            self.dogs.append(name)
        else:
            self.cats.append(name)

    def adopt(self, preferred_species):
        if preferred_species == "dog":
            if self.dogs:
                name = self.dogs.popleft()
                print(f"{name}, dog")
            elif self.cats:
                name = self.cats.popleft()
                print(f"{name}, cat")
            else:
                print("No pets available")
        else:  # cat
            if self.cats:
                name = self.cats.popleft()
                print(f"{name}, cat")
            elif self.dogs:
                name = self.dogs.popleft()
                print(f"{name}, dog")
            else:
                print("No pets available")
# Time Complexity = O(1) per adopt/add, Space Complexity = O(n)


# --- Tests ---

print("=== Example from task ===")
initial = [
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1),
]
shelter = Shelter(initial)

shelter.adopt("dog")       # Sadie, dog  (waited 4 days, longest among dogs)
shelter.add_animal("Floofy", "cat")
shelter.adopt("cat")       # Woof, cat   (waited 7 days)
shelter.adopt("cat")       # Floofy, cat (only cat left)
shelter.adopt("cat")       # Chirpy, dog (no cats, falls back to dog)

print()
print("=== Additional test: prefer dog, fall back to cat ===")
shelter2 = Shelter([("Luna", "cat", 3)])
shelter2.adopt("dog")      # Luna, cat (no dogs available)

print()
print("=== Additional test: multiple dogs ===")
shelter3 = Shelter([
    ("A", "dog", 10),
    ("B", "dog", 5),
    ("C", "dog", 1),
])
shelter3.adopt("dog")  # A (10 days)
shelter3.adopt("dog")  # B (5 days)
shelter3.adopt("dog")  # C (1 day)
shelter3.adopt("dog")  # No pets available

# Spent a total of 35 mins on this question
