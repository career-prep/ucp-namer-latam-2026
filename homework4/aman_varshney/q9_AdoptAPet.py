# spent 50 minutes
# deques
# TC - O(nlogn)
# SC - O(n)

from collections import deque


def adopt_pets(pets: list[tuple[str, str, int]], events: list[tuple[str, str, str] | tuple[str, str]]) -> None:
    """Prints adoption given database of available pets and preference. Or adds a pet to the database."""
    cats = deque()
    dogs = deque()

    # Oldest pets first
    for name, species, time in sorted(pets, key=lambda x:x[2], reverse=True):
        if species == "cat":
            cats.append(name)
        elif species == "dog":
            dogs.append(name)
        else:
            print("Invalid animal")
            return

    for event in events:
        if event[1] == "person":
            _, _, preference = event
            if preference == "cat":
                if cats:
                    adopted = cats.popleft()
                    print(f"{adopted}, cat")
                elif dogs:
                    adopted = dogs.popleft()
                    print(f"{adopted}, dog")
                else:
                    print("No available animals")
                    return
            else:
                if dogs:
                    adopted = dogs.popleft()
                    print(f"{adopted}, dog")
                elif cats:
                    adopted = cats.popleft()
                    print(f"{adopted}, cat")
                else:
                    print("No available animals")
                    return
        elif event[1] == "dog":
            name, _ = event
            dogs.append(name)
            print()
        elif event[1] == "cat":
            name, _ = event
            cats.append(name)
            print()
        else:
            print("Invalid animal")
            return


def run_tests():
    initial_input = [
        ("sadie", "dog", 4),
        ("woof", "cat", 7),
        ("chirpy", "dog", 2),
        ("lola", "dog", 1),
    ]
    events = [
        ("bob", "person", "dog"),
        ("floofy", "cat"),
        ("sally", "person", "cat"),
        ("ji", "person", "cat"),
        ("ali", "person", "cat"),
    ]

    print("Expected:")
    print("sadie, dog")
    print()
    print("woof, cat")
    print("floofy, cat")
    print("chirpy, dog")

    print()
    print("Actual:")
    adopt_pets(initial_input, events)


if __name__ == "__main__":
    run_tests()
