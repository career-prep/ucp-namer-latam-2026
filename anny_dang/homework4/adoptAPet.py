from collections import deque


def adoptAPets(shelter, new_comings):
    """
    idea:
    - sort shelter following to number of days they have been in shelter
    - create 2 queues cats and dogs
    - put all cats in shelter into cats queue
    - put all dogs in shelter into dogs queue
    - no need to add number of days in queues, because new dogs and cats 
    will be added in order
    - walk through each new coming input
        - if value at 2nd index of new coming = person 
            - if 3rd index of new coming = cat
                - if have cats -> adopt oldest cat
                - else -> adopt oldest dog
            - else:
                - if have dogs -> adopt oldest dog
                - else -> adopt oldest cat
        - else:
            - if cat -> add into cats queue
            - if dog -> add into dogs queue 
    
    time: O(nlogn + m) (n: total number of cats and dogs, m: number of new inputs)
    space: O(n + added pets)
    """
    shelter.sort(reverse=True, key=lambda pet: pet[2])
    cats = deque([])
    dogs = deque([])

    for name, species, _ in shelter:
        if species == "cat":
            cats.append((name, species))
        else:
            dogs.append((name, species))
    
    for new_coming in new_comings:
        if new_coming and new_coming[1] == "person":
            if new_coming[2] == "cat":
                if cats:
                    print(cats.popleft())
                else:
                    print(dogs.popleft())
            else:
                if dogs:
                    print(dogs.popleft())
                else:
                    print(cats.popleft())
        else:
            print("new pet is added")
            if new_coming[1] == "cat":
                cats.append((new_coming[0], new_coming[1]))
            else:
                dogs.append((new_coming[0], new_coming[1]))


shelter = [
    ("Sadie", "dog", 4),
    ("Woof", "cat", 7),
    ("Chirpy", "dog", 2),
    ("Lola", "dog", 1),
]

inputs = [
    ("Bob", "person", "dog"),
    ("Floofy", "cat"),
    ("Sally", "person", "cat"),
    ("Ji", "person", "cat"),
    ("Ali", "person", "cat"),
]

adoptAPets(shelter, inputs)
