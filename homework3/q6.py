"""
time = n^2
space = n

40 minutes
"""
"""
["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", 
"Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"], 
[("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"),
 ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), 
 ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]


"Skagway".       ->
"Juneau".        -> 
"Gustavus",      -> Glacier Bay,
"Homer",         -> Anchorage,
"Port Alsworth". ->
"Glacier Bay",   -> Gustavus,
"Fairbanks",     -> Copper Center, Healy
"McCarthy",      -> Copper Center,
"Copper Center", -> McCarthy, Anchorage, Fairbanks
"Healy",         -> Fairbanks, Anchorage
"Anchorage"      -> homer, Copper Center, Healy

Gustavus-Glacier Bay
Homer-Anchorage-Copper Center-McCarthy-Fairbanks-Healy




"""
from collections import defaultdict
from collections import deque
def main(input, lst):
    dic = defaultdict(list)
    for a, b in lst:
        dic[a].append(b)
        dic[b].append(a)

    count = 0
    visited = set()
    res = []
    for key, val in dic.items():
        
        cont = 0
        queue = deque([key])
        check = []
        
        while queue:
            val = queue.popleft()

            for each in dic[val]:
                if each not in visited:
                    queue.append(each)
            visited.add(val)
            check.append(val)
        
            cont += 1
            
            
    
        if cont > 1:
            count += 1
            res.append(check)


    return count, res
inpt = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]
lit = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
print(main(inpt, lit))


i2put =["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
l2t =[("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(main(i2put, l2t))
