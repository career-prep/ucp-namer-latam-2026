# time: O(n), space: O(n)

def zero_sum(arr):
    num_pairs = 0
    freq = {}
    pairs = set()

    for i in arr:
        freq[i] = 1 + freq.get(i, 0)

    for i in freq:
        if -i in freq and abs(i) not in pairs:
            if i == 0:
                num_pairs += freq[i] // 2
            else:
                num_pairs += min(freq[i], freq[-i])
            pairs.add(abs(i))
    
    return num_pairs

print("Input Array: [1, 2, 0, 2, -2, -1]")
print("Output:", zero_sum([1, 2, 0, 2, -2, -1]))

print("Input Array: [2, 0, 1, 2, 2, 0]")
print("Output:", zero_sum([2, 0, 1, 2, 2, 0]))

print ("---------------------------------")

# took 7 minutes


# time: O(n), space: O(n)

import math

def zero_sum_follow_up(arr):
    num_pairs = 0
    freq = {}
    pairs = set()

    for i in arr:
        freq[i] = 1 + freq.get(i, 0)

    for i in freq:
        if -i in freq and abs(i) not in pairs:
            if i == 0:
                num_pairs += math.factorial(freq[i] - 1)
            else:
                num_pairs += freq[i] * freq[-i]
            pairs.add(abs(i))
    
    return num_pairs

print("Input Array: [1, 2, 2, -2, 0]")
print("Output:", zero_sum_follow_up([1, 2, 2, -2, 0]))

print("Input Array: [-2, 2, 2, -2, 1, -1]")
print("Output:", zero_sum_follow_up([-2, 2, 2, -2, 1, -1]))

print("Input Array: [0, 0, 0, 0]")
print("Output:", zero_sum_follow_up([0, 0, 0, 0]))

print("Input Array: [1, 2, 0, 0]")
print("Output:", zero_sum_follow_up([1, 2, 0, 0]))

# took 16 minutes