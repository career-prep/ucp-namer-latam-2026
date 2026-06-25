#time complexity: O(n)
#space complexity: O(n)

import heapq
def AdoptAPet(pets, incoming):
    dogs = []
    cats = []

    for name, species, days in pets:
        if species == 'dog':
            heapq.heappush(dogs, (-days, name))
        else:
            heapq.heappush(cats, (-days, name))

    counter = 0
    for i in incoming:
        if len(i) == 2:
            if i[1] == 'dog':
                heapq.heappush(dogs, (counter, i[0]))
            else:
                heapq.heappush(cats, (counter, i[0]))
            counter += 1
        else:
            if len(dogs) == 0 and len(cats) == 0:
                print('no pets available')
            elif i[2] == 'dog':
                if len(dogs) > 0:
                    adopted = heapq.heappop(dogs)
                    print(f'{adopted[1]}, dog')
                else:
                    adopted = heapq.heappop(cats)
                    print(f'{adopted[1]}, cat')
            else:
                if len(cats) > 0:
                    adopted = heapq.heappop(cats)
                    print(f'{adopted[1]}, cat')
                else:
                    adopted = heapq.heappop(dogs)
                    print(f'{adopted[1]}, dog')

#test cases
initial = [("Sadie",  "dog", 4),("Woof",   "cat", 7),("Chirpy", "dog", 2),("Lola",   "dog", 1),]
operations = [("Bob","person", "dog"),("Floofy", "cat"),("Sally", "person", "cat"),("Ji","person",  "cat"),("Ali","person", "cat"),
]

AdoptAPet(initial, operations)