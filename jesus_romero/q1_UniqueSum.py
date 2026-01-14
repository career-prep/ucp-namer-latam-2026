"""Q2:
Given an array of ints, return the sum of unique elements in the array
"""

def UniqueSum(lst):
    #1. Create a set of seen variables and a count to track sum of unique numbers
    seen = set()
    count = 0
    #2. Iterate over our array
    for el in lst:
        #3. If it has been seen before, it is not unique => skip it
        if el in seen:
            continue
        #4. Else, it is unique => add it to the recurrent sum, and add it to our seen set
        else:
            count += el
            seen.add(el)
    #5. Return the total sum of unique elements
    return count # Works

# Time Complexity: O(n)
# Space Complexity: O(n)

if __name__ == "__main__":
    input_array_1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    input_array_3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    print(UniqueSum(input_array_1))
    print(UniqueSum(input_array_3))

# Time spent: ~10 mins