#Variable size sliding window
#O(n) time, O(1) space
def duplicate_array(numbers):
    l, r = 1, 1
    while r < len(numbers):
        if numbers[l-1] != numbers[r]:
            numbers[l] = numbers[r]
            l+= 1
        r += 1

    while l < len(numbers):
        numbers[l] = -1
        l+= 1
    return numbers

print(duplicate_array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
print(duplicate_array([1, 2, 3, 4]))
print(duplicate_array([2, 2, 2, 2]))
print(duplicate_array([1, 1, 1, 2, 3, 3, 4]))
print(duplicate_array([1]))
print(duplicate_array([]))

#36 minutes
