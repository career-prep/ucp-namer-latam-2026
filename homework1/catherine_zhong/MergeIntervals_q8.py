#time complexity: O(nlogn)
#space complexity: O(n)

#assuming order of the pairs does not matter
def MergeIntervals(pairs):
    #sorts pairs in increasing starting index
    pairs = sorted(pairs)
    mergedPairs = []

    i = 0
    #loops through all pairs
    while i < len(pairs):
        start = pairs[i][0]
        end = pairs[i][1]
        #checks if they overlap
        while i + 1 < len(pairs) and end >= pairs[i+1][0]:
            end = pairs[i+1][1]
            i += 1
        mergedPairs.append((start,end))
        i += 1
    
    return mergedPairs

test1 = [(2,3),(4,8),(1,2),(5,7),(9,12)]
test2 = [(5,8),(6,10),(2,4),(3,6)]
test3 = [(10,12),(5,6),(7,9),(1,3)]
print('test1: ', MergeIntervals(test1))
print('test2: ', MergeIntervals(test2))
print('test3: ', MergeIntervals(test3))

#time spent = 20 mins