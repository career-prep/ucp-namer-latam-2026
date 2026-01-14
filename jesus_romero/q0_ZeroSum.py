
"""Q1:
Given an array of integers, return the number of pairs of integers
in the array that sum to 0 assuming you can use the element at each 
index at most once"""

def ZeroSum1Rep(lst): # At most once
    #1. Declare a set that will keep track of seen elements and a count
    seen = set()
    count = 0
    
    #2. Iterate over the list of elements and calculate the inverse
    for el in lst:
        inverse = -el
        #3. If the inverse has been seen, increase the count by 1 since we
        #   have found a pair and remove it so that we count it at most once
        if inverse in seen:
            count += 1
            seen.remove(inverse)
        #4. Otherwise, add the seen element
        else: 
            seen.add(el)
    #5. Return the count
    return count # works for all test cases shown

# Time and Space Complexities -> O(n) for both

"""P2:
Now assume you can re-use elements in diff pairs. Elements in a pair must be from
diff indices but diff pairs may use an element from the same index
"""

def ZeroSumNoLimReps(lst): # any # of times
    #1. Same idea as before but this time using a hashmap to keep track of 
    #   time an element has been seen so far and a count of valid pairs
    seen ={}
    count = 0
    
    #2. Iterate over the list and calc the inverse
    for el in lst:
        inverse = -el
        #3. If the inverse has been seen before, then each prev ocurrence forms
        #   a valid pair with the current element so increase the count by that many
        if inverse in seen:
            count += seen[inverse]
        #4. Record that we now have seen one more occurence of this
        seen[el] = seen.get(el, 0) + 1

    #5. Return the total count
    return count # works for all test cases shown
# Time and Space Complexities -> O(n) for both

if __name__ == "__main__":
    input_array_1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    input_array_2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
    input_array_3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    input_array_4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]

    print(ZeroSum1Rep(input_array_4))
    print(ZeroSumNoLimReps(input_array_4))

# Time spent: ~35 minutes