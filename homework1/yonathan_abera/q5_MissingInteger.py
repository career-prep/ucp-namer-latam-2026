#Don't believe the listed techniques were used.
#O(n) time, O(1) space
def missing_int(numbers, max_n):
    predicted = 1
    for num in numbers:
        if num != predicted:
            return predicted
        predicted += 1
    if predicted <= max_n:
        return predicted

print(missing_int([1, 2, 3, 4, 6, 7], 7))
print(missing_int([1], 2))
print(missing_int([1, 2, 4, 5], 5))
print(missing_int([1, 2, 3], 4))
print(missing_int([1, 3, 4, 5], 5))

#10 minutes
