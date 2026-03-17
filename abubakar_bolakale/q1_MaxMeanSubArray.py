"""
Given an array of integers and an integer k, find the maximum mean of any subarray of size k.
"""
#Using a sliding window of size K.
#add all the element in the window and find the mean by dividing by two.
#store the answer. 
#add next element to the window and remove the left most element.
#return the maximum result stored
class solution:
    def MaxMeanSubArray (self, array, k):
        curr = 0
        for i in range(k):
            curr += array[i]
        ans = curr / k
            
        j = 0
        for i in range(k, len(array)):
            curr += array[i] - array[j]
            j += 1
            ans = max(ans, curr/k)
        return ans
    
sol = solution()

test_cases = [

    ([4, 5, -3, 2, 6, 1], 2),
    ([4, 5, -3, 2, 6, 1], 3),

    ([1, 1, 1, 1, -1, -1, 2, -1, -1], 3),
    ([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5),

    ([5], 1),
    ([2, 4, 6], 3),
    ([-5, -2, -9], 1),
    ([0, 0, 0, 0], 2),

    ([-8, -3, -6, -2], 2),
    ([-1, 10, -2, 9, -3], 2),

    ([5, 5, 5, 5], 2),
    ([1, 2, 1, 2], 2),

    ([3, -1, 2, -1, 4], 4),
    ([1, 2, 3, 4, 5], 3),
    ([5, 4, 3, 2, 1], 3),
]

for nums, k in test_cases:
    print(sol.MaxMeanSubArray(nums, k))
