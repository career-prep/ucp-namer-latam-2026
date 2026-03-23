from collections import defaultdict

"""
My Logic: 
- In order for two numbers to sum to zero, they must be the same number but opposite sign.
- Use a dictionary to count the occurrences of each number in the array.
- For each number in the array, check if its opposite number is in the dictionary.
"""

def ZeroSum(arr):
    dict = defaultdict(int)
    count = 0
    for i in arr:

        if dict.get(-i, 0) > 0:
            count += 1
            dict[-i] -= 1
            dict[i] -= 1
        else:
            dict[i] += 1
    return count

test = [
    [1, 10, 8, 3, 2, 5, 7, 2, -2, -1],
    [1, 10, 8, -2, 2, 5, 7, 2, -2, -1],
    [4, 3, 3, 5, 7, 0, 2, 3, 8, 6],
    [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]]

for i in test:
    print(ZeroSum(i))
    
# 40 mins