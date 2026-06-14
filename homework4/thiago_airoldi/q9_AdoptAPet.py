# Maintain Two Heaps
# O(nlog(n)) Time Complexity, because for n events, we do either a heap push or a heap pop, where both of those operations run in log(n) time.
# O(n) Space Complexity, where n is the number of animals in the heaps. In the worst case, one heap has all the animals.
# An animal shelter that houses cats and dogs wants to ensure no pet has to wait too long for a forever home.
# Therefore, anyone who comes to adopt a pet can pick the species (cat or dog) but not the specific animal;
# they are assigned the animal of that species that has been in the shelter longest.
# If there are no animals available of the desired species, they must take the other species.
# You are given a list of pets in the shelter with their names, species, and time in the shelter at the start of a week.
# You receive a sequence of incoming people (to adopt pets) and animals (new additions to the shelter) one at a time. 
# Print the names and species of the pets as they are adopted out.

import heapq

def adoptAPet(initialShelter, incoming):

    if not incoming:
        print("No persons or animals came today.")
        return


    # First, fill up two max heaps, one for the dogs, and another for the cats. Each animal is sorted based on how long they've been waiting.
    cats = []
    dogs = []


    # I would clarify this in an interview, but I am assuming that the input is given either as a 2D array or an array of tuples, like this:
    # [(Sadie, dog, 4), (Woof, cat, 7), ...] and [(Bob, person, dog), (Floofy, cat), ...]

    # Read from 'initialShelter' to fill up each max heap
    for name, species, days in initialShelter:

        if species == "cat": # I'm assuming all species input is lowercase, but I would ask if I need to clean the input before reading anything
            # Push (days, name) into the max heap
            heapq.heappush(cats, (-1 * days, name)) # Since heapq is a min heap by default, we need to push negative values to use heapq like a max heap
        else:
            # species == "dog"
            heapq.heappush(dogs, (-1 * days, name))


    
    # Now read one at a time from 'incoming' to complete adoptions or add more animals to the shelter
    for i in range(len(incoming)):

        # By reading the 2nd column in each row of the array of tuples or the 2D array, we will find out if we are dealing with a person or an animal


        # Case 1: Person wants to adopt an animal
        if incoming[i][1] == "person":

            # Before reading which animal this person wants, check if we even have any animals in the shelter
            if len(cats) == 0 and len(dogs) == 0:
                print("There are no animals in the shelter to adopt.")
                continue
            # If our program goes past this if-statement, we know that at least one of our heaps has an animal, so this person will be leaving with something
            
            # Read in which animal they want
            preferredAnimal = incoming[i][2]

            if preferredAnimal == "dog":
                
                # Now check if we have any dogs in the shelter
                if len(dogs) == 0:
                    # Since we know at least one of our heaps has an animal, and we just found out that we don't have dogs, then we must have at least one cat

                    # Therefore, this person will be adopting a cat
                    negDays, petName = heapq.heappop(cats)

                    print(f"{petName}, cat")

                else:
                    # len(dogs) > 0, so we have dogs in this shelter
                    negDays, petName = heapq.heappop(dogs)
                    print(f"{petName}, dog")

            else:
                # preferredAnimal == "cat"

                if len(cats) == 0:
                    # We have no cats in the shelter, but we do have dogs, so this person will be adopting a dog instead
                    negDays, petName = heapq.heappop(dogs)
                    print(f"{petName}, dog")

                else:
                    # len(cats) > 0, so this shelter has cats
                    negDays, petName = heapq.heappop(cats)
                    print(f"{petName}, cat")


        else:
            # An animal needs to be added to our shelter

            # Since this animal is being added after the initial storage, this cat will be assigned 0 for their number of days in the shelter
            # I would ask in an interview if there is any rule to increase days waited after a certain number of inputs processed from the incoming stream
            # Maybe that would be a follow-up?

            petName = incoming[i][0]
            species = incoming[i][1]

            if species == "cat":
                heapq.heappush(cats, (0, petName))
            else:
                # species == "dog"
                heapq.heappush(dogs, (0, petName))






# 15 minutes

shelter1 = [("Sadie", "dog", 4), ("Woof", "cat", 7), ("Chirpy", "dog", 2), ("Lola", "dog", 1)]
incoming1 = [("Bob", "person", "dog"), ("Floofy", "cat"), ("Sally", "person", "cat"), ("Ji", "person", "cat"), ("Ali", "person", "cat")]

shelter2 = [("Sadie", "dog", 4), ("Woof", "cat", 7)]
incoming2 = []



adoptAPet(shelter1, incoming1)
print()
adoptAPet(shelter1, incoming2)
print()
adoptAPet(shelter2, incoming1)
print()






    

