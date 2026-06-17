import heapq
# O(n) time and space complexity 
# This is a two heap problem

# Understanding the problem
""" 
We are given an initial list of animals which includes their names, 
how long they've been in the shelter for and their species 

We are then given a stream of either people looking to adopt or new animals
to be put up for adoption

If a person comes in for adoption, they get the species they want and the
animal that has been in the adoption center the longest

If there are no more of that species, they get another one that has been
in the adoption center the longest

Print the name and species of the pets as they are adopted out
"""
# Example Pets input [(Sadie, dog, 4), (Woof, cat, 7), (Chirpy, dog, 2), (Lola, dog, 1)]
# (Name, Species, Time in center)

cat_heap = []
dog_heap = []

def adoptAPet(pets):
    global cat_heap, dog_heap

    cat_heap = []
    dog_heap = []

    # First step, build a heap for each
    for name, species, time in pets:
        if species == 'cat':
            cat_heap.append((-time, species,name))

        if species == 'dog':
            dog_heap.append((-time, species,name))

    heapq.heapify(cat_heap)
    heapq.heapify(dog_heap) # O(n) operations 

# Example data_stream Input:
# (Bob, person, dog) which means Bob is a person who wants a dog
# Or (Floofy, cat) which means floofy the cat just got dropped off

def updatePets(data):
    name = data[0]
    species = data[1]

    if species == 'person':
        adopt_species = data[2]

        if adopt_species == 'cat' and cat_heap:
            time, pet_species, pet_name = heapq.heappop(cat_heap)
            print(f"{pet_name}, {pet_species}")
        elif adopt_species == 'dog' and dog_heap:
            time, pet_species, pet_name = heapq.heappop(dog_heap)
            print(f"{pet_name}, {pet_species}")
        elif dog_heap:
            time, pet_species, pet_name = heapq.heappop(dog_heap)
            print(f"{pet_name}, {pet_species}")
        elif cat_heap:
            time, pet_species, pet_name = heapq.heappop(cat_heap)
            print(f"{pet_name}, {pet_species}")
        else:
            print(" ")

    elif species == 'cat':
        heapq.heappush(cat_heap, (0, species, name))
    
    else:
        heapq.heappush(dog_heap, (0, species, name))

def main():
    initial_data = [('Sadie', 'dog', 4), ('Woof', 'cat', 7), ('Chirpy', 'dog', 2), ('Lola', 'dog', 1)]
    data_stream = [('Bob', 'person', 'dog'), ('Floofy', 'cat'), ('Sally', 'person', 'cat'), ('Ji', 'person', 'cat'), ('Ali', 'person', 'cat')]

    adoptAPet(initial_data)

    for data in data_stream:
        updatePets(data)


main()

# This took me 35 minutes total