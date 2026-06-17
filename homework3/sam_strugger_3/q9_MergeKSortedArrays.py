# O(n log k) time and O(k) space

def merge(k, arrs):
    result = []

    for arr in arrs:
        for val in arr:
            result.append(val)

    return result.sort()

# This took me 5 minutes