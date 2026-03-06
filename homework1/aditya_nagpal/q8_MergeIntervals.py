#time taken: 25 mins
#complexity: O(n)
# method used: stacks

#given:
  # a list of pairs representing intervals

#task:
  # return a list in which overlapping intervals are merged
  #r = [(1, 2), (2, 3), (4, 8), (5, 7), (9, 12)]
  #print(r[0][1])

#eg 
  #[(1, (2, 3), (4, 8), (5, 7), (9, 12)]
  # output: [(1, 3), (4, 8), (9, 12)]


#algo
  # sort the given list of intervals
  #  create a stack
  #push the interval in the stack and if
  # eg (a, b) [already in the stack] and (c, d)
  # if c is <= b, then merge new interval in the stack will be (a, max(b, d))
  # continue this until the end of the given list

def MergeIntervals(arr):
    arr.sort()
    stack = []
    for interval in arr:
        
        if not stack:
            stack.append(interval)
        
        if interval[0] <= stack[-1][1]:
            stack[-1] = (stack[-1][0], max(interval[1], stack[-1][1]))
        else:
            stack.append(interval)

    return stack

print(MergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(MergeIntervals([(5, 8), (6,10), (2,4), (3,6)]))
print(MergeIntervals([(10, 12), (5,6), (7,9), (1,3)]))

# new algo:
#sort the tuple
# convert tuple into list
# three pointers in the list:
  #i = 0, j = 1, k = 2

  # start the loop until k reaches end of list:
    # if arr[j] >= arr[k]
        # j = k
        # del d_arr[j]
        #k = k +1
    # else:
        # j = j + 1
        # k = k+ 1


