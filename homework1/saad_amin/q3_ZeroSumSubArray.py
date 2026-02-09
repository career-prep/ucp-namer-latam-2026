#Technique: One direction running total

#Time Complexiy: O(n)
#Space Complexity: O(n)


def zeroSub(arr):
    prefix_sum = 0
    count = 0
    freq = {0 : 1}

    for num in arr:
        prefix_sum += num

        if prefix_sum in freq:
            count += freq[prefix_sum]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

print(zeroSub([4, 5, 2, -1, -3, -3, 4, 6, -7]))
print(zeroSub([-1, -2, -3, -4]))

#Time taken: 27 min