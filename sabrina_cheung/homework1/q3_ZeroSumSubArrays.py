"""
Technique Used: One Directional Running Computation
Time Complexity: O(n)
Space Complexity: O(n)

"""
def ZeroSumSubArrays(arr):
    sum_counts = {0: 1}
    
    running_sum = 0
    total = 0
    
    for i in arr:
        running_sum += i
        
        if running_sum in sum_counts:
            total += sum_counts[running_sum]
            sum_counts[running_sum] += 1
        else:
            sum_counts[running_sum] = 1
            
    return total

test = [[4, 5, 2, -1, -3, -3, 4, 6, -7],
        [1, 8, 7, 3, 11, 9],
        [8, -5, 0, -2, 3, -4]]

for i in test:
    print(ZeroSumSubArrays(i))
# Time Spent: 40 mins