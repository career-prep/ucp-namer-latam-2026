# Question 3 ()
# Time Complexity: O(n)
# Space Complexity: O(n)
# Time spent: 37 mins




from collections import defaultdict

def zeroSumSubarrays(nums):
    prefix_count = defaultdict(int)
    prefix_count[0] = 1   

    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        
        count += prefix_count[current_sum]

        
        prefix_count[current_sum] += 1

    return count

print(zeroSumSubarrays([1, -1, 2, -2, 3, -3])) 

print(zeroSumSubarrays([4, 5, 2, -1, -3, -3, 4, 6, -7]))  # 2
print(zeroSumSubarrays([1, 8, 7, 3, 11, 9]))            # 0
print(zeroSumSubarrays([8, -5, 0, -2, 3, -4]))          # 2