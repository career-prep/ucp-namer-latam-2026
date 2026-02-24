# [(1,2), (2,3), (4,8), (5,7), (9,12)]
# [(1,3), (4,8), (9,12)]

# [(2,4), (3,6), (5,8), (6,10)]
# [(2,6),(6,8), (8,10)]
# [(2,10)]

def mergeIntervals(pairs: list) -> list:
    pairs.sort() # O(nlogn) Time
    result = []
    p = 0
    c = 1
    while c < len(pairs):
        # p1 = pairs[p][0]
        # p2 = pairs[p][1]

        # c1 = pairs[c][0]
        # c2 = pairs[c][1]
        
        while pairs[p][1] >= pairs[c][0] and c < len(pairs):
            pairs[c]= (min(pairs[p][0],pairs[c][0]), max(pairs[p][1],pairs[c][1]))

            p += 1
            c += 1
            # p1 = pairs[p][0]
            # p2 = pairs[p][1]
            # c1 = pairs[c][0]
            # c2 = pairs[c][1]


        result.append((pairs[p][0],pairs[p][1]))
        print(pairs[c][0], pairs[c][1])
        p += 1
        c += 1
        
    print("result",result)





print("mergeIntervals Results:")
test_cases = [
            # [(2,3), (4,8), (1,2), (5,7), (9,12)],
            [(5,8), (6,10), (2,4), (3,6)],
            # [(10,12), (5,6), (7,9), (1,3)],
              ]
for test_case in test_cases:
    print(mergeIntervals(test_case)) #Expected Output: 

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Time Taken: 40mins