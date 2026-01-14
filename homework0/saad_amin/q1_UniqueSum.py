#Time Complexity O(N)
#Space Complexity O(N)

def UniqueSum(arr):
    unique = set(arr)
    return sum(unique)

if __name__ == "__main__":
    print(UniqueSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1])) #33 given test case
    print(UniqueSum([1, 1, 1, 1, 1, 2, 2, 4, 4, 6,6, 7, 7, 7])) # should be 20 ( 1+ 2+ 4 + 6 + 7)
    print(UniqueSum([1, 0, 0, 0, -1, -1, -2]))

#Time taken 6 min 