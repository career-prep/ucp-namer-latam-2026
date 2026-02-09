"""
Technique Used: Fixed Size Sliding Window
Time Complexity: O(n)
Space Complexity: O(1)

Intuition: We can use a sliding window of fixed size k to traverse through the array. 
At each step, we calculate the sum of the elements in the current window and compare it with the current maximum sum.
Traverse through the array until the end, updating the maximum sum when a larger sum is found.
Need to deal with edge cases such as k being 0, k being larger than the length of the array, and when the array has length 0. 
"""


def MaxMeanSubArray(arr, k):
    # Deal with edge cases
    if k == 0:
        return 0
    
    if len(arr) < k or len(arr) == 0:
        return "Invalid Input"
       
    # Use the 2 pointer technique to create a sliding window of size k
    point1 = 0
    point2 = k - 1
    cur = 0

    # Iterate through the array comparing sums of each subarray of size k in order to get the window with the maximum sum
    while point2 < len(arr):
        if sum(arr[point1:(point2 + 1)]) > cur:
            cur = sum(arr[point1:(point2 + 1)])
        point1 += 1
        point2 += 1

    # Return the Max Mean Sub Array
    return cur / k

# Test Cases
test = [([4, 5, -3, 2, 6, 1], 2),
        ([4, 5, -3, 2, 6, 1], 3),
        ([5, 4, 2, 9, 1, 0, -1], 1),
        ([1, 1, 1, 1, -1, -1, 2, -1, -1], 3),
        ([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5),
        ([], 3),
        ([5, -1, 3], 0),
        ([2, 4], 5)]

for i in test:
    print(MaxMeanSubArray(i[0], i[1]))

# Time Spent: 17 Mins
    