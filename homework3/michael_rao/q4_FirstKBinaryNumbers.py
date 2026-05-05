# Data structure: Array
# Time: O(k log k) 
# Space: O(k log k) 


def first_k_binary_numbers(k):
    result = []
    for i in range(k):
        digits = []
        n = i
        while True:
            digits.append(str(n % 2))
            n //= 2
            if n == 0:
                break
        result.append("".join(reversed(digits)))
    return result


print("Correct:", ["0", "1", "10", "11", "100"])
print("Output: ", first_k_binary_numbers(5))
print()

print("Correct:", ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"])
print("Output: ", first_k_binary_numbers(10))
print()

print("Correct:", [])
print("Output: ", first_k_binary_numbers(0))
print()

# time taken: 20 min
