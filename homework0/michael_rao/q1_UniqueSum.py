# time: O(n), space: O(n)

def unique_sum(arr):
    arr_sum = 0
    seen = set()

    for n in arr:
        if n not in seen:
            arr_sum += n
            seen.add(n)
        
    return arr_sum

print("Input Array: [1, 2, 3, -2, -1, 1, 2, 3, 0]")
print("Output:", unique_sum([1, 2, 3, -2, -1, 1, 2, 3, 0]))

# took 5 minutes