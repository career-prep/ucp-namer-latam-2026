#Samaksh Arora
#Merge Intervals
#Time Complexity: O(n*log(n))
#Space Complexity: O(n)
#Sort Array then Solve

def MergeIntervals(pairs):
    pairs = sorted(pairs)
    leftPtr = 0
    rightPtr = 1
    result = []
    while rightPtr < len(pairs):
        curr_start, curr_end= pairs[leftPtr][0], pairs[leftPtr][1]
        next_start, next_end = pairs[rightPtr][0], pairs[rightPtr][1]

        if curr_end >= next_start:
            pairs[leftPtr] = (curr_start, max(curr_end, next_end))
        else:
            result.append(pairs[leftPtr])
            leftPtr = rightPtr

        rightPtr += 1

    result.append(pairs[leftPtr])
    return result

test = [(2,3), (4,8), (1,2), (5,7), (9,12)]
print(MergeIntervals(test)) #output = [(1, 3), (4, 8), (9, 12)]

test = [(5,8), (6,10), (2,4), (3,6)]
print(MergeIntervals(test)) #output = [(2, 10)]

#Time Spent: 35 minutes