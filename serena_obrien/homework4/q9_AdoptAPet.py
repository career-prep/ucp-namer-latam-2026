from collections import deque

# Time complexity: O(m + n) with m = initial pets and n = number of events
# Space complexity: O(m + n) with m = initial pets and n = number of events

# Technique: Multiple query problems: two queues 
# I am assuming that insertion order is chronological order, if they aren't we could just sort I think, but maybe there is a more elegant solution

def AdoptAPet(initial_pets, events):
    cat_q = deque()
    dog_q = deque()

    for name, species, time in initial_pets:
        if species == "cat":
            cat_q.append((name, species, time))
        else:
            dog_q.append((name, species, time))

    for event in events:
        parts = [x.strip() for x in event.split(",")]

        # adoption request
        if parts[1] == "person":
            preferred = parts[2]

            if preferred == "cat":
                if cat_q:
                    adopted = cat_q.popleft()
                else:
                    adopted = dog_q.popleft()
            else:
                if dog_q:
                    adopted = dog_q.popleft()
                else:
                    adopted = cat_q.popleft()

            print(f"{adopted[0]}, {adopted[1]}")

        else:
            name = parts[0]
            species = parts[1]
            time = len(cat_q) + len(dog_q) 

            if species == "cat":
                cat_q.append((name, species, time))
            else:
                dog_q.append((name, species, time))


if __name__ == "__main__":
    initial_pets = [
        ("Sadie", "dog", 4),
        ("Woof", "cat", 7),
        ("Chirpy", "dog", 2),
        ("Lola", "dog", 1)
    ]

    events = [
        "Bob, person, dog",
        "Floofy, cat",
        "Sally, person, cat",
        "Ji, person, cat",
        "Ali, person, cat"
    ]

    AdoptAPet(initial_pets, events)

# ~ time spent: ~30 minutes