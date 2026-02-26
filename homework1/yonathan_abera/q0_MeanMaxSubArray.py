#fixed size sliding window
# O(n) time, O(1) space
#assumptions: 
# k<=length(array) for a reasonable answer.
# array isn't empty


def max_mean(k, numbers):
    left, right = 0, k-1
    big_mean = -10**9
    running_sum = 0
    while right < len(numbers):
        for i in range(left, right + 1, 1):
            running_sum += numbers[i]

        curr_mean = running_sum/k
        big_mean = max(big_mean, curr_mean)

        left += 1
        right += 1
        running_sum = 0
        
    return big_mean

print(max_mean(5, [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]))
print(max_mean(3, [1, 2, 3, 4, 5]))
print(max_mean(2, [-5, -2, -3, -4]))
print(max_mean(1, [5, -2, 7, 3]))
print(max_mean(4, [1, 2, 3, 4]))
print(max_mean(2, [2, 2, 2, 2]))
print(max_mean(3, [-1, 3, -2, 5, -4, 6]))

            
#15 minutes
