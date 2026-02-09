# Time Complexity: O(n)
# Space Complexity: O(n)

def zero_sum_without_reuse(arr):
    counts = {}
    pairs = 0
    seen = set()
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    for num, count in counts.items():
        if num == 0:
            pairs += count // 2
            continue
        if num not in seen:
            opp = -num
            if opp not in counts:
                continue
            pairs += min(counts[num], counts[opp])
            seen.add(num)
            seen.add(opp)
    return pairs

def zero_sum_with_reuse(arr):
    counts = {}
    pairs = 0
    seen = set()
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    for num, count in counts.items():
        if num == 0:
            pairs += (count * (count - 1)) // 2
            continue

        if num not in seen:
            opp = -num
            if opp not in counts:
                continue
            pairs += counts[num] * counts[opp]
            seen.add(num)
            seen.add(opp)
    return pairs

print(zero_sum_without_reuse([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(zero_sum_without_reuse([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))
print(zero_sum_without_reuse([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))
print(zero_sum_without_reuse([4, 3, 3, 5, 7, 0, 2, 3, 8, 0]))

print(zero_sum_with_reuse([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))
print(zero_sum_with_reuse([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]))
print(zero_sum_with_reuse([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))
print(zero_sum_with_reuse([4, 3, 3, 5, 7, 0, 2, 3, 8, 0]))

# Time spent: 11mins