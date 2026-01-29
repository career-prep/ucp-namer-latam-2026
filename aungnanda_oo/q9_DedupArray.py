# Question 9: DedupArray

# Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once. If arrays are static (aka, not dynamic/resizable) in your language of choice, the remaining elements should appear in the left-hand side of the array and the extra space in the right-hand side should be padded with -1s.

# Examples:

# Input Array: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# Modified Array: [1, 2, 3, 4]
# or [1, 2, 3, 4, -1, -1, -1, -1, -1, -1] (depending on language)

# Input Array: [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
# Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15]
# or [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

# Input Array: [1, 3, 4, 8, 10, 12]
# Modified Array: [1, 3, 4, 8, 10, 12]

# Brute Force
def DedupArray_1(dup_arr):
    if not dup_arr:
        return []
    return list(set(dup_arr))


# Two Pointer (Optimal) - O(n) time, O(1) space
def DedupArray_2(dup_arr):
    if not dup_arr:
        return []

    write_idx = 1
    for read_idx in range(1, len(dup_arr)):
        if dup_arr[read_idx] != dup_arr[write_idx - 1]:
            dup_arr[write_idx] = dup_arr[read_idx]
            write_idx += 1

    return dup_arr[:write_idx]


test_cases = [[1, 2, 2, 3, 3, 3, 4, 4, 4, 4],[0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15],[1, 3, 4, 8, 10, 12]]

# Time Complexity: O(n)
# Space Complexity: O(n)

print("Brute Force Solu")
for test_case in test_cases:
    print(DedupArray_1(test_case.copy()))


# Time Complexity: O(n)
# Space Complexity: O(1)

print("Two Pointer (Optimal)")
for test_case in test_cases:
    print(DedupArray_2(test_case.copy()))


# Spent a total of 40 mins on this question