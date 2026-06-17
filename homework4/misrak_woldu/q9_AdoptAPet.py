from collections import deque

# Technique: Maintain a queue
# Data Structure: Two queues, one for cats and one for dogs
# Time Complexity: O(n log n + e)
# Space Complexity: O(n)


def adopt_a_pet(
    initial_pets: list[tuple[str, str, int]],
    events: list[tuple],
) -> list[tuple[str, str]]:
    dog_queue = deque()
    cat_queue = deque()

    # Sort initial pets by time in shelter so longest-waiting pets come first
    sorted_initial_pets = sorted(
        initial_pets,
        key=lambda pet: pet[2],
        reverse=True,
    )

    for pet_name, species, days_waiting in sorted_initial_pets:
        if species == "dog":
            dog_queue.append((pet_name, species))
        elif species == "cat":
            cat_queue.append((pet_name, species))

    adopted_pets = []

    for event in events:
        # Person event format: (person_name, "person", desired_species)
        if len(event) == 3 and event[1] == "person":
            desired_species = event[2]

            adopted_pet = adopt_pet_by_preference(
                desired_species,
                dog_queue,
                cat_queue,
            )

            if adopted_pet is not None:
                adopted_pets.append(adopted_pet)

        # New animal event format: (pet_name, species)
        elif len(event) == 2:
            pet_name, species = event

            if species == "dog":
                dog_queue.append((pet_name, species))
            elif species == "cat":
                cat_queue.append((pet_name, species))

    return adopted_pets


def adopt_pet_by_preference(
    desired_species: str,
    dog_queue: deque,
    cat_queue: deque,
) -> tuple[str, str] | None:
    if desired_species == "dog":
        if dog_queue:
            return dog_queue.popleft()

        if cat_queue:
            return cat_queue.popleft()

    elif desired_species == "cat":
        if cat_queue:
            return cat_queue.popleft()

        if dog_queue:
            return dog_queue.popleft()

    return None


def run_tests() -> None:
    initial_pets = [
        ("Sadie", "dog", 4),
        ("Woof", "cat", 7),
        ("Chirpy", "dog", 2),
        ("Lola", "dog", 1),
    ]

    events = [
        ("Bob", "person", "dog"),
        ("Floofy", "cat"),
        ("Sally", "person", "cat"),
        ("Ji", "person", "cat"),
        ("Ali", "person", "cat"),
    ]

    assert adopt_a_pet(initial_pets, events) == [
        ("Sadie", "dog"),
        ("Woof", "cat"),
        ("Floofy", "cat"),
        ("Chirpy", "dog"),
    ]

    # If desired species is unavailable, adopter takes the other species
    initial_pets_two = [
        ("DogA", "dog", 5),
    ]

    events_two = [
        ("PersonA", "person", "cat"),
    ]

    assert adopt_a_pet(initial_pets_two, events_two) == [
        ("DogA", "dog"),
    ]

    # New animals should go to the back of their species queue
    initial_pets_three = [
        ("CatA", "cat", 3),
    ]

    events_three = [
        ("CatB", "cat"),
        ("PersonA", "person", "cat"),
        ("PersonB", "person", "cat"),
    ]

    assert adopt_a_pet(initial_pets_three, events_three) == [
        ("CatA", "cat"),
        ("CatB", "cat"),
    ]

    # No pets available
    assert adopt_a_pet([], [("PersonA", "person", "dog")]) == []

    # Empty input
    assert adopt_a_pet([], []) == []

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
