#One Directional Running Computation
#O(n) time, O(n) space
def zero_subarray(numbers):
    prefix_sum = {0:1}
    currSum = 0
    results = 0
    for num in numbers:
        currSum += num
        
        if currSum in prefix_sum:
            results += prefix_sum[currSum]
        if currSum in prefix_sum:
            prefix_sum[currSum] += 1
        else:
            prefix_sum[currSum] = 1

    return results

print(zero_subarray([4, 5, 2, -1, -3, -3, 4, 6, -7]))
print(zero_subarray([1, -1, 2, -2, 3, -3]))
print(zero_subarray([0, 0, 0, 0]))
print(zero_subarray([1, 2, 3]))
print(zero_subarray([-1, 1, -1, 1, -1, 1]))
print(zero_subarray([3, 4, -7, 1, 3, 3, 1, -4]))

#40 minutes(Overtime)